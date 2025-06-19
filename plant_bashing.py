import time
import random
import sys
import os
#print("is running at START")
name = ""
day = 1
height = 0
leaves = 0
play_time = 0
weather = ["Rainy", "Sunny", "Cloudy", "Overcast", "Windstorm", "Rainy", "Foggy"]
plantNames= ["Morpheus", "Analies", "Izzy"]
morpheus = 0
analies=0
izzy = 0
growth_rate = 0


def greet_player():
    os.system('clear')
    global name
    print("Welcome to the game!")
    name = input("What is your name? ")
    print(f"Hello {name}!")
    time.sleep(3)
    


def if_answer_valid(input):
    input = input.strip().lower()
    return input in ['y', 'yes', 'n', 'no']


def choose_weather():
    global weather
    picked =random.choice(weather)

    return picked

def weather_effects(weather):
    global growth_rate
    global leaves

    if weather == "Rainy":
        growth = False
        growth_rate += 2
    elif weather == "Sunny":
        growth = True
        growth_rate += 3
    elif weather == "Cloudy":
        growth = False
    elif weather == "Overcast":
        growth = True
    elif weather == "Windstorm":
        growth = False
        growth_rate -= 2
        leaves -= 2
    elif weather == "Foggy":
        growth = False
        growth_rate -= 1

    if leaves < 0:
        leaves = 0
    if growth_rate < 0:
        growth_rate = 0
    
    return growth


    
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


def assign_name():
    global plantNames
    global morpheus
    global analies
    global izzy
    if is_yes_or_no("Do you want to name the plant?"):
        plant_name = input("What do you want to name it? ")
    else:
        if morpheus == 0:
            plant_name = plantNames[0]
            morpheus += 1
        elif analies == 0:
            plant_name = plantNames[1]
            analies += 1
        elif izzy == 0:
            plant_name = plantNames[2]
            izzy += 1
        else:
            plant_name = plant_name[0]
            morpheus = 1
            analies = 0
            izzy = 0
    
    print(f"Your plant's name is {plant_name}!")



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


def apply_growth(growth):
    global growth_rate
    global height
    global leaves

    if growth:
        height += 1.5
        gain_leaves = 2 + 2.5 * growth_rate
        leaves += round(gain_leaves)
    print(f"Height: {height}")
    print(f"Leaves: {leaves}")


def game_loop():
    global day, height, leaves
    day = 1
    height = 0
    leaves = 0

    while is_yes_or_no("continue?"):

        if day <= 5:
            print(f"Day {day}")
            messsage = store_message(day)
            print(messsage)
            day += 1
        elif height <= 32:
            print(f"Day {day}")
            today_weather = choose_weather()
            print(today_weather)
            growth = weather_effects(today_weather)
            
            apply_growth(growth)
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

    while is_yes_or_no("\nWould you like to grow a new plant?\n"):
        assign_name()
        print("In the Computer's digital world, time moves much faster than it does outside.")
        game_loop()

    farewell_player()

   

if __name__ == "__main__": 
    main()