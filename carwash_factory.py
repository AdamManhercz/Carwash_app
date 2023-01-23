from dataclasses import dataclass, field
from typing import Union

PROGRAMS = {
    "1": {"name": "Pre-washing", "price": 1.5},
    "2": {"name": "Active foaming", "price": 2},
    "3": {"name": "Pressure washing", "price": 2},
    "4": {"name": "Rinsing", "price": 1},
}


class ProgramOptions:
    """Introduces the available washing programs"""

    def __init__(self) -> None:
        self.programs = PROGRAMS

    def program_options(self) -> str:
        """Lists the program options"""

        options = ""
        for p in self.programs:

            options += "{}: {} ".format(p, self.programs[p]["name"])

        return options

    def program_choice(self, choice: str) -> dict | str:
        """Returns the chosen program and its data"""

        if choice in self.programs:
            return self.programs[choice]
        print("Please select a valid program!")


class MoneyCheck(ProgramOptions):
    """Sets up the money flow"""

    def __init__(self) -> None:

        self.price = 0

    def counter(self, choice: dict) -> str:
        """Counts the cost"""
        self.price += choice["price"]

        print(f"{self.price}$")

    def summary(self) -> str:
        """Displays the total cost and demand the payment"""

        print(f"Your total: {self.price}$.")
        self.total = float(input("Please insert your cash:"))

    def change(self) -> str:
        """Observes if any change arises"""

        if self.total < self.price:
            leftover = self.price - self.total

            left_over = float(
                input(f"You have left {leftover}$. Please pay the leftover amount!")
            )

            if left_over > leftover:
                change_left = left_over - leftover
                print(f"Your change: {change_left}$.")
                print("Please, don't forget your change!")

        elif self.total > self.price:
            change = self.total - self.price
            print(f"Your change: {change}$.")
            print("Please, don't forget your change!")


class Next:
    """Makes further actions available"""

    def program_end(self) -> str:

        print("Your washing program is over!")
        next = input("Would you like to continue? Y/N: ")

        return next

    def bye(self) -> str:
        """Time to say good bye"""

        print("Thank you for choosing us! Have a nice day!")
        print("Bye!")


def main(carwash: MoneyCheck, next: Next):

    on = True

    while on:

        choice = input(f"Which program do you choose: {carwash.program_options()}?")

        program = carwash.program_choice(choice)

        carwash.counter(program)

        if next.program_end() in {"Y", "y"}:

            on = True

        else:

            carwash.summary()
            carwash.change()
            next.bye()

            on = False


if __name__ == "__main__":

    carwash = MoneyCheck()
    next = Next()

    main(carwash, next)
