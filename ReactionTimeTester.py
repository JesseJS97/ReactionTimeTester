"""
Author: Jesse Scully
Script Name: ReactionTimeTester.py
Description: This Python script is a minigame in order to find the reaction time for the
current user and display the results in a simple table format.
"""

# Import modules
import random
import time

# Introduce user to program
print ('\nHi there and weclcome to the Response Time Tester!')
print ('Shortly, you will be asked to press Enter after a random amount of seconds')
print ('Try and get as close as you can!')

# Ensure user inputs a positive integer with appropriate error statements
while True:
    try:
        rounds = int(input('\nEnter total number of rounds: '))
        if rounds >= 1:
            break
        # Throw an error if a non positive integer is inputted
        else:
            print('Invalid input, please enter a positive integer')
    # Throw an error is anything other than an integer is inputted
    except ValueError:
        print('Invalid input, please enter a positive integer')

# Implement a calculate rating function
def calculate_rating(response):
    if abs(randomnum - response) <= 0.25:
        rating = 'Excellent!'
    elif abs(randomnum - response) <= 0.5:
        rating = 'Great!'
    elif abs(randomnum - response) <= 1:
        rating = 'Good!'
    elif abs(randomnum - response) <= 2:
        rating = 'Ok!'
    else:
        rating = 'Complete Miss!'
    return rating

# Assign lists to variables
Targets = []
Responses = []
Differences = []

# Initialise reaction time tester game logic
for numround in range(1, rounds+1):
    # Generate random number for reaction time
    randomnum = random.randint(2, 8)
    Targets.append(randomnum)

    # Print rounds and game instructions
    print (f'Round {numround} of {rounds}')
    print ('Please press Enter in', randomnum, 'seconds starting...')

    # Initialise a delay and ask for user's enter input
    time.sleep(3)
    print ('Now!')
    start_time = time.time()
    input()
    end_time = time.time()

    # Calculate reaction time and store relevant results
    response = float(end_time) - float(start_time)
    abs_response = abs(response)
    print ('That was', (round(abs_response, 2)), 'seconds')
    rating = calculate_rating(abs_response)
    print (rating)
    Responses.append(response)
    difference = randomnum - response
    Differences.append(difference)

    # Empty line
    print ('')

# Display breakdown of results
def difference_earlyorlate(difference):
    if randomnum > response:
        result = 'too early!'
    elif randomnum < response:
        result = 'too late!'
    elif randomnum == response:
        result = 'spot on!'
    return result

result = difference_earlyorlate(difference)

# Provide a table showcasing user's results
print("Testing Complete! Press Enter to see a breakdown of your results.")
input()
print ("Round : Target : Response : Difference")
print ("----- : ------ : -------- : ----------")
for numround in range(rounds):
    print (numround+1, '    :   ', Targets[numround], '  :  ',
round(Responses[numround],2), '  :', round(Differences[numround],2), result)
    
# Show user if they responded too early or too late
numberoflate_counts = 0
numberofearly_counts = 0

# Calculate the number of late or early counts
for difference in Differences:
    if difference < 0:
        numberoflate_counts = +1
    elif difference > 0:
        numberofearly_counts = +1

# Determine if user was too late or early using counts
if numberoflate_counts < numberofearly_counts:
    print("You usually respond too early.")
else:
    print("You usually respond too late.")

print('Your overall rating is: ', calculate_rating(response))