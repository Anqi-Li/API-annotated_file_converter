# API-annotated_file_converter
An API that converts different formats of JSON files.

## pip install package
In the terminal/command line, run the following command
```
pip install "git+https://github.com/Anqi-Li/API-annotated_file_converter"
```

Alternatively, clone the repository from https://github.com/Anqi-Li/API-annotated_file_converter. Then, go to your local directory where the repository is cloned and run the following command
```
pip install .
```

## Examples to use the `convert` function in Python
If you have a JSON file in kognic annotation format that is stored locally
```python
from annotation_converter.utils import convert
path_to_kognic_annotation = '/PATH/TO/FILE.json'

with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)

open_label_annotation = convert(kognic_annotation)
```

If you have an url that responses in a json format from a web service
```python
import requests
from annotation_converter.utils import convert
url = "DOMAIN/FILE.json" 
response = requests.get(url)
kognic_annotation = response.json()

open_label_annotation = convert(kognic_annotation)

```

## Flask API
To activate the Flask app locally, type in the terminal/command line the following
```
python flask_app.py

```
After executing these commands, we can reach our application by opening a browser and navigating to http://127.0.0.1:5000/ or by issuing `curl http://127.0.0.1:5000/`.

### Use `curl` to convert a JSON file
In a terminal/command line, type (assuming `curl` is installed)
```
curl -i http://127.0.0.1:5000/from_json_file -X POST -H "Content-Type: application/json" -d @PATH/To/FILE.json
```
where `PATH/TO/FILE.json` shall be replaced by your local JSON file, such as `./annotated_files/kognic_1.json` if you clone the repository.

### Use a browser
Navigate to http://127.0.0.1:5000/ and select the appropriate endpoint.
For example, go to http://127.0.0.1:5000/from_url, insert the url and click the `submit` button.
