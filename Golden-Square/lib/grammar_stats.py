class GrammarStats():
    def __init__(self):
        self.good = 0
        self.bad = 0
        pass

    def check(self, text):
        self.text = text
        if type(text) is str:
            if text[0].isupper() and text[-1] in ['.', '!', '?']:
                self.good += 1
                return True
            else:
                self.bad +=1
                return False
        else: 
            raise Exception("This is not a valid string")
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        pass

    def percentage_good(self):
        total = self.good + self.bad
        if total == 0:
            return 0
        else:
            return int(self.good / total * 100)
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass