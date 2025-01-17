import matplotlib.pyplot as plt  # Import the matplotlib.pyplot module for creating plots
import numpy as np  # Import numpy for numerical operations, though not used explicitly in this version

# Define a class to manage the personal finance tracker
class PersonalFinanceTracker:
    def __init__(self):
        # Initialize the list of months in a year and empty lists to store monthly income, expenses, and balance
        self.months = ["January", "February", "March", "April", "May", "June", 
                       "July", "August", "September", "October", "November", "December"]
        self.income = []  # List to store monthly income values
        self.expenses = []  # List to store monthly expense values
        self.balance = []  # List to store balance for each month (income - expenses)

    def get_user_input(self):
        """Get monthly income and expenses from user input"""
        # Loop through each month and ask the user for income and expenses
        for month in self.months:
            print(f"\nEnter the details for {month}:")  # Print a prompt for the current month
            income = float(input(f"  Income for {month}: $"))  # Ask the user for income and convert to float
            expenses = float(input(f"  Expenses for {month}: $"))  # Ask the user for expenses and convert to float
            
            # Append the input values to the respective lists (income, expenses)
            self.income.append(income)
            self.expenses.append(expenses)
            
            # Calculate the balance for the month (income - expenses) and append it to the balance list
            self.balance.append(income - expenses)

    def plot_finances(self):
        """Plot the monthly balance (income - expenses)"""
        # Create a figure and an axis object for the plot
        fig, ax = plt.subplots(figsize=(10, 6))  # Set the size of the figure
        
        # Determine the color for each bar based on whether the balance is positive or negative
        balance_color = ['green' if b >= 0 else 'red' for b in self.balance]

        # Create a bar plot with months on the x-axis and balance on the y-axis
        ax.bar(self.months, self.balance, color=balance_color)

        # Add a title to the plot
        ax.set_title('Personal Finance Tracking for 1 Year', fontsize=14)
        # Label the x-axis as 'Months'
        ax.set_xlabel('Months', fontsize=12)
        # Label the y-axis as 'Balance ($)'
        ax.set_ylabel('Balance ($)', fontsize=12)
        # Add a horizontal line at y = 0 for visual reference (to differentiate between surplus and deficit)
        ax.axhline(0, color='black', linewidth=1)
        
        # Rotate the month names on the x-axis for better readability
        plt.xticks(rotation=45)
        # Ensure that everything fits nicely in the plot layout
        plt.tight_layout()
        # Display the plot
        plt.show()

    def calculate_yearly_summary(self):
        """Calculate yearly summary of income, expenses, and savings"""
        # Sum up the total income and total expenses for the year
        total_income = sum(self.income)
        total_expenses = sum(self.expenses)
        # Calculate the total savings (income - expenses)
        total_savings = total_income - total_expenses
        
        # Print the summary of the year's financial performance
        print("\nYearly Summary:")
        print(f"  Total Income: ${total_income:,.2f}")  # Display total income with formatting
        print(f"  Total Expenses: ${total_expenses:,.2f}")  # Display total expenses with formatting
        print(f"  Total Savings: ${total_savings:,.2f}")  # Display total savings with formatting

    def run(self):
        """Run the finance tracker"""
        # First, get the user's monthly income and expenses
        self.get_user_input()
        # Then, plot the financial data for the year
        self.plot_finances()
        # Finally, calculate and display the yearly summary
        self.calculate_yearly_summary()

# Create an instance of the PersonalFinanceTracker class
finance_tracker = PersonalFinanceTracker()

# Run the finance tracker program
finance_tracker.run()
