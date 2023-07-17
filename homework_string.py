# Bидалити [bdd] , всі інші зробити upper, записати в 1 строчку
str = '[bdd] Check the motion'


fixed_str = str.replace('[bdd] ', '').upper().replace('\n', '')
print(fixed_str)
