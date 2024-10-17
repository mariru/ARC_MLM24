from torch.utils.data import DataLoader
from simulate_data_for_action_prediction import GymDataset

dataset = GymDataset(num_samples=1000)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

#TODO: Define a model that predicts the action taken given the previous state and the current state

#TODO: Train the model using the dataloader