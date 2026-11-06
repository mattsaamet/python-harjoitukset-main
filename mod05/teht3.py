luku = int(input("Syötä kokonaisluku: "))
if luku <= 1:
    on_alkuluku = False
else:
    on_alkuluku = True
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            on_alkuluku = False
            break

if on_alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")