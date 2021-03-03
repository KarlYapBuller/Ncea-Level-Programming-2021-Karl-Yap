import random

#Functions

#Gambling implications function
def gambling_implications(question):
    valid = False
    while not valid:
        response = input(question).lower()
#If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response
#If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response
#If user response is anything other than yes or no,user will be asked to answer yes or no.
        else:
            print("<error> please answer yes/no")
#gambling implication instructions, this will appear if user answers no to if they understand gambling implications.
def gambling_implications_instructions():
    print("*****Gambling Implications*****")
    print("Harm from gambling is not solely just losing money")
    print("Gambling can affect affect many aspects of a person's life such as")
    print("self-esteem, relationships, mental health and social life.")
    print("Gambling can cause extreme emotions and mood swings,")
    print("feeling that gambling is the only thing you can")
    print("enjoy;you can find other thing that are not gambling boring,")
    print("difficulty sleeping,have suicidal thoughts and")
    print("feel depressed or anxious.")
    print("Gambling does not only affect the gambler, but it can also affect ")
    print("the people around the gambler like their friends and family.")
    return""

#Played before function
def played_before(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> please answer yes/no")
#Game information function
def game_information():
    print("*****Game information*****")
    print("Doctors without borders")
    print("Rules of the game")
    print()
    print()
    return""

#Ask user how much they want to play for function
def number_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            #Ask the question
            response = int(input(question))

            #If the amount is to low/to high give
            if low < response <= high:
                return response

            #Output an error
            else:
                print(error)

        except ValueError:
            print(error)

#Main Routine goes here

#Calls gambling implication functions
show_gambling_implications = gambling_implications("Do you undertand the implications of gambling?")

#If user answers yes, ask user if they have played before is run
if show_gambling_implications == "yes":
    print("program continues")

else:
    gambling_implications_instructions()

#Calls ask user if they have played before funtionand game information
show_played_before = played_before("Have you played this game before?")

if show_played_before == "no":
    game_information()

print("program continues")

#Ask user how much they want to play with
how_much = number_check("How much money would you like to play with? ", 0, 10)

#Round looping
balance = how_much

rounds_played = 0

#.lower is used just in case user types in exit code, 'xxx' in uppercase
play_again = input("Press <Enter> to play").lower()
while play_again == "":

    #Increase #rounds played
    rounds_played += 1

    #Print number of rounds played
    print("*****Round#{}*****".format(rounds_played))

    chosen_number = random.randint(0,100)

    #Adjust balance of user
    #if the random #is between 1 and 5
    #User gets a Unicorn (add $4 to balance)
    if 1 <= chosen_number <= 5:
        chosen = "Unicorn"
        balance += 4

    #If the random #is between 6 and 36
    #User gets a Donkey (subtract $1 from balance)
    elif 6 <= chosen_number <= 36:
        chosen = "Donkey"
        balance -= 1

    #Token is either a Horse or Zebra
    #If user gets either a Horse or Zebra (subtract $0.50 from balance)
    else:
        #If number is even token generated is a Horse
        #Chosen item is Horse
        if chosen_number % 2 == 0:
            chosen = "Horse"
        #If number is not even token generated is a Zebra
        #Chosen item is a Zebra
        else:
            chosen = "Zebra"
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f} ".format(chosen,balance))

#If balance is less than one program displays sorry you have run out of money
#User can choose if they want to continue the game or quit the game
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press <Enter> to play again or 'xxx' to quit game")
        print()

print()
print("Final balance", balance)



