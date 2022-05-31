weight = float(input("Weight: "))
unit = input("KG or LB: ")
if unit.upper() == "KG":
    converted = str(weight / 0.45)
    print("Weight in Lbs: " + converted)
else:
    converted = str(weight * 0.45)
    print("Weight in Kgs: " + converted)
