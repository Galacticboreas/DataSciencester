from string import ascii_letters


class Person:

    S_EN = 'absdefghijklmnopqrstuvwxyz-'
    S_EN_UPPER = S_EN.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight
    
    @property
    def fio(self):
        return self.__fio
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old
    
    @property
    def passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, w):
        self.verify_weight(w)
        self.__weight = w

    
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("Full name should be a string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Invalid format of the full name record")
        letters = ascii_letters + cls.S_EN + cls.S_EN_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("The full name must have at least one character")
            if len(s.strip(letters)) != 0:
                raise TypeError("Only alphabetic characters and hyphens can be used in the full name")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("The age must be an integer in the range [14; 120]")
    
    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("The weight must be a real number from 20 and above")
    
    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("The passport must be a string")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Invalid passport format")
        
        for p in s:
            if not p.isdigit():
                raise TypeError("The passport series and number must be numbers")
    


p = Person("Galatov Jeyson Milanovich", 45, '1234 567890', 80.0)
print(p.__dict__)
p.old = 100
p.passport = '4567 123456'
p.weight = 70.0

print(p.__dict__)
