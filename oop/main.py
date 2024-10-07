from person import Person

p1 = Person('Arthur', 29)
print(f'p1_nome:{p1.nome}  p1_idade:{p1.idade}')

p2 = Person('Nani', 32)
print(f'p2_nome:{p2.nome} p2_idade:{p2.idade}')

p1.comer('Pastel')
p2.falar('Master Chef Brasil')
