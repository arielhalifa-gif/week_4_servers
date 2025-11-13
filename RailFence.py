class RailFence:
    @classmethod
    def delete_spaces(sentence: str):
        no_spaces = ""
        for letter in sentence:
            not_space = letter.isalpha()
            if not_space:
                no_spaces += letter
        return no_spaces

    @staticmethod
    def rail_fence_encription(to_encript: str):
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
    def rail_fence_decription(encripted: str):
        rail1 = encripted[:(len(encripted // 2)) + 1]
        rail2 = encripted[(len(encripted // 2)) + 1:]
        decripted_word = ""
        for i in range(len(rail1)):
            decripted_word += rail1[i]
            decripted_word += rail2[i]
        return decripted_word