print("De ingevoerde getallen zijn gelijk")
a = int(input("Vul het eerste getal in "))
b = int(input("Vul het tweede getal in "))

if a == b:
 result = True
else:
 result = False
 
print(result)

'''
Deze functie splitst de getallen middels een komma zodat ze niet als decimaal gezien worden. 
In de derde kolom wordt de invoer uit kolom 1 gechecked op de gelijkwaardigheid met een boolean als output.
En in de vierde kolom wordt gechecked of de booleans uit kolom twee en drie overeenkomen.
'''
print()
print("Testtabel:")
print()

def eqcheck(tabel):
    for rij, data in tabel.items():
        a_str, b_str = data['Invoer'].split(',')
        a = int(a_str)
        b = int(b_str)

        if a == b:
           result = True
        else:
           result = False
    
        data['Uitvoer'] = result
    
        if data['Uitvoer'] == data['Verwachte uitvoer']:
           data['Commentaar'] = 'Correct'
        else:
           data['Commentaar'] = 'Incorrect'
        
 
'''
Omdat een dictionary normaal gesproken alleen een key/value-pair heeft, 
heb ik een work-around gezocht om een tabel met meerdere kolommen te kunnen genereren.

'''
    
tabel = {
    'rij1': {'Invoer': '1,3', 'Verwachte uitvoer': False, 'Uitvoer': '', 'Commentaar': ''},
    'rij2': {'Invoer': '3,3', 'Verwachte uitvoer': True, 'Uitvoer': '', 'Commentaar': ''},
    'rij3': {'Invoer': '2,3', 'Verwachte uitvoer': False, 'Uitvoer': '', 'Commentaar': ''},
    'rij4': {'Invoer': '5,4', 'Verwachte uitvoer': False, 'Uitvoer': '', 'Commentaar': ''},
    'rij5': {'Invoer': '6,6', 'Verwachte uitvoer': False, 'Uitvoer': '', 'Commentaar': ''},
    'rij6': {'Invoer': '1,1', 'Verwachte uitvoer': True, 'Uitvoer': '', 'Commentaar': ''},
    'rij7': {'Invoer': '6,9', 'Verwachte uitvoer': False, 'Uitvoer': '', 'Commentaar': ''},
    'rij8': {'Invoer': '8,1', 'Verwachte uitvoer': False, 'Uitvoer': '', 'Commentaar': ''},
    'rij9': {'Invoer': '10,10', 'Verwachte uitvoer': True, 'Uitvoer': '', 'Commentaar': ''},
    'rij10': {'Invoer': '2,1', 'Verwachte uitvoer': False, 'Uitvoer': '', 'Commentaar': ''},
}

eqcheck(tabel)

for rij, info in tabel.items():
   invoer = info['Invoer']
   verwachte_uitvoer = info['Verwachte uitvoer']
   uitvoer = info['Uitvoer']
   commentaar = info['Commentaar']
   
   print(f"{rij}: Invoer : {invoer}, Verwachte uitvoer : {verwachte_uitvoer}, Uitvoer : {uitvoer}, Commentaar : {commentaar}")