# (i)

age = int(input("enter your age: "))
if age >=  18:
    print("you are eligible")
else:
    print("you are not eligible")


#  (ii) and (iii)

def grade_students(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    elif 0 <= mark < 60:
        return "F"
    else:
        return "Invalid Mark"
print(grade_students(85))

# (iv)

def grade_students(mark):
    try:
        mark = float(mark)
        if 90 <= mark <= 100:
            return "A"
        elif 80 <= mark < 90:
         return "B"
        elif 70 <= mark < 80:
            return "C"
        elif 60 <= mark < 70:
            return "D"
        elif 0 <= mark < 60 :
            return "F"
        else:
            return "Invalid Mark"
    except ValueError:
        return "Invalid Input"
    
print(grade_students(85))
print(grade_students("invalid"))

# (v)

def grade_students(mark):
    try:
        mark = float(mark)
        if 90 <= mark <= 100:
            return "A" , "Excellent"
        elif 80 <= mark < 90:
         return "B" , "Excellent"
        elif 70 <= mark < 80:
            return "C" , "Good"
        elif 60 <= mark < 70:
            return "D" , "Satisfactory"
        elif 0 <= mark < 60 :
            return "F" , "Needs Improvement"
        else:
            return "Invalid Mark"
    except ValueError:
        return "Invalid Input"

grade , comment = grade_students(85)
print(f"Grade: {grade}, comment: {comment}")

# (vi)

def grade_students(mark):
    try:
        mark = float(mark)
        if 90 <= mark <= 100:
            return "A" , "Excellent"
        elif 80 <= mark < 90:
         return "B" , "Excellent"
        elif 70 <= mark < 80:
            return "C" , "Good"
        elif 60 <= mark < 70:
            return "D" , "Satisfactory"
        elif 0 <= mark < 60 :
            return "F" , "Needs Improvement"
        else:
            return "Invalid Mark"
    except ValueError:
        return "Invalid Input"
    
grade, comment = grade_students(78)
print(f"Grade: {grade}, comment: {comment}")
