# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

def is_float( string_number ):
#    print(f"number: {string_number}")
    if string_number.replace(".", "").isnumeric():
#        print(f"string is numberic: {string_number}")
        return True
    else:
#        print(f"string is NOT numberic: {string_number}")
        return False

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print( "\nPlease enter your savings account information")
    while True:
        balance_str     = input(f"-- Enter your savings balance: ")
        if is_float(balance_str):
            savings_balance = float(balance_str)
            break
        else:
            print("-- Please enter a number for your savings balance --")
#    print(f"---- Savings balance: ${savings_balance:,.2f}")

    while True:
        interest_str     = input(f"-- Enter the interest rate on your account (enter 5.5 for 5.5%): ")
        if is_float(interest_str):
            savings_interest = float(interest_str)
            break
        else:
            print("-- Please enter a number for the interest --")
#    print(f"---- Interest: {savings_interest:,.2f}%")

    while True:
        savings_maturity_str     = input(f"-- Enter the months of interest earned: ")
        if is_float(savings_maturity_str):
            savings_maturity = int(savings_maturity_str)
            break
        else:
            print("-- Please enter a number for the months of interest earned --")
#    print(f"---- Months: {savings_maturity}")
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nYour updated savings balance is: ${updated_savings_balance:,.2f}")
    print(f"The savings interest earned is: ${savings_interest_earned:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print( "\nPlease enter your CD account information")
    while True:
        balance_str     = input(f"-- Enter your CD balance: ")
        if is_float(balance_str):
            cd_balance = float(balance_str)
            break
        else:
            print("-- Please enter a number for your CD balance --")
#    print(f"---- cd balance: ${cd_balance:,.2f}")

    while True:
        interest_str     = input(f"-- Enter the interest rate on your account (enter 5.5 for 5.5%): ")
        if is_float(interest_str):
            cd_interest = float(interest_str)
            break
        else:
            print("-- Please enter a number for the interest --")
#    print(f"---- Interest: {cd_interest:,.2f}%")

    while True:
        cd_maturity_str     = input(f"-- Enter the months of interest earned: ")
        if is_float(cd_maturity_str):
            cd_maturity = int(cd_maturity_str)
            break
        else:
            print("-- Please enter a number for the months of interest earned --")
#    print(f"---- Months: {cd_maturity}")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nYour updated CD balance is: {updated_cd_balance}")
    print(f"The CD interest earned is: {cd_interest_earned}")

if __name__ == "__main__":
    # Call the main function.
    main()