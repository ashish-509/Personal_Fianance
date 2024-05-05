from expense import Expense
import calendar
import datetime

currencyName = 'NRs.'

def main():
    
    def take_new_user_info():
        name = input("\nPlease, Enter your name : ")
        budget = input("\nEnter your monthly budget : ")
        currencyName = input("\nEnter your currency symbol (NRs.) ?: ")


    
    budget = 2000
    name = "Ashish"

    def welcome_message():
        print("\n\n....Welcome ", name , " to your budget plannar....\n")
        print("\nYour monthly budget is : ", budget)
        print("\t\t\t Date :  ", datetime.datetime.now())
    
    char_input = input("\nTo continue the session press 'y' else press 'n': ")
    
    if (char_input.lower() == 'n'):
        take_new_user_info()
        welcome_message()
        

    
    print(f"\n-----> Running Expense Tracker of {name} !")
    expense_file_path = "expenses.csv"
    

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(f"\n-----> Getting User Expense")
    expense_name = input("\n    Enter expense name : ")
    expense_amount = float(input("\n    Enter expense amount : "))
    expense_categories = [
       "\U0001F355 Food", 
        "\U0001F3E0 Home", 
        "\U0001F9D8 Lifestyle", 
        "\U0001F4DA Learning", 
        "\U0001F3A8 Entertainment", 
        "\U0001F9F9 Miscellaneous",
        "🚌 Travel"
    ]

    while True:
        print("\n Select a category : \n")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"\n   Enter a category number {value_range} : \n")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("\n Invalid category. Please try again with a valid number!")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"\n-----> Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    print(f"\n-----> Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    bold = "\033[1m" # ANSI escape code for bold text

    reset = "\033[0m" # Reset ANSI escape code

    text = "\nExpenses By Category 📈 : \n" # Text to be displayed in bold

    print("\n" + bold + text + reset + "\n") # Print the bold text

    for key, amount in amount_by_category.items():
        print(f"  {key}: {currencyName} {amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"\n💵 Total Spent: {currencyName} {total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"\n✅ Budget Remaining: {currencyName} {remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"\n👉 Budget Per Day: {currencyName} {daily_budget:.2f}\n\n"))


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()