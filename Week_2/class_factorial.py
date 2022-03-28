def driver():
  class Test:
      def _init_(self, n):
          f = 1
          for i in range(1, n + 1):
              f = f * i
          return f
  
  
  n = int(input("Enter a number:"))
  
  obj = Test()
  f = obj._init_(n)
  print("Factorial is:", f)

if __name__ == "__main__":
    driver()