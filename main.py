#Notes re: packages installed - see README for details

#Imports 
import pandas as pd
import matplotlib.pyplot as plt
import csv 
import math
import time
import datetime

from csv import DictReader

#Variables
hoursperday = 24
firstname = str()
specialneeds = str()
bestsize = str()
lifestage = str()
social = str()
sex = str()

#functions
def build_user(value1, value2, value3, value4, value5, value6):
    '''Return a dictionary of information about a user'''
    user = {'name': value1, 'specialneeds': value2, 'bestsize': value3, 'lifestage': value4, 'social': value5, 'sex': value6}
    return user

#Other necessary stuff
owner = {}
key1 = firstname
key2 = specialneeds
key3 = bestsize
key4 = lifestage
key5 = social
key6 = sex

#SECTION ONE Chatbot
#Introduce project to the User and collect input
#Elimination round (3 questions) force game EXIT
#Users who make it through elimination round continue to Round Two: Q&A section
print('***ADOPT A SHELTER PET***')
print("\U0001F43E", "\U0001F43E", "\U0001F43E", "\U0001F43E", "\U0001F43E")#pawprints
time.sleep(2)
print('\nThis program walks you through') 
time.sleep(2)
print('a logical series of considerations')
time.sleep(2)
print('and simple calculations')
time.sleep(2)
print('to successfully adopt a shelter pet.')
time.sleep(2)
print("\nFirst, you'll answer questions") 
time.sleep(2)
print('regarding your lifestyle, budget,')
time.sleep(2)
print('free time, and living space.') 
time.sleep(2)
print("\nAfter completing the Q&A section,")
time.sleep(2)
print("we'll take a quick look")
time.sleep(2)
print('at research regarding shelter pets')
time.sleep(2)
print('in the United States.')
time.sleep(2)
print('\U0001F496', '\U0001F496', '\U0001F496')
print("\nFinally, we'll use YOUR prerequisites")
time.sleep(2)
print('to search for YOUR perfect pet match')
time.sleep(2)
print('at an imaginary Animal Shelter.\n')
time.sleep(2)
print("Let's get started!\n")
time.sleep(2)

#DEALBREAKER responses that will force an Exit
print('***ROUND ONE: ELIMINATION***\n')
time.sleep(2)
print('\U0001f6a7', '\U0001f6a7', '\U0001f6a7')
print("We'll start with a brief ELIMINATION ROUND.\n")
time.sleep(2)
print("Let's establish that you meet MINIMAL criteria to adopt a shelter pet.\n")
time.sleep(2)
print('Here we go.')

#AGE REQUIREMENT
#Owner Age corresponds to recommended dog life stage
print('\n***AGE REQUIREMENT***\n')
time.sleep(2)
print('Adopting a shelter pet is a lifetime commitment.\n')
time.sleep(2)
print('Although people are often excited by the idea of adopting a puppy,')
time.sleep(3)
print('we recommend adopting a dog with a life stage that matches your age.\n')
time.sleep(3)
print('The average life expectancy for an adult in 2020 is 78 years.\n')
time.sleep(3) 
print('The average life expectancy for a dog is 12 years.\n')
time.sleep(3)
print('78 human years (adult life span) divided by 12 dog years (dog life span)')
time.sleep(3)
print('equates to 6.5 human years for each dog year.\n')
time.sleep(2)
print("Let's divide your age by 6.5 to find the equivalent in dog years.\n")
time.sleep(3)
owner_age = int(input('Enter your age in years. Use a whole number between 1 and 100: \n'))
while owner_age <= 0 or owner_age > 100:
    owner_age = int(input("Please choose a number between 1 and 100: "))
time.sleep(2)
if (owner_age) < 16:
    print("We're sorry.")
    print('For this exercise, you must be at least 16 years old to adopt a shelter dog.')
    print('Please consider volunteering at your local animal shelter instead.')
    exit()
elif (owner_age) > 66:
    print("We're sorry.")
    print("The maximum recommended age of a pet owner is 66 years old.")
    print("That's the average human life expenctancy (78yrs)")
    print('minus the average dog life expectancy (12yrs).')
    time.sleep(2)
    print('Please consider volunteering at your local animal shelter instead.')
    exit()
