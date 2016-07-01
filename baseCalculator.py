import abc, operator

class BaseCalculator(object):
	__metaclass__ = abc.ABCMeta

	ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div, '^': operator.pow}

	@abc.abstractmethod
	def calculate_equation(self):
		"Calculate the result"

	def __init__(self):
		self.actual_value, self.op = None, []

	@property
	def actual_value(self):
		return self._actual_value

	@actual_value.setter
	def actual_value(self, value):
		try:
			if value is not None:
				value = float(value)
		except:
			raise Exception('Value must be a number or None')
		else:
			self._actual_value = value

	def clear_operators(self):
		self.op = []

	def calculate_operation(self, op, value):
		if self.actual_value is None:
			if op == '=':
				return value
			self.actual_value = value
			self.op = [op] + self.op
		else:
			if op == '=':
				r, self.actual_value = self.actual_value, None
				if self.op == []:
					return r
				return self.ops[self.op.pop()](r, value)	
			self.op = [op] + self.op
			self.actual_value = self.ops[self.op.pop()](self.actual_value, value)

		return self.actual_value

	def calculate(self, op, num):
		self.operators = [op] + self.operators
		if self.nums == []:
			self.nums.append(num)
			self.res = num
		elif len(self.nums) == 1:
			self.res = self.ops[self.operators.pop()](self.nums[0], num)
			self.nums.pop()
			self.nums[0] = self.res			
		return self.res