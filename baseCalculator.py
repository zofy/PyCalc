import abc, operator

class BaseCalculator(object):
	__metaclass__ = abc.ABCMeta

	ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div, '^': operator.pow}

	@abc.abstractmethod
	def calculate_equation(self):
		"Calculate the result"

	def __init__(self):
		self.actual_value, self.op = None, []
		self.result = 0

	@property
	def actual_value(self):
		return self._actual_value

	@actual_value.setter
	def actual_value(self, value):
		self._actual_value = value

	def calculate_operation(self, op, value):
		if self.actual_value is None:
			self.actual_value = value
			self.op = [op] + self.op
		else:
			if op == '=':
				self.op = self.op[-1] + self.op
			else:
				self.op = [op] + self.op
				print self.actual_value, value
				self.actual_value = self.ops[self.op.pop()](self.actual_value, value)

		return self.actual_value