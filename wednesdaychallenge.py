#!/usr/bin/env python3

def main():

    user_name = input("What is your name? ")

    user_age = input("What is your age? ")

    fav_movie = input("What is your favorite movie? ")

    name = [user_name]

    age = [int(user_age)]

    movie = [fav_movie]

    print("Hello " + name[0].capitalize() + "! you're " + str(age[0]) + " years old and your favorite movie is " + movie[0].capitalize() + "!")

main()    
