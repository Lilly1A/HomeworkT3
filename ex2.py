"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera

"""
text=input(""" """)
lungime=len(text)
print(lungime)
vocale=text.count('a')+text.count('e')+text.count('i')+text.count('u')+text.count('o')
cifre=text.count('0')+text.count('1')+text.count('3')+text.count('4')+text.count('5')+text.count('6')+text.count('7')+text.count('8')+text.count('9')+text.count('0')

print(vocale)
print(lungime-vocale-text.count(' ')-cifre)