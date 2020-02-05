import json
from flask import Flask, request
# instance of Flask class, it's our application. We pass the name of the module.
app = Flask(__name__)

with open('names.json') as f:
    # the names dictionary is saved in the memory
    # once your restart your server, i.e. do the changes in the code and save, all the deleted/added names will be lost
    names = json.loads(f.read())


# route decorator specifies what URL should trigger our function
@app.route('/names/<string:name>', methods=['GET'])
def get_name_meaning(name):
    capitalized = name.capitalize()
    return names[capitalized]


@app.route('/names', methods=['GET'])
def get_all_names():
    return names


@app.route('/names', methods=['POST'])
def create_name():
    data = request.json  # data sent in POST request body
    print(f'Adding {data} to our list of names')

    keys = list(data)

    name = keys[0]
    name_capitalized = name.capitalize()
    status = 201

    if name_capitalized in names:
        status = 200
    names[name_capitalized] = data[name]

    return data, status


@app.route('/names/<string:name>', methods=['DELETE'])
def remove_name(name):
    capitalized = name.capitalize()
    for n in names:
        if n == capitalized:
            del names[capitalized]
