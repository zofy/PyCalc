import sys
import string
from PyQt4 import QtGui
from calculator import Calculator

class Eq_Input(QtGui.QTextEdit):
	allowed_chars = {ord(x) for x in string.digits + '+-/*.'}
	allowed_chars.add(16777219)

	def __init__(self, *args):
		QtGui.QTextEdit.__init__(self, *args)

	def keyPressEvent(self, event):
		if event.key() in self.allowed_chars:
			# print 'You clicked: ' + str(unichr(event.key()))
			QtGui.QTextEdit.keyPressEvent(self, event)
		else:
			event.ignore()

	def add_to_eq(self):
		b = self.sender()
		eq = self.toPlainText()
		if b.text() in ('+', '-', '*', '/'):
			self.setText(eq + ' ' + str(b.text()) + ' ')
		else:
			self.setText(eq + str(b.text()))

	def clear_eq(self):
		self.setText('')

	def calculate(self):
		eq = str(self.toPlainText())
		# print 'Eq: ' + eq
		c = Calculator(eq)
		result = c.give_result()
		# print result
		return result