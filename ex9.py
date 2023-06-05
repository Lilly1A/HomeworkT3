"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""
text=input(""" """)
simb=".,?!"
text1=text.replace(simb, " ")

print(text1)