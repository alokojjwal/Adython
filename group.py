import itertools
p=input()
result = ""
for k, group in itertools.groupby(p):
    result += '%d%s' % (len(list(group)),k)
print(result)