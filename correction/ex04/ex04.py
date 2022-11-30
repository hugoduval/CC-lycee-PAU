cadeaux = ["bleu", "rouge", "vert", "jaune", "jaune", "rouge", "rouge", "rouge", "bleu", "bleu", "rouge", "bleu", "rouge", "vert", "bleu","bleu", "vert", "vert", "jaune", "rouge", "jaune", "rouge", "jaune", "rouge", "rouge", "rouge", "vert", "vert", "vert"]
bleu = []
rouge = []
jaune = []
vert = []

for i in cadeaux:
    if i == "bleu":
        bleu.append(i)
    if i == "rouge":
        rouge.append(i)
    if i == "vert":
        vert.append(i)
    if i == "jaune":
        jaune.append(i)

print(bleu)
print(rouge)
print(jaune)
print(vert)