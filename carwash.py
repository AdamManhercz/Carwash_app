
# steps:
# which carwash program you choose?
# program is over, choose another or end?
# cash counter
# limits

from traceback import print_exc


class Carwash():

    # limits
    programs = {
        "1":{
            "name": "Pre-washing",
            "time": 45,
            "water": 5,
            "foam": 0.2,
            "price": 1.5 
        },
        "2":{
            "name": "Pressure washing",
            "time": 60,
            "water": 10,
            "foam": 0.4,
            "price": 2.5
        },
        "3":{
            "name": "Active foaming",
            "time": 60,
            "water": 6,
            "foam": 0.8,
            "price": 2
        },
        "4":{
            "name": "Rinsing",
            "time": 60,
            "water": 6,
            "foam": 0,
            "price": 1
        }
    }

    price = 0
    time = 0
    water = 0
    foam = 0

    def program_choice(self):

        self.choice = input(f"Which program do you choose: 1 - Pre-washing, 2 - Pressure washing, 3 - active foam or 4 - Rinsing")
        
        while self.choice not in {'1', '2', '3', '4'}:

            print("Please, choose from the given program options and enter the proper number of your choice!")

            self.choice = input("Which program do you choose: 1 - Pre-washing, 2 - Pressure washing, 3 - active foam or 4 - Rinsing")

    def counter(self):

        if  self.choice == '1':
            self.time += 45
            self.water += 5
            self.foam += 0.2
            self.price += 1.5 
        elif self.choice == '2':
            self.time += 60
            self.water += 10
            self.foam += 0.4
            self.price += 2.5 
        elif self.choice == '3':
            self.time += 60
            self.water += 6
            self.foam += 0.8
            self.price += 2 
        elif self.choice == '4':
            self.time += 60
            self.water += 6
            self.foam += 0
            self.price += 1

    def summary(self):

        print(f"You have used {self.water} liter of water, {round(self.foam,2)} liter of foam in {self.time} seconds.")
        print(f"Your total: {self.price}$.")
        total =  int(input("Please insert your cash:"))

        if total < self.price:
            leftover =  self.price - total
            
            left_over = int(input(f"You have left {leftover}$. Please pay the leftover amount!"))

            if left_over > leftover:
                change_left = left_over - leftover
                print(f"Your change: {change_left}$.")
                print("Please, don't forget your change!")

        elif total > self.price:
            change = total - self.price
            print(f"Your change: {change}$.")
            print("Please, don't forget your change!")

        print("Thank you for choosing us! Have a nice day!")

    def next_program(self):

        print("Your washing session is over!")
        next = input("Would you like to continue? Y/N:")

        while next not in {"Y", "N"}:

            next = input("Please insert the right letter! Would you like to continue? Y/N:")

        if next == 'Y':
            
            print(f"You have used {self.water} liter of water, {round(self.foam,2)} liter of foam in {self.time} seconds.")
            print(f"Your total: {self.price}$.")  

            Carwash.program_choice(self)
            Carwash.counter(self)
            Carwash.next_program(self) 

        elif next == "N":

            print("You have finished, your car is shining!")
            Carwash.summary(self)


carwash = Carwash()

if __name__ == "__main__":

    carwash.program_choice()

    carwash.counter()

    carwash.next_program()

    
    



        


