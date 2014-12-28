FILES = 13
COMPILE = True
WRITE = True

def create_file(index, kind, command):
    f = open("C%02d.%s.tex" % (index, kind), 'w')
    f.write("\\makeatletter\\let\\ifGm@compatii\\relax\\makeatother\n")
    f.write("\\documentclass[%s]{beamer}\n" % command)
    f.write("\\input{C%02d.tex}\n" % index)

def create_article_file(index):
    f = open("C%02d.%s.tex" % (index, 'article'), 'w')
    f.write("\\makeatletter\\let\\ifGm@compatii\\relax\\makeatother\n")
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{beamerarticle}\n")
    f.write("\\input{C%02d.tex}\n" % index)

for i in range(1,FILES+1):
    if WRITE:
        #create_file(i, 'handout', 'handout')
        #create_file(i, 'slides', '10pt')
        create_article_file(i)
    if COMPILE:
        import os
        #os.system('pdflatex C%02d.handout.tex' % i)
        #os.system('pdflatex C%02d.slides.tex' % i)
        os.system('pdflatex C%02d.article.tex' % i)
        