else:
    #REQUIREMENT MET: Build a conversion tool (calculator) to convert
    #one form of user input to another and display it
    #converts human years to dog years
    dog_years = int(owner_age) / 6.5
    print('\nVoila! Your age in dog years is', int(dog_years), 'years.')
    print("Let's continue.")
    time.sleep(2)

#FINANCIAL COMMITMENT
print('\n***FINANCIAL COMMITMENT***')
time.sleep(2)
print('\nYou told us you plan to adopt a shelter DOG.\n')
time.sleep(2)
print("\U0001F9AE", "\U0001F436", "\U0001F429")
print('According to ROVER.com,')
time.sleep(2)
print('the annual cost of owning a dog -') 
time.sleep(2)
print('adopted from a shelter,') 
time.sleep(2)
print('not purchased from a breeder -')
time.sleep(2) 
print('runs $650 to $1000 per year.\n')
time.sleep(2)
print('This estimate covers basic costs like food,')
time.sleep(2)
print('necessary vaccines, toenail trims,') 
time.sleep(2)
print('flea, tick, and heartworm protection,')
time.sleep(2)
print('bedding, collars, leash/harness, and toys.\n')
time.sleep(2)
print("Let's also factor in the adoption fee")
time.sleep(2)
print('and the cost to spay/neuter your pet.\n')
time.sleep(2)
print('And what if you need to board your pet at least once a year?\n')
time.sleep(2)
print("Let's estimate an annual cost between")
time.sleep(2)
print('$1000 and $1500 to be safe.\n') 
time.sleep(2)
print('\U0001F4B2', '\U0001F4B2', '\U0001F4B2')
print('Can you afford this financial commitment?')
time.sleep(2)
money = input('Type y for YES or n for NO: ').lower()
time.sleep(2)
while not (money == 'y' or money == 'n'):
    money = input('Invalid input. Enter y or n: ')
#Game will end if user answers NO
#If Y, proceed
if money == 'n':
    print('\nThank you for the honest assessment of your financial situation.')
    time.sleep(2)
    print('At this time, we cannot recommend adopting a shelter pet.')
    time.sleep(2)
    print('Please reconsider at a time when you have more wiggle room in your budget.')
    time.sleep(2)
    print('There will always be AWESOME dogs looking for FOREVER homes.')
    exit()
else:
    # beaming face with smiling eyes
    print("\U0001F601")
    print("Excellent! You're one step closer to sucessfully adopting a shelter pet.")
    time.sleep(2)

#FREE TIME PER DAY
print('\n***FREE TIME PER DAY***')
time.sleep(2)
print('\nInstructions: Enter the number of hours you spend') 
time.sleep(2)
print('on each of the activities below, per day.') 
time.sleep(2)
print("Please type a whole number between 0-24 for each answer.\n")
time.sleep(2)
sleep = int(input('Hours spent sleeping per day: '))
while sleep < 0 or sleep > 24:
    sleep = int(input("Please choose a number between 0 and 24: "))
time.sleep(2)
cook = int(input('Hours spent cooking + eating per day: '))
while cook < 0 or cook > 24:
    cook = int(input("Please choose a number between 0 and 24: "))
time.sleep(2)
groom = int(input('Hours spent on showering, hair, makeup, shaving, etc. daily: '))
while groom < 0 or groom > 24:
    groom = int(input("Please choose a number between 0 and 24: "))
time.sleep(2)
commute = int(input('Hours spent commuting daily: '))
while commute < 0 or commute > 24:
    commute = int(input("Please choose a number between 0 and 24: ")) 
time.sleep(2)
work = int(input('Hours spent working daily: '))
while work < 0 or work > 24:
    work = int(input("Please choose a number between 0 and 24: "))
time.sleep(2)
errands = int(input('Hours spent running errands daily: '))
while errands < 0 or errands > 24:
    errands = int(input("Please choose a number between 0 and 24: "))
time.sleep(2)
gym = int(input('Hours spent at the gym daily: '))
while gym < 0 or gym > 24:
    gym = int(input("Please choose a number between 0 and 24: "))
time.sleep(2)
children = int(input('Hours spent caring for children or other adults daily: '))
while children < 0 or children > 24:
    children = int(input("Please choose a number between 0 and 24: "))
time.sleep(2)
community = int(input('Hours spent volunteering, coaching, or at church daily: '))
while community < 0 or community > 24:
    community = int(input("Please choose a number between 0 and 24: "))
