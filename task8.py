'''key_conf_0 = ["abcdefghijklm", "nopqrstuvwxyz"]
key_conf_1 = ["789","456","123","0.-"]
key_conf_2 = ["chunk","vibex","gymps","fjord","waltz"]
key_conf_3 = ["bemix","vozhd","grypt","clunk","waqfs"]
'''
key_confs=[["abcdefghijklm", "nopqrstuvwxyz"], ["789","456","123","0.-"], 
           ["chunk","vibex","gymps","fjord","waltz"], ["bemix","vozhd","grypt","clunk","waqfs"]]

input_str = input("Enter the string: ")

def get_row_count(conf_char, key_conf):
    row_number = 0
    for i in key_conf:
        row_number += 1
        if conf_char in i:
            return row_number        

def get_last_string(conf_char, key_conf, last_row_number, first_entry):
    last_str = ""
    
    row_number = get_row_count(conf_char, key_conf)

    if(first_entry):
        row_number -= 1

    if(row_number >= last_row_number):
        diff_row = row_number - last_row_number
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
    robbie_instruction_without_newline = ""
    robbie_instr = ""
    for i in input_str:
        for j in key_conf:
            if(i in j):
                row_number = get_row_count(i, key_conf)
                last_str = get_last_string(i, key_conf, last_row_number, first_entry)
                character_position = (j.find(i)) + 1
                calculated_position = character_position - Last_character_position  
                Last_character_position = character_position
                if(first_entry):
                    calculated_position -= 1

                if(calculated_position <= 0):
                    robbie_instruction = "l" * abs(calculated_position) + f"{last_str} - {i} \n"
                    robbie_instr = "l" * abs(calculated_position) + f"{last_str}"
                else:
                    robbie_instruction = "r" * (calculated_position) + f"{last_str} - {i} \n"
                    robbie_instr = "r" * (calculated_position) + f"{last_str}"

                robbie_instruction_str += robbie_instruction 
                robbie_instruction_without_newline += robbie_instr 
                first_entry = False
                last_row_number = row_number
                
                

    if(robbie_instruction_str == ""):
        robbie_instruction_str = "The string cannot be typed out."
    
    return f"{robbie_instruction_without_newline}|{robbie_instruction_str}"

no_str = "The string cannot be typed out."
collated_str = ""
len_collated_str = []
conf_used = []

for conf in key_confs:
    get_robbie_str = generate_robbie_str(input_str, conf)
    if(no_str not in get_robbie_str):
        collated_str = get_robbie_str.split('|')[0]
        robbie_output_length = (len(collated_str))
        present_conf = conf
        present_conf_output = get_robbie_str.split('|')[1]
        conf_used.append([f"{robbie_output_length}|{present_conf}|{present_conf_output}|{collated_str}"])
        len_collated_str.append(robbie_output_length)

min_output = min(len_collated_str)



for conf in conf_used:
    for child_conf in conf:
        child_conf_arr = child_conf.split('|')
        robbie_moves = int(child_conf_arr[0])
        if(robbie_moves == min_output):
            print("+++++++++++++++++++++++Configuration chosen by Robbie++++++++++++++++++\n")
            print(f"{child_conf_arr[1]} \n")
            print("+++++++++++++++++++++++Output based on chosen configuration++++++++++++++++++\n")
            print(f"{child_conf_arr[3]} \n")
            print("+++++++++++++++++++++++Output in readable format++++++++++++++++++\n")
            print(child_conf_arr[2])
            



'''rdddp
luuup
ddp
rrup

rrp - . 
luuup - 7 
ddp - 1 
rrup - 6 '''
#print(key_confs[1])