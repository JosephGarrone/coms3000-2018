import os
import json 

scriptLocation = os.path.dirname(__file__)

data = {}
data["users"] = []
shadowLines = []
passwdLines = []

with open(os.path.join(scriptLocation, "..", "target", "raw", "shadow")) as file:
    shadowLines = file.readlines()

with open(os.path.join(scriptLocation, "..", "target", "raw", "passwd")) as file:
    passwdLines = file.readlines()

count = 0
totalCount = 0
for line in shadowLines:
    passwdParts = passwdLines[totalCount].split(':')
    parts = line.split(':')
    if parts[1][0] == '*' or parts[1][0] == '!':
        print(str.format("Ignoring user {} as no password supplied", parts[0]))
    else:
        user = {}
        user['username'] = parts[0]
        user['hashed_password'] = parts[1].split('$')[3]
        user['salt'] = parts[1].split('$')[2]
        user['user_id'] = passwdParts[2]
        user['group_id'] = passwdParts[3]
        user['user_info'] = passwdParts[4]
        data["users"].append(user)
        count = count + 1
    totalCount = totalCount + 1

output = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

with open(os.path.join(scriptLocation, "..", "target", "processed", "targets.json"), 'w') as file:
    file.write(output)