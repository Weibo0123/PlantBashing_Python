import time
import random
import sys
#print("is running at START")
name = ""
day = 1
height = 0
leaves = 0
play_time = 0


def greet_player():
    global name
    print("Welcome to the game!")
    name = input("What is your name? ")
    print(f"Hello {name}!")
    time.sleep(3)
    print("In the Computer's digital world, time moves much faster than it does outside.")


def if_answer_valid(input):
    input = input.strip().lower()
    return input in ['y', 'yes', 'n', 'no']


def choose_weathear():
    weather = ["Rainy", "Sunny", "Cloudy", "Overcast", "Windstorm", "Rainy", "Foggy"]
    picked =random.choice(weather)

    return picked
    
def is_yes_or_no(prompt="Please answer"):
    while True:
        choice = input(f"{prompt} (yes/no): ").strip().lower()
        if if_answer_valid(choice):
            if choice in ['y', 'yes']:
                return True  # user chose yes
            else:
                return False  # user chose no
        else:
            print("You can only answer yes or no. Please try again\n")


def store_message(day):
    if day == 1:
        message = "You have planted a seed in the soil. It looks like a grain of rice."
    elif day == 2:
        message = "The seed germinated overnight!"
    elif day == 3 or day == 4:
        message = "Nothing happened, do you want to wait for one more day?"
    elif day == 5:
        message = "The plant grew overnight into a sapling!"
    else:
        message = "Do you want to wait for the plant to grow?"

    return message


def farewell_player():
    print("Thank you for playing!")
    print(f"See you {name}!")
    
    sys.exit()


def apply_growth():
    global height
    global leaves
    height += 2
    leaves += 2
    print(f"Height: {height}")
    print(f"Leaves: {leaves}")


def game_loop():
    global day, height, leaves
    day = 1
    height = 0
    leaves = 0

    while is_yes_or_no("contimue?"):

        if day <= 5:
            print(f"Day {day}")
            messsage = store_message(day)
            print(messsage)
            day += 1
        elif height <= 32:
            print(f"Day {day}")
            weather = choose_weathear()
            print(weather)
            apply_growth()
            messsage = store_message(day)
            print(messsage)
            day += 1
        else:
            print ("Your plant is mature!")
            print (f"Days lived: {(day - 1)}")
            print (f"Final height: {height} cm")
            print (f"Total leaves: {leaves}")
            global play_time
            play_time += 1
            break

def main():
    #print("is running in MAIN")
    greet_player()

    while is_yes_or_no("\nWould you like to grow a new plant?"):
        game_loop()

    farewell_player()

   

if __name__ == "__main__": 
    main()