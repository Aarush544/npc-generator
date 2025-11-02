import time
import random

#Lists used for attributes and animation
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
personality_options = ["kind", "intellegent", "courageous", "skilled", "crafty", "creative", "calm"]        
professions = ["blacksmith", "farmer", "mason", "butcher", "fletcher"]


# Prints slowly so it looks cool

def cool_print(word_to_print):  
    for i in word_to_print:
        print(i, end = "", flush = True)
        time.sleep(0.1)

class NPC:
    # initializes class
    def __init__(self, name, gender, height, personality, profession, hostility):
        self.name = name
        self.gender = gender
        self.height = height
        self.personality = personality
        self.profession = profession
        self.hostility = hostility
    
    # Makes cool scrambling animation  

    def random_animation(self, name, gender, height, personality, profession, hostility ):
        global personality_options
        global professions
        begin_time = time.time()
        duration = 1.2
        while True:
            #changes the variable to give scrambling animation
            self.name = f"{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}"
            self.gender = f"{random.choice(["male", "female"])}"
            self.height = f"{random.randint(4, 7)}\"{random.randint(1, 12)}"
            self.personality = f"{random.choice(personality_options)}"
            self.profession = f"{random.choice(professions)}"
            self.hostility = f"{random.choice(["hostile", "friendly"])}"
            print(f"\r{self.name} is a {self.gender} person who is {self.height}. They are a {self.personality} {self.profession} who is {self.hostility} to you.", end = "", flush=True)
            
            #exits after certain amount of time

            if (time.time() - begin_time) > duration:
                break
            time.sleep(0.01)
        print("\r                                                                                                         ")
        
        
# Asks use for gender of NPC with error handling. Loops until valid input

def gender_check():
    cool_print("Enter the corresponding number for the gender:\n1. Male\n2. Female\nAnswer: ")
    gender_input = (input())
    while gender_input != '1' and gender_input != '2':   
        cool_print("Invalid")
        cool_print("Enter the corresponding number for the gender of the NPC:\n1. Male\n2. Female\nAnswer: ")
        gender_input = input("")
    output = "male" if gender_input == "1" else "female"  
    return output


# Asks for number of NPCs

cool_print("Enter the amount of NPCs you want to generate: ")
count = int(input(""))
   
# main part that loops for each NPC 

for i in range(1, count + 1):
    character = NPC(0,0,0,0,0,0)
    
    # Gets all of the attributes
    print("___________________________________________________________")
    cool_print("\nEnter NPC name: ")
    character.name = input("")
    character.gender = gender_check()
    character.height = f"{random.randint(50, 80)} inches"
    character.personality = random.choice(personality_options)
    character.profession = random.choice(professions)
    character.hostility = random.choice(["hostile", "friendly"]) 
    
    pronoun = "He" if character.gender == "male" else "She"

    answer = f"{character.name} is a {character.gender} person who is {character.height} tall. {pronoun} is a {character.personality} {character.profession} who is {character.hostility} to you."
    character.random_animation(0, 0, 0, 0, 0, 0)
    
    #Outputs the result

    print(f"NPC #{i}")
    print("\r")
    print(answer, flush = True)
