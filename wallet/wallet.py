#[ ] TODO's
#[ ] Must have a user.
#[ ] Create a function that will route through a main menu.
#[ ] Maintain hold a balance that can be deposited/withdrawn and then updated.
#[ ] Need to be able to check the current balance. 
#[ ] Be able to exit the program.

#class Wallet:
#    def __init__(self, user, ballance):
#        self.user=user
#        self.ballance=ballance
#        self.getuser()
#        self.menu()
#
#    def getuser(self):
#        self.user=input("Enter user name: ")
#        return self.user
#
#    def menu(self):
#        print(f"User:{self.user}")
#        print("[1] Deposit")
#        print("[2] Withdraw")
#        print("[3] Check Balance")
#        print("[4] EXIT")
#        print("")
#        self.menuselect()
#
#    def menuselect(self):
#        selection=float(input("please enter menu option: "))
#        if selection == 1:
#            self.deposit(self.ballance)
#        if selection == 2:
#            self.withdrawal(self.ballance)
#        if selection == 3:
#            self.getballance(self.ballance)
#        if selection == 4:
#            print("ThankYou")
#            exit 
#        else:
#            self.menu()
#
#    def getballance(self,ballance):
#        print(f"Ballance:{ballance}")
#        self.menu
#
#    def deposit(self,ballance):
#        depammount = float(input("Deposit amount: "))
#        self.ballance= float(ballance) + depammount
#        self.getballance(self.ballance)
#        self.menu
#
#    def withdrawal(self,ballance):
#        depammount = float(input("Withdrawal amount: "))
#        self.ballance= float(ballance) - depammount
#        self.getballance(self.ballance)
#        self.menu

#w=Wallet("blank", 0)
class Wallet:
    def __init__(self, user, ballance):
        self.user=user
        self.ballance=ballance
        self.getuser()
        self.menu()
    def getuser(self):
        self.user=input("Enter user name: ")
        return self.user
    def menu(self):
        print(f"User:{self.user}")
        print("[1] Deposit")
        print("[2] Withdraw")
        print("[3] Check Balance")
        print("[4] EXIT")
        print("")
        self.menuselect()
    def menuselect(self,):
        selection=float(input("please enter menu option: "))
        if selection == 1:
            self.deposit(self.ballance)
        if selection == 2:
            self.withdrawal(self.ballance)
        if selection == 3:
            self.getballance(self.ballance)
        if selection == 4:
            print("ThankYou")
            exit 
        else:
            self.menu()
    def getballance(self,ballance):
        print(f"Ballance:{ballance}")
        self.menu
    def deposit(self,ballance):
        depammount = float(input("Deposit amount: "))
        self.ballance= float(ballance) + depammount
        self.getballance(self.ballance)
        self.menu
    def withdrawal(self,ballance):
        depammount = float(input("Withdrawal amount: "))
        self.ballance= float(ballance) - depammount
        self.getballance(self.ballance)
        self.menu

w=Wallet("blank", 0)
