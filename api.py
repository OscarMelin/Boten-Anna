import json
import urllib.request


API_URL = "https://slack.com/api/"

with open("config.json") as config_file:
    settings = json.load(config_file)
    USERTOKENSTRING = settings["USERTOKENSTRING"]
    URLTOKENSTRING = settings["URLTOKENSTRING"]
    TEAMNAMESTRING = settings["TEAMNAMESTRING"]

def get_users():
    with urllib.request.urlopen("{0}users.list?token={1}".format(API_URL, USERTOKENSTRING)) as response:
        return json.loads(response.read().decode("utf-8"))["members"]


def get_channels():
    with urllib.request.urlopen("{0}channels.list?token={1}".format(API_URL, USERTOKENSTRING)) as response:
        return json.loads(response.read().decode("utf-8"))["channels"]

def post_message(message):
    #channel "test" id:C06E3DG6S
    with urllib.request.urlopen("{0}chat.postMessage?token={1}&channel=C06E3DG6S&text={2}&username=Boten%20Anna".format( \
        API_URL, USERTOKENSTRING, message)) as response:
        return response.read().decode("utf-8")

def get_latest_messages(amount):
    #channel "test" id:C06E3DG6S
    with urllib.request.urlopen("{0}channels.history?token={1}&channel=C06E3DG6S&count={2}".format( \
        API_URL, USERTOKENSTRING, str(amount))) as response:
        return json.loads(response.read().decode("utf-8"))["messages"]

