class fraction():
    def __init__(self,n,d=1):
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
    
    def __pow__(self, p):#TODO: Make this handle fractions as power value.
        return fraction(pow(self.n, p), pow(self.d, p))
    
    def __eq__(self, fr):
        return True if ((self.n==fr.n) and (self.d==fr.d)) else False 

    def __repr__(self):
        return 'fraction({0}, {1})'.format(self.n, self.d)
    
    def __str__(self):
        if self.n == self.d:
            return '{}'.format('1')
        elif self.d == 1:
            return '{}'.format(self.n)
        return '{0}/{1}'.format(self.n, self.d)
    
    # Returns True if one of the numerator or denominator are negative, but not both.
    def is_negative(self):
        if (self.n < 0) ^ (self.d < 0):
            return True
        return False
    
    #Reduces the fraction to its simplest form.
    def reduce(self):
        n = abs(self.n)
        d = abs(self.d)
        
        gap = min(max(n, d) - min(n, d), n, d)
        if gap == 0:
            n = 1
            d = 1
        else:
            for i in range(gap, 1):
                if n % gap == 0 and d % gap == 0:
                    n /= gap
                    d /= gap
        
        if self.is_negative():
            n = -n
        
        self.n = n
        self.d = d

