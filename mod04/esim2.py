#Yksinkertainen toistorakenne

coffee = 5
coins_given = 0

while True:
    coins_given += 1
    print("Annettu", coins_given, "kolikkoa.")
    if coins_given == coffee:
        break
print("Kiitos näkemiin!")