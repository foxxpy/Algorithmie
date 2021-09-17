from fill import fill, fill_length, z_fill

print("Test de fill")
nombre = 3
nb_de_zeros = 2
print("nombre : {}, nb_de_zeros : {}, fill : {}".format(nombre, nb_de_zeros, fill(nombre, nb_de_zeros)))

nombre = 16
nb_de_zeros = 5
print("nombre : {}, nb_de_zeros : {}, fill : {}".format(nombre, nb_de_zeros, fill(nombre, nb_de_zeros)))

nombre = 111
nb_de_zeros = -5
print("nombre : {}, nb_de_zeros : {}, fill : {}".format(nombre, nb_de_zeros, fill(nombre, nb_de_zeros)))

print("\nTest de fill_length")
nombre = 3
length = 2
print("nombre : {}, length: {}, fill : {}".format(nombre, length, fill_length(nombre, length)))

nombre = 111
length = 3
print("nombre : {}, length: {}, fill : {}".format(nombre, length, fill_length(nombre, length)))

nombre = 1234
length = 3
print("nombre : {}, length: {}, fill : {}".format(nombre, length, fill_length(nombre, length)))

print("\n Test de z_fill")
nombre = 1
z = 3
print("nombre : {}, z: {}, fill : {}".format(nombre, z, z_fill(nombre, z)))

nombre = 123
z = 2
print("nombre : {}, z: {}, fill : {}".format(nombre, z, z_fill(nombre, z)))
