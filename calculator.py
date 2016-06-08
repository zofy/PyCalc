import re

class Calculator(object):

	def __init__(self, equation='0.0'):
		self.equation = equation

	def get_chars(self):
		nums = []
		ops = []
		num = ''
		for x in self.equation:
			if x in ('+', '-', '*', '/'):
				ops.append(x)
				nums.append(float(num.strip()))
				num = ''
			else:
				num += x
		nums.append(float(num.strip()))
		return nums, ops

	def get_chars2(self):
		nums = re.split('\s*[+-/]\s*', self.equation)
		ops = re.findall('[+-/*]', self.equation)
		return nums, ops
		# nums = [float(x) for x in self.equation.split() if x not in ('+', '-', '/', '*')]
		# ops = [x for x in self.equation.split() if x in ('+', '-', '/', '*')]
		# return nums, ops

	def md(self, nums, ops):
		idx = 0
		result_list = []
		result = None
		while idx < len(ops):
			while idx < len(ops) and ops[idx] in ('/', '*'):
				if result is None:
					result = nums[idx]
				if ops[idx] == '/':
					result = result / nums[idx + 1]
				elif ops[idx] == '*':
					result *= nums[idx + 1]
				idx += 1
			if result is not None:
				result_list.append(result)
			result = None
			idx += 1
		return result_list

	def create_equation(self, nums, ops, res):
		new_nums = []
		i = 0
		j = 0
		while i < len(ops):
			if ops[i] in ('+', '-'):
				new_nums.append(nums[i])
			else:
				new_nums.append(res[j])
				j += 1
				while i < len(ops) and ops[i] in ('/', '*'):
					i += 1
			i += 1
		if ops[-1] in ('+', '-'):
			new_nums.append(nums[-1])
		new_ops = [op for op in ops if op in ('+', '-')]

		return new_nums, new_ops

	def calculate_equation(self, new_nums, new_ops):
		result = new_nums[0]
		for i, op in enumerate(new_ops):
			if op == '+':
				result += new_nums[i + 1]
			elif op == '-':
				result -= new_nums[i + 1]
		return result

	def give_result(self):
		if self.equation == '':
			return 0.0
		nums, ops = self.get_chars()
		res = self.md(nums, ops)
		new_nums, new_ops = self.create_equation(nums, ops, res)
		return self.calculate_equation(new_nums, new_ops)


# s = '1-1.2   /  22 +2.222'
# c = Calculator(s)
# print c.get_chars()
# print c.give_result()