time.sleep(2)
# grinning face with sweat
print("\U0001F605")
print("Whew! Aren't you exhausted?\n")
time.sleep(2)
print('The American Humane Society recommends')
time.sleep(2)
print('that pet owners have') 
time.sleep(2)
print('a minimum of 3 free hours per day')
time.sleep(2)
print('to devote to caring for, training, and playing with their pets.\n')
time.sleep(2)
hoursfordog = int(hoursperday) - int(sleep) - int(cook) - int(groom) - int(commute) - int(work) - int(errands) - int(gym) - int(children) - int(community)
print('You indicated you have ' + str(hoursfordog) + ' hours of FREE time daily.')
time.sleep(2)
if hoursfordog < 3: 
   print('\nThank you for the honest assessment of your free time per day.')
   time.sleep(2)
   print('At this time, we cannot recommend adopting a shelter pet.')
   time.sleep(2)
   print('Please reconsider when you have more wiggle room in your schedule.')
   time.sleep(2)
   print('There will always be AWESOME dogs looking for FOREVER homes.')
   exit()
else:
   # beaming face with smiling eyes
   print("\U0001F601")
   print("Excellent! You're one step closer to sucessfully adopting a shelter pet.\n")
   time.sleep(2)

#Collect Owner Input to create a Dictionary
print('***ROUND TWO: PREREQUISITES***\n')
print('***INTRODUCE YOURSELF***\n')
time.sleep(2)
#dict key1 is name
value1 = input('Enter your first name: ') 
time.sleep(2)
print("\U0001F44b")
print('Hello ' + value1 + '.')
print("It's nice to meet you.")
time.sleep(2)

#EXPERIENCED PET OWNER 
print('\n***PREVIOUS PET OWNERSHIP EXPERIENCE***')
time.sleep(2)
print('\nHave you been the primary caregiver for a dog before?') 
time.sleep(2)
experience = input('Type y for YES or n for NO: ').lower() 
time.sleep(2)
while not (experience == 'y' or experience == 'n'):
    experience = input('Invalid input. Enter y or n: ')
if experience == 'y':
    print('\nYou may want to consider adopting a puppy.')
else:
    print('\nWe recommend that NOVICE pet owners adopt a SENIOR dog.')
    time.sleep(2)
#Special Needs
print('\nWould you like to adopt a dog with Special Needs?')
time.sleep(2)
key2 = specialneeds
value2 = input('Type y for YES or n for NO:')
while not (value2 == 'y' or value2 == 'n'):
    value2 = input('Invalid input. Enter y or n: ')

#INDOOR OUTDOOR LIVING SPACE
print('\n***INDOOR + OUTDOOR LIVING SPACE***')
time.sleep(2)
print('\nWhen considering what size dog to adopt,')
time.sleep(2)
print('consider the size of your living space.')
time.sleep(2)
#Space corresponds to Size in pet dictionary: Small Medium Large
print('\nWhich statement best describes your indoor+outdoor living space?')
time.sleep(2)
print('Apartment or condo with nearby green space?')
time.sleep(2)
print('Modest home with fenced yard?')
time.sleep(2)
print('Large home with 1+ acres of fenced property?')
time.sleep(2)
home_size = input('\nType a for Apt.Condo, s for Small Home, or l for House.Land: ').lower()
time.sleep(2)
while not (home_size == 'a' or home_size == 's' or home_size == 'l'):
    home_size = input('Invalid input. Enter a, s, or l: ')
if home_size == 'a':
    print('\nA SMALL dog may be most comfortable in an apartment or condominium.')
elif home_size == 's':
    print ('\nA MEDIUM dog may be most comfortable in a modest home.')
else:
    print('\nYour living space will accomodate a LARGE dog.')
time.sleep(2)
print('\nREALITY CHECK: What size dog do you prefer?')
time.sleep(2)
#key3 bestsize
value3 = input('\nType s for Small, m for Medium, or l for Large: ').lower()
time.sleep(2)
while not (value3 == 's' or value3 == 'm' or value3 == 'l'):
    value3 = input('Invalid input. Enter s, m, or l: ')

