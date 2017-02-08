# Lists - remember square brackets for lists since they don't have a separate array(tuple)
li=['Today','Tomorrow',3]
for item in li:
    print(item)

li.append(43)
li.insert(2,'Hello')
li.pop()
li.remove(3)

def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars

functions = [currency_converter(100,1000),currency_converter(100,2000)]
print(functions)

# Tuple - immutable lists
t=(1,2,3)
type(t)
t.remove(2)
