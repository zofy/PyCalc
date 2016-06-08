import sys
import string
from PyQt4 import QtGui, QtCore
from calculator import Calculator

class Eq_Input(QtGui.QTextEdit):
	allowed_chars = {ord(x) for x in string.digits + '+-/*. '}
	allowed_chars.add(16777219)
	allowed_chars.add(16777234)
	allowed_chars.add(16777236)

	def __init__(self, *args):
		QtGui.QTextEdit.__init__(self, *args)

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
		c = Calculator(eq)
		try:
			result = c.give_result()
		except:
			print 'Invalid eqution'
		else:
			eq = self.toPlainText()
			self.setText(eq + ' = ' + str(result))
