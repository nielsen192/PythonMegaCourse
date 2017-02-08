def c_to_f():
    temp_choice = int(input("Please enter degrees in Celsius: "))
    converter = (temp_choice * 1.8) + 32.00
    if converter < -273.15:
        print("Since -273.15 is the lowest possible temp of all matter, you cannot choose anything lower than that.")
    else:
        print(converter)

c_to_f()
