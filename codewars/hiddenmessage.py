class Investigator:
    def __init__(self):
        self.output = ''
        self.alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def postcard(self, text):
        for i,x in enumerate(text):
            if x.isupper() and i>0 and text[i-1] in self.alpha:
                self.output += x
            if x ==' ' and text[i-1] == ' ':
                self.output += x

    def hidden_message(self):
        return self.output