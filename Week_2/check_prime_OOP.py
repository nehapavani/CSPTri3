class Test:
  def _init_(self, n):
    for i in range(2, n):
      
          if n % i == 0:
              print('not prime')
              break

          else:
              print('prime')
              break
          
def driver():
  n = int(input("Type a number: "))
  obj = Test()
  n = obj._init_(n)
  

if __name__ == "__main__":
    driver()