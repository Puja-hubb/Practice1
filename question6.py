expenses = [250, 1200, 450, 800, 150, 2000, 350]

total_expense = sum(expenses)
average_expense = total_expense / len(expenses)
highest_expense = max(expenses)
lowest_expense = min(expenses)

above_500 = 0
below_equal_500 = 0

for expense in expenses:
    if expense > 500:
        above_500 += 1
    else:
        below_equal_500 += 1

print("Total Expense:", total_expense)
print("Average Expense:", round(average_expense, 2))
print("Highest Expense:", highest_expense)
print("Lowest Expense:", lowest_expense)
print("Number of Expenses Above ₹500:", above_500)
print("Number of Expenses Below or Equal to ₹500:", below_equal_500)

print("Expenses Above Average:")

for expense in expenses:
    if expense > average_expense:
        print(expense)