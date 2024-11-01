import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from simulate_data_for_action_prediction import GymDataset
import argparse
import yaml
import torch.nn.functional as F

dataset = GymDataset(num_samples=10000)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

#TODO: Define a model that predicts the action taken given the previous state and the current state

from networks import CNN_encoder

shapes = {
    "trials_remain": (1,), 
    "terminated": (1,), 
    "input": (5, 5),
    "input_dim": (2,),
    "grid": (5, 5),
    "grid_dim": (2,),
}
def main(args):
    if args.encoder_type == "cnn_based":
        Encoder = CNN_encoder(embedding_dim=args.grid_embedding_dim, **args.network_configs)
    
    # Define an action predictor
    Action_predictor = nn.Sequential(
        nn.Linear(2*args.grid_embedding_dim, 256),
        nn.ReLU(),
        nn.Linear(256, 256),
        nn.ReLU(),
        nn.Linear(256, args.action_embedding_dim)
    )

    #TODO: Train the model using the dataloader
    criteria = nn.MSELoss()
    trainable_models = [Encoder, Action_predictor]
    params = sum([list(model.parameters()) for model in trainable_models],[])
    print(len(params))
    optimizer = torch.optim.Adam(params, lr=0.001)
    # optimizer = torch.optim.Adam(Action_predictor.parameters(), lr=0.001)
    # write me a baseline of training neural network

    for epoch in range(100):
        for i, data in enumerate(dataloader):
            obs_0, obs_1, action = data
            obs_0 = F.one_hot(obs_0['grid'].long(), num_classes=10).permute(0,3,1,2).float()
            obs_1 = F.one_hot(obs_1['grid'].long(), num_classes=10).permute(0,3,1,2).float()

            embedding = torch.cat([Encoder(obs_0), Encoder(obs_1)], dim=1)
            action_pred = Action_predictor(embedding)
            loss = criteria(action_pred, action)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            print(loss.item())




def yaml_loader(yaml_file):
    with open(yaml_file, "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", type=str, default="cnn_based_encoder.yaml")
    args = args.parse_args()
    if args.config:
        config = yaml_loader(args.config)
        for k, v in config.items():
            setattr(args, k, v)
    main(args)