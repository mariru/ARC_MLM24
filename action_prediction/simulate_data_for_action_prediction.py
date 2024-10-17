import torch
from torch.utils.data import Dataset
import arcle
import gymnasium as gym
import time
import numpy as np
from arcle.loaders import MiniARCLoader
from arcle.wrappers import BBoxWrapper

# TODO: Download Text Encoder Model from Huggingface

class GymDataset(Dataset):
    def __init__(self, num_samples, max_grid_size=(5, 5)):
        env = gym.make('ARCLE/RawARCEnv-v0',render_mode='ansi',data_loader = MiniARCLoader(),max_grid_size=max_grid_size)
        self.env = BBoxWrapper(env)
        obs, info = env.reset()
        self.num_samples = num_samples
        self.data = []
        self.generate_data()

    def generate_data(self):
        # Reset the environment
        obs, _ = self.env.reset()
        for _ in range(self.num_samples):
            # Sample random action
            action = self.env.action_space.sample()
            prev_obs = obs
            obs, _, term, trunc, _ = self.env.step(action)

            # If episode ends, reset the environment
            if term or trunc:
                obs, _ = self.env.reset()

            # Store the data: (prev_state, new_state, action)
            # TODO: uncomment the following line
            # action = self.encode_arcle_action(action)
            self.data.append((prev_obs, obs, action))

    def encode_arcle_action(self, action):
        # TODO: Map the action to text

        # TODO: Encode the text using the text encoder
        return torch.tensor(np.random.rand(128))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        prev_obs, obs, action = self.data[idx]
        return prev_obs, obs, action