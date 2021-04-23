class ComplexNumber :
    def __init__(self, r =0, i = 0):
        self.r = r
        self.i = i

    def get_data(self):
        print(f'{self.r}+{self.i}i')

num1 = ComplexNumber(2,3)
num1.get_data()

num2 = ComplexNumber(5)
num2.attr = 10

print(num2.r, num2.i, num2.attr)