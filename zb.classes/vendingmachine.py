    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":


    vendingmachine = VendingMachine()

    purchase = int(input())
    restock = int(input())
    vendingmachine.purchase(purchase)
    vendingmachine.restock(restock)
    vendingmachine.report()

    # TODO: Create VendingMachine object
    # TODO: Purchase input number of drinks
    # TODO: Restock input number of bottles
    # TODO: Report inventory
