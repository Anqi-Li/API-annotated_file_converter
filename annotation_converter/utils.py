# %%
def initialize_openlabel_annotation():
    # initiate the openlabel structure with empty content
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
    return openlabel_annotation

def convert_extreme_points_to_bbox(maxX, maxY, minX, minY):
    # convert to bounding boxes (bbox)
    x = (minX + maxX)/2
    y = (minY + maxY)/2
    w = maxX - minX
    h = maxY - minY

    return x,y,w,h

def populate_bbox_values(object_id, frames_objects, bbox_tuple):
    frames_objects[object_id] = {
        'object_data': {
            'bbox': [{
                'name': f'bbox-{object_id[:8]}',
                'stream': 'CAM',
                'val': list(bbox_tuple)
            }]
        }
    }
    
def populate_unclear_value(object_id, kognic_annotation, dict_frames_objects):
    if 'Unclear' in kognic_annotation['shapeProperties'][object_id]['@all'].keys():
        dict_frames_objects[object_id]['object_data']['boolean'] = [{
            'name': 'Unclear',
            'val': kognic_annotation['shapeProperties'][object_id]['@all']['Unclear'],
        }]

def populate_objecttype_value(object_id, kognic_annotation, dict_frames_objects):
    if 'ObjectType' in kognic_annotation['shapeProperties'][object_id]['@all'].keys():
        dict_frames_objects[object_id]['object_data']['text'] = [{
            'name': 'ObjectType',
            'val': kognic_annotation['shapeProperties'][object_id]['@all']['ObjectType'],
        }]
def populate_objects(object_id, kognic_annotation, dict_objects):
    dict_objects[object_id] = {
            'name': object_id,
            'type': kognic_annotation['shapeProperties'][object_id]['@all']['class'],
        }

def convert(kognic_annotation: dict) -> dict:
    '''
    convert annotation from kognic to openlabel  format
        parameters: 
            kognic_annotation (dict): dictionary of annotation in format
        returns: 
            openlabel_annotation (dict): dictionary of annotation in openlabel format
    '''
    
    #initiate the openlabel structure with empty content
    openlabel_annotation = initialize_openlabel_annotation()

    # retrieve 'features' in kognic_annotation
    list_of_objects = kognic_annotation['shapes']['CAM']['features']

    dict_frames_objects = openlabel_annotation['data']['openlabel']['frames']['0']['objects']
    dict_objects = openlabel_annotation['data']['openlabel']['objects']
    
    for i in range(len(list_of_objects)):
        object_id = list_of_objects[i]['id']
        
        # populate 'frame' - '0' - 'objects' in openlabel format
        
        # Extreme Point Bounding Boxes
        maxX = list_of_objects[i]['geometry']['coordinates']['maxX']['coordinates'][0]
        maxY = list_of_objects[i]['geometry']['coordinates']['maxY']['coordinates'][1]
        minX = list_of_objects[i]['geometry']['coordinates']['minX']['coordinates'][0]
        minY = list_of_objects[i]['geometry']['coordinates']['minY']['coordinates'][1]

        # convert to bounding boxes (bbox)
        x,y,w,h = convert_extreme_points_to_bbox(maxX, maxY, minX, minY)

        # populate 'bbox' values
        populate_bbox_values(object_id, dict_frames_objects, bbox_tuple=(x,y,w,h))

        # populate 'boolean' - 'Unclear' value
        populate_unclear_value(object_id, kognic_annotation, dict_frames_objects)

        # populate 'text' - 'ObjectType' value
        populate_objecttype_value(object_id, kognic_annotation, dict_frames_objects)

        # populate 'objects' in openlabel format
        populate_objects(object_id, kognic_annotation, dict_objects)

    return openlabel_annotation
