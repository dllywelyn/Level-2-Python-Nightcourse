import random
import os
import time
############ NOTES

###### Make easy, medium and hard modes. Medium = as is
# EASY with added instructions/hints  and a miracle of god:
##(change harvrate to 1-31, <10 = x1, <20 = x2, <30 = x3, ==31 = x10)
### maybe smaller odds? 1-91 split into 30s, 1 - 151 split into 50s, 1-301 split into 100s
#### less migrants, less change of rats (or amount eaten less)
# HARD mode = random floods, again using small odds system above,
## i.e. if disaster == 31/91/151, flood(destory crops), war/disease (kill population #low populatio is good, thnk of something else), fire (destory land)
### maybe more chance of rats?  More migrants, set range higher with min amount guaranteed
hint = ("\033[0m\033[1m\033[2m")

population = 100
land = 1000
grain = 2800
price = 19
starvation = 0
migrants = 0
harvest = 3000
harvrate = 3
ratloss = 200
apc = land / population  # acres per capita
rats = 1

def status():
    year = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]
    bar = "\033[0m\033[1;37m\033[1m\033[7m"
    off = "\033[0m\033[4m"
    print(f"\n \033[4m 🌾  {bar}{grain}{off} 🌱  {bar}{land}{off} \uC6C3 {bar}{population}\033[0m \
\033[1m                    \033[4m YEAR {year[i-1]} \033[0m\n")


def update():
    os.system("clear")
    status()


def yninput():
    while True:
        try:
            choice = str(input())
        except:
            print("\033[31mInvalid input. Please enter 'Y' for yes or 'N' for no\033[0m")
            continue
        if choice.lower() == "y" or choice.lower() == "n":
            return choice
        else:
            print("\033[31mInvalid input. Please enter 'Y' for yes or 'N' for no\033[0m")


def confirm():  #### need to choose between this one or the above,
    # useless and messy to have two such similar functions
    while True:
        try:
            choice = str(input())
        except:
            print("?????ASK ABOUT THIS. WHY NEEDED? HOW TO DO WITHOUT???")
            continue
        if choice != "Y" and choice != "N":
            print("Invalid input. Enter Y or N")  # need function to go back to for N
            continue
        else:
            return choice

# call with: choice = confirm()


def nxt(a):
    if a == "year":
        print("")
        input(f"   👑  Press \033[1m[ENTER]\033[0m to continue on to year {i+1}  👑 ".center(101, " "))
        os.system("clear")
    if a == "screen":
        print("")
        input(f"      ↠  Press \033[1m[ENTER]\033[0m to continue reading ↠  ".center(101, " "))
        os.system("clear")
        status()


# def restart(): # doesn't work, "maximum recursion depth"
#   time.sleep(0.5)
#  update()
# currentfunction


def invalid():
    print("")
    middle("        \033[31mInvalid entry. Try again\033[0m")
    time.sleep(0.8)
    #update()     # redundant now that i'm doing loops
    #if a == "trade":
     #   trade()
    #elif a == "food":
     #   food()
    #elif a == "plant":
     #   plant()


# already done a lot of centering, but just thought of an experiment...
def middle(m):
    print(f"{m}".center(101, " "))


# middle("test")


