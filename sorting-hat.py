#!/usr/bin/env python3
""" WRITE YOUR OWN IF-LOGIC SCRIPT! Sorting Hat Project """


def main():

    # Display the game menu while user is playing
    while True:
        display_menu()


def take_quiz():

    # Create a dictionary to keep count of the house
    points_counter = {"gryffindor": 0, "slytherin": 0, "ravenclaw": 0, "hufflepuff": 0}

    print("Welcome to Hogwarts!")

    # get the name of our young wizard
    first = input("What is your first name? ")
    last = input("What is your last name? ")

    # clean up the input
    first_name = first.lower().rstrip().capitalize()
    last_name = last.lower().rstrip().capitalize()

    print(f"Very well {first_name} {last_name}")

    print("It's time for us to sort you into your house.")
    print("\n* Professor McGonagall places the sorting hat on your head. *")

    if last_name == "Weasley":
        print("\nSorting Hat: \"Another Weasley, I know just what to do with you - Gryffindor!\"\n")
        return

    # Ask question one
    print("\nWhich of these traits best describes you? "
          "\n(a) Loyal"
          "\n(b) Cunning"
          "\n(c) Brave"
          "\n(d) Clever")
    # Grab the user response
    question_one = get_user_input()
    # Increment the house in points counter
    points_counter[evaluate_response(question_one)] += 1

    # Ask question two
    print("\nWhich house were your parents in? "
          "\n(a) Hufflepuff"
          "\n(b) Slytherin"
          "\n(c) Gryffindor"
          "\n(d) Ravenclaw"
          "\n(e) My parents are muggles!")
    # Grab the user response
    question_two = get_user_input()
    # if they parents didn't go to hogwarts then we skip this response
    if question_two != "e":
        # Increment the house in points counter
        points_counter[evaluate_response(question_two)] += 1

    # Ask question three
    print("\nWhich best describes you when playing board games? "
          "\n(a) I play them just to enjoy time with my friends and family"
          "\n(b) I look at games from all angles and find the loopholes"
          "\n(c) I take board games too seriously"
          "\n(d) Not to boast, but I nearly always win without trying")
    # Grab the user response
    question_three = get_user_input()
    # Increment the house in points counter
    points_counter[evaluate_response(question_three)] += 1

    # Ask question four
    print("\nDo you have a thirst to prove yourself? "
          "\n(a) I don’t feel the need to shout about my achievements in the same way as the others"
          "\n(b) Of course, reputation is important to me"
          "\n(c) Absolutely not"
          "\n(d) Not exactly, but I can be an over achiever")
    # Grab the user response
    question_four = get_user_input()
    # Increment the house in points counter
    points_counter[evaluate_response(question_four)] += 1

    # Decide which house to place the young wizard
    house = calculate_house(points_counter)

    print(f'\nSorting Hat: \"Your house is {house}!\"\n')


def evaluate_response(response):
    house = ""
    if response == "a":
        house = "hufflepuff"
    elif response == "b":
        house = "slytherin"
    elif response == "c":
        house = "gryffindor"
    else:
        house = "ravenclaw"

    return house


def calculate_house(house_dict):
    # set max value to 0
    max_value = 0
    # set house name to empty
    house_name = ""

    # find the house with the max number of points
    for key in house_dict.keys():
        if house_dict.get(key) > max_value:
            house_name = key
            max_value = house_dict.get(key)

    return house_name.capitalize()


def get_user_input():
    user_input = input("User input: ")
    return user_input.lower().rstrip()


def get_name():
    return None


def display_menu():
    user_input = input("Chose an option young wizard:"
                       "\n (a) Take the sorting hat quiz."
                       "\n (b) Quit Game"
                       "\n User input: ")
    # if user enters a then take the quiz
    if user_input == "a":
        take_quiz()
    else:
        print("Game Over")
        exit()


if __name__ == "__main__":
    main()