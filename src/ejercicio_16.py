import time
def main():
    for minute in range(60):
        for second in range(60):
            print(f"{minute:02}:{second:02}")
            time.sleep(1)  
if __name__ == "__main__":
    main()