def intinput(a):
    while True:
        try:
            answer = int(input())
        except:
            print("\033[31mInvalid input. Please enter a number.\033[0m\033[1m")
            continue
        if answer < 0:
            print("\033[31mInvalid input. Please enter a number above zero.\033[0m\033[1m")
            continue
        if a == "grain":
            if answer > (grain//price):
                print("\033[31mThis is more grain than you currently have. \
The maximum you can afford is",grain // price,"acres. \nPlease try again.\033[0m\033[1m",)
                continue
        if a == "land":
            if answer > land:
                print("\033[31mThis is more land than you currently have. Please try again.\033[0m\033[1m")
                continue
        if a == "grainfeed":
            if answer > grain:
                print("\033[31mThis is more grain than you currently have. Please try again.\033[0m\033[1m")
                continue    
                #invalid("food")
        if a == "planting":
            if answer > grain or answer > land:
                print("\033[31mEach bushel of grain requires one acre of land. \
\nYou do not have the resources for this. Please try again.\033[0m\033[1m")
                #invalid("plant")
            else:
                return answer
        else:
            return answer
            
            
def disaster():
    global land
    if mode == "h":
        if land >= 0:
            dischance = random.randint(1, 30)
            if dischance == 1:
                print("\n\n")
                middle ("A curse from the gods!")
                middle("A fire has started in one of your emply fields!")
                middle ("Luckily no crops were harmed but the land is now useless.")
                middle ("You've lost a tenth of you land")
                land = int(land *.9)
                nxt("screen")

#########################################################################################################################
while True:
    print("")
    middle(" 🫅 ")
    print("")
    middle("             \033[1m\033[4mLong live the new king of Samaria!\033[0m")
    print("")
    print("")
    middle("It is now yours to rule.")
    print("")
    middle("You must decide if land will be bought or sold.")
    middle("You hold the fate of your citizens in your hands, will they live or starve?")
    middle("You will be responsible for your kingdom's prosperity, or its downfall.")
    print("")
    middle(f"Your inhabitants enjoy the wealth of 10 acres for each person in your kingdom.")
    middle("Your goal is to improve this whilst keeping your people healthy.")
    print("")
    middle("If more than 30% of your population die in any given year")
    middle("you will be dethroned and cast out to the desert.")
    print("")
    middle("Be warned, each year your harvest is at the mercy of the gods ... and rats.")
    middle("You should plan ahead wisely if you wish to survive.")
    
    
    print("")
    middle("                       Enter \033[1m[E]\033[0m, \033[1m[M] or \033[1m[H]\033[0m to select Easy, Medium or Hard mode")
    middle("         👑  then \033[1m[ENTER]\033[0m to begin your first year as king 👑 ")
    print("\033[1m")
    mode = input((" ".center(50, " ")))
    if mode.lower() == "e":
        break
    elif mode.lower() == "m":
        break
    elif mode.lower() == "h":
        break
    else: 
        invalid()
        os.system("clear")
os.system("clear")
    
# LOOK UP that thing that can find prime numbers by dividing and seeing if there's any leftover
# '%'! Use % as divider to see remainder

# 10 YEAR REIGN, so either i in range(10) or loop counter like:
### r + 1 (if r ==10 \ break)
# for i in range(10): may have to do the same as higher/lower, saving data to list

# year 0 variables



# using unicodes and formatting fonts with \033... always messes up the spacing especially with centering, so manually adjust
if mode == "e":
    y = 6
elif mode == "m" or mode == "h":
    y = 11
for i in range(1, y):
    status()
    print("\033[0m")
    middle(f"           You are in year \033[1m\033[34m{i}\033[0m of your ten year rule.")
    print("")
    middle(f"           In the previous year \033[1m\033[34m{starvation}\033[0m people starved to death.")
    middle(f"           In the previous year \033[1m\033[34m{migrants}\033[0m people entered the kingdom.")
    middle(f"           The population is now \033[1m\033[34m{population}\033[0m.")
    print("")
    middle(f"                       We harvested \033[1m\033[34m{harvest}\033[0m bushels at \033[1m\033[34m{harvrate}\033[0m bushels per acre.")
    if rats == 1:
        middle(f"                      Rats destroyed \033[1m\033[34m{ratloss}\033[0m bushels, leaving \033[1m\033[34m{grain}\033[0m bushels in storage.")
    else:
        middle(f"Your grain was kept safe from rats (the local cats ate very well).")
    print("")
    middle(f"           The city owns \033[1m\033[34m{land}\033[0m acres of land.")
    middle(f"           Land is currently worth \033[1m\033[34m{price}\033[0m bushels per acre.")
    print("")

    nxt("screen")

    def trade():
        while True:
            global grain, land, choice # have to do this to avoid errors but also so intro can keep updated rather than use the initial variable definitions
            print(f"\nYou have the opportunity to trade grain for land. \
\nThe price of land is currently \033[1m\033[34m{price}\033[0m bushels per acre.")
            options = input("\nEnter \033[1m[B]\033[0m to buy land with grain, \033[1m[S]\033[0m to sell land for grain or \033[1m[X]\033[0m to move on without transaction \n \033[1m")
            if options.lower() == "b":
                print(f"\n\033[0mYou have \033[1m\033[34m{grain}\033[0m bushels.\n")
                print("How many acres of land would you like to buy?  \033[1m")
                if mode == "e":
                    print(hint,"At the current price you can afford\n\033[34m", int((grain/price) - (population*20)/price), hint,"acres if you \
want to feed everyone in your kingdom, or\n\033[34m", int((grain/price) - ((population*0.7)*20)/price), hint, "to feed the minimum number of people without being dethroned\033[0m\033[1m")
                buy = intinput("grain")
                buycost = price * buy
                gestimate = grain - buycost
                lestimate = land + buy
                print(f"\033[34m\033[1m{buy}\033[0m acres at \033[1m\033[34m{price}\033[0m bushels each will cost you \033[1m\033[34m{buycost}\033[0m bushels \
and leave you with \033[1m\033[34m{gestimate}\033[0m grain and \033[1m\033[34m{lestimate}\033[0m acres.\nWould you like to proceed with this transaction? \033[1m[Y/N]")
                choice = yninput()
                if choice.lower() == "y":
                    grain = grain - buycost
                    land = land + buy
                    update()
                    middle("Pleasure doing business with you")
                    break
                elif choice.lower() == "n":
                    update()
            elif options.lower() == "s":
                print(f"\033[0mYou have \033[1m\033[34m{land}\033[0m acres of land.")
                print("How many would you like to sell?:\033[1m")
                sell = intinput("land")
                sellprice = price * sell
                gestimate = grain + sellprice
                lestimate = land - sell
                print(f"\033[34m{sell}\033[0m acres at \033[1m\033[34m{price}\033[0m bushels each will make you \033[1m\033[34m{sellprice}\033[0m  \
and leave you with \033[1m\033[34m{gestimate}\033[0m grain and \033[1m\033[34m{lestimate}\033[0m acres.\nWould you like to proceed with this transaction? \033[1m[Y/N]  \033[1m")
                choice = yninput()
                if choice.lower() == "y":
                    grain = grain + sellprice
                    land = land - sell
                    update()
                    middle("Pleasure doing business with you")
                    break
                elif choice.lower() == "n":
                    update()
            elif options.lower() == "x":
                print("\033[0m\nAs you wish.")
                break
            else:
                invalid()
                update()
            
    trade()
    
    nxt("screen")
    disaster()
    
    def food():
        while True:
            global grain, population, choice, peoplefed, starvation 
            ### cost of living = 20 bushels per person,
            # i.e. one person dies for each 20bushels unused to feed population
            # so, if grain is 2400, that would feed 120 people
            bpp = 20  # bushel per person
            print("How many bushels would you like to allocate for food?\n\033[1m")
            if mode == "e":
                    print(hint,"Each inhabitant needs 20 bushels to survive, so you'll have to allocate \n\033[34m", int(population*bpp), hint,"bushels if you \
want to feed everyone in your kingdom, or\n\033[34m", int((population*bpp)*0.7), hint, "to feed the minimum number of people without being dethroned.\033[0m\033[1m")
            grainforfood = intinput("grainfeed")
            estpeoplefed = int(grainforfood / bpp)
            remainder = grainforfood % bpp
            # print(peoplefed, "with", remainder, "bushels remaining")
            if (remainder) != 0:
                print(f"Each person needs 20 bushels each to survive, so you should allocate food in \
multiples of 20 bushels. \n\033[1m\033[34m{grainforfood}\033[0m\033[1m will have \033[1m\033[34m{remainder}\033[0m\033[1m remaining. \
\nYou should revise your answer.\n\033[0mWould you like to try again? \033[1m[Y/N]:  ")  # do try/except here
                choice = yninput()
                if choice.lower() == "y":
                    grainforfood = 0
                    update()
                    continue
            # if grainforfood < 20:
            #   print("This is not enough to feed even one person, each member of your population needs at least \
            # 20 bushels")
            estgrain = grain - grainforfood
            # population = peoplefed
            # too simple maybe? is it better to have more steps/variables?
            # print("The population is now",population)
            eststarvation = population - estpeoplefed
            if estpeoplefed == 1:
                peoplef = "person"
            else:
                peoplef = "people"
            if eststarvation == 1:
                peoples = "person"
            else:
                peoples = "people"
            print(f"\033[0mThis will feed \033[1m\033[34m{estpeoplefed} {peoplef}\033[0m leaving you with \033[1m\033[34m{estgrain}\033[0m bushels of grain.\
\nWould you like to proceed with this decision? [Y/N] \033[1m")  # add validation here to make sure peoplefed is not > population
            choice = yninput()
            if choice.lower() == "n":
                update()
            else:
                peoplefed = int(grainforfood / bpp)
                starvation = population - peoplefed
                grain = grain - grainforfood
                pcentloss = int((starvation / population) * 100)
                if pcentloss > 30:
                    print(f"\033[0mYou let \033[1m\033[34m{starvation}\033[0m people starve, which is \033[1m\033[34m{pcentloss}%\033[0m of your population. \
This is unacceptable.\n")
                    print(" 💀  GAME OVER 💀".center(101, " "))
                    raise SystemExit
                else:
                    population = population - starvation
                    print(f"\033[0mYou fed \033[1m\033[34m{peoplefed} {peoplef}\033[0m and so \033[1m\033[34m{starvation} {peoples}\033[0m starved. \
Your population is now \033[1m\033[34m{population}\033[0m")
                break
                    # if starvation > (population*0.3):
                    # print(f"You let {starvation} people starve, which is", ((starvation/population)*100))," of your population."
                   

    food()
    nxt("screen")
    disaster()

    def plant():
        while True:
            global grain, land, update, nxt, harvest, harvrate
            ### farming: 1 bushel = 1 acre. rate of success 1-3, so
            if mode == "e":
                harvchance = random.randint(1, 10)
            elif mode == "m":
                harvchance = random.randint(1, 9)
            elif mode == "h":
                harvchance = random.randint(0, 9)
            #idea for hard mode, 1-10, 1-3 x1, 4-6 x2, 7-9 x 3 and 10 = 0.5 harvrate
            if harvchance == 0:
                harvrate = 0.5
            elif harvchance == 10:
                harvrate = 10
            elif harvchance <= 3:
                harvrate = 1
            elif harvchance <= 6:
                harvrate = 2
            elif harvchance <= 9:
                harvrate = 3
            # harvest is multiplier of roi on farming, so...
            # e.g. 10 bushels (would require 10 acres, costing 10*price bushels)
            # can potentially return 10, 20 or 30 bushels (for next year)
            print("How many bushels would you like to plant this year?\033[1m")
            planted = intinput("planting")
            estgrain = grain - planted
            estland = land - planted
            print("\033[0m")
            if planted == 0:
                harvrate = 0
                harvest = 0
                middle("Today's seeds determine tomorrow's harvest.")
                middle("Choosing not to sow is a sign of comfort or frugality.")
                middle("You are doing either very well, or very badly")
                break
            print(f"Planting {planted} bushels would leave you with {estgrain} grain and {estland} acres of land. \
Would you like to proceed? [Y/N] \033[1m")
            choice = yninput()
            if choice.lower() == "n":
                update()
            grain = grain - planted
            land = land - planted
            harvest = int(planted * harvrate)
            grain = grain + harvest
            print("\033[0m")
            if harvrate == 0.5:
                middle("Disaster has struck!")
                middle("The gods are angry and have bestowed punishment upon your land.")
                middle("A catastrophic flood has cut your harvest in half.")
            elif harvrate == 10:
                middle("It's a miracle!")
                middle("Praise the gods, for they have truly blessed you this year.")
                middle("This year's harvest is beyond bountiful. All those sacrifial lambs finally paid off.")
            elif harvrate == 1:
                middle("You have been cursed by bad weather and unforgiving soil this year.")
                middle("You are lucky to even reap just what you sow.")
            elif harvrate == 2:
                middle("The weather has been sufficient and your are fortunately free of plagues and rampaging hordes  .")
                middle("You have made back your investment and the same again in profit.")
            elif harvrate == 3:
                middle("You may rejoice, for the land has been kind to you this year.")
                middle("It looks like your harvest will be thricefold!")
            
            nxt("screen")
            print(f"You planted \033[1m\033[34m{planted}\033[0m bushels and harvested \033[1m\033[34m{harvest}\033[0m. \
    \nYou now have \033[1m\033[34m{grain}\033[0m bushels of grain and \033[1m\033[34m{land}\033[0m acres of land")
            break

    plant()
    nxt("screen")
    disaster()

    # truncate rat loss? It says it can be any percent between 10 and 30, which leads to float values for 'ratloss'
    ### rat infestation, maybe there is a better way to work out percentage
    # but for now try:
    # ratrate = [1,2,3,4,5,6,7,8,9,10]  NO NEED, just do the same with randint
    # rats =
    # rats = random.choice(ratrate)
    if mode == "e":
        r = 15
        ri = 20
    elif mode == "m":
        r = 10
        ri = 30
    elif mode == "h":
        r = 5
        ri = 40
    rats = random.randint(1, r)
    # print(rats)
    if rats == 1:
        infest = random.randint(10, ri)
        # print(infest)
        ratlossratio = float(infest / 100)
        # print(ratlosspc)
        ratloss = int(grain * ratlossratio)
        grain = int(grain - ratloss)
        ratlosspc = int(ratlossratio * 100)

        print(f"You have been infested with rats! They have eaten \033[1m\033[34m{ratloss}\033[0m bushels of grain, \
which is \033[1m\033[34m{ratlosspc}%\033[0m of your total store.")
        print(f"You now have \033[1m\033[34m{grain}\033[0m left")
    else:
        print(f"Your grain is safe from rats this year. You have \033[1m\033[34m{grain}\033[0m remaining.")
        ratloss = 0

    # do this as very last thing, declare (as in move print statements) start of next year
    price = random.randint(19, 22)
    # print(f"The price of land is now {price} bushels per acre.")
    if mode == "e":
        mini = 0
        maxi = 5
    elif mode == "m":
        mini = 1
        maxi = 10
    elif mode == "h":
        mini = 5
        maxi = 15
    migrants = random.randint(mini, maxi)
    # print (migrants, "migrants came this year.")
    population = population + migrants
    # print("Your population is now", population)

    nxt("year")
    

    # Add score system Is it worth including apc in status, or keeping as a surprise? Maybe as a warning triggered by if statement?
print("\n\n")
middle(f"           There are currently \033[1m\033[34m{apc}\033[0m acres for each person in your kingdom.")
print("\n")
if apc < 10:
    middle("What happened? Your kingdom is less prosperous than when you started. There is less land for each person.")
    middle("You should hang your head in shame, history will remember you as an uncaring and foolish king. It's the desert for you")
elif apc == 10:
    middle("You maintained your country's wealth, as each person has the same amount of land as when you started.")
    middle("You won't go down in the history books, but you could have done worse")
elif apc < 12:
    middle("Well done! You did a fine job in taking care for your people, as they now have more land than when you started your reign.")
    middle("There is room for improvement, but all in all a good job.")
elif apc < 14:
    middle("Fantastic! You grew the wealth of your people by a significant amount.")
    middle("They will sing your praises 'till the day you die and long after you have journeyed to the other realm.") 
    middle("You will be remembered as a strong and wise leader")
elif apc >= 14:
    middle("Ye Gods! Your reign as brought untold wealth to the kingdom,")
    middle("your people have prospered and you shall go down in history as one of the great leaders of all time!")
