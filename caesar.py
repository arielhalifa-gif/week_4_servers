class Caesar:
    @staticmethod
    def caesar_cipher_encryption(to_encript: str, hist: int = 2):
        alphabet =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        encripted = ""
        for word in to_encript:
            text = word.isalpha()
            if text:
                index1 = alphabet.index(word)
                to_hist_index = (index1 + hist) % len(alphabet)
                encripted += alphabet[to_hist_index]
            else:
                encripted += word
        return encripted

    @staticmethod
    def caesar_cipher_decryption(encripted: str, hist: int = 2):
        decripted = ""    
        alphabet =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for word in encripted:
            text = word.isalpha()
            if text:
                index1 = alphabet.index(word)
                to_hist_index = index1 - hist
                decripted += alphabet[to_hist_index]
            else:
                decripted += word
        return decripted