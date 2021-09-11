crossaint = 0.39
stokbrood = 2.78
kortingsbon = 1.50
hoeveelheid = 17
aantal = 2
factuurtekst = 'de feestlunch kost bij de bakker ' + str((hoeveelheid) * (crossaint) + (aantal) * (stokbrood) - (kortingsbon)) + ' euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!'

print(factuurtekst)
