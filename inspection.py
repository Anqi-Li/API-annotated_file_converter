#%%
import json

# %% inspection: kognic
path_to_kognic_annotation = './annotated_files/kognic_1.json'
with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)

# %%
for i in range(1,2):
    print(kognic_annotation['shapes']['CAM']['features'][i]['geometry'])

#%% 
for k,v in kognic_annotation['shapeProperties'].items():
    try:
        print(k, v['@all']['Unclear'])
    except KeyError:
        print(k, 'missing')

# %% inspection: openlabel
path_to_openlabel_annotation = './annotated_files/open_label_1.json'
with open(path_to_openlabel_annotation, 'r') as content:
    openlabel_annotation = json.load(content)
# %%
list_ids = list(openlabel_annotation['data']['openlabel']['frames']['0']['objects'].keys())
for i in range(0,1):
    print(openlabel_annotation['data']['openlabel']['frames']['0']['objects'][list_ids[i]]['object_data']['bbox'])

# %%
openlabel_objects = openlabel_annotation['data']['openlabel']['frames']['0']['objects']
for k,v in openlabel_objects.items():
    print(k, v['object_data']['bbox'])

# %%
for k,v in openlabel_objects.items():
    print(k, v)
# %%

def convert_extreme_point_bounding_to_bbox(i):
    # Extreme Point Bounding Boxes
    maxX = kognic_annotation['shapes']['CAM']['features'][i]['geometry']['coordinates']['maxX']['coordinates'][0]
    maxY = kognic_annotation['shapes']['CAM']['features'][i]['geometry']['coordinates']['maxY']['coordinates'][1]
    minX = kognic_annotation['shapes']['CAM']['features'][i]['geometry']['coordinates']['minX']['coordinates'][0]
    minY = kognic_annotation['shapes']['CAM']['features'][i]['geometry']['coordinates']['minY']['coordinates'][1]

    # convert to bounding boxes (bbox)
    x = (minX + maxX)/2
    y = (minY + maxY)/2
    w = maxX - minX
    h = maxY - minY
    return list((x, y, w, h))

i=1 # id = '11206831-2964-487b-a24b-abfc55f82013' in kognic
print(convert_extreme_point_bounding_to_bbox(i))
i=0 # id = '11206831-2964-487b-a24b-abfc55f82013' in openlabel
print(openlabel_annotation['data']['openlabel']['frames']['0']['objects'][list_ids[i]]['object_data']['bbox'][0]['val'])
# %%



