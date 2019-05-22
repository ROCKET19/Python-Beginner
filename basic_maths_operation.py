class Calculator:
    def sum(self, num1, num2):
        print(num1 + num2)

    def difference(self, num1, num2):
        print(num1 - num2)

    def mult(self, num1, num2):
        print(num2 * num1)

    def div(self, num1, num2):
        print(num1 / num2)


x = Calculator()
num1 = int(input('Enter the first number '))
num2 = int(input('Enter the second number '))
choice = input("Enter which operation is to be performed (+) (-) (*) (/) ")
dictionary = {
    "+": x.sum,
    '-': x.difference,
    '*': x.mult,
    '/': x.div

}
dictionary.get(choice)(num1, num2)
