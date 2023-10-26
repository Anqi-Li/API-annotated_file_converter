#%%
import json

# %%
def convert(kognic_annotation):
    # initiate the openlabel structure
    openlabel_annotation = {}
    openlabel_annotation['data'] = {
        'openlabel':{
            'frames':{
                '0':{
                    'objects': {},
                }
            }
        }
    }

    openlabel_annotation['data']['openlabel']['objects'] = {}

    # loop over each 'features' in kognic_annotation
    openlabel_annotation 
    frames_objects = openlabel_annotation['data']['openlabel']['frames']['0']['objects']
    objects = openlabel_annotation['data']['openlabel']['objects']

    list_of_objects = kognic_annotation['shapes']['CAM']['features']
    for i in range(len(list_of_objects)):
        object_id = list_of_objects[i]['id']
        
        # populate 'frame' - '0' - 'objects' in openlabel format
        # populate 'bbox' values
        # Extreme Point Bounding Boxes
        maxX = list_of_objects[i]['geometry']['coordinates']['maxX']['coordinates'][0]
        maxY = list_of_objects[i]['geometry']['coordinates']['maxY']['coordinates'][1]
        minX = list_of_objects[i]['geometry']['coordinates']['minX']['coordinates'][0]
        minY = list_of_objects[i]['geometry']['coordinates']['minY']['coordinates'][1]

        # convert to bounding boxes (bbox)
        x = (minX + maxX)/2
        y = (minY + maxY)/2
        w = maxX - minX
        h = maxY - minY

        frames_objects[object_id] = {
            'object_data': {
                'bbox': [{
                    'name': f'bbox-{object_id[:8]}',
                    'stream': 'CAM',
                    'val': [x,y,w,h]
                }]
            }
        }

        # populate 'boolean' - 'Unclear' value
        if 'Unclear' in kognic_annotation['shapeProperties'][object_id]['@all'].keys():
            frames_objects[object_id]['object_data']['boolean'] = [{
                'name': 'Unclear',
                'val': kognic_annotation['shapeProperties'][object_id]['@all']['Unclear'],
            }]

        # populate 'text' - 'ObjectType' value
        if 'ObjectType' in kognic_annotation['shapeProperties'][object_id]['@all'].keys():
            frames_objects[object_id]['object_data']['text'] = [{
                'name': 'ObjectType',
                'val': kognic_annotation['shapeProperties'][object_id]['@all']['ObjectType'],
            }]

        # populate 'objects' in openlabel format
        objects[object_id] = {
            'name': object_id,
            'type': kognic_annotation['shapeProperties'][object_id]['@all']['class'],
        }

    return openlabel_annotation


# %% temp for testing
path_to_kognic_annotation = './annotated_files/kognic_1.json'
with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)
    
path_to_openlabel_annotation = './annotated_files/open_label_1.json'
with open(path_to_openlabel_annotation, 'r') as content:
    openlabel_annotation_org = json.load(content)

openlabel_annotation_org == convert(kognic_annotation)

# %%
