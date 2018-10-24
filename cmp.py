sol = open('D:/virtualbox/shared/solu')
heur = open('D:/virtualbox/shared/heur')
solutions = sol.readlines()
heuristics = heur.readlines()

mean = 0
max = 0
cnt = 0
for i in range(len(solutions)):
    diff = (int(solutions[i]) - int(heuristics[i])) / int(solutions[i])
    mean = mean + diff
    if diff > max:
        max = diff
    if diff != 0:
        cnt = cnt + 1
mean = mean / 50
print('Mean relative difference: %s' % mean)
print('Maximum relative difference: %s' % max)
print('Count: %s' % cnt)
