CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius*CELSIUS_TO_FAHRENHEIT_FACTOR + 32

try: 
    temprature = int(input("Enter the temperature to convert: "))
    temprature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if temprature_unit == "C":
        converted_temprature = convert_to_fahrenheit(celsius=temprature)
        print(f"{temprature}°C is {converted_temprature}°F")
    elif temprature_unit == "F":
        converted_temprature = convert_to_celsius(fahrenheit=temprature)
        print(f"{temprature}°F is {converted_temprature}°C")

        
except:
    print("Invalid temperature. Please enter a numeric value.")

