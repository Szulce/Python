
##Generowanie dokumentu PDF

ścieżka: Python\Docs\praca\pandoc


pandoc --pdf-engine=xelatex -f markdown-implicit_figures  --metadata bibliography=bibliography.bib --csl=style.csl --citeproc Magdalena_Szulc.md -o Magdalena_Szulc.pdf  --toc --listings  --top-level-division=chapter -V classoption=oneside -V fontsize=12pt
