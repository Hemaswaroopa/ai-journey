expenses= []

def add_expense(description, amount, category):
    add_expense = {"description": description, "amount": amount, "category": category}
    expenses.append(add_expense)
    print(f"Added:{description}-Rs.{amount}-{category}.")
add_expense("Lunch", 250, "Food")
add_expense("Cab",500, "Transport")
add_expense("Personal loan", 45000, "EMI")
add_expense("Groceries", 2500, "Food")
add_expense("Metro card", 1000, "Transport")
add_expense("credit card",7000, "EMI")

def view_expense():
    for expense in expenses:
        print(f"{expense['description']}-Rs.{expense['amount']}({expense['category']})")
view_expense()

def get_total():
    total = 0
    for expense in expenses:
        total = total + expense['amount']
    return total
result= get_total()
print(f"Total spent:Rs.{result}")

def category_breakdown():
    totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in totals:
            totals[category] += amount
        else:
            totals[category]= amount
    return totals
result = category_breakdown()
print(result)

