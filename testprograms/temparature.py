temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (Celsius or Fahrenheit): ")

if unit == 'celsius':
    t = (temperature * 9/5) + 32
    print(temperature,"degree celsius is equal to",t,"degrees fahrenheit.")
elif unit == 'fahrenheit':
    t= (temperature - 32) * 5/9
    print(temperature,"degrees Fahrenheit is equal to",t,"degrees Celsius.")
else:
    print("Invalid unit. Please enter either Celsius or Fahrenheit.")
