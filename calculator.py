from baseCalculator import BaseCalculator
from rpn import Rpn

class Calculator(BaseCalculator):

	# def __init__(self, equation='0.0'):
		# self.equation = equation

	@staticmethod
	def refactor(equation):
		print equation
		output = ''
		for i, x in enumerate(equation):
			if x in ('+', '-'):
				if i == 0 or equation[i - 1] in ('+', '-') or equation[i + 1] == '(':
					output += x+'1*'
				else:
					output += x
			else:
				output += x
		return output

	@staticmethod
	def get_eq_list(equation):
		eq_list = []
		num = ''
		for x in equation:
			if x in ('+', '-', '*', '/', '^', '(', ')'):
				eq_list.append(num.strip())
				eq_list.append(x)
				num = ''
			else:
				num += x
		eq_list.append(num.strip())
		return [x for x in eq_list if x != '']

	@staticmethod
	def calculate_rpn(rpn_eq):
		stack = []
		ops = ('+', '-', '*', '/', '^')
		for x in rpn_eq:
			if x in ops:
				a = float(stack.pop())
				b = float(stack.pop())
				if x == '+':
					r = a + b
				elif x == '-':
					r = b - a
				elif x == '*':
					r = a * b
				elif x == '/':
					r = b / a
				elif x == '^':
					r = b**a
				stack.append(r)
			else:
				stack.append(x)
		return stack

	@classmethod
	def calculate_equation(cls, equation):
		eq_list = cls.get_eq_list(equation)
		rpn_eq_list = Rpn.to_postfix(eq_list)
		result = cls.calculate_rpn(rpn_eq_list)
		if len(result) != 1:
			print result
			raise Exception('Invalid input!')
		return result[0]


# s = '(1-1.2)   /  22 +2.222'
# s = '5+(6*2-2)*9+3^(7-1)'
s = '-(1+2)+((0)+-(2+-1)-(1)'
s = '(2+-1)--1'
print Calculator.refactor(s)
# print Calculator.get_eq_list(s)
# print Calculator.give_result(s)