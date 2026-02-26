scores = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94],
    [70, 75, 73],
    [88, 85, 90]
]

print(scores[2][1])

scores[3][0] = 75

avg_math = sum(row[0] for row in scores) / len(scores)
print(avg_math)

#I chose weekly test scores because it is a common and realistic dataset used in schools. A 2D array makes it easy to organize student scores by subject in a clear table-like structure. Each row groups all scores for one student, while each column represents the same subject across students. This makes accessing, updating, and calculating averages much faster and more organized than using separate lists. Using a 2D array also prepares us for handling more complex real-world data in programming.
