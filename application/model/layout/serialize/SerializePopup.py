from library.stigma.application import Popup


class SerializePopup(Popup):
    def __init__(self):
        super(SerializePopup, self).__init__()
        self.size_hint = (1, 1)