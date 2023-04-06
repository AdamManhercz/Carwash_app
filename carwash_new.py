from programs import Program, PreWashing, PressureWashing, ActiveFoam, Rinsing


class Carwash:
    """Repsresents the operations of th carwash"""

    def __init__(self) -> None:
        self.total: float = 0

    def add_price(self, program: Program) -> None:
        """Adds program price to total"""

        self.total += program.price

    def report_total(self) -> str:
        """Reports user's total"""

        return f"Your total: {self.total}$"

    def get_payment(self, money: float) -> bool:
        """User pays"""

        if money > self.total:
            change = money - self.total
            self.total = 0
            print(f"Your change: {change}$")
            print("Thank you for choosing us!")
            return False
        elif money < self.total:
            deficit = self.total - money
            self.total = deficit
            print(f"Your deficit: {deficit}$")
            return True
        else:
            self.total = 0
            print("Thank you for choosing us!")
            return False

    def end_or_continue(self) -> bool:
        """Option to continue or end washing session"""

        answer = input("Your program is over. Would you like to continue? y/n: ")

        if answer == "y":
            return True
        else:
            while self.total != 0:
                self.report_total()
                cash = float(input("Please, insert your cash:"))
                self.get_payment(cash)
            else:
                return False

    def run_washing(self, program: Program):
        """Compounds operations"""

        self.add_price(program)
        self.report_total()

        self.end_or_continue()


def get_program() -> Program:
    """Get the program"""

    choice = int(input("Which washing program would you choose?: "))

    programs = {
        1: PreWashing(),
        2: PressureWashing(),
        3: ActiveFoam(),
        4: Rinsing(),
    }

    if choice in programs:
        return programs[choice]
    print("Please, choose from the available programs!")


if __name__ == "__main__":
    carwash = Carwash()

    while True:
        print("====================================")
        print("1: Pre-washing, 2: Pressure washing, 3: Active foam, 4: Rinsing")
        print("====================================")

        program = get_program()

        carwash.run_washing(program)
