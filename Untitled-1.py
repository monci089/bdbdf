'''
this program simulates a turn based game with progresion to get stronger,
a shop to buy more in game items, and a bossroom as a means for a goal and win condition, 
including a inventory system and a combat system
'''
#title text and tutorial text
print("Adventure Game")
print("go to the shop to buy new gear with your gold")
print("go to the forest to fight enemies to gain gold")
print("use backpack to change armor and use items, in and out of battle")
print("fight the boss when ready by going to the bossroom")
print("______________________________________________________________________________")
print("your journey starts in a town")
import random
#setting large global variables
hp=1000
defencebonus=0
defencebonustime=0
attackbonus=0
attackbonustime=0
shopalive=True
battle="no"
gold=300
gold2=300
ghostgold=15
weapons=["broken fists",]
armor=["nothing",]
items=[]
itemstats=[]
shopitems=["blade of grass","pebble","spoon","stick","book","larger rock","weak wooden sword","hot metal stick","mutilated clothes","normal clothes","alluminum foil","trash bag","magazines","door chestplate","human scapegoat","large wood planks","small healing potion","healing potion","rage potion","defence potion","bomb"]
shopcost=[2,5,10,11,16,20,30,60,2,5,8,10,15,20,30,60,5,15,5,5,10]
#function to find the players armor stat
def getarmor():
    armortimecheck()
    global itemstats
    global armor
    equiped=armor[-1]
    try:
        index=shopitems.index(equiped)
        getstats()
        return itemstats[index]+defencebonus
    except ValueError:
        return 0+defencebonus
#function to change the gold stat based on a given amount along with the other gold variables
def goldcalc(amount):
   
    global gold
    global ghostgold
    gold=gold+amount
    if amount>0:
        ghostgold=ghostgold-((gold-amount)-gold)
    if gold<1:
        gold=0
    if ghostgold>50:
        ghostgold=ghostgold-(ghostgold-50)
#function to change hp based on a given amount
def hpchange(amount):
    global hp
    hp=hp+amount
    if hp>1000:
        hp=1000
#function to simulate turns to reduce the turn counter
#on limited time attack bonus potion effect
def attacktimecheck():
    global attackbonustime
    global attackbonus
    if attackbonustime>1:
        attackbonustime=attackbonustime-1
    if attackbonustime==0:
        attackbonus=0
#function to simulate turns to reduce the turn counter
#on limited time defence bonus potion effect
def armortimecheck():
    global defencebonustime
    global defencebonus
    if defencebonustime>1:
        defencebonustime=defencebonustime-1
    if defencebonustime==0:
        defencebonus=0
#function to find the attack power stat of the weapon selected
def power(weapon):
    attacktimecheck()
    global itemstats
    global weapons
    equiped=weapon
    secondbuff=0
    if armor[-1]=="human pelt":
        secondbuff=100
    else:
        secondbuff=0
    try:
        index=shopitems.index(equiped)
        getstats()
        return itemstats[index]+attackbonus+secondbuff
    except ValueError:
        return 20+attackbonus+secondbuff
#function to determine total dmg based on defence and offense
def attack(power,armor):
    if power-armor<20:
        attack=20
    else:
        attack=power-armor
    if random.randint(1,50)==1:
        attack=attack*2
        print("CRITICAL HIT")
    return attack
