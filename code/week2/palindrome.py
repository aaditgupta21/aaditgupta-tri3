class palindrome():
    def __init__(self,string):
        self.string = string
    def __call__(self):
        testStr = self.string.lower()
        for x in [" ","!",]:
          testStr = testStr.replace(x,"")
        if testStr == testStr[::-1]:
            return True
        else:
            return False


def tester():
      pal = palindrome("mom")
      print("A man, a plan, a canal -- Panama!", pal())    
      pal2 = palindrome("hotdog")
      print("hotdog is a palindrome = ", pal2())
if __name__ == "__main__":
    tester()