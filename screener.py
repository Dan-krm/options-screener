from yahoo_fin import options  # https://github.com/atreadw1492/yahoo_fin
import pandas as pd


def screen():
    underlying = str(input("Enter the ticker of the options underlying asset: "))
    print("Possible Expirations: ", options.get_expiration_dates(underlying))
    expiration = str(input("Enter the expiration date that you're interested in: "))
    print("*** Checking if the expiration date is valid ***")
    # Error checking that a correct expiration date has been selected
    for _ in options.get_expiration_dates(underlying):
        if expiration not in options.get_expiration_dates(underlying):
            print("\nInvalid Expiration Date! Please select one of these expiration dates:")
            print(options.get_expiration_dates(underlying), "\n")
            expiration = str(input("Enter the expiration date you're interested in with this format ex. December 23, 2021: "))
    print("*** Expiration is Valid! ***")
    option_type = str(input("Enter the option type, either a Call or Put: "))
    strike = float(input("Enter the maximum amount that you would pay for the strike price: "))
    # open_interest = int(input("Enter the minimum amount of open interest you'd like to see: "))
    pd.set_option('display.max_columns', None)  # show all columns of the options chain
    if option_type == "Put":
        chain = options.get_puts(underlying, expiration)
        print(chain[chain['Strike'] < strike])
        # print(chain[chain['Open Interest'] > open_interest])
    elif option_type == "Call":
        chain = options.get_calls(underlying, expiration)
        print(chain[chain['Strike'] < strike])
        # print(chain[chain['Open Interest'] > open_interest])
    else:
        print("You inputted an invalid option type, please try again and type either Call or Put")
