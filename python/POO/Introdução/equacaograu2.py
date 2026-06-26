class Equacao2Grau:

    def __init__(self, a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__delta =  self.__b ** 2 - 4 * self.__a * self.__c

    
    @property
    def raiz_1(self):
        if self.__delta > 0:
            return (-self.__b + self.__delta ** 0.5) / (2 * self.__a)
        
        elif self.__delta == 0:
            return (-self.__b + self.__delta ** 0.5) / (2 * self.__a)
        
        else:
            return f'a equacao nao possui a primeira raiz'
    
    @property
    def raiz_2(self):
        if self.__delta > 0:
            return (-self.__b - self.__delta ** 0.5) / (2 * self.__a)
        
        elif self.__delta == 0:
            return (-self.__b - self.__delta ** 0.5) / (2 * self.__a)
        
        else:
            return f'a equacao nao possui a segunda raiz'