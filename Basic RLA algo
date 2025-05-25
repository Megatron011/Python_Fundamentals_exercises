sequence = [1, 1, 1, 2, 2, 3, 1, 1]
sequence1 =['a', 'a', 'b', 'b', 'b']

def rla(seq):
    compressed = []
    counter = 0
    current = seq[0]

    for i in seq:
        if i == current:
            counter +=1
        else:
            compressed.append((current, counter))
            current = i
            counter = 1

    compressed.append((current, counter))
    return compressed

a = rla(sequence)
b = rla(sequence1)
print(a)
print(b)
