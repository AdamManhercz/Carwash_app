from dataclasses import dataclass
from abc import ABC


class Flavor(ABC):
    """Represents the abtract class of a flavor"""

    water: int
    coffee: int
    ground: int


@dataclass
class Ristretto(Flavor):
    """Resource demand of ristretto"""

    water: int = 50
    coffee: int = 10
    ground: int = 10


@dataclass
class Espresso(Flavor):
    """Resource demand of espresso"""

    water: int = 100
    coffee: int = 20
    ground: int = 20


@dataclass
class Lungo(Flavor):
    """Resource demand of lungo"""

    water: int = 150
    coffee: int = 35
    ground: int = 35


class CoffeeMachine:
    """Represents the attributes and operations of a coffee machine"""

    def __init__(self) -> None:
        self.name = input("Please, enter your name: ")
        self.order = input(
            "Please, enter your coffe order(ristretto, espresso, lungo): "
        )
        self.volume = int(input(f"How many {self.order} would you like to order?"))
        self.resources = {"water": 1000, "coffee": 500, "ground": 100}

    def report(self):
        """Reports the state of the resources"""

        print(
            f"Water: {self.resources['water']}\nCoffee: {self.resources['coffee']}\nGround: {self.resources['ground']}"
        )

    def get_flavor(self) -> Flavor:
        """Gets the order"""

        flavors = {"ristretto": Ristretto(), "espresso": Espresso(), "lungo": Lungo()}

        if self.order in flavors:
            return flavors[self.order]
        print("Please, choose from the available coffee flavors!")

    def check_resources(self, flavor: Flavor):
        """Checks the resources during the brewing"""

        flavor = flavor.__dict__

        for resource in self.resources:
            if self.resources[resource] >= flavor[resource]:
                if resource == "ground":
                    self.resources[resource] -= 1
                else:
                    self.resources[resource] -= flavor[resource]
            else:
                raise ValueError(f"{resource}")

    def refill_resource(self, missing_resource: str):
        """Enables the refill process"""

        refill_values = {"water": 1000, "coffee": 500, "ground": 100}

        refill_choice = input(f"Please, refill the {missing_resource} resource? y/n: ")

        while refill_choice != "y":
            refill_choice = input(
                f"Please, refill the {missing_resource} resource? y/n: "
            )
        else:
            if missing_resource in refill_values:
                self.resources[missing_resource] += (
                    refill_values[missing_resource] - self.resources[missing_resource]
                )
                print(f"{missing_resource.capitalize()} resource is filled up!")

    def brew(self):
        """Executes the brewing"""

        for i in range(self.volume):
            try:
                flavor = self.get_flavor()
                self.check_resources(flavor)

            except ValueError as error:
                missing_resource = error.args[0]
                self.refill_resource(missing_resource)
                self.check_resources(flavor)

        print(f"{self.name} your order is completed!")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    coffee_machine.brew()

    coffee_machine.report()
