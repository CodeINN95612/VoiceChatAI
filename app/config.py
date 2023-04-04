from . import globals
import os
import json


def loadConfig():
    try:
        createConfig()
        with open(globals.CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def createConfig():
    template = {
        "token": ""
    }
    if not os.path.exists(globals.DATA_DIR):
        os.makedirs(globals.DATA_DIR)
    if os.path.exists(globals.CONFIG_FILE):
        return
    with open(globals.CONFIG_FILE, "w") as file:
        json.dump(template, file, indent=4)


config = loadConfig()
if config["token"] == "":
    raise Exception("Insert token inside config.json file")
