ranking = ('Ruby', 'python', 'C','java','C#','javascript','C++','SQL','HTML','Scala')
tam = len(ranking)
print('As 10 primeiras Linguagens mais amadas são:')
for top10 in range(0, tam ,1):
  print(top10 + 1, '=', ranking[top10])
print('As 3 maiores',ranking[:3])
print('As 5 ultimos',ranking[-5:])
print(ranking[1],'esta na posição 2 ')





