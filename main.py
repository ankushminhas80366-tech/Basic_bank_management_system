import time
class Axis_Bank:

    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    #This function for select operation to do
    def main(self):
        print("1: 'For check your bank details'")
        print("2: 'For Debit/Withdrawl money'")
        print("3: 'For Credit/Deposit money in your account'")
        data=input("Enter which operation you want to perform:")

        #This loop is for first operation
        if data=="1":
            print("Fetching you info please wait:")
            time.sleep(2)
            print(f"The name of Account Holder is {self.name} and the balance is {self.balance}:")
            print("*" * 80)

        #this loop is for second option    
        elif data=="2":
            try:
                amount=int(input("Enter how much amount you want to debit:"))
                if amount>0 and amount<=self.balance:
                    self.balance -= amount
                    time.sleep(2)
                    print("Money debit successfully:")
                    print("*" * 80)
                elif amount<0:
                    print("you cannot debit less then 0: ")
                else:
                    print("Insufficient balance:")
            except ValueError:
                print("Please enter a valid number: ")
                
        #This loop is for third option
        elif data=="3":
            try:
                amount_=int(input("Enter how much amount you want to credit in your account:"))
                print("Please wait:")
                if amount_>0:
                    self.balance+=amount_
                    time.sleep(2)
                    print("Money credit successfully:")
                    print("*" * 80)
                else:
                    print("Cannot add less then Zero: ")
                
            except ValueError:
                print("Please enter a valid number: ")
                
        else:
            print("Select options from above Three: ")

c=Axis_Bank("ankush")

while True:
    one=input("press any key to continue or press 'q' for quit:")

    if one=="q":
        time.sleep(2)
        print("Thanks for visiting us:")
        break
    c.main()