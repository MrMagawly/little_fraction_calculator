class fraction():
    def __init__(self,n,d):
        self.n = n
        self.d = d
        self.reduce()

    def __add__(self, fr):
        return fraction(self.n * fr.d + fr.n * self.d, self.d * fr.d)
    
    def __sub__(self, fr):
		return fraction(self.n * fr.d - fr.n * self.d, self.d * fr.d)

    def __repr__(self):
        return 'fraction({0}, {1})'.format(self.n, self.d)

    def __str__(self):
        return '{0}/{1}'.format(self.n, self.d)

    def reduce(self):
        pass

