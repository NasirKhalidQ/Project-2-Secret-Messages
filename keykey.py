from ciphers import Cipher


class Keyword(Cipher):
    """This is our class of Keyword Cipher. A keyword is used as a key,
    and it determines the letter matchings of the cipher alphabet to the
    plain alphabet. No alphabets are repeated and the keyword plus the
    remaining alphabets are stored in new_list. No alphabet is repeated and
    the keyword is appended to the list first and then the remaining
    alphabets from the letters list are appended in order.
    """
    # This creates a list of alphabets using the chr() function so that we
    # don't have to hard code the alphabets.
    letters_list = [chr(i) for i in range(65, 91)]

    def __init__(self):
        pass

    def encrypt(self, text):
        """This method to encrypt the text asks the user for the keyword
        which is to be used in the encryption process. This will match the
        index of each letter of the string with the letters list and then
        append the output using the new_list and this index.
        """
        keyword = input('What keyword would you like to use?')
        keyword = keyword.upper()
        new_list = []

        for e in keyword:  # This removes any duplicate alphabets from keyword.
            if e not in new_list:
                new_list.append(e)

        for i in self.letters_list:
            if i not in new_list:
                new_list.append(i)
                output = []
                text = text.upper()

        for char in text:
            try:
                index = self.letters_list.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(new_list[index])

        return ''.join(output)

    def decrypt(self, text):
        """In order to decrypt the message the same keyword will be needed
        which was used at the time of encryption.
        """
        new_list = []
        keyword = input('What keyword would you like to use?')
        keyword = keyword.upper()

        for e in keyword:
            if e not in new_list:
                new_list.append(e)

        for i in self.letters_list:
            if i not in new_list:
                new_list.append(i)

        output = []
        for char in text:
            try:
                index = new_list.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.letters_list[index])

        return ''.join(output)


