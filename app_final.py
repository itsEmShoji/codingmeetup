import json
from flask import Flask, request
app = Flask(__name__)

with open('names.json') as f:
    # the names dictionary is saved in the memory
    # once your restart your server, i.e. do the changes in the code and save, all the deleted/added names will be lost
    names = json.loads(f.read())


# what URL should trigger our function
@app.route('/names/<string:name>', methods=['GET'])
def get_name_meaning(name):
    name_capitalized = name.capitalize()
    return names[name_capitalized]


@app.route('/names', methods=['GET'])
def get_all_names():
    return names


@app.route('/names', methods=['POST'])
def create_name():
    data = request.json  # data sent in POST request body
    print(f'Adding {data} to our list of names')

    # running list on data dictionary returns a list of all of the keys in the dictionary
    keys = list(data)
    # e.g. list({"anabella": 1, "brendon": 2}) => ["anabella", "brendon"]
    # select the first key in the dictionary. We should have only one key anyways
    name = keys[0]
    name_capitalized = name.capitalize()
    status = 201

    if name_capitalized in names:
        status = 200
    names[name_capitalized] = data[name]

    return data, status


@app.route('/names/<string:name>', methods=['DELETE'])
def remove_name(name):
    print(f'Removing {name} from the list of names')
    if name in names:
        del names[name]
    return name
