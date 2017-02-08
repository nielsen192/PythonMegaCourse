temperatures=[10,-20,-289,100]

def c_to_f(c):
    if c > -273.15:
        f=c*9/5+32
        return f

with open("temps.txt",'w+') as file:
    for temp in temperatures:
        file.write(str(c_to_f(temp)) + "\n")






## Solution 2

temperatures=[10,-20,-289,100]

def writer(temperatures):
    with open("temps.txt", 'w') as file:
        for c in temperatures:
            if c>-273.15:
                f=c*9/5+32
                file.write(str(f)+"\n")

writer(temperatures) #Here we're calling the function, otherwise no output will be generated
