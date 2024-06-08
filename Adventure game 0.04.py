#Below a couple of values that always start the same regardless of run. Might be an idea to change these depening on class/background in the future
HealthPotion = False
ManaPotion = False
DirtBucket = False
#This part of the code is utilized to select what class will be used and the corresponding stats
#Also need to add some kind of loop to this and future sections in case of a invalid answer
print("Hello adventurer, for this adventure you will have a choice of the following classes:\n"
      "1. A warrior.\n"
      "2. A mage.\n"
      "3. A rogue.")
while True:
   Class = input("As which of these classes would you like to play?\n")
   if '1' in Class:
    HP = 15 
    MP = 7 
    Dex = 10 
    print("Ah I see, a strong warrior")
    break
   elif '2' in Class:
    HP = 10 
    MP = 15 
    Dex = 7 
    print("A mage I see")
    break
   elif '3' in Class:
    HP = 7
    MP = 10
    Dex = 15
    print("So you are a stealthy rogue")
    break
   else: 
    print("The devs haven't made that class yet, try again bucko")
#Once the class has been selected, the player is informed about their stats below, could probably be written more efficiently
print("Your class is chosen,you should know about your stats."
      "\nYour health is HP, your magic power is MP and your dexterity is Dex."
      "\nYour stats are as follows:")
print("HP =", HP)
print("MP =", MP)
print("Dex =", Dex)
while True:
   location = input("Would you like to \n1. Go to a shop \n2. Delve into the dungeon?\n")
   if '1' in location: 
    print("You head towards the shop to prepare for your journey. You can purchase just one of the following items:\n"
          "1. A health potion.\n"
          "2. A mana potion.\n"
          "3. A seemingly useless bucket of dirt.")
    Shopkeeper = input("The shopkeeper approaches 'Which of these fine items would you like to buy, traveler?\n")
    if '1' in Shopkeeper:
        HealthPotion = True
        print("Here you go sir, a fine health potion capable of healing even the greatest wounds\n")
        break
    elif '2' in Shopkeeper:
        ManaPotion = True
        print("The strongest of mana potions for you, giving great power to your spells\n")
        break
    elif '3' in Shopkeeper:
        DirtBucket = True
        print("Y-you'll really buy this? Why of course, please take it!\n")
        break
    else:
        print("The shopkeeper doesn't really understand what you want, try again?")
   if '2' in location:
      print("You, perhaps unwisely, head towards the dungeon")
      break
print("As you arrive at the dungeon you walk inside, the halls illuminated by torches")
while True:
    Entrance = input("After a long hallway you reach a fork, and choose to \n1.Go the the left \n2. Go to the right\n")
    if '1' in Entrance:
        print("You head down the hallway to the left, slowly encroaching further into the darkness")

