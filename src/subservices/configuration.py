import json

def loadConfig():

    with open('./test-config.json') as json_file:
        json_config = json.load(json_file)
        print(json_config)
        return json_config