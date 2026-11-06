import random

def heita_noppaa(tahkot):
    """Palauttaa satunnaisen nopan silmäluvun väliltä 1 - tahkot."""
    return random.randint(1, tahkot)
def main():
    nopan_koko = int(input("Kuinka monta tahkoa nopassa on? "))

    if nopan_koko < 1:
        print("Nopassa täytyy olla vähintään yksi tahko!")
        return

    heittojen_maara = 0

    while True:
        heitto = heita_noppaa(nopan_koko)
        heittojen_maara += 1
        print(f"Heitto {heittojen_maara}: Sait {heitto}.")

        if heitto == nopan_koko:
            print(f"Sait maksimisilmäluvun {nopan_koko}! Peli päättyy.")
            break

if __name__ == "__main__":
    main()                       