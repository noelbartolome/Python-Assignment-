import bdo
import landbank
bal = 0
balacc = "bdo"
reply = "y"
while reply == "Y" or reply == "y":
    hold = bdo.Bdo(bal , balacc)
    holder = landbank.Landbank(bal, balacc)
    def main():
        print "\t[1]Bank Transaction"
        print "\t[2]Change Bank Name"
        print "\t[3]Exit"
    def main1():
        rep = "y"
        print '\n\t' , hold.vname() , "Account" , '\n'
        while rep == "y" or rep == "Y":
            print "\t[1]Bank Name"
            print "\t[2]Balance"
            print "\t[3]Withdraw"
            print "\t[4]Deposit"
            print "\t[5]Exit"
            cho = raw_input("Enter Choice:")
            if cho == '1':
                print "Bank name:" , hold.vname()
            elif cho == '2':
                print "Bank Balance:" , hold.getbalance()
            elif cho == '3':
                wit()
            elif cho == '4':
                dep()
            elif cho == '5':
                break
            else:
                print "Wrong Choice please enter again"
    def dep():
        cash = int(input("How much would you like to Deposit?:"))
        hold.deposit(cash)
        print "Deposited"
    def wit():
        mons = float(input("How much would you like to Withdraw?:"))
        hold.withdraw(mons)
    def enterb():
        balacc = raw_input("Enter Bank:")
        if balacc == hold.vname():
            main1()
        elif balacc == holder.vname():
            main1()
        else:
            print "No account found"
    def changeinfo():
        balacc = raw_input("Enter Old Bank Name:")
        acconame = raw_input("Enter New Bank Name:")
        hold.changeinfo(acconame)
        print "Info has been Change"
        print hold.changeinfo(acconame)
    main()
    choice = raw_input("Enter Choice:")
    if choice == "1":
        enterb()
    elif choice == "2":
        changeinfo()
    elif choice == "3":
        break
    else:
        print "Wrong Choice please enter again"
