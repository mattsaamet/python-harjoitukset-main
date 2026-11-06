def gallonat_litroiksi(gallonat):
    """Muuntaa Yhdysvaltain nestegallonat litroiksi."""
    litrakerroin = 3.78541
    return gallonat * litrakerroin

# Pääohjelma
def main():
    while True:
        
        syote = float(input("Syötä bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
        
        
        if syote < 0:
            print("Lopetetaan ohjelma.")
            break
            
        
        litrat = gallonat_litroiksi(syote)
        print(f"{syote} gallonaa on {litrat:.2f} litraa.\n")


if __name__ == "__main__":
    main()