
f = open('c:/data/bobig/abc.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


f = open('c:/data/bobig/abc.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(lines[1])
for line in lines:
    print(line)
f.close()


with open('c:/data/bobig/abc.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)
