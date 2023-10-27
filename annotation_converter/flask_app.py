from flask import Flask, jsonify, request
from utils import convert
import json
import requests as R

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <h1>Welcome to the annotation converter API!<h1>
    <h1>Please navigate to the end points<h1>
        <h1>- /from_url (input an url)<h1>
        <h1>- /from_json_file (post a json file)<h1>
        <h1>- /kognic_1.json (get a sample json file)<h1>
        <h1>- /convertion_test (test on the sample json file)<h1>
    <h1>for appropiate usage.  <h1>
'''

@app.route("/from_url",  methods=['GET', 'POST'])
def get_openlabel_annotation_from_url():
    # handle the POST request
    if request.method == 'POST':
        url = request.form.get('Enter url contains kognic annotation')
        json_str = R.get(url).json()
        json_data = json.loads(json_str)
        return jsonify(convert(json_data))
    
    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Enter URL: <input type="text" name="url"></label></div>
               <input type="submit" value="Submit">
           </form>'''

@app.route("/from_json_file", methods=['POST'])
def get_openlabel_annotation_from_file():
    json_data = request.get_json()
    if not json_data:
        return {"message": "Must provide a valid json file"}, 400
    else:
        return jsonify(convert(json_data))
    
@app.route("/kognic_1.json")
def get_kognic_annotation_test():
    path_to_kognic_annotation = '../annotated_files/kognic_1.json'
    with open(path_to_kognic_annotation, 'r') as content:
        kognic_annotation = json.load(content)
    return kognic_annotation

@app.route("/convertion_test")
def get_openlabel_annotation_test():
    return jsonify(convert(get_kognic_annotation_test()))

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)