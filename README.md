# Vending Machine Project

(Project Specification is for Singapore Dollar System, which is canonical, and for integer values only.)

This project offers a representation of a `VendingMachine`. `VendingMachine` maintains a collection of various drinks and provides methods to determine the list of notes that constitute the change a customer receives upon purchasing a drink. Users interact with the program by providing input to select drinks and specify the amount they are paying. The following Greedy approach to the Change-Making problem works for canonical coin/dollar systems.

## Features:
- Maintains a list of different drinks.
- Accept user input to select a drink and specify the amount given.
- Calculate and display the change to be returned to the user in terms of note denominations.

## Potential Improvements:

1. **Inventory Management**: Enhance the system by monitoring the quantity of each drink. This would ensure that drinks that are out of stock are not available for purchase.
2. **Cash Flow Management**: Keep track of the available notes within the vending machine to ensure that change can always be provided to the customer.

## Running the Program:
1. Navigate to the project directory using the terminal or command prompt.
2. Run the main script using the following command: 
`python VendingMachine.py`