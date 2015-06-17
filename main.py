import urllib.request
import json
import time
import funcs

API_URL = "https://slack.com/api/"

with open("config.json") as config_file:
    settings = json.load(config_file)
    USERTOKENSTRING = settings["USERTOKENSTRING"]
    URLTOKENSTRING = settings["URLTOKENSTRING"]
    TEAMNAMESTRING = settings["TEAMNAMESTRING"]


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

def load_all_users():
    all_users = dict()
    for user in get_users():
        user = User(user["name"], user["id"])
        all_users[user.id] = user
    return all_users        

def get_users():
    with urllib.request.urlopen("{0}api/users.list?token={1}".format(API_URL, USERTOKENSTRING)) as response:
        return json.loads(response.read().decode("utf-8"))["members"]


def get_channels():
    with urllib.request.urlopen("{0}channels.list?token={1}".format(API_URL, USERTOKENSTRING)) as response:
        return json.loads(response.read().decode("utf-8"))["channels"]

def post_message(message):
    #channel "test" id:C06E3DG6S
    params = {
        "channel": "",
        "text": ""
        }
    with urllib.request.urlopen("{0}chat.postMessage?token={1}&channel=C06E3DG6S&text={2}&username=Boten%20Anna".format( \
        API_URL, USERTOKENSTRING, message)) as response:
        return response.read().decode("utf-8")

def get_latest_messages(amount):
    #channel "test" id:C06E3DG6S
    with urllib.request.urlopen("{0}channels.history?token={1}&channel=C06E3DG6S&count=1".format( \
        API_URL, USERTOKENSTRING)) as response:
        return json.loads(response.read().decode("utf-8"))["messages"]

def start_listener(started):
    
    if not started:
        latest_messages = get_latest_messages()
        users = load_all_users()

        for message in latest_messages:
            if message["text"] == "start":
                post_message("Started%20by%20" + users[message["user"]].name)
        return True
    return False

def main():

    started = False

    while True:

        started = start_listener(started)

        if started:
            ##Samla namn å ALLT annat
            ##started = False
            time.sleep(20)
            participants = []
            for message in latest_messages:
                if message["text"] == "go":
                    post_message(users[message["user"]].name + "%20registered")
                    participants.append(users[message["user"]])
            break
        time.sleep(2)
        post_message("Ended")
    
if __name__ == "__main__":
    main()










    
