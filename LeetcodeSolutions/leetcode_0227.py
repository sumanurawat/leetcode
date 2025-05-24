class Evaluator:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.i = 0
    
    def skip_spaces(self):
        while self.i < self.n and self.s[self.i] == ' ':
            self.i += 1
    
    def read_number(self):
        self.skip_spaces()
        number = 0
        while self.i < self.n and self.s[self.i].isdigit():
            number = number * 10 + int(self.s[self.i])
            self.i += 1
        return number
    
    def read_operator(self):
        self.skip_spaces()
        if self.i < self.n and self.s[self.i] in '+-*/': 
            op = self.s[self.i]
            self.i += 1
            return op
        return None
        
    def evaluate(self):
        result = 0
        last_num = 0
        last_op = '+'

        while self.i < self.n:
            num = self.read_number()
            op = self.read_operator()
            if last_op == '+':
                result += last_num
                last_num = num
            if last_op == '-':
                result += last_num
                last_num = -num
            if last_op == '*':
                last_num *= num
            if last_op == '/':
                last_num = int(last_num / num)
            last_op = op
        return result + last_num
    
class Solution:
    def calculate(self, s: str) -> int:
        return Evaluator(s).evaluate()