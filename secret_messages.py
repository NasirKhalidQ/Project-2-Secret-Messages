from caesar import Caesar
from affine import Affine
from keykey import Keyword
from atbash import Atbash


def run_program():
    """This is a function which is called to run the program when
    secret_messages.py is run. It presents the user with a menu containing
    four options to choose from the Ciphers. After the Cipher is selected an
    object of the selected class is created by the name of our_class and the
    method of encrypt and decrypt is used on it. It asks the user for the
    message which they want to either encrypt or decrypt. It then displays the
    output as uppercase letters.
    """

    print('This is the secret messages project for the Treehouse Techdegree'
          '\n\n'
          'These are the current availabe ciphers:\n\n'
          '-Caesar \n'
          '-Atbash \n'
          '-Keyword \n'
          '-Affine \n\n\n'
          )

    response = input('Which cipher would you like to use?')
    response = response.lower()

    if response == 'keyword':
        our_class = Keyword()
    elif response == 'atbash':
        our_class = Atbash()
    elif response == 'caesar':
        our_class = Caesar()
    elif response == 'affine':
        our_class = Affine()

    text = input("That's an excellent cipher. What's the message?")
    action = input('Are we going to encrypt or decrypt?')

    if action == 'encrypt':
        print(our_class.encrypt(text))
    elif action == 'decrypt':
        print(our_class.decrypt(text))


if __name__ == '__main__':
    run_program()


