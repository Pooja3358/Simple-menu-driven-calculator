a=int(input("Enter ur first num: "))
b=int(input("Enter ur second num: "))
print(f"Choose 1 for Addition \nChoose 2 for Subtraction \nChoose 3 for  Multiplication \nChoose 4 for Divison")
c=int(input("Enter ur choice "))

def add(d,e):
    return d+e

def sub(d,e):
    if d>e:
        return d-e
    else:
        return e-d
    
def multi(d,e):
    return d*e

def divide(d,e):
    if d>e:
        return d//e
    else:
        return e//d
   

if c==1:
    print(f'Your first num is {a} & second num is {b}. You choose {c} for addition so ur ans is {add(a,b)}')
elif c==2:
    print(f'Your first num is {a} & second num is {b}. You choose {c} for subtraction so ur ans is {sub(a,b)}')
elif c==3:
    print(f'Your first num is {a} & second num is {b}. You choose {c} for multiplication so ur ans is {multi(a,b)}')
else:
    print(f'Your first num is {a} & second num is {b}. You choose {c} for division so ur ans is {divide(a,b)}')             

        