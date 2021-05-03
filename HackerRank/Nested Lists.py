if __name__ == '__main__':
    sheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sheet.append([name,score])
        
sets = set()
for name, score in sheet:
    sets.add(score)
sets = list(sets)
sets.sort()
second_high = sets[1]

for name, score in sorted(sheet):
    if score == second_high:
        print(name)
