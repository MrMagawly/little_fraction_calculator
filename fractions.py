class fraction():
    def __init__(self,n,d):
        self.n = n
        self.d = d
        self.reduce()

    def __add__(self, fr):
        return fraction(self.n * fr.d + fr.n * self.d, self.d * fr.d)
    
    def __truediv__(self, fr):
        return fraction(self.n * fr.d, self.d * fr.n)
    
    def __sub__(self, fr):
        return fraction(self.n * fr.d - fr.n * self.d, self.d * fr.d)
    
    def __mul__(self, fr):
        return fraction(self.n * fr.n, self.d * fr.d)

    def __repr__(self):
        return 'fraction({0}, {1})'.format(self.n, self.d)

    def __str__(self):
        return '{0}/{1}'.format(self.n, self.d)
    
    #Reduces the numerator and denominator to their simplest numbers.
    def reduce(self):
        n = self.n
        d = self.d
        gap = min(max(n, d) - min(n, d), n, d)
        if gap == 0:
            n = 1
            d = 1
        else:
            for i in range(gap, 1):
                if n % gap == 0 and d % gap == 0:
                    n /= gap
                    d /= gap
        self.n = n
        self.d = d

