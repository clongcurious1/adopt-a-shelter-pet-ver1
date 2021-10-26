**ADOPT A SHELTER PET – DOG – VER. 1**

**PROJECT-AT-A-GLANCE**
This Python program walks a user through the process of adopting a shelter pet. 

First, information is gathered about the user (age, income, available leisure time, indoor/outdoor living space, etc.) which establishes a set of prerequisites for a perfect pet match. 

Next, the user is presented with a data visualization illustrating reasons why animals “arrive” at shelters – including owner economic instability, anti-social animal behaviors, divorce, etc.

The user’s input responses from the initial Q&A section are then compared against values in a dictionary of 100 potential shelter pets available for adoption. The result of this “pet match” are displayed.

Finally, a Turtle drawing of a dog is displayed to the user with the reminder to “Save Lives: Rescue, Adopt, Foster.”

This program was created as a capstone project for an introductory Python class taken through Code Louisville in Fall 2021. 

In addition to meeting a set of specifications to pass the class, this project also helped me explore adopting a new shelter pet in my own life. 

I had the good fortune to adopt an AMAZING shelter dog 11 years ago. Through no fault of her own, she had been returned to shelters three times – due to negligent owners and abuse - in her life before I met her at a local animal adopted event. My furry companion passed away in the Spring. 

This project was created in her honor with the goal of helping educate prospective pet owners and facilitate healthy, happy, long-term pet/owner relationships.

**PACKAGES TO INSTALL**
**Matplotlib** is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
Documentation: 
https://pypi.org/project/matplotlib/
https://matplotlib.org/stable/users/installing.html 

Terminal command for Windows 10: 
Python -m pip install -U pip
Python -m pip install -U matplotlib
You will see messaging in the terminal regarding download and installation of tools including pillow, numpy, and matplotlib. WAIT for message stating install was successfully completed. 


**SECTION 1: Educate User & Gather User Information**

**Summary** – This section introduces the flow of the user experience through four sections of the program. The user can be FORCED to exit the program due to specific responses to the first three questions (**see special instructions below**). If the user successfully passes through the elimination sequence, the user’s response to the following six questions creates a list of prerequisites that are used in Section 3: Pet Match later in the program. 

**Method** – Chatbot
Input is collected via a questionnaire. Text (string) answers are provided via type hints and validated. These answers are also converted to all lower case.
**Disclaimer: ** An attempt has been made to validate that the user enters integers in the “leisure hours” section, but this is not foolproof. It works for validation of integers…but the program may break if a user types the <em>name</em> of a number as a string. 

**Special Instructions** – There are (3) DEAL BREAKER questions grouped as an Elimination Round at the start of this section. 
Users will be forced to exit the program if they are too young or too old; unable to meet the financial commitment of adopting a pet; or have fewer than 3 hours of leisure time available to care for, train, and bond with a pet. 

**To move successfully through the Elimination round, please follow these instructions:**
**Age** – enter an age between 16 and 66
**Financial Commitment** – answer YES
**Leisure Time** - enter “1” for each time allotment

**Code Louisville Project Requirement(s) Met in this Section:**  
- Build a conversion tool (calculator) that converts user input to another type and displays it. My project converts Human Years to Dog Years. This simple calculation is displayed and shown later in the program to help the user select the preferred Life Stage (puppy, adolescent, adult, senior) of a shelter pet.
- Create a dictionary or list, populate it with several values, retrieve at least one value and use it in your program. In my program, user input creates values in a User list. That list will later be converted to a dictionary in Section 3: Pet Match.







 
