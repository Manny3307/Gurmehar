#user = ["Gurmehar", "Raj", "Rahul", "Cathy", "John"]
user_list = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
#passw = ["pass1", "12345", "pass2", "pass3", "pass4"]
passw = ["12345", "abcde", "pass1", "qwert", "aaaaa", "zzzzz", "11111", "apple", "hello", "admin"]

trycounter = 3

passeduser = True
while(passeduser):
    username = input("Please enter your username: ")
    if(username in user_list):
        passeduser = False
    

if(username not in user_list):
    print("User not in the List!")
else:
    while(trycounter > 0):
        password = input("Enter your password: ")
        if(password in passw):
            print(f"Welcome {username}!")
            quit(0)
        else:
            trycounter = trycounter - 1
            if(trycounter != 0):
                print(f"tries left {trycounter}")
            else:
                print("No tries left!")
                quit(0)