# API-annotated_file_converter
An API that converts different annotation formats of JSON files.

## pip install package
In the terminal/command line, run the following command
```
pip install "git+https://github.com/Anqi-Li/API-annotated_file_converter"
```

Alternatively, clone the repository from https://github.com/Anqi-Li/API-annotated_file_converter. Then, go to your local directory where the repository is cloned and run the following command
```
pip install .
```

# Examples
There are several options to convert the annotation formats. The following describes some examples of them. You can also open [examples.py](annotation_converter/examples.py) to see some of these options in Python.

## Activate the Flask API and HTTP request
To activate the Flask app locally, type in the terminal/command line the following
```
python flask_app.py
```
After executing these commands, we can reach our application locally by sending requests in Python, by navigating to http://127.0.0.1:5000/ in a browser, or by issuing a `curl` command. Note: the local IP address can be replaced by `localhost`, i.e. http://localhost:5000. 

### POST requests in Python
You may use the Python `requests` library for sending HTTP requests. Use url "http://127.0.0.1:5000/from_json_file" as the API endpoint for the request, and the keyward argument `json=` to specify the payload.
```Python
import requests
path_to_kognic_annotation = '/PATH/TO/FILE.json'
with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)

url = "http://127.0.0.1:5000/from_json_file"
response = requests.post(url=url, json=kognic_annotation)

open_label_annotation = response.json()
```
where `PATH/TO/FILE.json` shall be replaced by your local JSON file, such as [`./annotated_files/kognic_1.json`](./annotated_files/kognic_1.json) if you clone the repository.

### Use a browser
Navigate to http://127.0.0.1:5000/ and select the appropriate endpoint.
For example, go to http://127.0.0.1:5000/from_url, insert the url and click the `submit` button.

### Use `curl` to convert a JSON file
In a terminal/command line, type (assuming `curl` is installed)
```
curl -i http://127.0.0.1:5000/from_json_file -X POST -H "Content-Type: application/json" -d @PATH/To/FILE.json
```
where `PATH/TO/FILE.json` shall be replaced by your local JSON file, such as `./annotated_files/kognic_1.json` if you clone the repository.

## Use the `convert` function directly in Python
If you have a JSON file in kognic annotation format that is stored locally
```python
from annotation_converter.utils import convert
path_to_kognic_annotation = '/PATH/TO/FILE.json'

with open(path_to_kognic_annotation, 'r') as content:
    kognic_annotation = json.load(content)

open_label_annotation = convert(kognic_annotation)
```
where `PATH/TO/FILE.json` shall be replaced by your local JSON file, such as `./annotated_files/kognic_1.json` if you clone the repository.

If you have an url that responses in a json format from a web service
```python
import requests
from annotation_converter.utils import convert
url = "http://DOMAIN/FILE.json" 
response = requests.get(url)
kognic_annotation = response.json()

open_label_annotation = convert(kognic_annotation)

```