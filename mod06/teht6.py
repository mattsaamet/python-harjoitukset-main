import math

def laske_yksikkohinta(halkaisija_cm, hinta_euro):
    """Laskee ja palauttaa pizzan neliöhinnan (e/m2)."""
   
    sade_m = (halkaisija_cm / 2) / 100
    
    
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    
   
    yksikkohinta = hinta_euro / pinta_ala_m2
    return yksikkohinta


def main():
    print("--- Pizza 1 ---")
    halkaisija1 = float(input("Syötä 1. pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä 1. pizzan hinta (€): "))
    
    print("\n--- Pizza 2 ---")
    halkaisija2 = float(input("Syötä 2. pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä 2. pizzan hinta (€): "))
    
    
    hinta_per_m2_pizza1 = laske_yksikkohinta(halkaisija1, hinta1)
    hinta_per_m2_pizza2 = laske_yksikkohinta(halkaisija2, hinta2)
    
   
    print(f"\nPizza 1 yksikköhinta: {hinta_per_m2_pizza1:.2f} €/m²")
    print(f"Pizza 2 yksikköhinta: {hinta_per_m2_pizza2:.2f} €/m²")
    
    
    if hinta_per_m2_pizza1 < hinta_per_m2_pizza2:
        print("\nPizza 1 antaa paremman vastineen rahalle!")
    elif hinta_per_m2_pizza2 < hinta_per_m2_pizza1:
        print("\nPizza 2 antaa paremman vastineen rahalle!")
    else:
        print("\nMolemmat pizzat antavat tismalleen saman vastineen rahalle!")


if __name__ == "__main__":
    main()