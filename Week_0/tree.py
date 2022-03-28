
# Function to print("Tree Pattern")


def driver():
  n = int(input('Enter the number of * in last line. Must be an odd number: '))

  for i in range(1, n+1, 2):
    print(int((n-i)/2) * ' ' + i * '*' + int((n-i)/2) * ' ')

  print(' ***  ')
  print(' ***  ')

if __name__ == "__main__":
    driver()