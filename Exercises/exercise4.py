temperatures=[10,-20,-289,100]

def c_to_f(c):
    if c > -273.3:
        f=c*9/5+32
        return f
    else:
        return "That temperature doesn't make sense!"

for t in temperatures:
    print(c_to_f(t))
