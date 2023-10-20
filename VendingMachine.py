class VendingMachine:
    #VendingMachine stores Drinks and Denominations for change
    def __init__(self):
        self.drinks = []
        self.denominations = [50, 20, 10, 5, 2, 1]
        self.denomination_names = ['$50', '$20', '$10', '$5', '$2', '$1']

    def add_drinks(self, drink):
        self.drinks.append(drink)

    def buy_drink(self, drink_id, amount_given):
        # Returns list of notes comprising change customer receives
        changeNotes = []

        if drink_id >= len(self.drinks):
            print("Invalid drink ID")
            changeAmt = amount_given
        else:
            changeAmt = amount_given - self.drinks[drink_id].price

        if changeAmt < 0:
            print("Insufficient amount given. Please provide enough money to purchase the drink.")
            return []

        for denom, name in zip(self.denominations, self.denomination_names):
            while changeAmt >= denom:
                changeAmt -= denom
                changeNotes.append(name)

        return changeNotes

    
    def buy_with_notes(self, drink_id, notes_given):
        # Takes in amount as list of notes, notes_given, instead eg. ['$10', '$2', '$5', ...].
        amount_given = sum([self.denominations[self.denomination_names.index(note)] for note in notes_given])
        return self.buy_drink(drink_id, amount_given)
    
    def display_drinks(self):
        print("Available drinks:")
        for idx, drink in enumerate(self.drinks):
                print(f"ID: {idx} - {drink.name} (${drink.price})")

class Drink:
    def __init__(self, name, price):
      self.name = name
      self.price = price

def main():
    vm = VendingMachine()

    # Initializing with a list of drinks
    drinks = [Drink("Milo", 8), Drink("Iced Coffee", 11), Drink("Iced Tea", 7), Drink("100 Plus", 4), Drink("Green Tea", 12)]
    for drink in drinks:
        vm.add_drinks(drink)

    while True:
        vm.display_drinks()
        
        drink_id = int(input("Enter the ID of the drink you want to purchase: "))
        amount_given = float(input("Enter the amount given ($): "))

        change = vm.buy_drink(drink_id, amount_given)
        print(f"Your change is: {', '.join(change)}\n")

        cont = input("Do you want to buy another drink? (yes/no): ").lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
  
#Test Cases

def test_add_drinks():
    vm = VendingMachine()
    d = Drink("Cola", 3)
    vm.add_drinks(d)
    assert vm.drinks[0].name == "Cola"
    assert vm.drinks[0].price == 3


def test_exact_amount():
    vm = VendingMachine()
    d = Drink("Coffee", 10)
    vm.add_drinks(d)
    change = vm.buy_drink(0, 10)
    assert change == []

def test_more_than_required_amount():
    vm = VendingMachine()
    d = Drink("Orange Juice", 12)
    vm.add_drinks(d)
    change = vm.buy_drink(0, 20)
    assert change == ['$5', '$2', '$1']

def test_insufficient_amount():
    vm = VendingMachine()
    d = Drink("Milo", 15)
    vm.add_drinks(d)
    change = vm.buy_drink(0, 11)
    assert change == []

def test_buy_with_exact_notes():
    vm = VendingMachine()
    d = Drink("7UP", 12)
    vm.add_drinks(d)
    change = vm.buy_with_notes(0, ['$10', '$2'])
    assert change == []

def test_buy_with_more_notes():
    vm = VendingMachine()
    d = Drink("Mountain Dew", 17)
    vm.add_drinks(d)
    change = vm.buy_with_notes(0, ['$10', '$10'])
    assert change == ['$2', '$1']

def test_invalid_drink_id():
    vm = VendingMachine()
    d = Drink("100 Plus", 5)
    vm.add_drinks(d)
    change = vm.buy_drink(5, 10)  # No drink with ID 5
    assert change == ['$10']

test_add_drinks()
test_exact_amount()
test_more_than_required_amount()
test_insufficient_amount()
test_buy_with_exact_notes()
test_buy_with_more_notes()
test_invalid_drink_id()