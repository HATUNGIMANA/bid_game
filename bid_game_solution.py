import os
print("\nWelcome biders! Let's get started with the first to auction")
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def auction():
    bids_made = {}
    bids_list = []
    while True:
        name = input("What is your name ")
        print(f"Hi {name}, Please enter your bid")
        b = int(input())
        bids_list.append(b)
        bids_made[name] = b

            
        cdtn = input("\nAre there any other biders? (Type Yes or No) ").lower()

        while cdtn != "no":

            if cdtn != "yes":
                print("Invalid input, make sure you type Yes or No")
                break
                break
              
            elif cdtn == "yes":
                clear_console()
                print("\nAlright! Let's get the information of the next bider. Please Enter your information below: \n")
                break
                
        else:
                wn = max(bids_list)
                for item in bids_made:
                    if bids_made[item] == wn:
                        print(f"""The winner is {item} with a bid of ${wn}
Thank you!""")
                        break
                break
           
auction()
