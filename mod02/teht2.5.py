import math
def main():
    # Kysytään käyttäjältä keskiaikaiset mitat
    try:
        leiviskat = float(input("Anna leiviskät: "))
        naulat = float(input("Anna naulat: "))
        luodit = float(input("Anna luodit: "))
    except ValueError:
        print("Virhe: Syötä vain numeroita.")
        return

    # Muunnoskertoimet
    LUOTI_GRAMMOINA = 13.3
    NAULA_LUOTEINA = 32
    LEIVISKA_NAULOINA = 20

    # Lasketaan kokonaismassa grammoina
    kokonaisluodit = luodit + (naulat * NAULA_LUOTEINA) + (leiviskat * LEIVISKA_NAULOINA * NAULA_LUOTEINA)
    kokonaisgrammat = kokonaisluodit * LUOTI_GRAMMOINA

    # Erotetaan täydet kilogrammat ja jäljelle jäävät grammat
    kilogrammat = int(kokonaisgrammat // 1000)
    grammat = kokonaisgrammat % 1000

    # Tulostetaan tulos
    print("\nMassa nykyyksikköinä:")
    print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")

if __name__ == "__main__":
    main()
