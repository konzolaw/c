#IRKE KONZOLO 
#REGNO:SCT211-0081/22
#Calculator for showing years months and days of a person


from datetime import datetime 
#salutations and greetings 

name=input ("Please input your name: ")
print("Hello", name)
print("Welcome to my calculator ",name)
print("It takes the year of birth of a person and calculates their age in years, months and days respectively.")

#take users info of the year ,month and date they were born 

year_of_birth = int(input('Please Enter Year Of Birth: '))
month_of_birth=int(input('Please Enter Month Of Birth:'))
day_of_birth=int(input('Please Enter  Day Of Birth:'))

#get current date.month year day

currentYear =datetime.now().year 
Currentmonth=datetime.now().month
Currentday=datetime.now().day 
Currentdate=datetime.now()  
#calculate age based on birthday

date_of_birth = datetime(year_of_birth, month_of_birth, day_of_birth)
age = Currentdate - date_of_birth    

# Extract years and days from the age difference
years = (age).days // 365  #// is is the floor division operator

days_remaining = (age).days % 365
# Calculate months from the remaining days

months = days_remaining // 30
days = days_remaining % 30

# Show the result
print(f"Dear {name} , Your age is {years} years, {months} months, and {days} days.")

####
####
#PART TWO:TIP $ BILLS
# Get user input for total bill, percentage tip , and number of people paying the bill
summation_of_bill = float(input("Please input your total bill amount: Ksh"))
percentage_tip = int(input("Please input the percentage tip you desire to offer (10, 12, or 15): "))
NumberOfpeople = int(input("Please input the total number of people splitting the bill: "))

# Check for invalid inputs
if percentage_tip not in [10, 12, 15] or summation_of_bill <= 0 or NumberOfpeople <= 0:
    print("Invalid input. Please enter correct values.")
else:
    # Calculate the total tip amount
    tip_amount = (summation_of_bill * percentage_tip) / 100

    # Calculate total amount including tip
    total_amount = summation_of_bill + tip_amount

    # Calculate the total amount to be paid per person
    amount_per_person = total_amount / NumberOfpeople
      # Show the results  to two decimal places
    print(f"Each person should pay a total of : Ksh{amount_per_person:.2f}")



    ###
    #part3
    ##A BMI CALCULATOR
    name1=name(input("Please input your name :"))
    print("Hello",name1)
    print("Welcome to my BMI calculator!")
        #  Input height and weight from the user
height = float(input("Please input your height (in meters): "))
weight = float(input("Please input your weight (in kilograms): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
else:
    category = "Overweight"

# Show the BMI and category
print(name1,f"Your BMI is: {bmi:.2f}")
print(name1,f"you are categorized as: {category}")

##LEAP YEAR DISPLAY 
# prompts user to inpput year
year = int(input("Please input a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
