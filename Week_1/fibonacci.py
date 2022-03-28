# Program to display the Fibonacci sequence up to n-th term
def driver():
  terms = int(input("How many terms? "))
  # first two terms
  n1, n2 = 0, 1
  count = 0
  if terms <= 0:
      print("Please enter a positive integer")
  # generate fibonacci sequence
  else:
    print("Fibonacci sequence for", terms, "number of terms:")
    while count < terms:
      print(n1)
      nth = n1 + n2
     # update values
      n1 = n2
      n2 = nth
      count += 1

if __name__ == "__main__":
    driver()
  





