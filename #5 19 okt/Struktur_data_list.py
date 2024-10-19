# buah = ["apel", "pisang", "manga"]

# print(buah[0])
# print(buah[1])
# print(buah[2])

# buah[1] = ""
# print(buah)

buah = ["Apel", "Pisang", "Mangga"]
#penambahan ke list, lebih dari satu :
buah.extend(["Sirsak", "Kelapa", "Markisa"])
#penambahan ke list, satu doang :
buah.append("Alpukat")
#penambahan ke list, di urutan :
buah.insert(0, "Anggur")
#ngilangin hal di list, satu doang
buah.remove("Apel")
#ngilangin hal di list, pakai urutan
del buah[2]
buah[1] = "Jeruk"
print(buah)