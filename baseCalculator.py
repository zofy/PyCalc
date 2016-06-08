import abc

class BaseCalculator(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def give_result(self):
		"Calculate the result"