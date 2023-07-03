import datetime
import time

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

time.sleep(3)

direction = input("Which direction would you like to head? (N)orth, (E)ast, (S)outh, or (W)est:")
    
if direction == "N":
     print("You are headed northward. Bring a coat; it's going be be cold where you're going!")

if direction == "E":
     print("You are headed eastward. Bring a healthy appetite; the eating is good where you're going!")

if direction == "S":
     print("You are headed southhward. Bring an airconditioner; it's going be be hot as F where you're going!")

if direction == "W":
     print("You are headed westhward. Bring your hiking boots; The mountains of Colorado are beautiful! Just be careful to avoid the diamondbacks, and whatever you do, DON'T STEP ON THE TUNDRA!!!")