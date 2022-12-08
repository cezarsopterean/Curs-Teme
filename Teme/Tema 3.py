# 1.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# 2.
print(f'Do apare de {str(note_muzicale.count("do"))} ori')

# 3.
list_a = [3, 1, 0, 2]
list_b = [6, 5, 4]
list_c = list_a + list_b
print(list_c)
list_a.extend(list_b)
print(list_a)

# 4.
list_a.sort()
print(list_a)
list_a.pop(0)
print(list_a)

# 5.
if len(list_c) > 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# 6.
list_c.clear()
print(list_c)

# 7.
if len(list_c) > 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# 8.
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

# 9.
print(f'Ana a luat nota {dict1.get("Ana")}')
print(f'Gigel a luat nota {dict1.get("Gigel")}')
print(f'Dorel a luat nota {dict1.get("Dorel")}')

# 10.
dict1['Dorel'] = 6
print(f'Dorel a luat nota {dict1.get("Dorel")}')

# 11.
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# 12.
zile_sapt = {'luni',  'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# 13.
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor saptamanii')
else:
    print('Weekend nu este un subset al zilelor saptamanii')

# 14.
print(zile_sapt.difference(weekend))\

# 15.
print(weekend.intersection(zile_sapt))