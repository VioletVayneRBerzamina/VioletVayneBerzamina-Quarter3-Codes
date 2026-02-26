scores = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94],
    [70, 75, 73],
    [88, 85, 90]
]

for i in range(len(scores)):
    print("Student", i + 1, "scores:", scores[i])

for i in range(len(scores)):
    total = sum(scores[i])
    average = total / len(scores[i])
    print("Student", i + 1, "Total:", total, "Average:", average)

max_score = max(max(row) for row in scores)
print("Highest score in the dataset:", max_score)

#Using a 2D array made it easier to organize and analyze the test scores because each student’s data was grouped in one row. Calculating totals and averages was simple since loops allowed me to process each row automatically. Printing the data clearly helped me see patterns in student performance. The easiest part was finding totals, while calculating averages required careful division to avoid mistakes.
