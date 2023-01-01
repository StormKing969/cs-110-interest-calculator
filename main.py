# Checks if the input can be converted to a float i.e. is a numeric input
def is_float(user_entry):
    try:
        float(user_entry)
        return True
    except ValueError:
        return False


# Checks if the input in greater than zero
def is_greater(user_entry):
    try:
        if float(user_entry) > 0:
            return True
    except ValueError:
        return False


# Checks if the user input matches the required criteria
def investmentEntry():
    UserPV = input("What's your investment? ")
    # Checks if the input contains only numbers
    while not is_float(UserPV) and not UserPV.isnumeric():
        print("Please enter a numeric value")
        UserPV = input("What's your investment? ")
        # Checks if the input in greater than zero
        while not is_greater(UserPV):
            print("Please enter a numeric value that is greater than zero")
            UserPV = input("What's your investment? ")
    return float(UserPV)


# Checks if the user input matches the required criteria
def ratesEntry():
    UserR = input("What's the interest rate? ")
    # Checks if the input contains only numbers
    while not is_float(UserR) and not UserR.isnumeric():
        print("Please enter a numeric value")
        UserR = input("What's the interest rate? ")
        # Checks if the input in greater than zero
        while not is_greater(UserR):
            print("Please enter a numeric value that is greater than zero")
            UserR = input("What's the interest rate? ")
    return float(UserR)


# Checks if the user input matches the required criteria
def durationEntry():
    Time = input("How long the money is deposited for? ")
    # Checks if the input contains only numbers
    while not is_float(Time) and not Time.isnumeric():
        print("Please enter a numeric value")
        Time = input("How long the money is deposited for? ")
        # Checks if the input in greater than zero
        while not is_greater(Time):
            print("Please enter a numeric value that is greater than zero")
            Time = input("How long the money is deposited for? ")
    return int(Time)


# Checks if the user input matches the required criteria
def goalEntry():
    Goal = input("What's your goal amount? ")
    # Checks if the input contains only numbers
    while not is_float(Goal) and not Goal.isnumeric():
        print("Please enter a numeric value")
        Goal = input("What's your goal amount? ")
        # Checks if the input in a positive integer
        while not Goal < 0:
            print("Please enter a positive numeric value")
            Goal = input("How long the money is deposited for? ")
    return float(Goal)


# Capture user investment input
UserPV = investmentEntry()
# Checks if the user input matches the required criteria
while UserPV < 0:
    print("Please enter a numeric value that is greater than zero")
    UserPV = investmentEntry()

# Capture user interest rate input
UserR = ratesEntry()
# Checks if the user input matches the required criteria
while UserR < 0:
    print("Please enter a numeric value that is greater than zero")
    UserR = ratesEntry()

# Capture user duration input
Time = durationEntry()
# Checks if the user input matches the required criteria
while Time < 0:
    print("Please enter a numeric value that is greater than zero")
    Time = durationEntry()

# Capture user goal input
Goal = goalEntry()
# Checks if the user input matches the required criteria
while Goal < 0:
    print("Please enter a positive numeric value")
    Goal = goalEntry()

# Calculate the monthly rates
monthly_interest_rate = (UserR / 100) / 12

# Counter to track of the while loop iterations
num_iteration = 1
# Makes a copy of the original investment
copy_userPV = UserPV


# Loops until the number of iterations reaches the user duration
while num_iteration <= Time:
    monthly_interest_amount = UserPV * monthly_interest_rate
    UserPV = UserPV + monthly_interest_amount
    print(f"Month: {num_iteration} Account Balance is: ${UserPV : ,.2f}")
    num_iteration += 1

num_months = 0

# Loops until user investment reach the user goal
while copy_userPV <= Goal:
    monthly_interest_amount = copy_userPV * monthly_interest_rate
    copy_userPV = copy_userPV + monthly_interest_amount
    # Rounds to 2 decimal places
    round(copy_userPV, 2)
    num_months += 1

print(f"It will take: {num_months} months to reach the goal of ${Goal : ,.2f}")
quit()
