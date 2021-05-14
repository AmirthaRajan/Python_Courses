import json
import pickle

user_input = True
users = []
mode = '1'

def save_data():
    if mode == '2':
        with open('user.p',mode='wb') as f:
            f.write(pickle.dumps(users))
            print("data saved in pickle")
    elif mode == '1':
         with open('user.json',mode='w') as f:
            f.write(json.dumps(users))
            print("data saved json")

def load_data():
    global users
    if mode == '2':
        with open('user.p',mode='rb') as f:
            file_data = f.read()
            users = pickle.loads(file_data)
    elif mode == '1':
         with open('user.json',mode='r') as f:
            file_data = f.read()
            users = json.loads(file_data)

def set_user():
    print("select a mode to read and write")
    print("1 : json")
    print("2 : pickle")
    global mode
    mode = input("Enter data mode")
    user_name = input("Enter user name")
    user_gender = input("Enter user gender")
    user_faction = input("Enter user faction")
    user_race = input("enter user race ")
    user_class = input("Enter user class")

    user = {
        'name' : user_name,
        'gender' : user_gender,
        'faction' : user_faction,
        'race' : user_race,
        'class' : user_class
    }

    users.append(user)
    save_data()

def get_user():
    load_data()
    print(users)


while user_input:
    print("1 : Enter user details")
    print("2 : Show user details")
    print("q : Quit")
    user_choice = input("Enter your option")
    if user_choice == '1':
        set_user()
    elif user_choice == '2':
        get_user()
    elif user_choice == 'q':
        user_input = False
    else:
        print("Enter a valid choice")
print("done!")

