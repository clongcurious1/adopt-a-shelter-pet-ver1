#Include PIP INSTALL info at beginning of README
#pip install emoji --upgrade

#Imports 
import math
import time

#Variables
hoursperday = 24

#Functions

#Other necessary stuff

#PHASE ONE User Prerequisites
#Introduce project to the User
print('***ADOPT A SHELTER PET***')
print("\U0001F43E", "\U0001F43E", "\U0001F43E")#pawprints
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
print("\nAfter the Q&A section,")
time.sleep(2)
print("we'll take a quick look")
time.sleep(2)
print('at research regarding shelter pets')
time.sleep(2)
print('in the United States.')
time.sleep(2)
print("'\nWe'll also look at") 
time.sleep(2)
print('what people are saying')
time.sleep(2)
print('about shelter pets on Twitter.\n')
time.sleep(2)
print('\U0001F496', '\U0001F496', '\U0001F496')
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
print("\U0001F44b")
print('Hello ' + firstname + '.')
print("It's nice to meet you.")
time.sleep(2)
print('\n***QUESTIONS AND ANSWERS***')
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
gym = input('Hours spent at the gym daily: ')
time.sleep(2)
children = input('Hours spent caring for children or other adults daily: ')
time.sleep(2)
community = input('Hours spent volunteering, coaching, or at church daily: ')
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
   print("Excellent! You're one step closer to sucessfully adopting a shelter pet.")
time.sleep(2)
#REQUIREMENT...(script above) use 3+ methods with returned value used again in the code
#EXPERIENCED PET OWNER 
print('\n***PREVIOUS PET OWNERSHIP EXPERIENCE***')
time.sleep(2)
print('\nHave you been the primary caregiver for a dog before?') 
time.sleep(2)
experience = input('Type y for YES or n for NO: ') 
time.sleep(2)
#Corresponds to pet dictionary: Special Needs
if experience == 'y':
    print('\nWould you adopt a dog with Special Needs?')
    time.sleep(2)
    specialneeds = input('Type y for YES or n for NO:')
else:
    print('\nWe recommend that NOVICE pet owners adopt a SENIOR dog.')
    time.sleep(2)
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
space = input('\nType a for Apt.Condo, s for Small Home, or l for House.Land: ')
time.sleep(2)
if space == 'a':
    print('\nA SMALL dog may be most comfortable in an apartment or condominium.')
elif space == 's':
    print ('\nA MEDIUM dog may be most comfortable in a modest home.')
else:
    print('\nYour living space will accomodate a LARGE dog.')
time.sleep(2)
print('\nREALITY CHECK: What size dog is best for you?')
time.sleep(2)
bestsize = input('\nType s for Small, m for Medium, or l for Large: ')
time.sleep(2)
#YOUR ENERGY LEVEL
#owner_energy: Low Moderate High
#Corresponds to pet_energy pet dictionary value: Low Moderate High
print('\n***YOUR ENERGY LEVEL***')
time.sleep(2)
print('\nHow would you describe your average energy level?')
time.sleep(2)
print('Are you sedentary, moderately active, or high energy?')
time.sleep(2) 
owner_energy = input('\nType s for sedentary, m for moderate, or h for high energy: ')
time.sleep(2)
print('\nOnly TWO more questions!')
time.sleep(2)
# smiling face with halo
print("\U0001F607")
print('PATIENCE and FOLLOW-THROUGH are important traits in a pet owner.')
time.sleep(2)
#SOCIAL ACTIVITY
#Solo Pursuits: 1 dog HH, Small Groups: Reliably Social, Comfortable in Crowds: Never Met a Stranger
print('\n***SOCIAL SETTING***')
time.sleep(2)
print('\nYour dog will look to you as Pack Leader for his/her social cues.')
time.sleep(2)
print('If you are anxious or relaxed, the dog will mirror your energy.')
time.sleep(2)
print('\nWhat type of social setting works best for you?') 
time.sleep(2)
print('Options: Solo Pursuits, Small Groups, or Comfortable in Crowds\n') 
time.sleep(2)
owner_social = input('Type sp for Solo Pursuits, sg for Small Groups, or cc for Comfortable in Crowds: ')
time.sleep(2)
#DEALBREAKER! Male or Female pet
#used as deciding factor if more than one matching pet remains at end of program
print('\n***PET GENDER***')
time.sleep(2)
print('\nDoes it matter to you if your dog is male or female?')
time.sleep(2)
gender_pref = input('Type m for Male, f for Female, or n for Neutral: ')
time.sleep(2)
print('\n***PHASE ONE COMPLETED***')
print('\nCongratulations! You completed the Prerequisites section.')
time.sleep(2)
# beaming face with smiling eyes
print("\U0001F601")
print("You're one step closer to sucessfully adopting a shelter pet.\n")

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
#You appear to be a level-headed human who can delay gratification!
#You patiently examinded your lifestyle and your resources.
#You also took the time to review data about shelter pets in the USA.
#SHELTER VISIT 
#In this exercise, you will evauluate available pets, 
#comparing their attributes 
#against your adoption prerequisites. 
#On the day you visit our imaginary shelter
#there are 10 pets available for adoption.
#Let's meet the pets assembled in the Green Room. 
#MEET THE PETS
#REQUIREMENT: create DICTIONARY, several values, retrieve at least 1 value & use it
#Today's DOGS available for adoption are:
# Print dictionary contents as Pet Name, Special Needs, Size, Life Stage, Social, Gender
#PET MATCH
#perfectpet = [start with FULL set]
#LOOP: Iterate over values in Owner Dictionary
#Compare against value in same indice position in Pet Dictionary
#In each loop, additional dogs will be deleted
#DECISION
#If perfectpet < 1:
#We're sorry. None of our available pets meet your prerequisites.
#Please return next week and try again. 
#There will always be AWESOME dogs looking for STABLE forever homes. Exit game.
#elif perfect == 1:
#Congratulations. You found your perfect shelter pet!
#else:
#Surprise! You found multiple pets that match your criteria.

#PHASE FOUR: COUNTDOWN TIMER AND PROGRAM ENDS
#COUNTING DOWN TO A REAL RESCUE 
#REQUIREMENT: Calculate + display data based on an external factor (like a count down)
#How are you feeling? 
#Ready to adopt a shelter pet in real life! 
#Use our Countdown Timer to get ready for your BIG DAY.
#Assess your personal situation (money, time, living space, etc.)
#Create YOUR list of pet prerequisites
#Visit local shelter and assess available pets
#Find a match? Fill out adoption paperwork
#No match? Come back next weekend 
#Wait 7-10 days for review and approval of adoption application 
#Receive adoption decision
#Buy supplies 
#Pet-proof your indoor and outdoor living space
#END GOAL: TODAY'S THE DAY! Bring home your new 4-Legged Friend
#Thank you for taking the time to explore successfully adopting a shelter pet. 
#Bonus: Add a Turtle graphics drawing of a dog with the words Rescue Foster Adopt