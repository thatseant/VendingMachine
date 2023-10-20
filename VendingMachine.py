class VendingMachine:
    #VendingMachine stores Drinks and Denominations for change
    def __init__(self):
        self.drinks = []
        self.denominations = [50, 20, 10, 5, 2, 1]
        self.denomination_names = ['$50', '$20', '$10', '$5', '$2', '$1']

    def add_drinks(self, drink):
        self.drinks.append(drink)

    def buy_drink(self, drink_id, amount_given):
        #Returns change as list of notes
        changeNotes = []

        # Check for valid drink_id
        if drink_id < 0 or drink_id >= len(self.drinks):
            print("Invalid drink ID.")
            changeAmt = amount_given
        else:
            changeAmt = amount_given - self.drinks[drink_id].price

            # Check if amount_given is less than the drink's price
            if changeAmt < 0:
                print(f"Insufficient funds. {self.drinks[drink_id].name} costs ${self.drinks[drink_id].price}.")
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

class Drink:
    def __init__(self, name, price):
      self.name = name
      self.price = price
  
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