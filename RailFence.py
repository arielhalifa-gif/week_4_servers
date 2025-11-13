class RailFence:
    @classmethod
    def delete_spaces(cls, sentence: str):
        no_spaces = ""
        for letter in sentence:
            not_space = letter.isalpha()
            if not_space:
                no_spaces += letter
        return no_spaces

    @staticmethod
    def rail_fence_encryption(to_encript: str):
        without_spaces = RailFence.delete_spaces(to_encript)
        rail1 = ""
        rail2 = ""
        for i in range(len(without_spaces)):
            if i %2 == 0:
                rail1 += without_spaces[i]
            else:
                rail2 += without_spaces[i]
        return rail1 + rail2
    
    @staticmethod
    def rail_fence_decryption(encrypted: str):
        rail1 = encrypted[:(len(encrypted // 2)) + 1]
        rail2 = encrypted[(len(encrypted // 2)) + 1:]
        decrypted_word = ""
        for i in range(len(rail1)):
            decrypted_word += rail1[i]
            decrypted_word += rail2[i]
        return decrypted_word