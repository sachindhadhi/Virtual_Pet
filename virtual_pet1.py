import threading 
import time


#Defining the pet class
class pet:
    def __init__(self,name):
        self.name=name
        self.hunger=50
        self.happiness=50
        self.inventory={"worms":10,"seeds":5}
        self.mood="happy"
        self.running= True

#defining the functionalities of pet class
    def feed(self,food_type):
        if food_type=="worms":
            self.hunger -= 20
        else:
            self.hunger -= 5
        if self.hunger < 0:
            self.hunfer = 0
        print(f"{self.name} is now feeling full after eating {food_type}")
        self.update_mood()
    
    def play(self,time_played):
        self.happiness += time_played
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} is happy aftert playing with you")
        self.update_mood()

    def update_mood(self):
        if self.hunger > 75 and self.happiness < 25:
            self.mood = "sad"
        else:
            self.mood="happy"

    def add_inventory_item(self,item,amt):
        if item not in self.inventory:
            self.inventory[item] = amt
        else:
            self.inventory[item] += amt
    
    def use_inventoey_itam(self,item,amt):
        if item not in self.inventory or self.inventory[item]==0:
            print("No such item in inventory")
        
        elif (self.inventory[item] - amt) < 0:
            print("please choose a valid amt")
            
        else:
            self.inventory[item] -= amt

    def display_inventory(self):
        for item,amt in self.inventory.items():
            if amt == 0:
                continue
            else:
                print(f"{item} : {amt}" )

    def update_status(self):
        while self.running:
            time.sleep(20)
            self.hunger += 1
            self.happiness -= 1
            if self.hunger >100:
                self.hunger = 100
            if self.happiness < 0:
                self.happiness = 0
            self.update_mood()

    def stop(self):
        self.running = False
            
    
    def pet_face(self):
        if self.mood == "happy":
            print('''
                     (\_/)
                    (o^_^o)
                    (")_(")
        ''')
        if self.mood =="sad":
            print('''
                    (\_/)
                    (o.o )
                   (")_(")
                  '''
                )
            
    def rename(self,rename):
        temp=self.name
        self.name=rename
        print(f"{temp} name has been changed to {self.name}")
    
    def get_status(self):
        name = f"{self.name:>16}"[:16]   # Ensuring fixed width
        hunger = f"{self.hunger:>16}"[:16]  # Ensuring fixed width
        happiness = f"{self.happiness:>16}"[:16]
        mood = f"{self.mood:>16}"[:16]
        print(f"""
╔════════════════════════════╗
║        PET STATUS          ║
╠════════════════════════════╣
║ Name:      {name}║
║ Hunger:    {hunger}║
║ Happiness: {happiness}║
║ Mood:      {mood}║
╚════════════════════════════╝
        """)


     
#Game functionalities start from here.
intro_statement = """
                *******************************
                |    Welcome to Pet Paradise! |
                *******************************
                
Petmaster : Congratulations on adopting your new virtual pet!
Take good care of your pet by feeding, playing, and nurturing it.
Watch it grow and thrive as you embark on this heartwarming journey together!
"""
#For main intro
print(intro_statement)

#Naming the pet and displaying it in happy mood
pet_name=input("Petmaster : Please enter a name for your pet: ")
print(f'Petmaster : {pet_name} is happy with its name')
my_pet=pet(pet_name)
my_pet.pet_face()
time.sleep(3) #provide effect

#start thread to update pets mood
update_thread = threading.Thread(target=my_pet.update_status)
update_thread.start()

#Asking player for int(action)s to perform for pet
while True:
    my_pet.pet_face()
    print("""
Petmaster : What would you like to do:
1.Pet
2.Play
3.Feed
4.Settings
5.Exit                    
""")
    action=input()
    #for displaying pet and its status
    if int(action) == 1:
        my_pet.pet_face()
        my_pet.get_status()
        time.sleep(5)
        continue

    #for playing with pet
    elif int(action) == 2:
        my_pet.play(10)
        my_pet.get_status()
        time.sleep(5)

    #for feeding the pet
    elif int(action) == 3:
        feed=int(input({"""  
Petmaster : What would you like to feed: 1.seeds (hunger -5) ║ 2.Worms (hunger -20)
"""}))
        if feed == 2:
            my_pet.feed("worms")
        else:
            my_pet.feed(".")
        time.sleep(5)
    
    #for settings
    elif int(action) == 4:
        #for renaming your pet
        choice=int(input(''''
Petmaster : Rename your pet: 
1.Yes
2.No
              '''))
        if choice == 1:
            name2 = input("Petmaster : Enter the new name: ")
            my_pet.rename(name2)
        time.sleep(5)

    #for exiting the game
    elif int(action) == 5:
        print("Petmaster : Thank you")
        my_pet.stop()
        update_thread.join()
        break

    else:
        print("Please choose a valid input")
        time.sleep(5)
    

