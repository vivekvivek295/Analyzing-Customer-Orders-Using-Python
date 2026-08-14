#!/usr/bin/env python3
"""
Project: Text-Based Adventure Game using Python
Description: An interactive CLI game where an explorer searches for a legendary treasure.
"""

def start_game():
    print("\n--- Welcome to the Adventure Quest! ---")
    
    player_name = input("Please enter your hero's name: ")
    print(f"Welcome, {player_name}! Your legendary quest begins now.\n")
    
    print("You find yourself at a crossroad.")
    print("1. Explore the Dark Forest")
    print("2. Enter the Mysterious Cave")
    
    choice = input("Make your choice (1 or 2): ")
    
    if choice == "1":
        forest_path()
    elif choice == "2":
        cave_path()
    else:
        print("Invalid choice! The adventure ends prematurely.")

def forest_path():
    print("\nYou stepped into the dense, dark forest.")
    print("The trees whisper secrets. You see two paths ahead:")
    print("1. Follow the glowing river")
    print("2. Climb the ancient tree")
    
    choice = input("Make your choice (1 or 2): ")
    
    if choice == "1":
        print("\nSuccess! The river leads you to a hidden chest filled with gold. YOU WIN!")
    else:
        print("\nOh no! A branch snaps under your weight. You fall and the adventure ends. GAME OVER!")

def cave_path():
    print("\nYou entered the cold, dark cave.")
    print("It's pitch black. You have limited options:")
    print("1. Light your torch")
    print("2. Proceed carefully in the dark")
    
    choice = input("Make your choice (1 or 2): ")
    
    if choice == "1":
        print("\nThe torch light reveals a path to an ancient relic. YOU WIN!")
    else:
        print("\nYou stumble over a rock and get lost in the darkness. GAME OVER!")

def main():
    while True:
        start_game()
        
        restart = input("\nDo you want to embark on another quest? (yes/no): ").lower()
        if restart != "yes":
            print("\nThank you for playing! Farewell, brave hero.")
            break

if __name__ == "__main__":
    main()