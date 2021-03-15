name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        sw = words[5:6]
        make_string = ''.join(sw)
        x = make_string.split(':',1)
        hours = x[:1]
        for word in hours:
            counts[word] = counts.get(word,0) +1

lst = list()
for key, value in counts.items():
    lst.append((key, value))
lst = sorted(lst)

for key,val in lst:
    print(key, val)
