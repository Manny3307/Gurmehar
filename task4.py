user_list = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
passeduser = False

while(not passeduser):
    user_name = input("Enter username: ")
    if(user_name not in user_list):
        print(f"Login incorrect.")
    else:
        print(f"Login successful. Welcome {user_name} !")
        passeduser = True