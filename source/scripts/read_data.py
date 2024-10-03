import json
import numpy as np

# to be continued
file_dir = r'ARC_MLM24\data\arc-agi_training_challenges.json'

with open(file_dir, 'r') as data_file:
    data = json.load(data_file)
    print(list(list(data.values())[0].values())[0])

# STRUCTURE of JSON file

# {"puzzle_id" :{
#     "test" : [{"input" : inputarray}],
#     "train" : [{"input": inputarray, "output": outputarray}, ...]
# }}
