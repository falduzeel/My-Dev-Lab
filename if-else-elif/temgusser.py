temperature = float(input("Enter the temperature: "))

if temperature >= 40:
    print("Very Hot")

elif temperature >= 30:
    print("Hot")

elif temperature >= 20:
    print("Normal Weather")

elif temperature >= 10:
    print("Cool Weather")

else:
    print("Very Cold")
