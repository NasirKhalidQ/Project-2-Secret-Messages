import string
from ciphers import Cipher


class Caesar(Cipher):
    """This is our class for the Caesar Cipher. Two strings are created inside
    the class, FORWARD and BACKWARD. The FORWARD string contains all the
    alphabets from A to Z plus 4 extra alphabets from the start. The BACKWARD
    string contains all the alphabets from A to Z plus 4 extra alphabets
    from the end."""

    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
        """This method is used to encrypt the string provided by the user. A
        loop is used on the string to check each letter and match it with
        the FORWARD string to fetch the index of that letter where it occurs
        first in the FORWARD string. That index is stored in the variable
        index and the encrypted letter is appended to a list declared below
        as output.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        """This method is used to decrypt the string provided by the user. A
        loop is used on the string to check each letter and match it with
        the BACKWWARD string to fetch the index of that letter where it occurs
        first in the BACKWARD string. That index is stored in the variable
        index and the encrypted letter is appended to a list declared below
        as output.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)


