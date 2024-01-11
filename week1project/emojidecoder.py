#!/usr/bin/env python3

import demoji

#declare function
def main():

    name = input("What is your name? ")

    user_correct = input(f"You told me your name is {name.capitalize()}.\nIs this correct? ")

    if user_correct in ["yes", "y", "Yes", "Y"]:
        print(f"Excellent!\nHi {name.capitalize()}! I'm your friendly emoji decoder and I'm able to help you with decoding those tough millennial emoji's.\n")
    elif user_correct in  ["no", "n", "No", "N"]:
            print(name)
            #TASK: if name is incorrect, ask [name] again
    else:
        print(name)
    
    #user includes text with emoji's for demoji module to decode
    user_text = input("Please enter your text with those pesky emoji's here and I'll get to decording right away for you.\nPress [Enter] when you're ready to continue.\n")        

    demoji.findall(user_text)

#call function
main()