#shop function to present all the text that shows whats in the shop and what they do
#also calls functions to purchanse the items and add them to the players inventory
def shop():
    if shopalive:
        print("______________________________________________________________________________")
        global gold
        print("Welcome to the Shop")
        print("You have: "+str(gold)+" gold")
        print("______")
        print("weapons")
        print("")
        print("Blade of Grass(10-60)                          2 gold")
        print("Pebble(40-50)                                  5 gold")
        print("Spoon(70-80)                                  10 gold")
        print("Stick(25-180)                                 11 gold")
        print("Book(120-120)                                 16 gold")
        print("Larger Rock(130-160)                          20 gold")
        print("Weak Wooden Sword(110-240)                    30 gold")
        print("hot metal stick(350-400)                      60 gold")
        print("______")
        print("armor")
        print("")
        print("mutilated clothes(10)                         2 gold")
        print("normal clothes(20)                            5 gold")
        print("Alluminum foil(10-60)                         8 gold")
        print("trash bag(30)                                10 gold")
        print("magazines(50)                                15 gold")
        print("door chestplate(10-130)                      20 gold")
        print("human scapegoat(80)                          30 gold")
        print("large wood planks(50-200)                    60 gold")
        print("______")
        print("items")
        print("")
        print("small healing potion(+250 HP)                 5 gold")
        print("healing potion(+500 HP)                      15 gold")
        print("rage potion(+30 atk for 5 turns)              5 gold")
        print("defence potion(+20 defence for 5 turns)       5 gold")
        print("bomb(300 atk, ignores armor)                 10 gold")
        buy=input("enter item to buy or enter leave to leave: ").lower()
        if buy=="leave":
            place()
        goldcalc(-purchase(buy))
        shop()
    else:
        print("______________________________________________________________________________")
        print("you have killed the shop keeper you can't buy anything now")
#function to randomize stats in a orderly manner to keep them all in a neat list
def getstats():
    global itemstats
    itemstats=[random.randint(10,60),random.randint(40,50),random.randint(70,80),random.randint(25,180),120,random.randint(130,160),random.randint(110,240),random.randint(350,400),10,20,random.randint(10,60),random.randint(30,30),random.randint(50,50),random.randint(10,130),80,random.randint(50,200)]
#function called by the shop with the item that the player enterd 
#to determine if the item is a real item then remove the amount of gold that item cost
#and finaly add it to the players inventory 
def purchase(item):
    global gold
    if item=="fight":
        global shopalive
        print("______________________________________________________________________________")
        print("you have killed the shop owner everyone hates you")
        print("and you have aquired his human pelt")
        armor.append("human pelt")
        shopalive=False
        place()

    try:
        index=shopitems.index(item)
    except ValueError:
        print("enter a real option")
        shop()
    if gold>=shopcost[index]:
        if index<8:
            weapons.append(shopitems[index])
        elif index<16:
            armor.append(shopitems[index])
        else:
            items.append(shopitems[index])
        print("______________________________________________________________________________")
        print("You have bought "+shopitems[index])
        return shopcost[index]
    else:
        print("you dont have enough gold")
        shop()
#function called by the place() function to determine if the player really wants to fight the boss
def bossroom():
    if input("do you want to fight the boss?(yes/no) ")=="yes":
        boss()
