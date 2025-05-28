import math

class Calc:
    def __init__(self, s):
        self.s = s
        self.i = 0

    def skip_spaces(self):
        while self.i < len(self.s) and self.s[self.i] == ' ':
            self.i += 1
    
    def read_op(self): # op can give ")"
        self.skip_spaces()
        if self.i < len(self.s):
            self.i += 1
            return self.s[self.i-1]
        return None

    def read_number(self):
        self.skip_spaces()
        number = 0
        while self.i < len(self.s) and self.s[self.i].isdigit():
            number *= 10
            number += int(self.s[self.i])
            self.i += 1
        return number 
    
    def evaluate(self):
        result = 0
        number = 0
        op = '+'

        next_number = 0
        next_op = None
        
        while self.i < len(self.s):
            if self.s[self.i] == ')':
                break
            elif self.s[self.i] == '(':
                self.i += 1
                next_number = self.evaluate()
            else: # it will be a number 
                next_number = self.read_number()
            next_op = self.read_op()

            if op == '+':
                result += number
                number = next_number
            elif op == '-':
                result += number
                number = -next_number
            elif op == '*':
                number = number * next_number
            elif op == '/':
                # Truncate toward zero
                number = int(number / next_number)
            
            if next_op is None or next_op == ')':
                break
            op = next_op
        
        return result + number
            
            
            
class Solution:

    def calculate(self, s: str) -> int:
        return Calc(s).evaluate()


