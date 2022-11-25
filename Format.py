name = 'Kenia'
last_name = 'Valverde'
study = 'Python'

#Format

template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name + " y estudio " + study
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {} y estudio {}".format(name, last_name, study)
print('v2', template)


#la manera mas usada de formato en python
template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y estudio {study}"
print('v3', template)