#function called to fight the boss by the bossroom() function if they answer yes
def boss():

        #setting values and text on screen
        enemie="Rat"
        print("______________________________________________________________________________")
        print("In the boss room you run into a mighty "+enemie)
        global battle
        battle="yes"
        global hp
        global gold
        enemiehp=2500
        enemiehp2=enemiehp
        enemiearmor=150
        lowatk=250
        highatk=350
        tempgold=0
        itemowlcount=0
        tempvar=True
        x=0
        owlitemcount=0
        #creates the battle loop to continuley battle till the fight is over
        while True:
            #setting values for constantly changing variables and ui
            print("______")
            block=False
            dodge=False
            print("enemie hp: "+str(enemiehp))
            print("your hp: "+str(round(hp)))
            #gets input on what the first action from the player is and executes it
            turn=input("'a' to attack, 'b' to use backpack, run to run: ")
            #run action gives the player a chance to run sending them back to place() function
            if turn=="run":
                if random.randint(0,100)==1:
                    print("you sucsesfully ran!")
                    place()
                else:
                    print("you failed to run, the "+enemie+" wont let you get away that easily")
            #backpack action opens the players backpack
            elif turn=="b":
                tempvar=backpack(enemiearmor,enemiehp,lowatk,highatk)
                if tempvar==True:
                    continue
                else:
                    enemiehp=tempvar

            
            #attack action lets the player choose a weapon
            #then the program calculates the damage and tell the player
            elif turn=="a":
                print(weapons)
                weaponuse=input("choose what weapon to use from left to right(1,2,3,etc) x for last weapon: ")
                if weaponuse=="x":
                    weaponuse=0
                try:
                    if weaponuse==0:
                        index=weapons.index(weapons[-1])
                    else:
                        index=weapons.index(weapons[int(weaponuse)-1])
                    
                except ValueError:
                    print("enter a correct weapon")
                    continue
                dmg=attack(power(weapons[int(weaponuse)-1]),enemiearmor)
                enemiehp=enemiehp-dmg
                print("______")
                print("you did "+str(dmg)+" damage")
            else:
                print("enter a real answer")
                continue
            #win condition if statement
            if enemiehp<1:
                    print("______")
                    print("game over, you won")
                    exit()
            #sets up the enemies turn and calculates their attack
            #also gives the player a choice to dodge or block to help reduce damage
            print("______")
            print(enemie+"s turn")
            print("")
            blockdodge="z"
            #while loop to figure out if the player wants to dodge or block the attack
            while blockdodge=="z":
                blockdodge=input("do you want to 'b' (block) or 'd' (dodge) the attack? ").lower()
                if blockdodge=="b":
                    block=True
                elif blockdodge=="d":
                    if random.randint(0,10)==10:
                        dodge=True
                        print("you succsesfully dodged")
                    else:
                        print("you failed to dodge")
                else:
                    blockdodge="z"
                    print("enter a real answer")
            if enemiehp<1300:
                
                x=x+1
                if x==1:
                    #initiation of bosses second phase
                    print("______________________________________________________________________________")
                    print("the rat turns into a giant owl and steals half of your items")
                    print("gaining additional hp and attack based on the amount of items stolen")
                    print("______________________________________________________________________________")
                    enemie="Giant Owl"
                    for i in range(len(items)):
                        if random.randint(0,1)==1:
                            tempvar=items[i]
                            items[i]="stolen"
                            itemowlcount=itemowlcount+1
                    enemiehp=enemiehp+itemowlcount*100
                    highatk=highatk+(itemowlcount*80)
            enemiedmg=attack(random.randint(lowatk,highatk),getarmor())
            if block==True:
                enemiedmg=round(enemiedmg*0.9,0)
            if dodge==True:
                enemiedmg=0
            hp=hp-enemiedmg
            print("______")
            print("you took "+str(enemiedmg)+" damage")
            #if statement to see if the player has died
            if hp<1:
                print("you have been killed by a "+enemie)
                print("THE END")
                exit()
            
# forest function, gives the player 2 options fight something or leave
def forest():
    while True:
        action=input("what do you want to do (fight, leave): ")
        #action to leave the forest
        if action=="leave":
            break
        #action to find a fight
        elif action=="fight":
            global battle
            

                #code to get a random number manipulated by the players total ever gold
                #and give the player a encounter
                #based on that number
            encounter=random.randint(int(0+((ghostgold*2))),200)
            if encounter<80:
                fight("Mud Puddle",random.randint(80,150),10,60,1)
            elif encounter<120:
                fight("Dragon",random.randint(200,400),30,90,5)
            elif encounter<155:
                fight("Crazy Alien",random.randint(540,630),50,120,10)
            elif encounter<178:
                fight("Rabbit",random.randint(890,900),90,150,20)
            elif encounter<189:
                fight("Mothman",random.randint(1000,1200),150,200,25)
            elif encounter<197:
                fight("God",random.randint(1350,1450),200,300,50)
            else:
                fight("Trap",random.randint(10,25),10,100,0)
            battle="no"

