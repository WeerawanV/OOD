h,w = (input("Enter your High and Weight : ").split())
bmi = (float(w) / (float(h)*float(h)))
if bmi < 18.5 :
    print("Less Weight")
elif bmi >= 18.5 and bmi < 23 :
    print("Normal Weight")
elif bmi >= 23 and bmi < 25 :
    print("More than Normal Weight")
elif bmi >= 25 and bmi < 30:
    print("Getting Fat")
elif bmi >= 30 :
    print("Fat")
