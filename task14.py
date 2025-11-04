class Calculator:
    
       
    def divide(self, a, b):
        try:
            result = a / b
        except:
            return "Bo‘lishda xatolik"
        else:
            return result


calc = Calculator()

print(calc.divide(10, 2))   
print(calc.divide(10, 0))  