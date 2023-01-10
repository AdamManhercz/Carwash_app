
# Carwash app

class Carwash:

    # programs and their data
    programs = {
        "1":{"name": "Pre-washing", "price": 1.5},
        "2":{"name": "Pressure washing", "price": 2.5},                                           
        "3":{"name": "Active foaming", "price": 2},
        "4":{"name": "Rinsing", "price": 1}
    }

    # Counting the consumed materials and the price
    price = 0

    # Choose the right program for washing our car
    def program_choice(self):

        self.choice = input("Which program do you choose: 1 - {}, 2 - {}, 3 - {} or 4 - {}:"\
        .format(self.programs["1"]["name"], self.programs["2"]["name"], self.programs["3"]["name"], self.programs["4"]["name"]))
        
        while self.choice not in {'1', '2', '3', '4'}:

            print("Please, choose from the given program options and enter the proper number of your choice!")

            self.choice = input("Which program do you choose: 1 - Pre-washing, 2 - Pressure washing, 3 - active foam or 4 - Rinsing")


    # Counting the consumption for each program
    def counter(self):

        if self.choice in self.programs:
            self.price += self.programs[self.choice]["price"]
        
        print(f"{self.price}$")

    # Summarize our washing session
    def summary(self):

        print(f"Your total: {self.price}$.")
        self.total =  float(input("Please insert your cash:"))

    # Observe if any change arises
    def change(self):

        if self.total < self.price:
            leftover =  self.price - self.total
            
            left_over = float(input(f"You have left {leftover}$. Please pay the leftover amount!"))

            if left_over > leftover:
                change_left = left_over - leftover
                print(f"Your change: {change_left}$.")
                print("Please, don't forget your change!")

        elif self.total > self.price:
            change = self.total - self.price
            print(f"Your change: {change}$.")
            print("Please, don't forget your change!")

    # Time to say good bye
    def bye(self):

        print("You have finished, your car is shining!")
        print("Thank you for choosing us! Have a nice day!")
        print("Bye!")

    # Make further choices available
    def next_program(self):

        print("Your washing program is over!")
        next = input("Would you like to continue? Y/N: ")

        while next not in {"Y", "N", "y", "n"}:
            next = input("Please insert the right letter! Would you like to continue? Y/N:")

        if next == 'Y' or next == 'y':
        
            self.program_choice()
            self.counter()
            self.next_program() 

        elif next == "N" or next == 'n':
            
            self.summary()
            self.change()
            self.bye()                                   


if __name__ == "__main__":

    app = Carwash()

    app.program_choice()

    app.counter()

    app.next_program()

    

    
    

    

    
    



        


