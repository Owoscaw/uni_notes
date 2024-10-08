import sys
programChars = {}
for line in open(sys.argv[0] ,'r'):
    for i in line[:-1]:
        try:
            programChars[i] += 1
        except KeyError:
            programChars[i] = 1

for char in sorted(programChars.keys()):
    print("{}: {}".format(char, programChars[char]))
