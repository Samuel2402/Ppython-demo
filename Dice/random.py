
import random

def rolldice(min, max):
    print("rolling dice...") 
    number = random.randint(min, max) 
    print(f"You have rolled a : {number}")

rolldice(1,6)
 


