
# Carwash app

class Carwash:

    # programs and their data
    programs = {
        "1":{
            "name": "Pre-washing", "time": 45, "water": 5, "foam": 0.2, "price": 1.5 
        },
        "2":{
            "name": "Pressure washing","time": 60, "water": 10,"foam": 0.4,"price": 2.5 
        },                                           
        "3":{
            "name": "Active foaming", "time": 60, "water": 6, "foam": 0.8, "price": 2
        },
        "4":{
            "name": "Rinsing", "time": 60, "water": 6, "foam": 0, "price": 1
        }
    }


    # counting the consumed materials and the price
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

        if  self.choice == '1':
            self.price += 1.5 
        elif self.choice == '2':
            self.price += 2.5 
        elif self.choice == '3':
            self.price += 2 
        elif self.choice == '4':
            self.price += 1


    # Summarize our washing session
    def summary(self):

        print(f"Your total: {self.price}$.")
        total =  float(input("Please insert your cash:"))

        if total < self.price:
            leftover =  self.price - total
            
            left_over = float(input(f"You have left {leftover}$. Please pay the leftover amount!"))

            if left_over > leftover:
                change_left = left_over - leftover
                print(f"Your change: {change_left}$.")
                print("Please, don't forget your change!")

        elif total > self.price:
            change = total - self.price
            print(f"Your change: {change}$.")
            print("Please, don't forget your change!")

        print("Thank you for choosing us! Have a nice day!")
        print("Bye!")


    # Making further choices available
    def next_program(self):

        print("Your washing session is over!")
        next = input("Would you like to continue? Y/N:")

        while next not in {"Y", "N"}:

            next = input("Please insert the right letter! Would you like to continue? Y/N:")

        if next == 'Y':
            
            print(f"Your total: {self.price}$.")  

            self.program_choice()
            self.counter()
            self.next_program() 

        elif next == "N":

            print("You have finished, your car is shining!")
            self.summary()


if __name__ == "__main__":

    carwash = Carwash()

    carwash.program_choice()

    carwash.counter()

    carwash.next_program()

    
    



        


