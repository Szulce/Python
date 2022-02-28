# Wymagania instalacji oraz uruchomienia

pip install --upgrade pip
pip install pytest coverage
pip install joblib
pip3 install auto-sklearn
pip install -U jsonpickle

Solution 3: time.clock replace with time.time
Just Find C:\Users\ssc\anaconda3\envs\.. this folder.
select compat.py file and Open.
search for time.clock in compat.py
Then replace time.clock with time.time
and save it.
Now your error should be solved.

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