#Life Stage
print('\n***LIFE STAGE***')
time.sleep(2)
print('\nWe established your age in dog years is', int(dog_years), 'years.')
time.sleep(2)
print("\nCompare your age in DOG YEARS to the pet Life Stage below:")
time.sleep(2)
print('\nPuppy...less than 1 year old')
print ('\nRemember: Only experienced dog owners with ample leisure time should adopt a puppy.')
time.sleep(3)
print('\nAdolescent...1-2 years old')
time.sleep(2)
print('\nAdult...3-6 years old')
time.sleep(2)
print('\nSenior...7+ years old\n')
time.sleep(2)
print('Which pet Life Stage aligns with your age in dog years?')
time.sleep(2)
#key4 lifestage
value4 = input('Type p for Puppy, a for Adolescent, d for Adult, or s for Senior: ').lower()
time.sleep(2)
while not (value4 == 'p' or value4 == 'a' or value4 == 'd' or value4 == 's'):
    value4 = input('Invalid input. Enter p, a, d or s: ')

#Thank user for perserverance
print('\nOnly TWO more questions!')
time.sleep(2)
# smiling face with halo
print("\U0001F607")
print('PATIENCE and FOLLOW-THROUGH are important traits in a pet owner.')
time.sleep(2)

#SOCIAL BEHAVIOR
#Solo Pursuits: 1 dog HH, Small Groups: Reliably Social, Comfortable in Crowds: Never Met a Stranger
print('\n***SOCIAL BEHAVIOR***')
time.sleep(2)
print('\nYour dog will look to you as Pack Leader for his/her social cues.')
time.sleep(2)
print('If you are anxious or relaxed, the dog will mirror your energy.\n')
time.sleep(2)
print('Which description below best describes your Social Behavior?') 
time.sleep(2)
print('Solo Pursuits, Small Groups, or Comfortable in Crowds?\n') 
time.sleep(2)
#key5 social
value5 = input('Type sp for Solo Pursuits, sg for Small Groups, or cc for Comfortable in Crowds: ').lower()
time.sleep(2)
while not (value5 == 'sp' or value5 == 'sg' or value5 == 'cc'):
    value5 = input('Invalid input. Enter sp, sg, or cc: ')

#Preference for Male or Female pet
print('\n***MALE OR FEMALE PET?***')
time.sleep(2)
print('\nFor this exercise, please select either a MALE or FEMALE pet.')
time.sleep(2)
#key6 sex
value6 = input("Type m for Male or f for Female: ").lower()
time.sleep(2)
while not (value6 == 'm' or value6 == 'f'):
    value6 = input('Invalid input. Enter m or f: ')

#Leave Section One
print('\n***PHASE ONE COMPLETED***')
print("\U0001F3C6")
print('\nCongratulations! You completed the Prerequisites section.\n')
time.sleep(2)
# beaming face with smiling eyes
print("\U0001F601")
print("You're one step closer to sucessfully adopting a shelter pet.\n")

#Pull user input into a list
#Requirement met: Create a list or dictionary with multiple values
#Use at least one value elsewhere in your program
#Will be used in Section 3: Pet Match
owner_list = [value1, value2, value3, value4, value5, value6]
print('We recorded the answers you gave us as follows:\n')
print(owner_list)
time.sleep(3)
print("\nLater in this program, we'll will match your answers")
print('to attributes of available shelter dogs')
print('to identify your Perfect Pet Match.\n')
time.sleep(3)

##PHASE TWO: Data Analysis + Visualization
#DATA ON US SHELTER PETS
print('***SECTION 2: SHELTER PET DATA***\n')
time.sleep(2)
print('On the surface,') 
time.sleep(2)
print('America appears to be a nation of PET LOVERS.')
time.sleep(2)
print('\nAccording to the American Pet Products Association') 
time.sleep(2)
print('APPA 2020 Pet Owner Survey:\n')
time.sleep(2)
print('Americans spent over $100 BILLION') 
time.sleep(2)
print('on pet products and services in 2020')
time.sleep(2)
print('\n70 percent of all US households include at least 1 pet')
time.sleep(2)
print('\n44 percent of all US households include at least 1 dog')
time.sleep(2)
print("\nBut there's a darker side to this story.")
print("\U0001F631", "\U0001F631", "\U0001F631")
time.sleep(2)
print('\nSadly, according to the ASPCA - ') 
time.sleep(2)
print('7.6 million companion animals end up in US shelters each year.\n')
time.sleep(3)
print("Many are surrendered due to an owner's economic instability") 
time.sleep(2)
print("or because they are incompatible with an owner's lifestyle.\n")
time.sleep(2)
print('35 percent of these animals (2.7 million)')
time.sleep(2) 
print('will be EUTHANIZED within 12 months.') 
time.sleep(2)

