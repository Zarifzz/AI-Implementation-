import json

def load_json_key(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
        api_key = config['openai_key']
    return api_key



print(load_json_key("Api_Key.json"))

