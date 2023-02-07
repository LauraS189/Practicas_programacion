#Operaciones entre conjuntos
paises1 = {'col','bra','per', 'bol'}
paises2 = {'arg','chi','bol','bra'}

set_c =paises1.union(paises2)
print(set_c)

set_c = paises1.intersection(paises2)
print(set_c)

set_c = paises1.difference(paises2)
print(set_c)

set_c = paises1.symmetric_difference(paises2)
print(set_c)
print(paises1^paises2)

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set(countries.union(northAm).union(centralAm).union(southAm))

print(new_set)


