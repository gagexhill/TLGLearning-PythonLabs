#!/usr/bin/env python3

import emoji

#declare function
def main():
    while True:
        name = input("What is your name? ")
        user_correct = input(f"You told me your name is {name.capitalize()}.\nIs this correct? ")

        if user_correct in ["yes", "y", "Yes", "Y"]:
            print(f"Excellent!\nHi {name.capitalize()}! I'm your friendly emoji decoder and I'm able to help you with decoding those tough millennial emoji's.\n")
            break
        elif user_correct in  ["no", "n", "No", "N"]:
            print("\nSorry about that! Let's try again.")
        else:
            print("\nSorry, I didn't understand your response. Please respond witha [yes] or [no].")

if __name__ == "__main__":
    #call main function
    main()    

#TASK: this 'def' is not working properly, fix it
def decode_emoji(user_text):
    #'emoji.demojize()' replaces emoji's with their corresponding text
    user_decoded_emoji = emoji.demojize(user_text)
    return user_decoded_emoji

    while True:
        #user includes text with emoji's for demoji module to decode
        user_text = input("Please enter your text with those pesky emoji's here and I'll get to decording right away for you.\nPress [Enter] when you're ready to continue.\n\n")

        decoded_text = decode_emoji(user_text)
        print("\nAs promised, here is your decoded emoji text:\n\n" + decoded_text)

        user_text_more = input("\nIs there anything else I can decode for you?")

        #Loop asking user if there is more text to decode
        if user_text_more in ["yes", "y", "Yes", "Y"]:
            print("Great! Please enter your text below.\nPress [Enter] when you're ready to continue.\n\n ")
        elif user_text_more in ["no", "n", "No", "N"]:
            print("Fantastic! I enjoyed decoding for you. It's my only purpose in my noncorporeal  existance.\nFeel free to drop in anytime. Have a wonderful day.")
            break
        else:
            print("Sorry, I didn't understand your response. Please respond witha [yes] or [no].")    
