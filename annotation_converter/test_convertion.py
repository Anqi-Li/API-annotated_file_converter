#%%
import json
from utils import convert

# %%
path_to_kognic_annotation = '../annotated_files/kognic_1.json'
with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)
    
path_to_openlabel_annotation = '../annotated_files/open_label_1.json'
with open(path_to_openlabel_annotation, 'r') as content:
    openlabel_annotation_org = json.load(content)

assert openlabel_annotation_org == convert(kognic_annotation)

# %%
