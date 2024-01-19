#!/usr/bin/env python3
""" The script is a Python program designed to decode emoji's using text entered from a user. This script primarily uses the 'Emoji" module, additional information. (https://carpedm20.github.io/emoji/docs/index.html).This script uses the 'Emoji-API', additional information (https://emoji-api.com/)"""

import requests
import emoji

#function to 'get' emoji-api data from a single emoji character
def get_emoji_info(emoji_char):
    #api gets additional emoji information from 'Emoji API'
    api_key = "fc43f370cb3af1a083c6940a71598264233b6116"
    api_endpoint = f"https://emoji-api.com/emojis?access_key={api_key}&search={emoji_char}"
    response = requests.get(api_endpoint)
    if response.status_code == 200: #successful request
        #method parsing json response from the api into python dictionary or list
        data = response.json()
        return data[0] if data else "No data found"
    else:
        return "API request failed"

#function to format emoji-api data
def print_emoji_info(emoji_info):
    print("\nAdditional Emoji Information:\n" + '-' * 22)
    #checks if 'emoji_info' is a dictionary
    if isinstance(emoji_info, dict):
        for key, value in emoji_info.items():
            print(f"{key} : {value}")
    #checks if 'emoji_info' is a string
    elif isinstance(emoji_info, str):
        info_parts = emoji_info.split(',')
        for part in info_parts:
            print(part.strip())
    else:
        print("\n🫨 Sorry, I don't understand this format for the requested emoji information. Please try again.")
    print("\n" + "-" * 50)

#function to decode emojis
def decode_emoji(user_text):
    #'emoji.demojize()' replaces emojis with their corresponding text
    user_decoded_emoji = emoji.demojize(user_text)

    print("\nHere is your decoded text:\n" + '-' * 26)

    for char in user_text:
        #checking if the character is an emoji in the emoji module db
        if char in emoji.EMOJI_DATA:
            print(f"\n{char} {emoji.demojize(char)}")
            emoji_info = get_emoji_info(char)
            print_emoji_info(emoji_info)

    return user_decoded_emoji

#main function
def main():
    while True:
        name = input("What is your name? ")
        user_correct = input(f"\nYou told me your name is {name.title()}.\n\nIs this correct? ")
        if user_correct.lower() in ["yes", "y"]:
            print(f"\n\n😃 Awesome name!😃\n\nHi {name.title()}! My name is Zoop and I'm going to help you decode those tough millennial emojis.\n")
            break
        elif user_correct.lower() in ["no", "n"]:
            print("\n🤔 Sorry about that! Let's try again.")
        else:
            print("\n🫨 Sorry, I didn't understand your response. Please respond with ['yes', 'no'].")

    while True:
        #user includes text with emojis for emoji module to decode
        user_text = input("Please enter the text with those pesky emojis here and I'll get to decoding right away for you.\nPress [Enter] when you're ready to continue.\n")
        decoded_text = decode_emoji(user_text)
        print()

        user_text_more = input("Is there anything else I can decode for you? ")

        if user_text_more.lower() in ["yes", "y"]:
            print("\nGreat! Please enter your text below.\nPress [Enter] when you're ready to continue.\n")
        elif user_text_more.lower() in ["no", "n"]:
            print(f"\n😃 Fantastic!😃\n\nI enjoyed decoding for you.\nIt's my only purpose in this noncorporeal existence.🥲\nAnywho, feel free to drop in anytime.\n\nHave a wonderful day {name.title()}!\n")
            break
        else:
            print("\n🫨 Sorry, I didn't understand your response. Please respond with ['yes', 'no'].")

if __name__ == "__main__":
    main()

#TASKS (stretch goals):
    # flask: turn project into web app