sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ")
hg = int(input("Anna hemoglobiiniarvosi (g/l): "))
if sukupuoli == "nainen":
    if hg < 117:
        print("Hemoglobiiniarvosi on alhainen..")
    elif hg > 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "mies":
    if hg < 134:
        print("Hemoglobiiniarvosi on alhainen..")
    elif hg <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virheellinen sukupuoli.")