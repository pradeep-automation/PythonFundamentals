class CustomEx(Exception):

    def __init__(self, msg="This is custom error"):
        self.msg = msg
        super().__init__(self.msg)

    # @property
    # def msg(self):
    #     return self.__msg
    #
    # @msg.setter
    # def msg(self, value):
    #     self.__msg = value
    #
    #
    #
    #
