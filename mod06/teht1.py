import random

def heita_noppaa():
    return random.randint(1, 6)

def main():
    while True:
        heitto = heita_noppaa()
        print(f"Heitit: {heitto}")
        if heitto == 6:
            print("Sait kuutosen! Peli päättyy.")
            break

if __name__ == "__main__":
    main()        

     