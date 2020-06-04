weight = int(input("Enter your Weight :"))
unit = input("(L)bs or (K)g:")
if unit.upper() == "L":
    converter = weight * 0.45
    print("You are {} Kilos".format(converter))
else:
    converter = weight / 0.45
    print("You are {} Pounds".format(converter))
