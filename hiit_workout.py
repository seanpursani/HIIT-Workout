import random
import json
import time

"""This console app creates and performs a custom HIIT workout based on given user information 
    by extracting exercises from a JSON file"""
    

def main():
    level = difficulty_level()
    length = length_of_hiit()
    focus = workout_focus()
    print(f"\nYou have chosen a {length} minute {level} workout, with extra focus on {focus}!")
    hiit_set = get_exercises(level, focus)
    show_hiit_routine(hiit_set)
    start_hiit(length, hiit_set, level)


def number_sets(length):
    
    """
    Summary: Determines the total amount of sets the user will do during the workout
    Args: length [integer]: either 15 or 30 representing total minutes of workout
    Returns: [integer] representing the amount of sets in the routine 
    """
    
    if length == '15':
        return 3
    else:
        return 6


def workout_times(level):
    
    """
    Summary: Determines active and rest times for the workout which together equal 1 minute in total
    Args: level [string]: Either 'beginner', 'intermediate' or 'advanced'
    Returns: [integer]: a tuple of 2 integer elements representing active and rest time in seconds
    """
    
    if level == 'beginner':
        return 30, 30
    elif level == 'intermediate':
        return 40, 20
    else:
        return 45, 15


def start_hiit(length, hiit_set, level):
    
    """
    Summary: This initiates the workout and prints instructions onto the console
    Args:
        length [integer]: Either 3 or 6 representing the amount of routine repetitions 
        hiit_set [list]: A list containing 5 different exercises
        level [string]: 'Beginner', 'Intermediate' or 'Advanced'
    """
    
    sets = number_sets(length)
    active, rest = workout_times(level)
    input("Press enter when you are ready to start!")
    print("\nStarting in...\n")
    countdown(5)
    for x in range(sets):
        print(f"\nSet number {x + 1}!")
        for y in range(len(hiit_set)):
            print(f"\n{str.upper(hiit_set[y])}\n", end="\r")
            countdown(active)
            print(f"\nTake a {rest} second break!")
            countdown(rest)


def countdown(t):
    
    """
    Summary: Timer to count user into the workout
    Args: t [integer]: Starting number from which to countdown from 
    """
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("")


def show_hiit_routine(hiit_set):
    
    """
    Summary: Displays HIIT routine
    Args: hiit_set [list]: Exercises in the HIIT routine
    """
    
    print("\nHere's your workout for today...\n")
    for x in hiit_set:
        print(str.upper(x))
    print("")


def get_exercises(level, focus):
    
    """
    Summary: Gets the exercises for the workout based on level and focus 
    Args:
        level [string]: Either 'beginner', 'intermediate' or 'advanced'
        focus [string]: One of 4 options: 'core', 'upper body', 'lower body', 'cardio'
    Returns: [list]: 5 different exercises for the workout
    """
    
    # load JSON file
    # use 'r' raw string treating (\) as a literal character
    with open(r"C:\Users\seanp\Software Dev\PYTHON CIP PROJECTS\CodeInPlace\FinalProject\exercises.json") as f:
        exercises = json.load(f)
        
    # create list to append exercises into
    hiit_set = []
        
    # loop through key value pairs in the json
    for category in exercises:
        for difficulty in exercises[category].items():
                
            # if difficulty is equal to user level append a random exercise to list
            if difficulty[0] == level:
                # if the exercise is identical to one already generated, repeat until given a unique item
                while True:
                    exercise = random.choice(list(exercises[category][level]))
                    if exercise not in hiit_set:
                        hiit_set.append(exercise)
                        break
                        
    # append the 5th exercise which is based on the users chosen 'focus', again avoiding duplicates
    while True:
        focus = random.choice(list(exercises[focus][level]))
        if focus != hiit_set[-1]:
            hiit_set.append(focus)
            break

    return hiit_set


def workout_focus():
    
    """
    Summary: Determines the last exercise in the HIIT routine so the user can 'focus' on that area 
    Returns: [string]: One of 4 options: 'core', 'upper body', 'lower body', 'cardio'
    """
    
    while True:
        focus = input("\nWhat would you like to focus on your core, upper body, lower body or cardio? ")
        if focus not in ('core', 'upper body', 'lower body', 'cardio'):
            print("Oops! I didn't understand that! Try again.\n")
            continue
        else:
            return focus


def length_of_hiit():
    
    """
    Summary: Determines the length of the workout by asking for input from user
    Returns: [string]: Either 15 or 30 (minutes)
    """
    
    while True:
        length = input("\nSelect the length of your workout in minutes: 15 or 30? ")
        if length not in ('15', '30'):
            print("Oops! I didn't understand that! Try again.\n")
            continue
        else:
            return length


def difficulty_level():
    
    """
    Summary: Determines the level of the user by asking for input from user
    Returns: [string]: Either 'beginner', 'intermediate', 'advanced'
    """
    
    while True:
        level = input("\nSelect beginner, intermediate or advanced: ")
        if level not in ('beginner', 'intermediate', 'advanced'):
            print("\nOops! I didn't understand that! Try again.")
            continue
        else:
            return level


if __name__ == '__main__':
    main()
