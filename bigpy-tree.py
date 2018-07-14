import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
    dirname = r'D:\Python3\Lib'
else:
    dirname = '/usr/lib/python'

allsizes = []
for(thisDir, subHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace:print('...',filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])