def karsi_parittomat(lukulista):
    """Palauttaa uuden listan, jossa on vain alkuperäisen listan parilliset luvut."""
    parilliset = []
    for luku in lukulista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def main():
    
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    
    karsittu_lista = karsi_parittomat(alkuperainen_lista)
    
    
    print(f"Alkuperäinen lista: {alkuperainen_lista}")
    print(f"Karsittu lista (vain parilliset): {karsittu_lista}")


if __name__ == "__main__":
    main()