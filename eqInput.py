import sys
import string
from PyQt4 import QtGui, QtCore
from calculator import Calculator

class Eq_Input(QtGui.QTextEdit):
	allowed_chars = {ord(x) for x in string.digits + '+-/*.() '}
	allowed_chars.add(16777219)
	allowed_chars.add(16777234)
	allowed_chars.add(16777236)

	def __init__(self, *args, **kwargs):
		QtGui.QTextEdit.__init__(self, *args)
		self.mode = 'normal'

	@property
	def mode(self):
		return self._mode

	@mode.setter
	def mode(self, value):
		if value in ('normal', 'equation'):
			self._mode = value
		else:
			raise Exception('Mode does not exist!')

	def check_mode(func):
		def wraper(self, *args, **kwargs):
			if self.mode == 'equation':
				return func(self)
			elif self.mode == 'normal':
				return self.add_to_eq()
		return wraper

	def keyPressEvent(self, event):
		modifiers = QtGui.QApplication.keyboardModifiers()
		if modifiers == QtCore.Qt.ControlModifier and event.key() in (67, 86):
			QtGui.QTextEdit.keyPressEvent(self, event)
		if modifiers == QtCore.Qt.ShiftModifier and event.key() in (16777232, 16777233):
			QtGui.QTextEdit.keyPressEvent(self, event)
		# if user hits enter, result should be calculated
		if event.key() in (16777220, 16777221) and self.toPlainText() != '':
			self.calculate()

		# print 'You clicked: ' + str(event.key())
		if event.key() in self.allowed_chars:
			QtGui.QTextEdit.keyPressEvent(self, event)
		else:
			event.ignore()

	def add_to_eq(self):
		print self.mode
		b = self.sender()
		
		eq = self.toPlainText()
		if self.mode == 'equation' and b.text() in ('+', '-', '*', '/'):
			self.setText(eq + ' ' + str(b.text()) + ' ')
		elif self.mode == 'normal' and b.text() in ('+', '-', '*', '/', '='):
			result = Calculator.calculate_operation(eq, b.text())
			self.setText(str(result))
		else:
			self.setText(eq + str(b.text()))

	def clear_eq(self):
		self.setText('')

	@check_mode
	def calculate(self):
		eq = str(self.toPlainText())
		try:
			result = Calculator.give_result(eq)
		except:
			print 'Invalid eqution'
		else:
			eq = self.toPlainText()
			self.setText(eq + ' = ' + str(result))