elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

for i in range(len(elevi)):
    print(elevi[i], "are nota", note[i])

nota_max = note[0]
nota_min = note[0]
elev_max = elevi[0]
elev_min = elevi[0]

for i in range(len(note)):
    if note[i] > nota_max:
        nota_max = note[i]
        elev_max = elevi[i]
    if note[i] < nota_min:
        nota_min = note[i]
        elev_min = elevi[i]

print("Nota maximă este", nota_max, "și aparține elevei", elev_max)
print("Nota minimă este", nota_min, "și aparține elevului", elev_min)

suma = 0
for nota in note:
    suma += nota

media = suma / len(note)

print("Media notelor este:", round(media, 2))

print("Elevii cu nota >= 5 sunt:")

for i in range(len(elevi)):
    if note[i] >= 5:
        print(elevi[i])
for i in range(len(note)):
    note[i] = note[i] + 1

print("Notele după creștere:", note)

elev_nou = "Felix"
nota_elev_nou = 6

elevi.append(elev_nou)
note.append(nota_elev_nou)

print("Lista elevilor:", elevi)
print("Lista notelor:", note)

elev_de_sters = "Darius"

if elev_de_sters in elevi:
    pozitie = elevi.index(elev_de_sters)
    elevi.pop(pozitie)
    note.pop(pozitie)
    print(elev_de_sters, "a fost șters.")
else:
    print(elev_de_sters, "nu se află în listă.")

print("Lista elevilor:", elevi)
print("Lista notelor:", note)

print("Lista actualizată de elevi și note:")
for i in range(len(elevi)):
    print(elevi[i], "are nota", note[i])
interogari_nume = ["Ana", "Mara", "Elena", "stop"]

i = 0
while i < len(interogari_nume) and interogari_nume[i] != "stop":
    nume = interogari_nume[i]

    if nume in elevi:
        poz = elevi.index(nume)
        print(nume, "are nota", note[poz])
    else:
        print(nume, "nu există în listă.")

    i += 1

    numar_trecuti = 0
    numar_picati = 0

    for i in range(len(note)):
        if note[i] >= 5:
            numar_trecuti += 1
        else:
            numar_picati += 1

    print("Număr elevi cu nota ≥ 5:", numar_trecuti)
    print("Număr elevi cu nota < 5:", numar_picati)

note_trecute = []

for n in note:
    if n >= 5:
        note_trecute.append(n)

if len(note_trecute) > 0:
    media = sum(note_trecute) / len(note_trecute)
    print("Notele trecute:", note_trecute)
    print("Media notelor trecute este:", round(media, 2))
else:
    print("Nu există note ≥ 5.")
