import time
class Axis_Bank:

    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    #This function for select operation to do
    def main(self):
        print("-" * 80)
        print("1: 'For check your bank details'")
        print("2: 'For Debit/Withdrawl money'")
        print("3: 'For Credit/Deposit money in your account'")
        print("4: 'For Feedback'")
        print("-" * 80)
        data=input("Enter which operation you want to perform:\n")

        #This loop is for first operation
        if data=="1":
            count=3
            while count>0:
                passw=input("Please enter your Password :")
                if passw=="Ankush":
                    print("Fetching you info please wait:\n")
                    time.sleep(2)
                    print("-" * 80)
                    print(f"The name of Account Holder is {self.name} and the balance is {self.balance}:")
                    print("-" * 80)
                    break
                else:
                    count-=1
                    print("Incorrect Password:")
                    
                print(f"Attempts left: {count}")
                if count==0:
                    print("Now try after 24 hours")
                    break

        #this loop is for second option    
        elif data=="2":
            try:
                count=3
                while count>0:
                    passw=input("Please enter your Password :")
                    if passw=="Ankush":
                        amount=int(input("Enter how much amount you want to debit:"))
                        if amount>0 and amount<=self.balance:
                            self.balance -= amount
                            time.sleep(2)
                            print("-" * 80)
                            print("Money debit successfully:")
                            print("-" * 80)
                        elif amount<0:
                            print("you cannot debit less then 0: \n")
                        else:
                            print("Insufficient balance:\n")
                        break
                    else:
                        count-=1
                        print("Incorrect Password:\n")
                    attem=print(f"Attempts left: {count}")
                    if count==0:
                        print("Now try after 24 hours")
                        break
            except ValueError:
                print("Please enter a valid number: \n")
                
        #This loop is for third option
        elif data=="3":
            try:
                count=3
                while count>0:
                    passw=input("Please enter your Password :")
                    if passw=="Ankush":
                        amount_=int(input("Enter how much amount you want to credit in your account:"))
                        print("Please wait:\n")
                        if amount_>0:
                            self.balance+=amount_
                            time.sleep(2)
                            print("-" * 80)
                            print("Money credit successfully:\n")
                            print("-" * 80)
                        else:
                            print("Cannot add less then Zero: \n")
                        break

                    else:
                        count-=1
                        print("Incorrect Password:\n")
                    attem=print(f"Attempts left: {count}")
                    
                    if count==0:
                        print("Now try after 24 hours")
                        break
            except ValueError:
                print("Please enter a valid number: \n")  

        elif data=="4":
            try:
                new=input("How much you are satisfied with our services\na: 'Very Satisfied'\nb: 'Satisfied'\nc: 'Not Satisfied'")
                if new=="a" or new=="b" or new=="c":
                    print("Thank you for your feedback😊:\n")
            except Exception as e:
                print(f"Error: {e}\n")
        else:
            print("Select options from above Three: \n")

c=Axis_Bank("Ankush")

while True:
    one=input("press any key to continue or press 'q' for quit:")

    if one=="q":
        time.sleep(2)
        print("Thanks for visiting us:\n")
        break
    c.main()