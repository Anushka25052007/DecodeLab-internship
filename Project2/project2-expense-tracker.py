# Expenses Tracker Application in Python.
# Where user can add expenses, view expenses, show total expenses, delete expenses and also track expenses by category

expense_list=[]

print("Expense Tracker:")
print("1. Add Expense"+"\n"+"2. View Expenses"+"\n"+"3. Show Total Expense"+"\n"+"4. Show Total Expense by Category"+"\n"+"5. Delete Expense"+"\n"+"6. Exit")
next_expense_id=1

# Add expenses Add the expenses with the details in the list of expenses
def add_expense():
    global next_expense_id
    title=input("Enter the Title of Expense:")
    amount=float(input("Enter Expense Amount:"))
    print("Expense Categories:")
    print("1. Food\n"+"2. Travel\n"+"3. Shopping\n"+"4. Education\n"+"5. Entertainment\n"+"6. Health\n"+"7. Bills\n"+"8. Other\n")
    category_input=input("Enter Expense Category number(1/2/3/4/5/6/7/8):")
    date=input("Enter Date (DD-MM-YYYY):")

    if category_input=="1":
        category="Food"
    elif category_input=="2":
        category="Travel"
    elif category_input=="3":
        category="Shopping"
    elif category_input=="4":
        category="Education"
    elif category_input=="5":
        category="Entertainment"
    elif category_input=="6":
        category="Health"
    elif category_input=="7":
        category="Bills"
    elif category_input=="8":
        category="Other"
    else:
        category="Other"


    expense={
        "id":next_expense_id,
        "title":title,
        "amount":amount,
        "category": category,
        "date":date
    }

    expense_list.append(expense)
    print("Expense added successfully")
    next_expense_id=next_expense_id+1  


# View expenses function displays the add expenses in the list with the details
def view_expense():
    if not expense_list:
        print("No Expenses to display.")
    else:
        total_number_of_expense=len(expense_list)

        print("||\tTotal Number of Expenses:"+str(total_number_of_expense)+"||")
        
        # Table of Expense Details
        print("-"*100)
        print("\tID\tTITLE\tAMOUNT\tCATEGORY\tDATE\t")
        print("-"*100)
        for expense in expense_list:
            print(f"\t{expense['id']}\t{expense['title']}\t{expense['amount']}\t{expense['category']}\t{expense['date']}\t")


# total expense function to calculate the total of expenses spend by the user and display the total amount of expenses

def total_expense():
    if not expense_list:
        print("Total Expenses is Zero(0).")
    else:
        total_spend=0
        for expense in expense_list:
            total_spend +=expense['amount']
        print("Total Expenses Spend:"+str(total_spend))


# delete expense function to delete the expenses from the list based on ID.

def delete_expense():
    expense_id=int(input("Enter Expense ID to delete the expense:"))
    for expense in expense_list:
        if expense["id"]==expense_id:
            expense_list.remove(expense)
            print("Expense is deleted")
            return
    print("That expense is not found")

# show total expense by category works in two way like if user want to see only the total of one category or all the categories at the same time it can be possible

def show_total_expense_by_category():
    if not expense_list:
        print("Expenses for all the categories are zero(0).")
    else:
        food_total=0
        travel_total=0
        shopping_total=0
        education_total=0
        entertainment_total=0
        health_total=0
        bills_total=0
        other_total=0

        for expense in expense_list:
            if expense["category"]=="Food":
                food_total=food_total+expense["amount"]
            elif expense["category"]=="Travel":
                travel_total=travel_total+expense["amount"]
            elif expense["category"]=="Shopping":
                shopping_total=shopping_total+expense["amount"]
            elif expense["category"]=="Education":
                education_total=education_total+expense["amount"]
            elif expense["category"]=="Entertainment":
                entertainment_total=entertainment_total+expense["amount"]
            elif expense["category"]=="Health":
                health_total=health_total+expense["amount"]
            elif expense["category"]=="Bills":
                bills_total=bills_total+expense["amount"]
            elif expense["category"]=="Other":
                other_total=other_total+expense["amount"]
        
        # one category total expense tracking or the all categories total expenses trakcing based on user choice
        # if want to see one category total expenses then enter 1
        # if want to see all categories total expenses then enter 2
        choice=input("Enter the choice for Expense Tracking as one category expenses(1) or all categories expenses(2): ")

        # show total expense by category for one category at a time
        if choice=="1":
            category_input=input("Enter Expense Category number(1/2/3/4/5/6/7/8):")
            if category_input=="1":
                print(f"Food: {food_total}")
            elif category_input=="2":
                print(f"Travel: {travel_total}")
            elif category_input=="3":
                print(f"Shopping: {shopping_total}")
            elif category_input=="4":
                print(f"Education: {education_total}")
            elif category_input=="5":
                print(f"Entertainment: {entertainment_total}")
            elif category_input=="6":
                print(f"Health: {health_total}")
            elif category_input=="7":
                print(f"Bills: {bills_total}")
            elif category_input=="8":
                print(f"Other: {other_total}")
            else:
                print("Invalid Choice")

        ## show total expense by category for all category at a time
        elif choice=="2":
            print("Total Expenses by Category:")
            print(f"Food: {food_total}")
            print(f"Travel: {travel_total}")
            print(f"Shopping: {shopping_total}")
            print(f"Education: {education_total}")
            print(f"Entertainment: {entertainment_total}")
            print(f"Health: {health_total}")
            print(f"Bills: {bills_total}")
            print(f"Other: {other_total}")
        else:
            print("Invalid Choice Please enter 1 or 2.")

# Main Loop to interact with user
while True:
    choice=input("Enter you Choice:")

    if choice == "1":
        add_expense()
    elif choice=="2":
        view_expense()
    elif choice=="3":
        total_expense()
    elif choice=="4":
        show_total_expense_by_category()
    elif choice=="5":
        delete_expense()
    elif choice=="6":
        print("Exiting the Expense Tracker Application, Thank you for using Expense Tracker Application!...")
        break
    else:
        print("Invalid Choice")