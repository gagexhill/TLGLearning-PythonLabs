#!/usr/bin/env python3

def main():

    user_name = input("What is your name? ")

    user_age = input("What is your age? ")

    fav_movie = input("What is your favorite movie? ")

    name = [user_name]

    age = [int(user_age)]

    movie = [fav_movie]

    print(f"Hello {name[0].capitalize()}! you're {str(age[0])} years old and your favorite movie is {movie[0].title()}!")

    user_genre = input("What is the genre of your favorite movie? ")

    user_actor = input("Who is your favorite star actor in " + movie[0].title() + "?")

    genre = [user_genre]

    actor = [user_actor]

    print(f"Interesting! You like {genre[0].capitalize()} movies, that's so funny, so do I. Although, I'm not sure about your choice of favorite actor... {actor[0].title()}. To each their own I suppose! Haha!! Good luck sport.")

main()    
