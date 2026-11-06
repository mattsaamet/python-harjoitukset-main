import random
def main():
    koodi_3 = ""
    for i in range(3):
        koodi_3 += str(random.randint(0, 9))
    print(f"3-numeroinen koodi: {koodi_3}")

if __name__ == "__main__":
    main()
    koodi_4 = ""
    for i in range(4):
        koodi_4 += str(random.randint(0, 9))
    print(f"4-numeroinen koodi: {koodi_4}")