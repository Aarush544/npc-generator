import time
import random

#Lists used for attributes and animation
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
personality_options = ["kind", "intellegent", "courageous", "skilled", "loyal", "creative", "calm"]        
professions = ["blacksmith", "farmer", "mason", "butcher", "fletcher"]
genders = ["male", "female", "transgender"]


# Prints slowly so it looks cool

def cool_print(word_to_print):  
    for i in word_to_print:
        print(i, end = "", flush = True)
        time.sleep(0.1)

class NPC:
    def __init__(self, name, gender, height, personality, profession, hostility):
        self.name = name
        self.gender = gender
        self.height = height
        self.personality = personality
        self.profession = profession
        self.hostility = hostility
    
    # Makes cool animation and outputs result

    def random_animation(self):
        global personality_options
        global professions
        global i
        begin_time = time.time()
        duration = 1.2
        while True:
            rand_name = f"{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}"
            rand_gender = f"{random.choice(genders)}"
            rand_height = f"{random.randint(4, 7)}\"{random.randint(1, 12)}"
            rand_personality = f"{random.choice(personality_options)}"
            rand_profession = f"{random.choice(professions)}"
            print(f"\r{rand_name} is a {rand_gender} person who is {rand_height}. {rand_name} is a {rand_personality} {rand_profession}.", end = "", flush=True)
            
            if (time.time() - begin_time) > duration:
                break
            time.sleep(0.01)
        print("\r                                                                                              ")
        print(f"{self.name} is a {self.gender} person who is {self.height}. {self.name} is a {self.personality} {self.profession}.", flush=True)



# Asks use for gender of NPC with error handling. Loops until valid input

def gender_check():
    cool_print("Enter the corresponding number for the gender:\n1. Male\n2. Female\nAnswer: ")
    gender_input = (input()).strip()
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
    character = NPC(0,0,0,0,0)
    
    #Gets all of the attributes
    cool_print("Enter NPC name: ")
    character.name = input("")
    character.gender = gender_check()
    character.height = f"{random.randint(5, 6)}\" {random.randint(1, 11)}"
    character.personality = random.choice(personality_options)
    character.profession = random.choice(professions)
    character.random_animation()
  
   
    
