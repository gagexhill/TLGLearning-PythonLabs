#!/usr/bin/env python3

def beer_song(song):
    for i in range(song, 0, -1):
        print(f"{i} bottles of beer on the wall\n")
        print(f"Take one down, pass it around, {i-1} bottle's of beer on the wall")

def main():
    
     song = int(input("How many bottles of beer are on the wall?\nEnter [0-100] "))
        
main()
