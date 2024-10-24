import torch
from torch.utils.data import Dataset
import arcle
import pickle
import gymnasium as gym
import time
import numpy as np
from arcle.loaders import MiniARCLoader
from arcle.wrappers import BBoxWrapper
#from transformers import BartTokenizer, BartModel

#BartTokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
#Bart = BartModel.from_pretrained('facebook/bart-base')

from arcle.envs.o2arcenv import O2ARCv2Env
operations = O2ARCv2Env().operations

action_descriptions = pickle.load(open('generated_action_descriptions.pkl', 'rb'))

def get_action_embedding(action):
    return torch.tensor(action_descriptions[action]['embedding'])

def get_action_name(action):
    idx = int(action['operation'])
    cnt = sum(sum(action['selection']))
    return f"{cnt} pixels are manipulated with {operations[idx].__name__}"

# TODO: Download Text Encoder Model from Huggingface

class GymDataset(Dataset):
    def __init__(self, num_samples, max_grid_size=(5, 5)):
        self.env = gym.make('ARCLE/RawARCEnv-v0',render_mode='ansi',data_loader = MiniARCLoader(),max_grid_size=max_grid_size)
        #self.env = BBoxWrapper(self.env)
        obs, info = self.env.reset()
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
            action = self.encode_arcle_action(action)
            self.data.append((prev_obs, obs, action))

    def encode_arcle_action(self, action):
        # TODO: Map the action to text
        action_name = get_action_name(action)
        action_embedding = get_action_embedding(action_name)
        #inputs = BartTokenizer(action_name, return_tensors="pt")
        #outputs = Bart(**inputs)

        #return outputs.last_hidden_state
        # TODO: Encode the text using the text encoder
        return action_embedding

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        prev_obs, obs, action = self.data[idx]
        return prev_obs, obs, action