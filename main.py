import time
class Axis_Bank:

    def __init__(self):
        self.dic=[{"name":"Ankush","balance":10000,"acc":123456},
                  {"name":"Rohit","balance":20000,"acc":789012}]

    def get_account(self,acc_):
        for user in self.dic:
            if user["acc"]==acc_:
                return user

    def main(self):
        print("-" * 80)
        print("Welcome to Axis Bank:\n")
        print("1: 'For create an account'")
        print("2: 'For check your bank details'")
        print("3: 'For Debit/Withdrawl money'")
        print("4: 'For Credit/Deposit money in your account'")
        print("5: 'For Feedback'")
        print("-" * 80)
        data=input("Enter which operation you want to perform:")

        if data=="1":
            try:
                def update_dict(**kwargs):
                    self.dic.append(kwargs)
                input_=int(input("Enter your account number:"))
                input_name=input("Enter your name:")
                balance_=int(input("Enter your balance:"))
                
                if input_ not in [user["acc"] for user in self.dic]:
                    update_dict(name=input_name,balance=balance_,acc=input_)
                    print("Account created successfully:")
                    for user in self.dic:
                        if user["acc"]==input_:    
                            print(f"{user['name']} | Balance: {user['balance']} | Account Number: {user['acc']}")
                else:
                    print("This account already exists:")
            except ValueError as e:
                print(f"Error: {e}")

        elif data in ["2","3","4"]:
            try: 
                input_=int(input("Enter your acc no. to login:"))
                current_user=self.get_account(input_)

                if not current_user:
                    print("Account not found. Please check your account number.")
                    return
                count=3
                while count>0:
                    passw=input(f"Please enter your (Name) for account {input_}:")
                    if passw==current_user["name"]:
                        break
                    else:
                        count-=1
                        print("Incorrect Password:")
                        
                    print(f"Attempts left: {count}")
                    if count==0:
                        print("Now try after 24 hours")
                        return

                if data=="2":
                    print("Fetching your info please wait...\n")
                    time.sleep(1)
                    print("-" * 80)
                    print(f"Account Holder: {current_user['name']} | Balance: {current_user['balance']} | Account Number: {current_user['acc']}")
                    print("-" * 80)

                elif data=="3":
                    amount=int(input("Enter how much amount you want to debit:"))
                    if amount>0 and amount<=current_user["balance"]:
                        current_user["balance"]-=amount
                        time.sleep(2)
                        print("-" * 80)
                        print(f"Money debit successfully:,New Balance={current_user['balance']}")
                        print("-" * 80)
                    elif amount<0:
                        print("you cannot debit less then 0: \n")
                    else:
                        print("Insufficient balance:\n")

                elif data=="4":
                    amount_=int(input("Enter how much amount you want to credit in your account:"))
                    print("Please wait:")
                    if amount_>0:
                        current_user["balance"]+=amount_
                        time.sleep(2)
                        print("-" * 80)
                        print(f"Money credit successfully:,New Balance={current_user['balance']}")
                        print("-" * 80)
                    else:
                        print("Cannot add less then Zero: \n")
            except ValueError as e:
                print(f"Error: {e}\n")
            
        elif data=="5":
            try:
                new=input("How much you are satisfied with our services\na: 'Very Satisfied'\nb: 'Satisfied'\nc: 'Not Satisfied'")
                if new=="a" or new=="b" or new=="c":
                    print("Thank you for your feedback😊:\n")
            except Exception as e:
                print(f"Error: {e}\n")
        else:
            print("Select options from above 5: \n")

c=Axis_Bank()

while True:
    one=input("press any key to continue or press 'q' for quit:")

    if one=="q":
        time.sleep(2)
        print("Thanks for visiting us:\n")
        break
    c.main()