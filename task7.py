# abcdefghijklm
# nopqrstuvwxyz

#h e l p i a m s e n t i e n t

#k rrrrrrrrrrp
#  rrrrrrrrrrp

# a b c d e f g h i j k l m
# n o p q r s t u v w x y z

# rrrrrrrp - h
# lllp - e
# rrrrrrrp - l
# llllllllldp - p
# rrrrrrup - i
# llllllllp - a
# rrrrrrrrrrrrp - m
# llllllldp - s
# lup - e
# lllldp - n
# rrrrrrp - t
# rrup - i
# llllp - e
# lllldp - n
# rrrrrrp - t
key_conf = ["abcdefghijklm", "nopqrstuvwxyz"]
input_str = input("Enter a string to type: ")
character_position = 0 
robbie_instruction = ""
conf_row_counter = 0


def get_row_count(conf_char, key_conf):
    row_number = 0
    for i in key_conf:
        row_number += 1
        if conf_char in i:
            return row_number        

def get_last_string(conf_char, key_conf, last_row_number, first_entry):
    last_str = ""
    if(first_entry):
        row_number = 0
    else:
        row_number = get_row_count(conf_char, key_conf)
    
    if(row_number > last_row_number):
        diff_row = row_number - last_row_number
        #print(diff_row)
        last_str = "d" * diff_row + "p"
    else:
        diff_row = last_row_number - row_number
        last_str = "u" * diff_row + "p"
    
    if(diff_row == 0):
        last_str = "p"

    return last_str

def generate_robbie_str(input_str, key_conf):
    last_row_number = 0
    first_entry = True
    Last_character_position = 0
    robbie_instruction_str = ""
    for i in input_str: #i = g input_str = gurmehar
        for j in key_conf: #j = abcdefghijklm , nopqrstuvwxyz
            if(i in j):
                row_number = get_row_count(i, key_conf)
                last_str = get_last_string(i, key_conf, last_row_number, first_entry)
                character_position = (j.find(i)) + 1 #j.find('g')
                calculated_position = character_position - Last_character_position  
                Last_character_position = character_position
                if(calculated_position <= 0):
                    robbie_instruction = "l" * abs(calculated_position) + f"{last_str} - {i} \n"
                else:
                    robbie_instruction = "r" * (calculated_position) + f"{last_str} - {i} \n"

                robbie_instruction_str += robbie_instruction 
                first_entry = False
                last_row_number = row_number

    if(robbie_instruction_str == ""):
        robbie_instruction_str = "The string cannot be typed out."
    
    return robbie_instruction_str

get_robbie_str = generate_robbie_str(input_str, key_conf)
print(get_robbie_str)