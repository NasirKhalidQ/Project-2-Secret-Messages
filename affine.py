from ciphers import Cipher


class Affine(Cipher):
    """This is our class of Affine Cipher. The general formula for this
    cipher is (ax +b) mod m where m is the total number of letters which is
    26, a is any number which is co prime with m, x is the index of the
    letter in the letter list which is being encrypted and b can be any
    number. In this program the values of a,b have been set to 3,5 but
    can be changed by the user when initializing. The variable encryption in
    the encrypt method holds the calculated answer after applying the formula.
    """
    letters_list = [chr(i) for i in range(65, 91)]

    def __init__(self, a=3, b=5, m=26, a_inverse=9):
        self.a = a
        self.b = b
        self.m = m
        self.a_inverse = a_inverse

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.letters_list.index(char)
                encryption = (((self.a*index)+self.b) % self.m)
            except ValueError:
                output.append(char)
            else:
                output.append(self.letters_list[encryption])
        return ''.join(output)

    def decrypt(self, text):
        """This is the method for decryption. The formula for decryption is
        (a_inverse*(x-b)) where a_inverse is the modular inverse of the
        number co prime with m. For this program the modular inverse has
        been calculated as 9 as has been set. The variable decryption holds
        the calculated answer after applying the formula.
        """
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.letters_list.index(char)
                decryption = ((self.a_inverse*(index-self.b)) % self.m)
            except ValueError:
                output.append(char)
            else:
                output.append(self.letters_list[decryption])
        return ''.join(output)

