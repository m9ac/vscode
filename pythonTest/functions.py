import datetime

#print ("the print command is actually a function! The parenthese are a clue.")

def greet(name):
    dt = datetime.datetime.now()

    if dt.hour <= 11:
        greeting = "morning"
    elif dt.hour <= 17:
        greeting = "afternoon"
    else:
        greeting = "night"
    
    print("Hello, " +name+ " good " + greeting+ ".")
username = input("What is your name? ")
greet(username)
