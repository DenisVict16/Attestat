#Древнеримский калькулятор
class RimNumber:

   def rim_to_arab(self, number): # s = 'I ,II ,III'    def roman_to_arabic(roman):
       integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
       result = 0
       for i, c in enumerate(number):
           if i+1<len(number) and integers[number[i]] < integers[number[i+1]]:
              result-=integers[number[i]]
           else:
              result+=integers[number[i]]
       return(result)

   def arab_to_rim(self, num):   # s = '1 ,2 ,3'
        all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        # на старте в римском числе ничего нет
        roman = ''
        # пока наше число больше нуля
        while num > 0:
            # перебираем все пары из словаря
            for i, r in all_roman:
                # пока наше число больше или равно числу из словаря
                while num >= i:
                    # добавляем соответствующую букву в римское число
                     roman += r
                    # вычитаем словарное число из нашего числа
                     num -= i
        # как все циклы закончились — возвращаем римское число
        return(int(roman))

class Calculate:
   def __init__(self):
       pass

   def calculate(self, s): # s= '1 + 2'
      num1, operation, num2 = s.split(',') # ['1','+','2']
      match operation:
          case '+':
              return f'{num1} + {num2} = {num1 + num2}'
          case '-':
              return f'{num1} - {num2} = {num1 - num2}'
          case '*':
              return f'{num1} * {num2} = {num1 * num2}'
          case '/':
              return f'{num1} / {num2} = {num1 / num2}'

class AdapterCalculate:
    def __init__(self, s):  # I + II
        self.s = s
        self.rimnumber = Rimnumber

    def calculate(self, s): # I + II
        num1, operation, num2 = s.split()
        num1 = self.rimnumber.rim_to_arab(num1)
        num2 = self.rimnumber.rim_to_arab(num2)
        s = f'{str(num1)} + {str(num2)}'
        return self.obj.calculate(s)


if __name__ == '__main__':
    print('Калькулятор')
    print("Меню программы")
    print('1.Перевод чисел из римских в арабские:')
    print('2.Перевод чисел из арабских в римские:')
    print('3.Вычисление выражения:')
    print('4.Выход:')
    rim = RimNumber()
    while True:
        menu = input('Выберете пункт меню')
        match menu:
            case '1':
                s = input('Введите римские числа через запятую')
                sp = s.split(',')
                for el in sp:
                    print(f'{el} -> {rim.rim_to_arab(el)}')
            case '2':
                s = input('Введите арабские числа через запятую')
                sp = s.split(',')
                for el in sp:
                    print(f'{el} -> {rim.arab_to_rim(el)}')
            case '3':
                s = input('Введите выражение по типу: num1, operation, num2')
                l = input (str('rimskie или arabskie?'))
                if l == 'rimskie':
                   print(f'{AdapterCalculate.calculate(s)}')
                else:
                    print(f'{Calculate.calculate(s)}')
            case '4':
                break
            case _: #дефолтный вариант
                print('Неверный пункт меню')
