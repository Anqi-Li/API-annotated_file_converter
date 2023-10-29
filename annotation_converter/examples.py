#%%
import requests
from utils import convert
import json

#%% 1. supply with a json file and post request to the API
path_to_kognic_annotation = '../annotated_files/kognic_1.json'
with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)

# this particualr url requires the flask app is activated locally
# run 'python flask_app.py' in terminal to activate the app
# you may replace with your own url 
url = "http://localhost:5000/from_json_file"
response = requests.post(url=url, json=kognic_annotation)

open_label_annotation = response.json()

#%% 2. supply with an url which gives a response in json
# this particualr url requires the flask app is activated locally
# run 'python flask_app.py' in terminal to activate the app
# you may replace with your own url 
api_url = "http://localhost:5000/kognic_1.json" 
response = requests.get(api_url)
kognic_annotation = response.json()

open_label_annotation = convert(kognic_annotation)

# %% 3. supply with a json file and convert in python directly
# replace with your own path
path_to_kognic_annotation = '../annotated_files/kognic_1.json'
with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)

open_label_annotation = convert(kognic_annotation)
