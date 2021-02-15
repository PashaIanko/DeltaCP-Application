from PyQt5.QtWidgets import QMessageBox


class PopUpNotifier:

    def __init__(self):
        pass

    error_types = {
        'error': QMessageBox.Critical,
        'info': QMessageBox.Information,
        'warning': QMessageBox.Warning
    }

    @staticmethod
    def Notify(title, text, error_type='fail'):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setIcon(PopUpNotifier.error_types[error_type])
        msg_box.exec_()

    @staticmethod
    def Error(text):
        PopUpNotifier.Notify('Error', text, error_type='error')

    @staticmethod
    def Info(text):
       PopUpNotifier.Notify('Information', text, error_type='info')

    @staticmethod
    def Warning(text):
       PopUpNotifier.Notify('Warning', text, error_type='warning')

    @staticmethod
    def PresetSavingQUestion():
        msg_box = QMessageBox()
        return_val = msg_box.question(None, "Preset override", "You will re-write existing preset!\nAre you sure?", msg_box.Yes | msg_box.No)
        if return_val == msg_box.Yes:
            return True
        else:
            return False

