import urllib.request
import json
import time
import funcs
import random

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

def start_listener(started, users, latest_messages):
    if not started:
        for message in latest_messages:
            if message["text"] == "start":
                post_message("Started%20by%20" + users[message["user"]].name)
                return True
    return False

def main():

    started = False
    ended = False
    post_message("New%20session%20active.")
    post_message("Type%20'start'%20to%20start.")

    while True:
        
        latest_messages = get_latest_messages(5)
        users = load_all_users()
        started = start_listener(started, users, latest_messages)

        if started:
            
            post_message("Started.%20Type%20'register'%20to%20register")
            time.sleep(20)
            participants = []
            for message in get_latest_messages(10):                

                if message["text"] == "register":
                    post_message(users[message["user"]].name + "%20registered")
                    participants.append(users[message["user"]])
                    ended = True
                elif message["text"] == "Started.%20Type%20'register'%20to%20register":
                    break
                    
        if ended:
            
            post_message("Registered%20participants:")
            participants = list(set(participants))
            for user in participants:
                post_message(user.name)
                
            post_message("Session%20ended")
            break
        
        else:        
            continue          
        time.sleep(2)
        
    
if __name__ == "__main__":
    main()










    
