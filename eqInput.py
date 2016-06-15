import sys
import string
from PyQt4 import QtGui, QtCore
from calculator import Calculator

class Eq_Input(QtGui.QTextEdit):
	operators = {ord(x): x for x in '+-*/^'}
	allowed_chars = {ord(x) for x in string.digits + '+-*/^.() '}
	allowed_chars.add(16777219)
	allowed_chars.add(16777234)
	allowed_chars.add(16777236)

	def __init__(self, *args, **kwargs):
		QtGui.QTextEdit.__init__(self, *args)
		self.mode = 'normal'
		self.calc = Calculator()
		self.addNumber = True

	@property
	def mode(self):
		return self._mode

	@mode.setter
	def mode(self, value):
		if value in ('normal', 'equation'):
			self._mode = value
		else:
			raise Exception('Mode does not exist!')

	def keyPressEvent(self, event):
		modifiers = QtGui.QApplication.keyboardModifiers()
		if modifiers == QtCore.Qt.ControlModifier and event.key() in (67, 86):
			QtGui.QTextEdit.keyPressEvent(self, event)
		if modifiers == QtCore.Qt.ShiftModifier and event.key() in (16777232, 16777233):
			QtGui.QTextEdit.keyPressEvent(self, event)
		# if user hits enter, result should be calculated
		if event.key() in (16777220, 16777221) and self.toPlainText() != '':
			if self.mode == 'normal':
				self.normal_addition('=', self.toPlainText())
			else:
				self.show_result()

		# print 'You clicked: ' + str(event.key())
		if event.key() in self.allowed_chars:
			if self.mode == 'normal' and event.key() in self.operators:
				self.normal_addition(self.operators[event.key()], self.toPlainText())
			elif self.mode == 'equation' or (self.mode == 'normal' and event.key() not in (ord('('), ord(')'), ord(' '))):
				QtGui.QTextEdit.keyPressEvent(self, event)
		else:
			event.ignore()

	def equation_addition(self, sender, eq):
		if sender in ('+', '-', '*', '/'):
			self.setText(eq + ' ' + str(sender) + ' ')
		else:
			self.setText(eq + str(sender))

	def normal_addition(self, sender, eq):
		if sender in ('+', '-', '*', '/', '='):
			if eq == '':
				result = self.calc.calculate_operation(str(sender), 0)
			else:
				result = self.calc.calculate_operation(str(sender), float(eq))
			self.setText(str(result))
			self.addNumber = False
		elif not self.addNumber:
			self.setText(str(sender))
			self.addNumber = True
		elif self.addNumber:
			self.setText(eq + str(sender))

	def add_to_eq(self):
		eq = self.toPlainText()
		if self.mode == 'normal':
			self.normal_addition(self.sender().text(), eq)
		elif self.mode == 'equation':
			self.equation_addition(self.sender().text(), eq)

	def clear_eq(self):
		self.setText('')
		self.calc.actual_value = None
		self.calc.clear_operators()

	def show_result(self):
		eq = str(self.toPlainText())
		if self.mode == 'equation':
			try:
				result = self.calc.calculate_equation(eq)
			except:
				print 'Invalid eqution'
			else:
				eq = self.toPlainText()
				self.setText(eq + ' = ' + str(result))
		elif self.mode == 'normal':
			self.normal_addition(self.sender().text(), eq)