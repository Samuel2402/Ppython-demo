def grade(name, homework, assessment, final_exam):
    total_score = homework + assessment + final_exam
    score = round((total_score/175)*100)

    if score >= 90:
        grade = 'A(star)'
    elif score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = 'D'
    elif score >= 40:
        grade = 'E'
    else:
        grade = "Fail"
    return grade

homework = int(input("Please enter your Homework score here (out of 25): "))
assessment = int(input("Please enter your Assessment score here (out of 50): "))
final_exam = int(input("Please enter your Final Exam score here (out of 100): "))
student_name = input("Please enter your name: ")

grade1 = grade(student_name, homework, assessment, final_exam) 

print(f"name: {student_name} with grade: {grade1}")






