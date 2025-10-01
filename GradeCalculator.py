def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

subjects = ["Math", "Science", "English", "History", "Computer"]
marks = []

for subject in subjects:
    score = int(input(f"Enter marks for {subject}: "))
    marks.append(score)

total = sum(marks)
percentage = total / len(subjects)

print("\nTotal:", total)
print("Percentage:", percentage)
print("Grade:", calculate_grade(percentage))
