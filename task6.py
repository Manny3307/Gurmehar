#user_list = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
#passw = ["12345", "abcde", "pass1", "qwert", "aaaaa", "zzzzz", "11111", "apple", "hello", "admin"]
user_pass = {
    "Ava" : "12345",
    "Leo" : "abcde",
    "Raj" : "pass1",
    "Zoe" : "qwert",
    "Max" : "aaaaa",
    "Sam" : "zzzzz",
    "Eli" : "11111",
    "Mia" : "apple",
    "Ian" : "hello",
    "Kim" : "admin"
}

'''west_delhi_picode = {
    "Tilak_Nagar": "110018",
    "Janakpuri": "110019",
    "Patel_Nagar": "110008",
    "FaridaBad": "121001"
}
print(west_delhi_picode.get('Tilak_Nagar'))
'''

trycounter = 3

correct_user = False
robot_flag = True

while(not correct_user):
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")

    if(user_name in user_pass and (user_password in user_pass[user_name] and user_password != "")):
        print(f"Login successful. Welcome {user_name} !")
        correct_user = True
    else:
        print(f"Login incorrect. Tries left: {trycounter - 1}")
        trycounter -= 1
        
        if(trycounter == 0):
            while(robot_flag):
                robot_input = input("Are you a robot (Y/n)?")
                if(robot_input == "n"):
                    trycounter = 3
                    break
                elif(robot_input == "Y"):
                    correct_user = True
                    break