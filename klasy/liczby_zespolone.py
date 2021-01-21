class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __abs__(self):
        return ((self.real * self.real) + (self.imag * self.imag)) ** 0.5

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "j"
