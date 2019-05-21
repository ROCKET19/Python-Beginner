weight = int(input("Enter your weight "))
unit = input("Is is in (K)g or (l)bs ")
if unit.upper() == 'K':
    converter_weight = weight/.45
    print(f"Your weight is {converter_weight} lbs")
else:
    converter_weight = .45*weight
    print(f"Your weight is {converter_weight} kg")