#Function to simulate a fight after getting information from the encounter
#from the forest function, then rewardsing the player or possibly ending the program
def fight(enemie,enemiehp,lowatk,highatk,enemiearmor):
    #if statement to figure out if its a trap, as trap's 
    #act differntly than other monsters
    if enemie=="Trap":
        print("you have ran into a trap!")
        if attack(random.randint(lowatk,highatk),getarmor())>0:
            print("you have been caught by the trap")
            print("you lost "+str(enemiehp)+" gold")
            goldcalc(-enemiehp)
            forest()
        else:
            print("you escaped the trap!")
    else:
        #setting values and text on screen
        print("______________________________________________________________________________")
        print("you ran into a "+enemie)
        global battle
        battle="yes"
        global hp
        global gold
        tempgold=0
        #creates the battle loop to continuley battle till the fight is over
        while True:
            #setting values for constantly changing variables and ui
            print("______")
            block=False
            dodge=False
            print("enemie hp: "+str(enemiehp))
            print("your hp: "+str(round(hp)))
            #gets input on what the first action from the player is and executes it
            turn=input("'a' to attack, 'b' for back pack, run to run: ")
            #action to give the player a chance to escape 
            if turn=="run":
                global ghostgold
                if random.randint(int(highatk),int(1000))<800:
                    print("you sucsesfully ran!")
                    forest()
                else:
                    print("you failed to run")
            #action to open the players backpack
            elif turn=="b":
                tempvar=backpack(enemiearmor,enemiehp,lowatk,highatk)
                if tempvar==True:
                    continue
                else:
                    enemiehp=tempvar
            #attack action to determine the players damage and what weapon they use
            elif turn=="a":
                print(weapons)
                weaponuse=input("choose what weapon to use from left to right(1,2,3,etc) x for last weapon: ")
                if weaponuse=="x":
                    weaponuse=0
                try:
                    if weaponuse==0:
                        index=weapons.index(weapons[-1])
                    else:
                        index=weapons.index(weapons[int(weaponuse)-1])
                    
                except ValueError:
                    print("enter a correct weapon")
                    continue
                dmg=attack(power(weapons[int(weaponuse)-1]),enemiearmor)
                enemiehp=enemiehp-dmg
                print("______")
                print("you did "+str(dmg)+" damage")
            else:
                print("enter a real answer")
                continue
            #win condition with text to tell the player they won and their reward
            if enemiehp<1:
                    print("______")
                    print("you won")
                    tempgold=gold
                    goldcalc(highatk/10)
                    print("you gained "+str(gold-tempgold)+" gold")
                    battle="no"
                    break
            #sets up the enemies turn and calculates their attack
            #also gives the player a choice to dodge or block to help reduce damage
            print("______")
            print(enemie+"s turn")
            print("")
            blockdodge="z"
            #determines if the player wants to block or dodge
            while blockdodge=="z":
                blockdodge=input("do you want to 'b' (block) or 'd' (dodge) the attack? ").lower()
                if blockdodge=="b":
                    block=True
                elif blockdodge=="d":
                    if random.randint(0,4)==4:
                        dodge=True
                        print("you succsesfully dodged")
                    else:
                        print("you failed to dodge")
                else:
                    blockdodge="z"
                    print("enter a real answer")
            #executes block or dodges function
            enemiedmg=attack(random.randint(lowatk,highatk),getarmor())
            if block==True:
                enemiedmg=round(enemiedmg*0.8,0)
            if dodge==True:
                enemiedmg=0
            hp=hp-enemiedmg
            print("______")
            print("you took "+str(enemiedmg)+" damage")
            #if statement to see if the player has died and then give them
            #game over screen
            if hp<1:
                print("you have been killed by a "+enemie)
                print("THE END")
                exit()
            
#function to show backpack components and to calculate the components
#and to use bombs in battle
def backpack(enemiearmor=0,enemiehp=0,lowatk=0,highatk=0):
    #call all needed global variables and print information
    global battle
    global armor
    global items
    global gold
    global hp
    global attackbonus
    global defencebonus
    global attackbonustime
    global defencebonustime
    print("______")
    print("backpack")
    print("hp: "+str(hp))
    print("gold: "+str(gold))
    print("attack bonus: "+"+"+str(attackbonus)+" for "+str(attackbonustime)+" turns")
    print("defence bonus: "+"+"+str(defencebonus)+" for "+str(defencebonustime)+" turns")
    print("______")
    print("weapons")
    print(weapons)
    print("______")
    print("armor")
    print(armor)
    print("______")
    print("items")
    print(items)
    action=input("leave, or select a armor to change to, or item to use: ").lower()
    if action=="leave":
        if battle=="no":
            place()
        else:
            return True
    try:
        #a try to see if the player enters a armor that is in their armor list
        #moving it to the fron if so
        index=armor.index(action)
        armor.remove(action)
        armor.append(action)
        print("changed armor to "+action)
    except ValueError:
        try:
            #checks if the user enterd a valid item to use
            index=items.index(action)
        except ValueError:
            print("______________________________________________________________________________")
            print("enter a real option")
            backpack()
        #if statement to figure out wha item the player is using and then do what the item does
        if action=="bomb":
            if battle=="yes":
                if armor[-1]=="human pelt":
                    secondbuff=100
                else:
                    secondbuff=0
                dmg=300+attackbonus+secondbuff
                enemiehp=enemiehp-dmg
                print("you did "+str(dmg)+" damage")
                return enemiehp
            else:
                print("only usable in combat")
        elif action=="defence potion": 
            items.remove("defence potion")
            defencebonus=20
            defencebonustime=5
            print("used "+action)
        elif action=="rage potion":
            attackbonus=20
            attackbonustime=5
            items.remove("rage potion")
            print("used "+action)
        elif action=="small healing potion":
            items.remove("small healing potion")
            hpchange(250)
            print("used "+action)
        elif action=="healing potion":
            items.remove("healing potion")
            hpchange(500)
            print("used "+action)
            
    if battle=="no":
        backpack()
    else:
        return enemiehp
