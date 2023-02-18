class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class CoffeeTooColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature
        
    def drink_coffee(self):
        if self.__temperature > 85:
            #print('Coffee Too Hot')
            raise CoffeeTooHotException('Coffee Temperature:' + str(self.__temperature))
        elif self.__temperature < 65:
            #print('Coffee Too Cold')
            raise CoffeeTooColdException('Coffee Temperature:' + str(self.__temperature)) 
        else:
            print('Coffee ok to Drink')
            
            
cup = CoffeeCup(100)
cup.drink_coffee()
 