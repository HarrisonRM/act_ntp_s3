import time
def main():
    a, b = 1, 1
    while a <= 1000:
        print(a)
        a, b = b, a + b
        time.sleep(0.5)  
if __name__ == "__main__":
    main()
