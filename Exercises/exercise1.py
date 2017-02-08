# Convert Celsius to Fahrenheit
def c_to_f():
    temp_choice = int(input("Please enter degrees in Celsius: "))
    converter = (temp_choice * 1.8) + 32.00

    print(converter)

c_to_f()