def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
 
    base36 = ''
    sign = ''
 
    if number < 0:
        sign = '-'
        number = -number
 
    if 0 <= number < len(alphabet):
        return sign + alphabet[number]
 
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36
 
    return sign + base36
saveencryptinput=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0",".","/"," "]
saveencryptoutput=["56","71","26","72","81","91","20","79","84","58","67","92","86","25","29","95","46","67","78","94","99","87","96","62","58","22","9","6","7","2","8","3","5","1","0","4","54","64","55"]
def save():
    savestr=str(gold)+"."+str(hp)+"."+str(attackbonus)+"."+str(attackbonustime)+"."+str(defencebonus)+"."+str(defencebonustime)
    savestr=savestr+"."
    tempweapons="/".join(weapons)
    savestr=savestr+tempweapons
    savestr=savestr+"."
    temparmor="/".join(armor)
    savestr=savestr+temparmor
    savestr=savestr+"."
    tempitems="/".join(items)
    savestr=savestr+tempitems
    encryptedsavestr=""
    for i in range(len(savestr)):
        index=saveencryptinput.index(savestr[i])
        encryptedsavestr=encryptedsavestr+saveencryptoutput[index]
    decoder=encryptedsavestr
    print(savestr)
    encryptedsavestr=(((((((float(encryptedsavestr))*1.42)/2043543534254350015.5)+583489102732.1)/11044343559.4)*7.678)-3728543153452378.6)/574815461431875
    print(encryptedsavestr)
    print(str(len(str(encryptedsavestr))))
    while True:
        if len(str(round(encryptedsavestr)))>15:
            encryptedsavestr=encryptedsavestr/643264234
        else:
            break
    encryptedsavestr=round(encryptedsavestr)
    print("this is your save code copy and paste it into a load input to load it")
    print(str(base36encode(int(encryptedsavestr)))+"-"+str(base36encode(int(decoder))))
#important function to determine where the player wants to go
def load():
    print(text)
    loadcode=input("paste load code: ")
    index=loadcode.find("-")
    encryptcode=((((((float(loadcode[index+1:])*1.42)/2043543534254350015.5)+583489102732.1)/11044343559.4)*7.678)-3728543153452378.6)/574815461431875
    while True:
        if len(str(round(encryptcode)))>15:
            encryptcode=encryptcode/643264234
        else:
            break
    encryptcode=round(encryptcode)
    encryptcode=str(base36encode(int(encryptcode)))
    if encryptcode==loadcode[:index]:
        print(loadcode)
        print(encryptcode)
    encryptedsavestr=round(encryptedsavestr)
def place():
    while 1==1:
        print("______________________________________________________________________________")
        temp_location=(input("where do you want to go (shop, forest, bossroom, backpack): "))
        print(temp_location)
        if temp_location=="shop":
            shop()
        elif temp_location=="forest":
            forest()
        elif temp_location=="bossroom":
            bossroom()
        elif temp_location=="backpack":
            backpack()
        elif temp_location=="save":
            save()
        elif temp_location=="load":
            load()
        else:
            print("enter a correct location")
#calls the place function which starts the whole program 
#everything stems off of its while loop
place()