class Evaluator:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.i = 0
    
    def skip_spaces(self):
        # Move the index forward past any spaces
        while self.i < self.n and self.s[self.i] == ' ':
            self.i += 1

    def read_number(self):
        # Skip spaces and read a full integer (could be multiple digits)
        self.skip_spaces()
        number = 0
        while self.i < self.n and self.s[self.i].isdigit():
            number = number * 10 + int(self.s[self.i])
            self.i += 1
        return number

    def read_operator(self):
        # Skip spaces and read the next operator if present
        self.skip_spaces()
        if self.i < self.n and self.s[self.i] in '+-*/': 
            op = self.s[self.i]
            self.i += 1
            return op
        return None
        
    def evaluate(self):
        # result: accumulates the sum of all finalized numbers (not affected by * or / anymore)
        result = 0
        # last_num: holds the most recent number, which may be updated by * or /
        last_num = 0
        # last_op: the last operator seen (starts as '+')
        last_op = '+'

        # Main loop: process the string left to right
        while self.i < self.n:
            # Read the next number (skipping spaces)
            num = self.read_number()
            # Read the next operator (skipping spaces)
            op = self.read_operator()
            # Apply the previous operator to last_num and num
            if last_op == '+':
                # For +, add last_num to result and set last_num to num
                result += last_num
                last_num = num
            elif last_op == '-':
                # For -, add last_num to result and set last_num to -num
                result += last_num
                last_num = -num
            elif last_op == '*':
                # For *, update last_num by multiplying with num
                last_num *= num
            elif last_op == '/':
                # For /, update last_num by dividing by num (truncate toward zero)
                last_num = int(last_num / num)
            # Update last_op to the next operator (or None if end of string)
            last_op = op
        # Add the last pending number to the result
        return result + last_num

# ---
# Approach Overview:
# We scan the string from left to right, reading numbers and operators. For + and -, we add the previous number to the result and start a new one. For * and /, we update the last number in place (to handle precedence). At the end, we add the last pending number to the result. This approach uses only a few variables and no extra space.
#
# Time Complexity: O(n), where n is the length of the string s.
#   - Each character is processed at most once.
#   - All operations inside the loop are O(1).
# Space Complexity: O(1), only a few integer variables are used (no stack or recursion).
    
class Solution:
    def calculate(self, s: str) -> int:
        return Evaluator(s).evaluate()