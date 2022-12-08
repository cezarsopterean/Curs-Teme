# 1.

string=input('Introduce sting impar: ')
print(string[len(string)//2])
print('---------------------------------------')

# 2.

word1='civic'
word2='altceva'
assert word1 == word1[::-1], 'Cuvantul nu este polindrom'; print('Cuvantul este polindrom')
assert word2 == word2[::-1], 'Cuvantul nu este polindrom'; print('Cuvantul este polindrom')
print('---------------------------------------')

# 3.

string=input('String ales: '); primul=string[0:string.find(' ')]; al_doilea=string[(string.find(' ')+1):len(string)]; print(primul); print(al_doilea)
print('---------------------------------------')

# 4.

text = input('String: ')
a = text[0]
replace = text.replace(a, a.upper())
rez = replace[0].lower() + replace[1:len(text) - 1] + replace[-1].lower()
print(rez)
print('---------------------------------------')

# 5.
user=input('User: ')
password=input('Password: ')
password_safe='*'*len(password)
print(f'Parola pentru {user} este {password_safe} si are {len(password)} caractere')