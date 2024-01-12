#!/usr/bin/env python3
""" The script is a Python program designed to decode emoji's, primarily using the 'Emoji' module, in text entered by a   user. """

import emoji

#function to decode emojis
def decode_emoji(user_text):
    #'emoji.demojize()' replaces emojis with their corresponding text
    user_decoded_emoji = emoji.demojize(user_text)

    #iterating through each character
    for char in user_text:
        #checking if the character is an emoji
        if char in emoji.EMOJI_DATA:
            print(f"\nHere is your decoded text:\n{char} : {emoji.demojize(char)}")
            #visual seperator for user readability
            print("-" * 50)

    return user_decoded_emoji

#main function
def main():
    while True:
        name = input("What is your name? ")
        user_correct = input(f"You told me your name is {name.title()}.\nIs this correct? ")

        if user_correct.lower() in ["yes", "y"]:
            print(f"\n😃 Excellent!😃\nHi {name.title()}! I'm your friendly emoji decoder and I'm able to help you with decoding those tough millennial emoji's.\n")
            break
        elif user_correct.lower() in ["no", "n"]:
            print("\n🤔 Sorry about that! Let's try again.")
        else:
            print("\n🫨 Sorry, I didn't understand your response. Please respond with 'yes' or 'no'.")

    while True:
        #user includes text with emojis for demoji module to decode
        user_text = input("\nPlease enter your text with those pesky emoji's here and I'll get to decoding right away for you.\nPress [Enter] when you're ready to continue.\n")

        decoded_text = decode_emoji(user_text)
        print()

        user_text_more = input("Is there anything else I can decode for you? ")

        if user_text_more.lower() in ["yes", "y"]:
            print("\nGreat! Please enter your text below.\nPress [Enter] when you're ready to continue.\n")
        elif user_text_more.lower() in ["no", "n"]:
            print("\n😃 Fantastic!😃\n\nI enjoyed decoding for you.\nIt's my only purpose in my noncorporeal existence.\nFeel free to drop in anytime.\n\nHave a wonderful day!\n")
            break
        else:
            print("\n🫨 Sorry, I didn't understand your response. Please respond with 'yes' or 'no'.")

if __name__ == "__main__":
    main()