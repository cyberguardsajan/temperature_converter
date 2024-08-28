
# function to convert from one unit to another

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return ((fahrenheit - 32) * 5/9) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return ((kelvin - 273.15) * 9/5) + 32






# Display options
def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")



# Taking input from user
    choice = input("Enter your choice (1-6): ")


#conditions

    if choice in ('1', '2', '3', '4', '5', '6'):
        temp = float(input("Enter the temperature: "))
        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp} Celsius is {result:.2f} Fahrenheit")
        elif choice == '2':
            result = celsius_to_kelvin(temp)
            print(f"{temp} Celsius is {result:.2f} Kelvin")
        elif choice == '3':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp} Fahrenheit is {result:.2f} Celsius")
        elif choice == '4':
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp} Fahrenheit is {result:.2f} Kelvin")
        elif choice == '5':
            result = kelvin_to_celsius(temp)
            print(f"{temp} Kelvin is {result:.2f} Celsius")
        elif choice == '6':
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp} Kelvin is {result:.2f} Fahrenheit")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")





# main part of program 
if __name__ == "__main__":
    main()
