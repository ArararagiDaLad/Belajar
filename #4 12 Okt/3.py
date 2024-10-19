# nilai = 80

# if nilai >= 80:
#     print("A")
# if nilai >= 75 <= 80:
#     print("B")
# if nilai >= 56 <= 75:
#     print("C")
# if nilai >= 45 <= 56:
#     print("D")
# if nilai <= 44:
#     print("E")

# nilai = [80, 75, 56, 45, 44,]

# for i in nilai:
#     if i >= 80:
#         grade = "A"
#     elif i >= 75:
#         grade = "B"
#     elif i >= 56:
#         grade = "C"
#     elif i >= 45:
#         grade = "D"
#     else:
#         grade = "E"
#     print(f"Nilai : {i}, Grade: {grade}")

nilai = int(input("Masukkan nilai Ujian : "))

if nilai >= 80:
    print("Anda mendapatkan A")
elif nilai >= 75:
    print("Anda mendapatkan B")
elif nilai >= 56:
    print("Anda mendapatkan C")
elif nilai >= 45:
    print("Anda mendapatkan D")
else:
    print("Anda tidak Lulus")