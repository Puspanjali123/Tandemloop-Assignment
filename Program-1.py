# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#            Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#            Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
 
class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower() 

    def calculate(self):
        if self.operation == "add" or self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtract" or self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiply" or self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "divide" or self.operation == "division":
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            return self.a / self.b
        else:
            return "Error: Invalid operation."


if __name__ == "__main__":
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    calc = Calculator(a, b, operation)
    result = calc.calculate()

    print("Result:", result)
