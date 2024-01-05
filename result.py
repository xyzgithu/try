print("** Welcome insert marks that you obtained in each subject: **")
while True:
    ma=int(input("Math: "))
    sc=int(input("Science: "))
    ne=int(input("Nepali: "))
    so=int(input("Social: "))
    en=int(input("English: "))
    he=int(input("Health: "))
    op=int(input("OPT-math: "))
    ac=int(input("Account: "))

    total=ma+sc+ne+so+en+he+op+ac
    average=total/800
    percentage=average *100
    print("You obtained", percentage, "%")
    
    if percentage >= 90:
        print("You obtained A+")
    elif percentage >= 80:
        print("You obtained A")
    elif percentage >= 70:
        print("You obtained B+")
    elif percentage >= 60:
        print("You obtained B")
    elif percentage >= 50:
        print("You obtained C+")
    elif percentage >= 40:
        print("You obtained C")
    else:
        print("You obtained NG")
    
    exit_input=input("Press 'e' to exit and other key to continue: \n--> ")
    if exit_input.lower()=="e":
        break

