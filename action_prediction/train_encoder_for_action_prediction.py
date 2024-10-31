import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from simulate_data_for_action_prediction import GymDataset

dataset = GymDataset(num_samples=1000)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

#TODO: Define a model that predicts the action taken given the previous state and the current state
# Plan A, use the off-the-shelf model from dreamerv3
from networks import MultiEncoder
shapes = {
    "trials_remain": (1,), 
    "terminated": (1,), 
    "input": (5, 5),
    "input_dim": (2,),
    "grid": (5, 5),
    "grid_dim": (2,),
}
config = {
    "mlp_keys": r"features",
    "cnn_keys": r"input|grid",
    "act": "ReLU",
    "norm": True,
    "cnn_depth": 128,
    "kernel_size": 4,
    "minres": 4,
    "mlp_layers": 2,
    "mlp_units": 256,
    "symlog_inputs": True,
}
Encoder = MultiEncoder(shapes, **config)
# Plan B, use a simple model like a linear layer
...
# Define an action predictor
from my_network import ActionPredictor
A_predictor = ActionPredictor(input_dim=config["cnn_depth"], output_dim=128, hidden_dim=256)

#TODO: Train the model using the dataloader
criteria = nn.MSELoss()
trainable_models = [Encoder, A_predictor]
print(Encoder.parameters())
print(A_predictor.parameters())
# optimizer = torch.optim.Adam([model.parameters() for model in trainable_models], lr=0.001)
optimizer = torch.optim.Adam(A_predictor.parameters(), lr=0.001)
# write me a baseline of training neural network

for epoch in range(10):
    for i, data in enumerate(dataloader):
        obs_0, obs_1, action = data
        obs_0 = {k: torch.Tensor(v).float() for k, v in obs_0.items()}
        print('-----------------------------------------------')
        print(obs_0.keys())
        print(obs_0['grid'][0])
        print(obs_1['grid'][0])
        break
    break
        # obs_1 = {k: torch.Tensor(v).float() for k, v in obs_1.items()}
        # embedding_0 = Encoder(obs_0)
        # embedding_1 = Encoder(obs_1)
        # print('hello')
        # print(embedding_0.shape)
