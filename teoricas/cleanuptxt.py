import re

def cleanup(txt):
    txt = re.sub('<\\d-?>', '', txt)
    txt = txt.replace('[fragile]', '')
    txt = re.sub('(\r\n){3,}', '\n\n\n', txt)
    return txt

def cleanup_txt(filename):
    f = open(filename, 'r')
    txt = f.read()
    f.close()
    txt = cleanup(txt)
    f = open(filename, 'w')
    f.write(txt)
    f.close()

for filename in ["C%02d.txt" % i for i in range(1,14)]:
    cleanup_txt(filename)
