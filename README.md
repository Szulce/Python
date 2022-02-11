# Wymagania instalacji oraz uruchomienia

pip install --upgrade pip
pip install pytest coverage
pip install joblib

##Python
md dla kodu 
komenda instalacyjna 

komenda dla update 

##Biblioteki 
###
md dla kodu 
komenda instalacyjna 

komenda dla update 

##Generowanie dokumentu PDF

ścieżka: Python\Docs\praca\pandoc

pandoc --pdf-engine=xelatex  Magdalena_Szulc.md -o Magdalena_Szulc.pdf  --toc --listings   -V classoption=oneside  -V book --top-level-division=chapter

pandoc --pdf-engine=xelatex  Magdalena_Szulc.md -o Magdalena_Szulc.pdf  --toc --listings   -V classoption=oneside  -V book --top-level-division=chapter

pandoc --pdf-engine=xelatex  Magdalena_Szulc.md -o Magdalena_Szulc.pdf  --toc --listings   -V classoption=oneside  -V book

pandoc --pdf-engine=xelatex  Magdalena_Szulc.md -o Magdalena_Szulc.pdf  --toc --listings

pandoc --pdf-engine=xelatex  Magdalena_Szulc.md -o Magdalena_Szulc.pdf  --toc --listings --template=template.latex --top-level-division=chapter

pandoc --pdf-engine=xelatex  Magdalena_Szulc.md -o Magdalena_Szulc.pdf  --toc --listings  --top-level-division=chapter -V classoption=oneside