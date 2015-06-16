import urllib.request
import json

with open("config.json") as config_file:
    settings = json.load(config_file)
    USERTOKENSTRING = settings["USERTOKENSTRING"]
    URLTOKENSTRING = settings["URLTOKENSTRING"]
    TEAMNAMESTRING = settings["TEAMNAMESTRING"]

def get_users():
    with urllib.request.urlopen("https://slack.com/api/users.list?token={0}".format(USERTOKENSTRING)) as response:
        for i in get_users():
            print(i["name"])
            print(i["id"])
        return json.loads(response.read().decode("utf-8"))["members"]

def get_channels():
    with urllib.request.urlopen("https://slack.com/api/channels.list?token={0}".format(USERTOKENSTRING)) as response:
        return json.loads(response.read().decode("utf-8"))["channels"]

def post_message():
    with urllib.request.urlopen("https://slack.com/api/chat.postMessage?token={0}&channel=CHANNELID&text=Hej%20Jonas".format(USERTOKENSTRING)) as response:
        return response.read().decode("utf-8")
