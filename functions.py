def hi_user(first_name, last_name):
    answer = first_name + " " + last_name
    return answer

user1 = hi_user("Samuel", "Castle")

print("Hi, " + user1)

homework = print(int(input("Please enter your Homework score here (out of 25): ")))
assessment = print(int(input("Please enter your Assessment score here (out of 50): ")))
final_exam = print(int(input("Please enter your Final Exam score here (out of 100): ")))

grade1 = float((homework/25)*100)
grade2 = float((assessment/50)*100)
grade3 = float(final_exam/100)
print("Final grade:" + grade1)
print("Final grade:" + grade2)
print("Final grade:" + grade3)
