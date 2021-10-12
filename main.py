#Imports 
import math
import time
#Variables
hoursperday = 24
#Functions
#PHASE ONE User Prerequisites
#Introduce project to the User
print('***ADOPT A SHELTER PET***\n')
time.sleep(2)
print('This program walks you through') 
time.sleep(2)
print('a logical series of considerations')
time.sleep(2)
print('and simple calculations')
time.sleep(2)
print('to successfully adopt a shelter pet.\n')
time.sleep(2)
print("First, you'll answer questions") 
time.sleep(2)
print('regarding your lifestyle, budget,')
time.sleep(2)
print('free time, and living space.\n') 
time.sleep(2)
print("After the Q&A section,")
time.sleep(2)
print("we'll take a quick look")
time.sleep(2)
print('at research regarding shelter pets')
time.sleep(2)
print('in the United States.\n')
time.sleep(2)
print("We'll also look at") 
time.sleep(2)
print('what people are saying')
time.sleep(2)
print('about shelter pets on Twitter.\n')
time.sleep(2)
print("Finally, we'll use YOUR prerequisites")
time.sleep(2)
print('to search for YOUR perfect pet match')
time.sleep(2)
print('at an imaginary Animal Shelter.\n')
time.sleep(2)
print("Let's get started!\n")
time.sleep(2)
print('***INTRODUCE YOURSELF***\n')
time.sleep(2)
firstname = input('Enter your first name: ')
time.sleep(2)
print('\nHello ' + firstname + '.')
print("It's nice to meet you.")
time.sleep(2)
print('\n***QUESTIONS AND ANSWERS***')
time.sleep(2)
#FINANCIAL COMMITMENT
print('\n***FINANCIAL COMMITMENT***')
time.sleep(2)
print('\nYou told us you plan to adopt a shelter DOG.\n')
time.sleep(2)
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
print('Can you afford this financial commitment?')
time.sleep(2)
money = input('Type y for YES or n for NO: ')
time.sleep(2)
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
    print("\nExcellent! You're one step closer to sucessfully adopting a shelter pet.")
time.sleep(2)
#FREE TIME PER DAY
print('\n***FREE TIME PER DAY***')
time.sleep(2)
print('\nInstructions: Enter the number of hours you spend') 
time.sleep(2)
print('on each of the activities below, per day.') 
time.sleep(2)
print('Hours spent is calculated using whole numbers.\n')
time.sleep(2)
sleep = input('Hours spent sleeping per day: ')
time.sleep(2)
cook = input('Hours spent cooking + eating per day: ') 
time.sleep(2)
groom = input('Hours spent on showering, hair, makeup, shaving, etc. daily: ')
time.sleep(2)
commute = input('Hours spent commuting daily: ') 
time.sleep(2)
work = input('Hours spent working daily: ')
time.sleep(2)
errands = input('Hours spent running errands daily: ')
time.sleep(2)
gym = input('Hours spent exercising daily: ')
time.sleep(2)
children = input('Hours spent caring for children or other adults daily: ')
time.sleep(2)
community = input('Hours spent volunteering, coaching, or at church daily: ')
time.sleep(2)
print("\nWhew! Aren't you exhausted?\n")
time.sleep(2)
print('The American Humane Society recommends')
print('that pet owners have') 
print('a minimum of 3 free hours per day')
print('to devote to caring for, training, and playing with their pets.\n')
hoursfordog = int(hoursperday) - int(sleep) - int(cook) - int(groom) - int(commute) - int(work) - int(errands) - int(gym) - int(children) - int(community)
print('You indicated you have ' + str(hoursfordog) + ' hours of FREE time daily.')
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
   print("\nExcellent! You're one step closer to sucessfully adopting a shelter pet.")
time.sleep(2)
#REQUIREMENT...(script above) use 3+ methods with returned value used again in the code
#EXPERIENCED PET OWNER 
#Corresponds to pet dictionary: Special Needs
#INDOOR OUTDOOR LIVING SPACE
#Corresponds to pet dictionary: Size Small Medium Large
#HOW OLD ARE YOU IN DOG YEARS
#REQUIREMENT...item above...Convert user input to another type and display (years to dog years)
#YOUR ENERGY LEVEL
#Corresponds to pet dictionary value Senior Adult Puppy
#SOCIAL PATTERNS
#Solo Pursuits: 1 dog HH, Small Groups: Reliably Social, Comfortable in Crowds: Never Met a Stranger
#MALE OR FEMALE PET
#used as deciding factor if more than one matching pet remains at end of program
##PHASE TWO: Data Analysis + Visualization
#DATA ON US SHELTER PETS
#Analyze open-source JSON file re: shelter pets (dogs) in US
#REQUIREMENT: Read JSON file into your app MUST USE pc of data from file in the program
#REQUIREMENT: Visualize data in color plot
#SHELTER PETS AND SOCIAL MEDIA
#REQUIREMENT: Connect to an API, read data into your app
#Use Twython and Twiter API, aggregate tweets using DOG + "shelter", "rescue", "adopt"
#Before you practice adopting a dog in our make-believe Shelter,
#let's check Twitter to see what people are sharing about adopting a rescue DOG
#REQUIREMENT: Analyze text and display info about it, Visualize data
#Use aggregated tweets to create a Word cloud shaped like a dog (dog "mask")
#YOU ARE READY FOR PHASE 3
#Congratulations! 
# You appear to be a level-headed human who can delay gratification!
# You took the time to examine your lifestyle and your resources.
#You also did some preliminary research about shelter pets in the USA.
#SHELTER VISIT 
#In this exercise, you will practice meeting pets 
#and considering their attributes 
#against your lifestyle prerequisites. 
#On the day you visit our imaginary shelter
#there are 10 pets available for adoption.
#Let's meet the pets assembled in the Green Room. 
#MEET THE PETS
#REQUIREMENT: create DICTIONARY, several values, retrieve at least 1 value & use it
#Today's DOGS available for adoption are:
# Print dictionary contents as Pet Name, Special Needs, Size, Age, Life Stage, Social, Gender
#PET MATCH
#perfectpet = []
#LOOP: Iterate over values in Owner Dictionary vs. values in Pets Dictionary
#use .append or .delete methods to alter list of pets matching each prerequisite
#DECISION
#If perfectpet < 1:
#We're sorry. None of our available pets meet your prerequisites.
#Please return next week and try again. 
#There will always be AWESOME dogs looking for STABLE forever homes. Exit game.
#elif perfect == 1:
#Congratulations. You found your perfect (pretend) shelter pet!
#else:
#Surprise! You found multiple (pretend) pets that match your criteria.
#PHASE FOUR: COUNTDOWN TIMER AND PROGRAM ENDS
#COUNTING DOWN TO A REAL RESCUE 
#REQUIREMENT: Calculate + display data based on an external factor (like a count down)
#You've come so far in your search for the perfect shelter pet.
#Let's create a Countdown Timer to help you manage preparations in real life. 
#Assess your personal situation (money, time, living space, etc.)
#Create list of pet prerequisites
#Visit local shelter and assess available pets
#Find a match? Fill out adoption paperwork
#No match? Come back each weekend for a month
#Wait 7-10 days for adoption application to be reviewed and decided upon
#Receive adoption clearance
#Buy supplies 
# Pet-proof your indoor and outdoor living space
#END GOAL: Visit shelter and pick up your pet
#Thank you for taking the time to explore successfully adopting a shelter pet. 
#Bonus: Add a Turtle graphics drawing of a dog with the words Rescue Foster Adopt