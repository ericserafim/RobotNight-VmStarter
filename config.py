import json

with open('appsettings.json') as f:
    data = json.load(f)
    VMPLAYER_PATH = data['vm_player_path']
    VM_NAME_TO_START = data['vm_name_to_start']
    VM_USERNAME = data['username']
    VM_PASSWORD = data['password']
    f.close()