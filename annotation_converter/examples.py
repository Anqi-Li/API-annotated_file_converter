#%%
import requests
from utils import convert
import json

# %% supply with json file given the path
# replace with your own path
path_to_kognic_annotation = '../annotated_files/kognic_1.json'
with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)

open_label_annotation = convert(kognic_annotation)


#%% suuply with an url which gives a response in json
# this particualr url requires the flask app is activated
# replace with your own url 
api_url = "http://localhost:5000/kognic_1.json" 
response = requests.get(api_url)
kognic_annotation = response.json()

open_label_annotation = convert(kognic_annotation)
