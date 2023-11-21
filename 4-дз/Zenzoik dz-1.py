class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, message):
        encrypted = []
        alphabet = self.alphabet
        key = self.key
        alphabet_len = len(alphabet)
        key_len = len(key)

        for i in range(len(message)):
            char = message[i]
            if char in alphabet:
                char_index = alphabet.index(char)
                key_character = key[i % key_len]
                key_index = alphabet.index(key_character)
                new_index = (char_index + key_index) % alphabet_len
                encrypted.append(alphabet[new_index])
            else:
                encrypted.append(char)
        return ''.join(encrypted)

    def decode(self, message):
        decrypted = []
        key = self.key
        key_len = len(key)
        alphabet = self.alphabet

        for i in range(len(message)):
            char = message[i]
            if char in alphabet:
                char_index = alphabet.index(char)
                key_character = key[i % key_len]
                key_index = alphabet.index(key_character)
                new_index = (char_index - key_index) % len(alphabet)
                decrypted.append(alphabet[new_index])
            else:
                decrypted.append(char)
        return ''.join(decrypted)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

c = VigenereCipher(key, alphabet)
print(c.decode('rovwsoiv'))