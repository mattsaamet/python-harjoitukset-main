def laske_summa(lukulista):
    """Laskee ja palauttaa listassa olevien kokonaislukujen summan."""
    summa = 0
    for luku in lukulista:
        summa += luku
    return summa


def main():
    
    testilista = [5, 12, 3, 8, 21, 7]
    
   
    tulos = laske_summa(testilista)
    
    
    print(f"Testilista: {testilista}")
    print(f"Listan lukujen summa on: {tulos}")


if __name__ == "__main__":
    main()