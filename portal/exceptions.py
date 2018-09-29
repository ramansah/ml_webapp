class ModelException(Exception):
    def __init__(self, message, *args):
        Exception.__init__(self, *args)
        self.message = message

    def get_message(self):
        return self.message
