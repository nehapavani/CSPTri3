class Test:
  def _init_(self, word):
    if word == word[::-1]:
        print('its a palindrome')
    else:
        print('not a palindrome')

def driver():
  word = input("Type a Word: ")
  obj = Test()
  word = obj._init_(word)

if __name__ == "__main__":
    driver()