import os
import json
import sys

def brute():
    """
    Attempts to bruteforce the hashed password of each user
    """
    for user in data["users"]:
        print(str.format("Attempting to brute force {}", user["username"]))

scriptLocation = os.path.dirname(__file__)

data = {}

with open(os.path.join(scriptLocation, "..", "target", "processed", "targets.json")) as file:
    data = json.load(file)

attackType = "brute"

if len(sys.argv) > 1:
    attackType = sys.argv[1]
 
if attackType == "brute":
    brute()
