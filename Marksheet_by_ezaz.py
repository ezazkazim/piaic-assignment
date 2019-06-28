name = input("Name: ")
eng = float(input("Obtained Marks in ENGLISH: "))
if eng > 100:
    print("Marks should be between 0 and 100")
else:
    maths = float(input("Obtained Marks in MATHS: "))
    if maths > 100:
        print("Marks should be between 0 and 100")
    else:
        urdu = float(input("Obtained Marks in UDRU: "))
		if urdu > 100:
			print("Marks should be between 0 and 100")
        total_marks = 300
        obt_marks = eng+maths+urdu
        percentage = (obt_marks/total_marks)*100
        print("Total Marks :" ,total_marks, ", Obtained Marks :" ,obt_marks, "and Percentage :" ,percentage, "%.")
        if percentage >= 90:
            print("GRADE = A++")
        elif percentage >= 80:
            print("GRADE = A+")
        elif percentage >= 70:
            print("GRADE = A")
        elif percentage >= 60:
            print("GRADE = B")
        elif percentage >= 50:
            print("GRADE = C")
        else:
            print("Remarks = FAIL")