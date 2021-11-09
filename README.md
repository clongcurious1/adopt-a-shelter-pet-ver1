**ADOPT A SHELTER PET – DOG – VER. 1**

**PROJECT-AT-A-GLANCE**
This Python program walks a user through the process of adopting a shelter pet. 

First, information is gathered about the user (age, income, available leisure time, indoor/outdoor living space, etc.) which establishes a set of prerequisites for a perfect pet match. 

Next, the user is presented with a data visualization illustrating reasons why animals “arrive” at shelters – including owner economic instability, anti-social animal behaviors, divorce, etc.

The user’s input responses from the initial Q&A section are then compared against values in a dictionary of 100 potential shelter pets available for adoption. The results of this “pet match” are communicated to the user.

In the final section of the program, the user is presented with a Countdown Timer that shows time necessary to prepare to adopt a pet in real life. A Turtle Graphics drawing of a dog is displayed to the user with the reminder to “Save Lives: Rescue, Adopt, Foster.”

This program was created as a capstone project (on Windows10 OS) for an introductory Python class taken through Code Louisville in Fall 2021. 

In addition to meeting a set of specifications to pass the class, this project also helped me explore adopting a new shelter pet. 

I had the good fortune to adopt an AMAZING shelter dog 11 years ago. Through no fault of her own, she landed at shelters three times in her life – due to negligent owners and abuse - as a puppy, a pregnant adolescent, and a neglected adult - before I met her as a senior dog at a local shelter pet adoption event. 

This project was created in her honor to help educate prospective pet owners and facilitate mutually beneficial, long-term pet/owner relationships.

**PLEASE READ ENTIRE README BEFORE ATTEMPTING TO CLONE THIS PROJECT**

Please take a few minutes to skim this ReadMe so that you understand the different sections in the project, notice where Special Instructions come into play, and understand packages you must download to run the program. 

**CLONING A REPOSITORY FROM GITHUB TO YOUR LOCAL MACHINE**

If you are not familiar with this process, please follow the steps in this article: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository 

**PACKAGES TO INSTALL**

Once you have successfully downloaded the project to your local machine, you will also need to install these packages before attempting the run this project. 

**Matplotlib** is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
Documentation: 
https://pypi.org/project/matplotlib/
https://matplotlib.org/stable/users/installing.html 

Terminal command for Windows 10: 
Python -m pip install -U pip
Python -m pip install -U matplotlib

Note: While the commands above worked for me, a user who helped test this program said a simple “pip install matplotlib” worked for him. 

This installation takes A FEW MINUTES. You will see messaging in the terminal regarding download and installation of tools including pillow, numpy, and matplotlib. WAIT for message stating install was successfully completed. 
 
**Pandas** is a fast, powerful, flexible and easy to use open-source data analysis and manipulation tool, built on top of the Python programming language.
Terminal command to install: 
pip install pandas
Documentation: https://pandas.pydata.org/docs/getting_started/install.html 

**MAIN.PY is the file you need to run**

There are a handful of files in this project folder. In the terminal, type **python main.py** to run the correct file. 

Sidebar: Because of the amount of text that runs in the terminal, I tried to add visual interest to the program using emojis. Sadly, they only seem to appear for testers who are using Windows with VS Code as their editor. Users using other editors may only see square tile(s) with a question mark(s) where emojis were supposed to appear. This does not affect how the program runs and will be addressed in a later version. 

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
- Create a dictionary or list, populate it with several values, retrieve at least one value and use it in your program. In my program, user input creates 6 values that are combined and displayed in a user list at the end of Section 1.

**SECTION 2: Read, Write, and Visualize Data**

**Summary** – The purpose of this program is to educate potential dog owners regarding the full scope of responsibilities associated with adopting a shelter pet. I wanted to share information re: why animals wind up at shelters. This visualization shows that the top two reasons are the owner’s economic instability, often resulting in (dumped) stray pets.

**Method** – I selected an open data set from Kaggle.com that included intake and physical attribute data on shelter animals (dogs, cats, horses, snakes, hamsters...) in Indianapolis. I removed animals other than dogs from the file, then sorted remaining dogs by intake reason. I created a simple csv file with only those two columns: # of Dogs, Intake Reason. Data is visualized two ways: Pandas dataframe, bar chart. 

Additional data from the larger Kaggle file will be read/written into the program separately to create a PET dictionary in Section III.

**Special Instructions** – NONE.

**Code Louisville Project Requirement(s) Met in this Section** 
- Read data from an external file (text, csv, JSON, etc.) and use that data in your application
- Visualize data in a graph, chart, or other visual representation of data. I visualize the data from the .csv file as a Pandas data frame and as a horizontal bar chart.

**SECTION 3: Perfect Pet Match Exercise**

**Summary** – This section matches the pet adoption prerequisite values input by the user in Section 1 against the attributes of 100 pets stored as a list of dictionaries. 

**Method** – A csv file with 100 “dog” rows and columns of attributes is passed as a file object to DictReader(), converted to a list of dictionaries, and then the list is printed. The comparison of user prerequisites against dog attributes happens one key, one value at a time. The matching pet dictionaries and number of matching pets are printed to the screen. At the end, the user may – or may not – have any pet matches. It varies each time the program is run based on user input. 

**Special Instructions** – None. 

**Code Louisville Project Requirement(s) Met in this Section** 
- Create and call at least 3 functions or methods, at least one of which must return a value used elsewhere in your code. The build_user function is defined at the beginning of the program. This function returns an “owner” dictionary. The function is called in Section III and the return value is printed.

**SECTION 4: Countdown to Adopt a Shelter Pet in Real Life**

**Summary** – In this section, user is told that the average amount of time to process a shelter adoption form and reach a decision is approximately 14 days. A countdown timer is printed to the terminal, starting with today’s date, and counting forward over the next 14 days, one day at a time. For each new date, a new activity is recommended to prepare to bring home a shelter pet. 

**Method** – Import datetime module. After getting current date using datetime.datetime.now(), the countdown by day from the current date is accomplished using datetime.timedelta(days=x).

**Special Instructions** – None.

**Code Louisville Project Requirement(s) Met in this Section** 
Calculate and display data based on an external factor (example: get the current date and display how many days remaining until some event). I got the current date and then planned forward, calculating and printing multiple dates, up to 14 days out from the current date.  

**IDEAS for FUTURE VERSIONS of this Program**

**Version 2** - In Section 2 (Data and Visualization), add an additional section. The new section would involve using the Twitter API and possibly Tweepy or Twython to aggregate a set of tweets including keywords (adopt a dog, adopted a dog, adopted a shelter dog, rescue dog…). Sentiment analysis would be performed on the group of Tweets so that only the positive statements were retained. Those statements would then be broken down into single words and the recurrence of the words would be calculated. Ultimately, the most frequently recurring 150 words would be displayed in a Word Cloud in the shape of a dog (using a mask to control the shape). 

**Version 3** - Code a GUI for the Countdown Calendar in Section 4.

**Version 4** - Create a web app using Django. 

**Version 5** - Expand the program, and all options within, allowing user to specify selection of a dog OR a cat. 




 
