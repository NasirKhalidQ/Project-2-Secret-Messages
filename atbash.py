import string
from ciphers import Cipher


class Atbash(Cipher):
    """This is our class of Atbash Cipher. The Atbash cipher is a particular
    type of monoalphabetic cipher formed by taking the alphabet and mapping
    it to its reverse, so that the first letter becomes the last letter,the
    second letter becomes the second to last letter, and so on. The FORWARD
    string contains all the alphabets in the regular order and the BACKWARD
    string contains all the alphabets in reversed order.
    """
    def __init__(self):
        self.FORWARD = string.ascii_uppercase
        self.BACKWARD = string.ascii_uppercase[::-1]

    def encrypt(self, text):
        """The encrypt method takes the string as input from the user and
        using a for loop checks each letter of the string with the FORWARD
        string and fetches the index in the FORWARD string. Then the letter
        is encrypted using BACKWARD string and the index calculated above.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index])
        return ''.join(output)

    def decrypt(self, text):
        """In the decrypt method the index is matched with the BACKWARD
        string and it is decrypted by appending the output using the FORWARD
        string and the calculated index."""
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index])
        return ''.join(output)


