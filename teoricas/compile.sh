for i in $(seq 1 14); do 
  cd $(printf C%02d ${i});
  pdflatex $(printf C%02d.handout.tex ${i});
  pdflatex $(printf C%02d.slides.tex ${i});
  cd ..;
done
