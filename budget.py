#task1
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name  # Private attribute for category name
        self.__allocated_budget = allocated_budget  # Private attribute for allocated budget
        self.__remaining_budget = allocated_budget  # Start with full budget
#task2
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number.")

    # Getter for remaining budget
    def get_remaining_budget(self):
        return self.__remaining_budget
#task3
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # ... (Getters and Setters as before)

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        if amount > self.__remaining_budget:
            raise ValueError("Expense exceeds the remaining budget.")
        self.__remaining_budget -= amount
#task4
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # ... (Getters, Setters, and add_expense as before)

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")
#task5
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number.")

    # Getter for remaining budget
    def get_remaining_budget(self):
        return self.__remaining_budget

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        if amount > self.__remaining_budget:
            raise ValueError("Expense exceeds the remaining budget.")
        self.__remaining_budget -= amount

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self.get_category_name()}")
        print(f"Allocated Budget: ${self.get_allocated_budget()}")
        print(f"Remaining Budget: ${self.get_remaining_budget()}")


# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
