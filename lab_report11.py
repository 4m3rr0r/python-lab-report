marks = {
    "Bangla": 86,
    "Math": 77,
    "Science": 80
}

highest_subject = max(marks, key=marks.get)

print(f"Highest scoring subject: {highest_subject}")
