import random
class handcricket:
    def balling():
        s1=0
        while(1):
            x1=random.randint(1,6)
            y1=int(input("enter value between 1 to 6 for balling:"))
            print("upto this computer score is:",s1)
            m=input("if already lose press any key else c to continue:").lower()
            if m=='c':
                if x1==y1:
                    print("computer is out")
                    print("computer score is",s1)
                    return s1
                    break
                else:
                    s1=s1+y1
            else:
                return s1
                break        
    def batting():
        s=0
        print("welcome to handcricket game")
        while(1):
            x=random.randint(1,6)
            y=int(input("enter value between 1 to 6 for batting:"))
            if x==y:
                print("you are out")
                print("your score is: ",s)
                return s
                break
            else:
                s=s+y
    def batting1():
        s=0
        print("welcome to handcricket game")
        while(1):
            x=random.randint(1,6)
            y=int(input("enter value between 1 to 6 for balling:"))
            if x==y:
                print("computer is out")
                print("computer score is: ",s)
                return s
                break
            else:
                s=s+y
    def balling1():
        s1=0
        while(1):
            x1=random.randint(1,6)
            y1=int(input("enter value between 1 to 6 for batting:"))
            print("upto this your score is:",s1)
            m=input("if already win press any key else c to continue:").lower()
            if m=='c':
                if x1==y1:
                    print("you are out")
                    print("your score is",s1)
                    return s1
                    break
                else:
                    s1=s1+y1
            else:
                return s1
                break 
while(1):
    a=random.randint(0,1)
    print("If you won the toss then you will get batting fast otherwise computer will batting first")
    b=int(input("enter 1 for head and 0 for tail:"))
    if a==b:
        print("you won the toss")
        z=handcricket.batting()
        z1=handcricket.balling()
        if z>z1:
            print("you win the match ",z-z1," runs")
        elif z==z1:
            print("match draw")
        else:
            print("you lose the match ",z1-z,"runs")

    else:
        print("you lose the toss")
        z=handcricket.batting1()
        z1=handcricket.balling1()
        if z>z1:
            print("you loss the match ",z-z1," runs")
        elif z==z1:
            print("match draw")
        else:
            print("you win the match ",z1-z,"runs")        
