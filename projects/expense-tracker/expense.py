class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def to_file_string(self):
        return f"{self.description}, {self.amount}"

    def __str__(self):
        return f"{self.description}: ₹{self.amount}"

    @classmethod
    def from_file_line(cls, line):
        description, amount = line.strip().split(",")
        return cls(description, int(amount))
