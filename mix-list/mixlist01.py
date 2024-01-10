#!/usr/bin/env python3

def main():

    wordbank = ["indentation", "spaces"]

    tlgstudents = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    wordbank.append(4)

    num = int(input("Pick a student number? [0-20] "))

    name = tlgstudents[num]

    print(f"Your tribute is {name}.")

main()    
