# your code goes here!
class Anagram:
    def __init__(self, base_word):
        self.base_word = base_word
    
    def mk_word_dict(self, word):
        word_dict = {}
        for c in word:
            if c in word_dict:
                word_dict[c] += 1
            else:
                word_dict[c] = 1
        return word_dict

    def match(self, word_list):
        base_word_dict = self.mk_word_dict(self.base_word)
        
        res = []
        for word in word_list:
            if self.mk_word_dict(word) == base_word_dict:
                res.append(word)
        
        return res
