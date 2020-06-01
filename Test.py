import sys
import unittest
import CallbackManager
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

class Test(unittest.TestCase):

    def setUp(self):
        self.form = CallbackManager.CallBackManager()

    def test_initial(self):
        print('in test')
        #self.form.ui.pushButton_2.click()
        #self.form.ui.pushButton.click()
        #self.form.ui.pushButton_3.click()
        #self.assertEqual(self.form.callback_connectors[0].flag, True)

    def test_protocol_combo_box(self):
        print('in ptest')
        self.form.ui.ProtocolcomboBox.setAccessibleName('ASCII')
        QTest.mouseClick(self.form.ui.ProtocolcomboBox, Qt.LeftButton)
        QTest.keyClick(self.form.ui.ProtocolcomboBox, Qt.Key_Down, Qt.Key_Enter)
        #QTest.keySequence(self.form.ui.ProtocolcomboBox, [Qt.Key_Down, Qt.Key_Enter])
        self.assertEqual(self.form.callback_connectors[3].Protocol, 'ASCII')

app = QtWidgets.QApplication(sys.argv)
if __name__ == "__main__":
    unittest.main()