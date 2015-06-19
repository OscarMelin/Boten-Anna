import time
import api
import random


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

def load_all_users():
    all_users = dict()
    for user in api.get_users():
        user = User(user["name"], user["id"])
        all_users[user.id] = user
    return all_users        

def start_listener(started, users, latest_messages):
    """
    First stage.
    """
    if not started:
        for message in latest_messages:
            if message["text"] == "start":
                api.post_message("Started%20by%20" + users[message["user"]].name)
                return True
    return False

def register():
    """
    Second stage.
    """
    pass

def choose_loser():
    """
    Last stage.
    """
    pass

def main():

    started = False
    ended = False
    api.post_message("New%20session%20active.")
    api.post_message("Type%20'start'%20to%20start.")

    while True:
        
        latest_messages = api.get_latest_messages(5)
        users = load_all_users()
        started = start_listener(started, users, latest_messages)

        if started:
            started_message = "Started.%20Type%20'register'%20to%20register"
            api.post_message(started_message)
            time.sleep(20)
            participants = []
            for message in api.get_latest_messages(10):                
                if message["text"] == "register":
                    api.post_message(users[message["user"]].name + "%20registered")
                    participants.append(users[message["user"]])
                    ended = True
                elif message["text"] == started_message.replace("%20", " "):
                    break
                    
        if ended:
            
            api.post_message("Registered%20participants:")
            #Remove duplicate registrations
            participants = list(set(participants))
            for user in participants:
                api.post_message(user.name)

            api.post_message("Loser:%20{0}".format(random.choice(participants).name))
            api.post_message("Session%20ended")
            break
        
        else:        
            continue          
        time.sleep(2)
        
    
if __name__ == "__main__":
    main()










    
