
class Expense:
    def __init__ (self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self) -> str:
        return f"<Expenses : \n\t {self.name}, {self.category}, NRs.{self.amount : .2f} >"
         