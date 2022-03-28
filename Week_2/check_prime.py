def driver():
    n = int(input("Type a number: "))
    for i in range(2, n):
    
            if n % i == 0:
                print('not prime')
                break

            else:
                print('prime')
                break

if __name__ == "__main__":
    driver()