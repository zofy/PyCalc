import abc

class BasePizza(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_shape(self):
		'method to implement'

class Pizza(BasePizza):

	@classmethod
	def p(cls):
		print 'static'

	# def __init__(self):
		# print 'hhhh'

	# def get_shape(self):
		# print 'round'

# p = BasePizza()
# p.get_shape()

p2 = Pizza()
# p2.get_shape()

Pizza.p()