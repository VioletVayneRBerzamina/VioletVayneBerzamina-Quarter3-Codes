
names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

for i in range(len(steps)):
    print(f"{names[i]}'s steps: {steps[i]}")

print("\nSummary per person:")

for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    print(f"{names[i]} - Total Steps: {total}, Average Steps: {average:.2f}")

max_steps = max(max(row) for row in steps)
min_steps = min(min(row) for row in steps)
print(f"\nMaximum steps in the dataset: {max_steps}")
print(f"Minimum steps in the dataset: {min_steps}")


#Using a 2D array allowed me to organize each person’s daily steps neatly in rows, making it easier to calculate totals and averages. I could loop through each row to summarize each person’s data without repeating code for every individual. Finding the maximum and minimum values was simple because all the data was stored in one structured array. The easiest part was summing each row, while the slightly tricky part was using nested functions to find the overall maximum and minimum.
