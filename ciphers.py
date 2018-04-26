class Cipher:
    """"This is the parent class Cipher from which all the other classes
    have inherited.
    """
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
