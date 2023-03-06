class SnippedString():
    def make_snippet(self, string):
        self.string = string
        if len(self.string) > 5:
            mystring = self.string.split()[:5]
            newstring = " ".join(mystring)
            return f"{newstring} ..."
        else:
            return self.string


#string.split()[:5] first 5 words