#introduce data
print("\nLet's look at simple table of data")
time.sleep(2)
print('illustrating various intake reasons') 
time.sleep(2)
print('for 2000+ dogs at a shelter in Indianapolis.\n')
time.sleep(2)

#REQUIREMENT MET: read data from external file + visualize it
#pandas reads csv file to create a data frame
df = pd.read_csv("csv.dogs2visualize.csv")
#sort data in the dataframe by column Number of Dogs
#pandas sorts values in ascending order by default
df.sort_values(by="numberOfDogs")
#print the resulting data frame
print(df)

#User closes screen with the plot
input("Press any key to continue: ")
time.sleep(2)
print('\nOK. That was interesting - but DEPRESSING.')
time.sleep(2)
print('\nThe most frequently recorded intake reason')
time.sleep(2)
print('is Stray/Dumped.')
time.sleep(2)
print('\nThis is easier to see displayed as a bar chart.\n')
time.sleep(2)

#display horizontal bar chart using pandas
data = pd.read_csv("csv.dogs2visualize.csv")
df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

plt.barh(X,Y, color = 'g')
#rotate y-labels and align horizontally with bar
plt.xticks(rotation=20, horizontalalignment="center")
plt.title("Shelter Dogs - Intake Reasons")
plt.xlabel('Number of Dogs')
plt.ylabel("Intake Reasons")
plt.show()

#User closes screen with the plot
input("Press any key to continue: ")
time.sleep(2)
print("\nLet's move on to something more fun!")

#SHELTER PETS AND SOCIAL MEDIA
#Explore in version 2
# Connect to an API, read data into your app
#Use Twiter API + Twython or Tweepy
#aggregate tweets using DOG + "shelter", "rescue", "adopt"
#perform sentiment analysis
#display positive words as Word cloud shaped like a dog (dog "mask")

print('\n***PHASE TWO COMPLETED***')
print("\U0001F947", "\U0001F947")
print('\nYou appear to be RARE human who can delay gratification!')
time.sleep(2)
print('You patiently examinded your lifestyle and resources.')
time.sleep(2)
print('You also reviewed data re: shelter pets.')
time.sleep(2)
print('\nCongratulations!')
# beaming face with smiling eyes
print("\U0001F601")
print("You're one step closer to sucessfully adopting a shelter pet.\n")

#PHASE 3
#SHELTER VISIT 
print('***PHASE 3: SHELTER PET MATCHING***\n')
time.sleep(2)
print('In this exercise, we will evauluate available pets,')
time.sleep(2) 
print('comparing their attributes')
time.sleep(2) 
print('against the adoption prerequisites')
time.sleep(2) 
print('you entered earlier.\n') 
time.sleep(2)
print('On the day you visit')
time.sleep(2)
print('our imaginary shelter,')
time.sleep(2)
print('there are 100 dogs available for adoption.')
time.sleep(2)
print("\nLet's start the matching process!") 
time.sleep(2)

#Convert owner_list values to the value pairs in a new owner dictionary
#Dictionary keys are:
#key1 = 'name'
#key2 = 'specialneeds'
#key3 = 'bestsize'
#key4 = 'lifestage'
#key5 = 'social'
#key6 = 'sex'
print("We start with your information:\n")
time.sleep(2)
#REQUIREMENT MET: 3+functions and/or methods; 1 function must return a value
owner = build_user(value1, value2, value3, value4, value5, value6)
print(owner)

#PET MATCH
print("\nAnd here come today's available dogs!")
print("\U0001F43E", "\U0001F43E", "\U0001F43E", "\U0001F43E", "\U0001F43E", "\U0001F43E")#pawprints
time.sleep(2)
#convert csv.dogs100dictprep.csv file to a LIST of dictionaries
#Each dictionary in the list holds the attributes of a single pet
#open file in read mode
with open('csv.dogs100dictprep.csv', 'r') as read_obj:
    #pass file object to DictReader(), get DictReader object
    dict_reader = DictReader(read_obj)
    #get a list of dictionaries from dict_reader
    list_of_dict = list(dict_reader)
    print(list_of_dict)

time.sleep(2)
print("\nYikes! That's confusing.\n")
time.sleep(2)
print("\U0001F4A5", "\U0001F4A5", "\U0001F4A5")
print("Let's use the POWER of P-Y-T-H-O-N")
print('to quickly return ONLY those dogs that match your needs.')
time.sleep(3)

#compare values in owner dictionary against values in petstoadopt dictionary
#assign list_of_dict to a new variable
petstoadopt = list_of_dict
#start with full complement of available pets...petstoadopt
#start matching against user prerequisites
#rename list_of_dict
petstoadopt = list_of_dict
print('\nHere is the full list of available pets:\n')
print(petstoadopt)
time.sleep(4)

#Round 1 Pet Match: Special Needs (value2)
#use a dictionary comprehension to match specialneeds:value2
print ("\nFILTER: Match pets against user's 'specialneeds' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
keyValList = [str(value2)] #value you are matching against
newList1 = [d for d in petstoadopt if d['specialneeds'] in keyValList]
print(newList1)
time.sleep(3)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
result1 = len([ele for ele in newList1 if isinstance(ele, dict)])
print("\nSPECIAL NEEDS: The number of matching pets is " + str(result1))
time.sleep(3)

#Round 2 Pet Match: Best Size (value3)
#use a dictionary comprehension to match bestsize:value3
print ("\nFILTER: Match pets against user's 'bestsize' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
keyValList = [str(value3)] #value you are matching against
newList2 = [d for d in newList1 if d['bestsize'] in keyValList]
print(newList2)
time.sleep(3)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
result2 = len([ele for ele in newList2 if isinstance(ele, dict)])
print("\nSpecial Needs + Best Size: NEW number of matching pets is " + str(result2))
time.sleep(3)

#Round 3 Pet Match: Life Stage (value4)
#use a dictionary comprehension to match lifestage:value4
print ("\nFILTER: Match pets against user's 'lifestage' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
keyValList = [str(value4)] #value you are matching against
newList3 = [d for d in newList2 if d['lifestage'] in keyValList]
print(newList3)
time.sleep(3)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
result3 = len([ele for ele in newList3 if isinstance(ele, dict)])
print("\nSpecial Needs, Best Size, Life Stage: NEW number of matching pets is " + str(result3))
time.sleep(3)

#Round 4 Pet Match: Social Needs (value5)
#use a dictionary comprehension to match social:value5
print ("\nFILTER: Match pets against user's 'social' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
keyValList = [str(value5)] #value you are matching against
newList4 = [d for d in newList3 if d['social'] in keyValList]
print(newList4)
time.sleep(3)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
result4 = len([ele for ele in newList4 if isinstance(ele, dict)])
print("\nSpecial Needs, Best Size, Life Stage, Social Needs: Number of matching pets is " + str(result4))
time.sleep(3)

#Commenting out lines 649- 663 because there is a problem with dictreader
#when dictreader converts my csv file, it adds an extra space for column 6, sex
#values in the new dictionaries appear with an extra space - 
#"f " or "m " rather then 'f' or 'm' - which crashes the program
#could not find any explanation online - will need to resolve at a later date

#Round 5 Pet Match: Sex (value6)
#use a dictionary comprehension to match sex:value6
#print ("\nFILTER: Match pets against user's 'sex' answer: \n" )
#filter by list comprehension to dreate a new list of pet dictionaries
#keyValList = [str(value6)] #value you are matching against
#newList5 = [d for d in newList4 if d['sex'] in keyValList]
#print(newList5)
#time.sleep(2)

#How many pet dictionaries are in the new list?
#Use list comprehension and isinstance()
#result5 = len([ele for ele in newList5 if isinstance(ele, dict)])
#print("\nSpecial Needs, Best Size, Life Stage, Social Needs, Sex: Number of matching pets is " + str(result5))
#time.sleep(2)

#PET MATCH RESULTS
if result4 < 1:
    print("\nWe're sorry. None of today's available pets met your prerequisites.")
    time.sleep(2)
    print('Please return next week and try again.') 
    time.sleep(2)
    print('There will always be AWESOME dogs looking for STABLE forever homes.') 
    time.sleep(2)
elif result4 == 1:
    print('\nKISMET! You found your ONE AND ONLY perfect shelter pet!')
    time.sleep(2)
else:
    print('\nSurprise! Multiple pets met your criteria. How will you decide?')
    time.sleep(2)
    print('This could easily happen in real life. What would you do?')
    time.sleep(2)

print('\n***PHASE THREE COMPLETED***')
print("\U0001F680", "\U0001F680", "\U0001F680")#rockets
time.sleep(2)
print('\nCongratulations!')
# beaming face with smiling eyes
print("\U0001F601")
print("You're one step closer to sucessfully adopting a shelter pet.\n")

#PHASE FOUR: COUNTDOWN TIMER AND PROGRAM ENDS
print('***PHASE 4: COUNTDOWN TO ADOPTING A PET IN REAL LIFE***')
time.sleep(2)
#REQUIREMENT MET: Calculate + display data based on an external factor (like a count down)
print("\nYou've learned so much!")
time.sleep(2)
print("You've assessed your situation, looked at data,")
time.sleep(2)
print('and practiced meeting adoptable pets at a make-believe shelter.') 
time.sleep(2)
print("\nNow you're ready to adopt a shelter pet in real life!\n") 

#REQUIREMENT MET: Calculate + display data based on an external factor (example: like a count down)
current_date = datetime.datetime.now()
print("Today's date is", current_date, '.')
time.sleep(2)

print('\nIt typically takes about 14 days') 
print('for an animal shelter to process a pet adoption form.')
time.sleep(2)

print("\nHere's a handy calendar to help you use that time wisely!")
time.sleep(2)

visit_shelter = current_date + datetime.timedelta(days=1)
print('\nDate:', visit_shelter)
print('Tomorrow, visit your local animal shelter.')
time.sleep(2)
print('Discuss your adoption prerequisites with shelter staff,') 
time.sleep(2)
print('and meet several possible pet matches.') 
time.sleep(2)
print("DON'T sign the adoption papers today!")
time.sleep(2)

think_over = current_date + datetime.timedelta(days=2)
print('\nDate:', think_over)
time.sleep(2)
print('Go home and think about the animals you met.')
time.sleep(2)
print('Allow at least 24hrs to make this important decision.')
time.sleep(2)

make_decision = current_date + datetime.timedelta(days=3)
print('\nDate:', make_decision)
time.sleep(2)
print("Make your decision. If possible, identify your Top 2 choices.")
time.sleep(2)

submit_form = current_date + datetime.timedelta(days=4)
print('\nDate:', submit_form)
time.sleep(2)
print("Submit your pet adoption application online or in-person.")
time.sleep(2)

purchase_supplies = current_date + datetime.timedelta(days=5)
print('\nDate:', purchase_supplies)
time.sleep(2)
print("Purchase supplies from local merchants.")
time.sleep(2)

order_supplies = current_date + datetime.timedelta(days=6)
print('\nDate:', order_supplies)
time.sleep(2)
print("Order any supplies not available locally.")
time.sleep(2)

screening_call = current_date + datetime.timedelta(days=8)
print('\nDate:', screening_call)
time.sleep(2)
print('Screening Call: Answer any questions from the shelter adoption coordinator.')
time.sleep(2)

orders_arrive = current_date + datetime.timedelta(days=9)
print('\nDate:', orders_arrive)
time.sleep(2)
print('The supplies you ordered should have arrived.')
time.sleep(2)

outdoor_space = current_date + datetime.timedelta(days=10)
print('\nDate:', outdoor_space)
time.sleep(2)
print("Dog-proof your outdoor space, including your car.")
time.sleep(2)

indoor_space = current_date + datetime.timedelta(days=11)
print('\nDate:', indoor_space)
time.sleep(2)
print("Dog-proof your indoor space.")
time.sleep(2)

notification = current_date + datetime.timedelta(days = 13)
print('\nDate:', notification)
time.sleep(2)
print('Notification received! Your application has been approved!')
time.sleep(2)

come_home = current_date + datetime.timedelta(days = 14)
print('\nDate:', come_home)
time.sleep(2)
print("Today's the day! Bring home your new furry friend!")
time.sleep(2)

print('***\nYOU DID IT!***')
print("\U0001F43E", "\U0001F43E", "\U0001F43E")#pawprints
time.sleep(2)
print('\nThank you for completing this Adopt a Shelter Pet exercise.') 
time.sleep(2)
print('Remember: To Save Lives - Advocate, Volunteer, or Donate.')
time.sleep(2)
print('\U0001F496', '\U0001F496', '\U0001F496')#hearts
print('And if you can do more - Rescue, Foster, Adopt.') 
print('***THE END***')

