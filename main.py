
#1-masala:

t1 = (34, 34, 66)
t2 = (12, 32, 15)

result = tuple(t1[i] * t2[i] for i in range(len(t1)))
print(result)

#2-masala:

t1 = (99, 67, 76, 40)
teskari = tuple(reversed(t1))
print(teskari)

#3-masala

tupl = ("nagap", 77, 98, "jigar", 97, True)
natija = ""

for i in tupl:
    if type(i) == str:
        natija += i

print(natija)

#4-masala:
t = (10, 3, 25, 7, 3)

eng_kichik = min(t)
eng_katta = max(t)

min_index = t.index(eng_kichik)
max_index = t.index(eng_katta)

print("Eng kichik:", eng_kichik, "indeksi:", min_index)
print("Eng katta:", eng_katta, "indeksi:", max_index)


