import json

def parse_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
        return data
    
def write_json(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)
        return 0

