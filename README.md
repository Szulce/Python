# Instalation 

pip install --upgrade pip
pip3 install -r requirements.txt

# Run
apply run according to :

-Run_Learning_Proces.XML
-Run_Web_Application.XML

##Generowanie dokumentu PDF

ścieżka: Python\Docs\praca\pandoc

pandoc --pdf-engine=xelatex  Magdalena_Szulc.md -o Magdalena_Szulc.pdf  --toc --listings  --top-level-division=chapter -V classoption=oneside