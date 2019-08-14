import re
class StringIterator(object):
    def __init__(self, compressedString):
        self.values = re.split('[a-zA-Z]+', compressedString)[1:][::-1]        
        self.letter = re.split('[0-9]+', compressedString)[0:-1][::-1]
        print(self.letter)        
    
    def next(self):
        if self.hasNext():
            value = self.values.pop()
            letter = self.letter.pop()
            if int(value) > 1:
                self.values.append(str(int(value)-1))
                self.letter.append(letter)
            return letter
        raise StopIteration
    
    def hasNext(self):
        return not (len(self.values) == 0)
    
