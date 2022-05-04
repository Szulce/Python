\usepackage{ulem}---
title: "Wykrywanie występowanie chorób serca,porównanie algorytów uczenia maszynowego nadzorowanego na podstawie zbioru danych dotyczących chorób układu krążenia z repozytorium  UCI"
author: [Magdalena Szulc]
header: UNIWERSYSTET MIKOŁAJA KOPERNIKA WYDZIAŁ MATEMATYKI I INFORMATYKI
date: "Toruń,2022-05-01"
footer: Praca inż. napisana pod kierunkiem dr Piotr Przymus
geometry: "left=1.5cm,right=1.5cm,top=2cm,bottom=2cm"
output: pdf_document
titlepage: true
titlepage-background: "`titlepage1.pdf`{=latex}"
book: true
titlepage-logo: "`img/umkLogo.png`{=latex}"
logo-width: 30mm
bibliography: true
disable-header-and-footer: true
toc-own-page: true
...

**Abstrakt**{.unnumbered}
========

The aim of the work is to compare selected algorithms of supervised machine learning and build a model based on medical
data, which diagnoses the presence or absence of cardiovascular disorders.

Medical data is distinguished by the fact that it is difficult to access, in most cases it is restricted information not
 available for public use. Therefore, a key step is to choose the features taken into account when creating the
model. The data obtained from the UCI repository has already undergone pre-processing. The dataset itself, due
to its small size, allows checking effects of algorithms without getting rid of redundant and insignificant
features.

The main motive is to answer the question of how data deficiency strongly influences the outcome and whether there is a
difference between the use of selected supervised learning algorithms requires a comparison of the difficulty level of creating a
model, accuracy, complexity and time to obtain an answer.


**Wykrywanie występowanie chorób serca,porównanie algorytów uczenia maszynowego nadzorowanego na podstawie zbioru danych dotyczących chorób układu krążenia z repozytorium UCI**{.unnumbered}
========


**Wstęp**{.unnumbered}
========

Sztuczna inteligencja wśród szerokiego zakresu swoich zastosowań może zostać wykorzytana do analizy bardziej lub mniej
złożonych danych medycznych, w celu przewidzenia wystąpienia choroby u konkretnej osoby, bez udziału procesu myślowego
od stony specjalisty.

Do tego przeznaczenia istnieje możliwość zastosowania uczenia nadzorowanego (ang. _supervised learning_) tj. rodzaj
uczenia maszynowego zakładający istnienie zbioru danych testowych zawierających odpowiedzi, na których podstawie wyszukiwane
są zależności, cechy znaczące oraz budowany jest w ten sposób model służący przykładowo do przewidywania przyszłych wartości.

W przypadku danych dotyczących chorób zależności typujące występowanie choroby, bazują na podstawie konkretnych wyników
badań zgormadzonych w repozytorium UCI.

W dzisiejszych czasach choroby sercowo-naczyniowe stanowią najczęstszą przyczynę zgonów, a liczba osób cierpiących na te
dolegliwości stale rośnie. Głównymi przyczynami zachorowalności diagnozowanymi przez specjalistów są niski poziom
świadomości i profilaktyki chorób serca.Dlatego prowadzone są intensywne prace nad zwiększeniem dostępności badań, które wspomogą diagnostykę kardiologiczną na
jak najwcześniejszym etapie [@1].

Powodem szukania dokładniejszych sposobów diagnozowania są również wysokie koszty leczenia generowane przez choroby
układu krwionośnego. Według analityków firmy konsultingowej KPMG [@KPMG] w 2011 r. koszty diagnostyki i terapii chorób
serca wyniosły ponad 15 miliardów polskich złotych.

Uczenie maszynowe poprzez przetwarzanie dużych zasobów klinicznych danych historycznych pod kątem zależności przyczynowo skutkowych, 
 może zostać wykorzystane do wczesnej diagnostyki lub wspomagania leczenia pacjentów [@2].

Słowa kluczowe: uczenie maszynowe, uczenie nadzorowane, lasy losowe, maszyna wektorów nośnych, k-najbliższych sąsiadów

**Cel i zakres pracy**{.unnumbered}
========

Celem pracy jest porównanie wybranych algorytmów uczenia maszynowego nadzorowanego, przy założeniu że dane wejściowe są
wybrakowane, a w rezultacie zbudowanie modelu który na podstawie danych medycznych wystawia diagnozę o występowaniu
zaburzeń sercowo-naczyniowych lub ich braku.

Dane medyczne wyróżniają się tym, że trudno uzyskać do nich dostęp, najczęściej nie są to informacje, które się
udostępnia do użytku publicznego, z tego powodu, kluczowym krokiem jest wybór cech branych pod uwagę przy tworzeniu
modelu. Dane pozyskane z repozytorium UCI przeszły już wstepną obróbkę , sam dataset ze względu na swoje niewielkie
rozmiary pozwala na sprawdzenie działań algorytmów bez pozbywania się nadmiarowych i mało znaczących cech.

Zatem odpowiedź na pytanie jak wybrakowanie danych mocno wpływa na rezultat i czy istnieją róznicę między zastosowaniem
wybranych algorytmów nauczania nadzorowanego wymaga przedstawienia porówniania łatwości tworzenia modelu, dokładności,
złożoności oraz czasu uzyskania odpowiedzi.

W pracy opisano następujące algorytmu uczenia nadzorowanego:

- losowe lasy decyzyjne (ang. _random_ _decision_ _forests_)
- maszyna wektorów nośnych (ang. _support vector machines_, SVM)
- k-najbliższych sąsiadów (ang. _k-neares neighbours_, KNN)

**Wprowadzenie teorertyczne**
========

**Uczenie maszynowe** (ang. _machine learning_, ML) to dziedzina zajmująca się tworzeniem modeli do analizy bardzo obszernych zasobów danch. Modele utworzone za pomocą algorytmów uczenia maszynowego są w stanie z wysokim prawdopodobieństwem wystawić predyckję lub dokonać klasyfikacji na temat zadanego problemu. 

Model _klasyfikacjny_ służy do przewidzenia etykiety klasy poprzez mapowanie na już z góry ustalony jednowymiarowy pozdział, model _regresywny_ natomiast mapuje przestrzeń ustalając liczbę klas podziału oraz grupując wartości. [@clsvsreg] Istnieje możliwość przeksztaucenia problemu regresywnego na klasyfikacyje i na odwrót poprzez zamiane wartości oczekiwanego wyniku. Taką modyfikację zastosowano w praktycznej częsci projektu. Wyniki dla danych występowały w wartościach od 0 do 4 , dla wartości <1,4> przypadek testowy uznawany był za sklasyfikowany pozytywny (chory), dlatego przeksztaucenie z modelu regresywnego do modelu klasyfikacyjnego polega na konwersji wyników do wartości liczbowych 0 - brak stwierdzenia stanu choroboweo oraz 1 - stwierdzenie o chorobie układu krążenia. 

Sposób wykorzystania segreguje alorytmy uczenia maszynowego na dwie kategorie, jednak powszechnie stosowanym podziałem jest podział zależnie od
sposobu _trenowania_ algorytmu. Algorytmy dzieli się na min.: uczenie nadzorowane, uczenie częściowo nadzorowane, uczenie bez nadzoru oraz uczenie przez
wzmacnianie [@3] .

![Schemat 1](img/1algorithms_category.png "Algorytmy z podziałem na kategorie"){ width=100% }

Dobór typu uczenia oraz algorytmu uzależniony jest od danych wejściowych oraz oczekiwanego rezultatu. Dane wyjściowe
mogą przyjmować format odpowiedzi TAK/NIE , klasyfikacji do danego zbioru czy np procentowej oceny ryzyka.


**Uczenie maszynowe nadzorowane** (ang. _supervised learning_) to klasa algorytmów uczenia maszynowego, która bazuje na
poetykietowanych danych. Nadzór polega na porównaniu rezultatów działania modelu z wynikami które są zawarte w danych wejściowych ( _dane oznaczone_ ) [@learning].
Algorytm po osiągnięciu żądanej efektywnosci jest w stanie dokonać klasyfikacji przykładu dla którego nie posiada
odpowiedzi. Sprawdza się to obecnie w rekomendacji produktów oraz diagnozie chorób. Z matematycznego puntu widzenia
dopasowanie danych oznaczonych nazywane jest aproksymacją funkcji [@3] .

**Uczenie maszynowe bez nadzoru** (ang. _unsupervised learning_) to klasa algroytmów uczenia maszynowego która wiodąco
rozwiązuje problemy grupowania. Dane dostarczane do modelu nie zawierają _oznaczeń_, zatem nauczanie polega na
wyciąganiu konkluzji z poprzednio wykonanych iteracji. Na skuteczność modeli budownych w oparciu o uczenie bez nadzoru
wpływ ma rozmiar dostarczonego do nauki zbioru danch, im jest on większy tym bardziej wzrasta effektywność. Takie zbiory
można uzyskać rejestrując dane na bierząco dlatego do najczęstrzych zastosowań tej klasy algorytmów, można zaliczyć
rozpoznawanie mowy czy obrazu [@3] .

**Uczenie maszynowe przez wzmacnianie** (ang. _reinforcement learning_) to klasa algorytmów uczenia maszynowego której nauczanie nie opiera się
na danych wejściowych czy wyjściowych a rezultatach otrzymanych podczas testu nazywanych tzw. sygnałami wzmocnienia który może przyjmować wartość pozytwną lub negatywną.
Algorytm generując dane wejściowe dostosowuje reguły by uzyskać zwrotnie sygnał pozytywny w jak największej liczbie przypadków. [@reinfor-learning] .


**Uczenie częściowo nadzorowane** (ang. _semi-supervised_ _learning_) to klasa algorytmów uczenia maszynowego która wykorzystuje zbór danych w większości niepoetykietowany na podstawie których tworzony jest model [@semi-learning] .

Podział osób na kategorie cierpiące na choroby sercowo-naczyniwe oraz zdrowe, to dylemat klasyfikayjny nadający się do
rozwiązania za pomoca algorytmów uczenia maszynowego nadzorowanego i na nich skupia się dalsza część pracy.

## Ścieżka działania algorytmów uczenia maszynowego nadzorowanego

![Schemat 2](img/7podstawowy_schemat_blokowy_uczenia_maszynowego.png "Podstawowy schemat blokowy uczenia maszynowego"){ width=70% }

## Model Danych

![Schemat 3](img/12UCI.png "UCI logo"){ width=50% } [@UCI]

### Repozytorium uczenia maszynowego UCI

Sensem wykorzystania uczenia maszynowego jest prognoza lub klasyfikacja rzeczywistych wartości z dużego zbioru danych
które mogą znaleść zastosowanie w praktycznych dziedzinach. Im bardziej dokładne i rzeczywiste dane do testowania i
tworzenia modelu tym większe prawdopodobieństwo otrzymania realnych wyników na końcu ścieżki uczenia. W celu
gromadzenia miarodajnej bazy dostępnych zbiorów danych testowych powstało repozytorium uczenia maszynowego UCI. Jak podaje
strona informacyjna :

> ... było ono cytowane ponad 1000 razy, co czyni je
> jednym ze 100 najczęściej cytowanych „artykułów” w całej informatyce ... [@UCI]

Repozytorium gromadzi dane z wielu rozbieżnych dziedzin , dane medyczne umieszczone w repozytorium nie zawierają
wrażliwych danych pacjentów , a niektóre zbiory są poddane już wstępnej obróbce tak jak zbiór danych
"Heart Disease Databases" wykorzystany w tym dokumencie, który powstał na podstawie realnych danych medycznych zebrany z
lokalizacji

1. Fundacja Cleveland Clinic [@5]
2. Węgierski Instytut Kardiologii, Budapeszt  [@hungary]
3. V.A. Centrum medyczne, Long Beach, Kalifornia  [@5]
4. Szpital Uniwersytecki, Zurych, Szwajcaria  [@switzerland].

#### Stratyfikacja

Wyróżniono 14 atrybutów spośród 76 zebrancyh do wykorzystania w algorytmach uczenia maszynowego, wszystkie z nich mają
wartośi liczbowe.

![Schemat 22](img/22corelation1.png "corelation"){ width=50% } ![Schemat 23](img/23corelation2.png "corelation"){ width=50% } 

Rozkład chorób serca w danych testowych to 44.67% chorych czyli 509 prób pozytywnych oraz  411 negatywnych.
W danych testowych znajduje się 726 przypadków osób płci męskiej oraz 194 żeńskiej. Dla zachorowań widać nierówność ale jest ona spowodowana rzeczywistą statystyką.
Tylko u 25.77% badanych kobiet stwierdzono występowanie chorób wieńcowych, natomiast wśród badanych mężczyzn jest to aż 63.22%. [@UCI]


Lista atrybutów wykorzystanych w algorytmie:

- wiek
- płeć
- rodzaj bólu w klatce piersiowej
- spoczynkowe ciśnienie krwi
- cholesterol w surowicy w mg/dl
- poziom cukru we krwi na czczo > 120 mg/dl
- spoczynkowe wyniki elektrokardiograficzne
- osiągnięto maksymalne tętno
- dławica piersiowa wywołana wysiłkiem fizycznym
- obniżenie odcinka ST wywołane wysiłkiem fizycznym w stosunku do odpoczynku
- nachylenie szczytowego odcinka ST ćwiczenia
- liczba głównych naczyń pokolorowanych fluorozopią
- skan serca z talem lub test wysiłkowy
- stan (brak choroby serca/choroba serca)

W przypadku danych testowych z repozytorium UCI, fakt iż dane pochodziły z róźnych lokalizacji ma duże znaczenie ,gdyż
od placówki medycznej zależy jakim badaniom poddani zostali pacjęci a co za tym idzie w jakich kolumnach tabelarycznego
przedstawienia będą mieć uzupełnione bądź puste wartości. Scalenie ze sobą wyników badań dostarcza większej różnorodności
również dzięki temu że dane pochodzą z wielu krajów. Jeżeli zestaw wejściowy zostałby ograniczony do jednej
lokalizacji to cecha dla której nie uzupełniono wartości zostałaby pominięta podczas treningu ze względu na brak
danych, co skutowało by uboższym modelem i możliwe że pominięciem kluczowej cechy wpływającej na działanie.



example: try DecisionTreeClassifier(random_state=0)

Explaination:

This occurs because, you are not using a random_state variable while declaring decision_tree_classifier = DecisionTreeClassifier() .

So, each time a different Decision Tree is generated because:

Decision trees can be unstable because small variations in the data might result in a completely different tree being generated. This problem is mitigated by using decision trees within an ensemble.

This is also mentioned in interface Documentation:

The problem of learning an optimal decision tree is known to be NP-complete under several aspects of optimality and even for simple concepts. Consequently, practical decision-tree learning algorithms are based on heuristic algorithms such as the greedy algorithm where locally optimal decisions are made at each node. Such algorithms cannot guarantee to return the globally optimal decision tree. This can be mitigated by training multiple trees in an ensemble learner, where the features and samples are randomly sampled with replacement.


### Wstępna obróbka danych

Proces przetwarzania danych może skladać sie z wielu róźnych kroków zależenie od typu, w uczeniu nadzorowanym operującym
na danych tekstowo-liczbowych poprawnym będzie zastosowanie schematu przedstawionego poniżej:

![Schemat 4](img/2data_preprocessing.png "Wstępna obróbka danych"){ width=50% }


 Po złączeniu można przeprowadzić szereg działań w celu sztucznego uzupełnienia pustych wartości bazując na
wartościach które już istnieją.

*Obsługa brakujących wartości*

Możliwościami obsługi brakujących wartości są : mniej polecana ze względu na utrate danych, redukcja zestawu danych lub uzupełnienie go zgodnie z wybrany przez siebie założeniem. Biblioteki do nauczania
maszynowego dostarczają już gotowe rozwiązania do upuszczenie wierszy lub kolumn zawierających wartości
_null_. Uzupełnienie danych inaczej _imputacja_, rozwiązuje problem w mniej stratny sposób i tak samo jak do redukcji są już
gotowe rozwiązania w bibliotece sklearn. Istnieją 4 różne strategie uzupełniania wykorzystujące proste matematyczne
obliczenia takie jak :

- średnia,
- mediana,
- stała,
- najczęściej występująca wartość.

Do wyznaczenia wartości uzupełniających można również użyć regresji liniowej.

*Standaryzacja*

Przeksztaucenie danych również bazujące na statystycznych założeniach i również ustandaryzowane w popularnych
bibliotekach. Dąrzymy aby średnia wartoś wynosiła 0, a odchylenie standardowe 1 dla liczbowyh reprezentacji danych. Z
matematyczne punktu widzenia wykonujemy działanie

![Schemat 5](img/13wzor_1.png "wzór: podejmujemy średnią i dzielimy ją przez odchylenie standardowe"){ width=20% } [@standar]

*Obsługa zmiennych kategorialnych*

Cechy kategorialne dzielą się na dwie zasadnicze grupy ze względu na mozliwość uprorządkowania , dane takie jak
wyksztaucenie , rozmiar podlegają mapowaniu , dane typu kolor lub płeć podlegaja kodowaniu. W ten sposób dane
kategoryczne staja się wartosciami liczbowymi.

*Reporezentacja wektorowa*

Obsługa danych kategorialnych pozwoliła zmapować/zakodować je w postaci liczbowej, ale można pójść o krok dalej i te
same dane mieć w postaci 0 lub 1 na odpowiedniej kolumnie. Rozwiązanie reprezentacji wektorowej polega na utworzeniu
tylu kolumn ile jest unikalnych wartości dla kategorii i wpisanie 0 lub 1 dla każdego rekordu danych [@wektor] .

*Współliniowość cech*

Aby znaleść korelacje współliniowości należy szukać liniowej zależności pomiędzy danymi, najłatwiej zauważyć to tworząc
wykresy z danych testowych dla każdej pary [@wektor].


Zgodnie z poniższym schematem po przeprocesowaniu wejściowego zbioru danych, należy go podzielić na dane treingowe oraz ewaluacyjne. Powszechnie stosowana K krzyżowa walidacja umożliwia maksymalne wykorzystanie dostarczonego wejścia do dostrajania parametrów modelu, ponieważ optymalizacja hiperparametrów połączone z ciągłą weryfikacją poprawności to sedno treningu.


![Schemat 8](img/6Nauczanie_maszynowe_rozszerzone.png "Szczegółowy schemat machine learning flow"){ height=45% }


**K-krotna walidacja krzyżowa** (ang. _K-fold Cross Validation_, KCV ) - metoda weryfikacji działająca poprzez podział
zbioru danych na k podzbiorów z których każdy przynajmniej raz jest zbiorem oceniającym wydajność , zaznaczając że K
musi być równe lub mniejsze niż liczba elementów w zbiorze [@kfold;@kfold2] .

Kluczowym elementem jest ewaluacja która odbywa się na końcu każdej z k-1 iteracji w celu dostosowania parametrów, po
osiągnięciu wymaganych lub ustalonych wartości dokładności modelu lub weryfikacji wszystkich możliwych opcji i
znalezienie najlepszego modelu można go wykorzystać do weryfikacji na danych spoza zestawu testowego.


## Wybrane algorytmy uczenia maszynowego nadzorowanego

### Losowe lasy decyzyjne

**Drzewa decyzyjne** (ang. _decisions trees_ ) są uznawane za najprostyszy i najbliższy ludzkiemu zrozumieniu algorytm
uczenia, który swoją nazwę zawdzięcza graficznej reprezentacji w postaci drzewa. Każdy węzeł oznacza atrybut, na
podstawie którego następuje rozróżnienie. W modelu kluczowa jest kolejnośc cech, które wystęują po sobie ponieważ
determinuje to otrzymany rezultat [@3;@32] .

![Schemat 9](img/3drzewo_decyzyjne_schemat.png "Schmat Drzewa decyzyjnego"){ width=50% }

Prawie każdy algorytm uczenia maszynowego nadzorowanego można podzielić na dwa etapy. W pierwszym opracowywany jest wzorzec, na którym bazuję późniejsza predykcja. Etap nauki dla drzewa decyzyjnego polega na typowaniu atrybutów, które staja się węzłami decyzyjnymi, dzielącymi rekordy na dwa mniejsze zestawy i tak aż nie ma możliwości dalszego podziału.

Na metodologie drzew decyzyjnych oparta jest dokładniejsza forma nauczania nadzorowanego:  _losowe lasy decyzyjne._

**Losowe lasy decyzyjne** (ang. _random decision forests_) to technika polegająca na połączeniu wielu drzew decyzyjnych
w celu uniknięcia problemu z _nadmiernym dopasowaniem_ do treningowego zestawu danych na którym został przeszkolony.

Utworzony szablon aby poprawnie działać na danych testowych i służacych weryfikacji, nie może stać się
charakterystycznym przypadkiem rozwiązującym przypadek testowy [@3;@32]. W tym celu dla loswoych lasów decyzyjnych najpierw stosuję się **agregację bootstrap'ową**.
Z treningowego zestawu danch losuję się, z możliwymi powtorzeniami, wiersze danych dla których trenowany będzie
model. Jako rezutat brana jest większość lub średnia wartości uzyskanych wyników dla poszczególnych drzew dezycyjnch.
Dodatkowo dla drzew decyzyjnych w lasach losowych, atrybuty odpowiadające za kategoryzację są wybierane z wylosowanego
podzbioru.[@forest]

Wśrod zalet lasów losowych nalezy wyróżnić iż potrafią one trafnie wykalkulować brakujace wartości cech. Idealnie
znajdują zastosowanie dla realnych danych, których zasadniczym problemem jest ich niekompletność.  
Dane medyczne posiadają szeroką wariację zmiennych z dużym prawdopodobieństwem wybrakownia, zastosowanie do nich lasów
decyzyjnych ma potencjał na pozytywne rezulataty.


### Maszyna wektorów nośnych

**Metoda wektorów nośnych** (ang. _support_ _vector_ _machines_ , skr. **_SVM_**) to algorytm uczenia maszynowego
nadzorowanego, który każdy parametr z dostępnych cech dla danych wejściowych, traktuje jako punkt w przestrzeni. Na
podstawie ułożenia punktów dzieli się je na 2 klasy. Graficznie jest to reprezentowane przez prostą dla której odległość
między najbliższymi dwoma punktami dla wektorów jest możliwie największa.

![Schemat 10 ](img/10svm_schemat.png "Schmat SVM"){ height=20% } [^schemat_wzorowany]

Taka prosta nazywana jest  _prostą marginalną_
i powstaje ona poprzez generowanie i selekcję tych prostych które rzetelnie szufladkują klasy danych [@3;@32].

Techinka ta gwarantuje precyzyjniejsze rezulatay niż drzewa decyzyjne, niestety dla dużych zbiorów danych czas trwania
szkolenia znacznie się wydłuża oraz istnieją przypadki dla których podział jedną prostą jest niewykonalny, taki
przypadek reprezentuje rozkład na schemacie nr. 2.

![Schemat 11](img/9svm_niemozliwy_podzial_schemat.png "Schmat SVM niemożliwy podział"){ height=20% } [^schemat_wzorowany]

Z powyższego schematu widać że prosta marginalna ma zastosowanie w przypadku dwóch wymiarów, 
dla większej ilości stosowane jest przeksztaucenie do innego systemu współrzędnych i szukanie hiperpłaszczyzny brzegowej dzielącej tak samo jak prosta punkty w przestrzeni na dwa zbiory.[@hiper] 
 
#### Wyszukiwanie podziału 

Idea działania maszyny wektorów nośnych opiera się na wyznaczenia minimalnej wartości wektora wag oraz przesunięcia (ang. _bias_) który geometrycznie opisuje współrzędne hiperpłaszczyzny. 

![Schemat 13](img/16svm_wzor2.png "svm wzor"){ height=10% } [@svmW0]


### K najbliższych sąsiadów

**K najbliższych sąsiadów** (ang. _k nearest neighbours_, skr. **_KNN_**) to algorytm uczenia maszynowego nadzorowanego
operający swoje estymacje dla konkretnego przypadku danch na wartościach jego K najbliższych sąsiadów(punktów) liczonych
min. dla przestrzeni Euklidesowej [@3]. Do wyznaczenia odległości w metryce Euklidesowej stosowany jest wzór:

![Schemat 14 ](img/17euklides.png "Euklides"){ width=22% } [@manhattan]

popularne są również przestrzenie Manhattan:

![Schemat 15 ](img/18manhattan.png "Manhattan"){ width=22% } [@manhattan]

oraz Mińkowskiego:

![Schemat 16 ](img/19minkowski.png "Minkowski"){ width=22% } [@minkowski]

Atrybut który nastraja proces uczenia się modelu i ma na niego największy wpływ określany jest jako hiperparametr. Dla
KNN jest to liczba sąsiadów i może przyjmować maksymalnie wartości do rozmiaru zbioru cech. Im większa ilość jednostek mających wpływ, tym potęguje się niestety złożoność czasowa algorytmu, znacząco już większa od przedstawionych powyżej innych algoryrtmów,[@3] oraz tym bardziej wzrasta ryzyko nadmiernego dopasowania do modelu testowanego. 

W celu przewidzenia wartości dla nowych danych, należy odnaleść K najbliższych punktów wyliczając odległości, a
następnie przpisać odpowiedź implikowaną przez większość sąsiadów. Dla wartości K równej jeden, metoda ta nazywana jest
algorytmem najbliższego sąsiada.
![Schemat 12](img/5knn_schemat.png "Schmat KNN"){ width=50% } [^schemat_wzorowany]

Dla lekarza wartością dodatnią jest wykrycie zależności które decyzują o uznaniu lub zaprzeczeniu występowania choroby.
Zastosowanie algorytmu KNN może nie tylko zakwalifikować osoby chorujące na serce, ale również ułatwić swoją graficzną
reprezentacją wpływ cech na ostateczny osąd próbki.


# Opis praktycznej częsci projektu

## Narzędzia i biblioteki zastosowane w pojekcie

Biblioteki w większości posiadają otwarty kod źródłowy,  napisany w języku Python [@libpyth].

### Python

[todo]

### Scikit-learn

Praktyczna część pracy napisana została w języku Python z wykorzystaniem *scikit-learn*, obsługującym wiele algorytmów
maszynowego uczenia się w tym uczenia nadzorowanego i docelowo wybranych algorytmów przedstawionych w teoretycznej
części pracy.

![Schemat 7](img/15scikit-learn-logo.png "scikit-learn logo"){ height=10% }

Biblioteka opiera się o *Numpy* oraz *Scipy*, daje zestaw narzędzi do obliczeń na macierzach, wektorach oraz umożliwiający metody
numeryczne takie jak całkowanie, różniczkowanie i temu podobne  [@scikit]. W rezultacie można za jej pomoca wykonać elementy procesu nauczania algorytmu, takie jak: przetwarzanie wstępne, redukcja wymiarowości, klasyfikacja, regresja. [@libpyth] 

[todo]

### Pandas
Do przygotowania danych wykorzystano zestaw narzędzi *Pandas*, ułatwiający tworzenie struktur danych i ich analizę. 
[todo]
### Matplotlib

W celu wizualizacji wyników w postaci wykresów zastosowano, opartą na *Matplotlib*, bibliotekę *Seaborn* powszechnie stosowaną do rysowania estetycznej grfiki statystycznej.
[todo]
### Flask

Część prezentacyjna czyli możliwość wprowadzenia danych w formularzu na stronie i weryfikacja wyniku dla wyuczonych już modeli wykorzystuje bibliotkę *Flask*. Framework Flask ułatwia pisanie aplikacji internetowch i jest rozwiązaniem które daje duży zakres dowolności oraz możliwości. Flask sam z siebie nie definiuje warstwy bazy danych czy formularzy, pozwala za to na obsługę rozszerzeń które ubogacają aplikację o wybraną funkcjonalność. [@flask]

[todo]
### JsonPickle
Przekazywanie obiektów o bardziej skomplikowanej budowie i ich _serializacja_ oraz _deserializacja_ do formatu JSON wykonane są za pomocą biblioteki *jsonpickle*, a zapis
modeli wykonano za pomocą *joblib* która zapewnia obsługę obiektów Pythona i jest zoptymalizowana pod kątem pracy na dużych tablicach Numpy. [@libpyth] 

[todo]
### JobLib

[todo]

### Środowisko wykonania

Wykonanie programu i analizę danych testowych wykonano na maszynie o parametrach :
```doctest
Procesor	Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz   2.50 GHz
Zainstalowana pamięć RAM	8,00 GB (dostępne: 7,82 GB)
Typ systemu	64-bitowy system operacyjny, procesor x64
```

Wersjie bibliotek wykorzystanych w projekcie:

```doctest
setuptools~=49.2.1
Flask~=2.0.1
matplotlib~=3.4.2
numpy~=1.20.3
pandas~=1.2.4
scikit-learn~=0.24.2
pytest~=6.2.5
joblib~=1.0.1
scipy~=1.6.3
seaborn~=0.11.2
jsonpickle~=2.1
```

Interpreter Python w wersji _3.9_.

## Moduły projektu:

- Config - zawiera statyczne zasoby oraz konfigurację logowania projektu
- Data - moduł odpowiada za wczytywanie i obróbkę danych testowych, oraz zawiera definicje objektów wykorzystywanych przy uczeniu oraz zapisu modelu
- Management:

    - PlotGeneration - moduł odpowiedzialny za prezentację wyników w postaci wykresów porównujących algorytmy oraz
      odpowiedzi na zadany problem
    - Prediction :

        - RF - implepmentacja treningu algorytmu Lasów losowych
        - KNN - implepmentacja treningu algorytmu K-najbliższych sąsiadów
        - SVM - implepmentacja treningu algorytmu Maszyny wektorów nośnych
- Static - forlder z grafikami, plikami stylów, skryptami javascript i jQuerry 
- Templates - folder z stronami html wykorzystującymi dyrektywy Flask

Projekt posiada dwa tryby pracy :

- tryb nauczania na podstawie danych testowych\
machine learning z wykorzystaniem 3 algorytmów (_Run_Learning_Proces.xml_)
- tryb aplikacji web\
wykorzystanie Flask do prezentacji i wykorzystania utworzonych modeli (_Run_Web_Application.xml_)

## Trening algorytmu

Głównym zadaniem trybu nauczania jest utworzenie i wytrenowanie modeli dla 3 algorytmów nauczania nienazdorowanego, w tym celu wykonywany jest preprocesing danych czyli kolejno:

2. Załadowanie i konkatenacja dataset'u
3. Uzupełnienie pustych wartości - dla późniejszego porównania tworzone są imputery dla 4 różnych form uzupełnienia
4. Standaryzacja
5. Konwersja danych dla kategorii
6. Normalizacja z wykorzystaniem MinMaxScaler.

Następnie wykonywany jest podział na dane treningowe i testowe z wykorzystaniem zdefiniowanej w bibliotece sklearn predefiniowanej metody. Tak spreparowany zestaw danych poddawany jest treningowi modelu kolejno dla każdego z algorytmów. 
Do dostrojenia parametrów oraz znalezienia najlepszego modelu wykorzystuwany jest:
```Python

GridSearchCV

```

W projekcie dla każdego algorytmy zapróbkowano większość dostępnych dla danego modelu klasyfikacji hiperparametrów przekazywane w param_grid.

Wykorzystane parametry wykonania GridSearchCv [@scikit]:

- estimator: implementacja interfejsu obiekt estymatora scikit-learn,
- param_grid: słownik parametrów które są potem testowane w dowolnej sekwencji ustawień,
- refit: dopasowanie best_estimator_ ,best_index_, best_score_ i best_params_ dla najlepszej sekwencji ustawień parametrów
- cv: parametr k dla KFold walidacji krzyżowej,
- verbose: obszerność logowanych informacji 


*HalvingGridSearchCV*

Sciikit-learn udostępnia również inne implmentacj zastosowania walidacy krzyżowej np.: _HalvingGridSearchCV_ lub _HalvingRandomSearchCV_.
HalvingGridSearchCV polega na zmniejszaniu o połowe (z ang. _half_) zbioru parametrów po każdej iteracji algorytmu krzyżowego.
Ta strategia wyszukiwania sukcesywnie zmniejsza ilość wymaganych iteracji dla danego zestawienia przez co wykonania jest szybsze niż w przypadku zwykłego GridSearchCv.
Na poniższym wykresie  przedstawiającym średni wynik dla algorytmu SVC widać że czas wykonania zmniejszył się ponad 6 krotnie w stosunku do GridSearch.

![Schemat 24](img/24halving.png "HalvingGridSearchCV")[@scikit]{ width=60% }

Umieszczone oznaczenia od 0 do 5 informują o tym w której iteracji kombinacja parmaretów została oznaczona jako najlepsze zestawienie.

Implementacja ta nie została wykorzystana ze względu na nadal pozycjonowanie jej jako eksperymentalnej.


Estymatory to impementacja z skleran która powstała w oparciu o dokumntacje sklearn oraz dostępną dla nich parametryzacje.

Zestawienie najlepszych osiągniętych estymatorów przedstawia się następująco:

*KNeighborsClassifier* [@scikit] :
 
- n_neighbors: 8 - liczba sąsiadów z których wnioskowany jest jednostkowy resultat
- weights: distance - wagi na podsatwie których wyliczana jest predykcja , można zastosować wagę 1:1 lub nałożyć wagi zgodnie z dystansem.
- algorithm: auto - algorytm zastosowany do znalezienia najbliższych sąsiadów, w projekcie wykorzystano : brute-force oraz auto
- leaf_size: 1 - rozmiar liścia dla algorytmów BallTree or KDTree
- p: 1 - wykorzystanie miar odległości dla manhattan
- metric: canberra -metryka odległości


*RandomForestClassifier* [@scikit] :

- criterion: [todo] - funkcja pomiaru dokładności rozgałęzienia
- min_samples_leaf: [todo] -minimalna liczba probek wymagana na liściu.
- min_weight_fraction_leaf: [todo] -minimalny ułamek sumy wag wymagany na liściu 
- min_impurity_decrease: [todo] - większe lub równe zmniejszenie zanieczyszczenia powoduje podział danego węzła\
Zmniejszenie zanieczyszczenia liczone jest zgodnie z wzorem:\
```
N_t / N * (impurity - N_t_R / N_t * right_impurity
                    - N_t_L / N_t * left_impurity)
```

gdzie N to całkowita liczba próbek, N_t to liczba próbek w bieżącym węźle, N_t_L to liczba próbek w lewym liściu, a N_t_R to liczba próbek w prawym liściu.

- max_features: [todo] - liczba funkcji  najlepszego podziału
- random_state: [todo] - wykorzystywany przy próbkowaniu cech przy poszukiwaniu najlepszego podziału w węźle
- cpp_aplha: [todo] - zastosowanie to przycinanie drzewa o największej złożoności mniejszej niż cpp_alpha


*SVC* [@scikit] :
 
- C: [todo]float, default=1.0
Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive. The penalty is a squared l2 penalty.

- kernel: [todo]- jądro wykorzystane w algorytmie
- degree: [todo] - stopień dla funkcji jądra _poly_
- gamma: [todo] - współczynnik jądra dla wartości _scale_ parametr jądra ustawiany jest na wartość:\
```text
1 / (n * X.var())
```
dla wartości auto jest to :
```text
1 / n
```
gdzie n to liczba cech.

- coef0: [todo] - niezależny parametr funkcji jądra , wykorzystywany tylko przy jądrach _poly_ i _sigmoid_.
- shrinking: [todo] - heurystyka kurcząca
- cache_size: [todo] - cache jądra (w MB).

Po odnalezieniu najlepszego estymatora model jest zapisywany oraz generowane sa wykresy dla trybu aplikacji webowej:

- wykresy modeli datasetu wejściowego i rozłożenia cech
- wykresy prezentujące zestawienia danych zebranych na temat algorytmu podczas wykonywania treningu.

## Opis działania aplikacji webowej

Poniżej przedstawiono architektówe działania:

![Schemat 6](img/14Architektura.png "Architektura"){ height=70% }

Aplikacja posiada 4 widoki :

- widok głowny strony 
- widok prezentacji danych wejściowych 
- widok omówienia treningu algorytmów
- widok formularza pozwalającego na wykonanie predycji na wyuczonych modelach na podstawie własnych danych wejściowych

Zatwierdzenie formularza wyzwala odczytanie zapisanych modeli , iteracje i wykonanie predykcji na każdym z nich , następnie prezentowane są wyniki dla najlepszych estymatorów oraz wykresy wskazujące na umiejscowienie nowych danych na tle zbior testowego.

![Schemat 20](img/20form.png "form"){ width=60% }

## Porównanie działania modeli

W tym podrozdziale zamieszczone zostały wyniki oraz wykresy wygenerowane podczas treningu i weryfikacji danych testowych.

|     | Algorytm                   | <td colspan=2> Dokładność w %    |
|-----|----------------------------|----------------------------------|
| --- | -------------------------- | <td colspan=4>parametry domyślne |<td colspan=4> wyznaczanie parametrow|
| --- | imputer                    | średnia                          |mediana|stała -1|najczęstrza wartość|średnia                          |mediana|stała -1|najczęstrza wartość|
|     | Losowe lasy decyzyjne      | 98.2                             |98.2|100|100|98.2                             |98.2|100|100|
|     | Maszyna wektorów nośnych   | 98.2                             |100|100|100|98.2                             |98.2|100|100|
|     | K-najbliższych sąsiadów    | 97.8                             |100 |100|100|98.2                             |98.2|100|100|


#### Zestawienie efektywności działania algorytmów

Konfrontacja technik ucznia maszynowego zaleznie od zestawu danch będzie dawała odmienne wyniki ze względu na ich
predyspozycje do zajmowania się odpowiednimi zbiorami danych.

*Potencjał algorytmów dla niewielkiego kompletu danych zawierającego wartości* 

Zczynając od drzew decyzyjnych,można od razu stwierdzić ich niski potencjał. Istnieje zbyt duże prawdopodobieństwo
dopasowania się do modelu treningowego, gdyż wspomniany zbiór dancyh wejściowych nie jest wystarczająco liczny. Dlatego
w pracy omówione zostały lasy decyzyjne.

Większej dokładności można się spodziewać po metodzie wektorów nośnych, ale jego złożoność czasowa oraz pamięciowa mogą
zaniżyc jego ogólną klasyfikację.

K-najbliższego sąsiada może być przydatny w przypadku danych nieliniowych oraz łatwo wykorzystany w problemach regresji. Wartość
wyjściowa obiektu jest obliczana przez średnią k wartości najbliższych sąsiadów. Niestety tak samo jak w przypadku maszyny wektorów nośnych jest wolniejsza i bardziej kosztowna pod względem czasu i
pamięci. Wymaga dużej pamięci do przechowywania całego zestawu danych treningowych do przewidywania oraz nie nadaje się również do dużych danych wymiarowych. 

**Wskaźniki wydajności**

Określenie stopnia, w jakim skonstruowany model z powodzeniem realizuje wyznaczone zadanie należy do wskaźnika
wydajności. Przykładem nieprawidłowego wyboru może być próba przewidzenia wystąpienia rzadkiej choroby u pacjenta i
określenie głownym miernikiem _dokładność_. W takim scenariuszu klasyfikacja wszystkich pacjentów jako zdrowych , daje
niewiele odbiegającą od perfekcji dokładność, a jednocześnie błędnie osądzać każde wystąpienie choroby.


###  Losowe lasy decyzyjne

##todo liczenie błędów 
macież pomysłek

###  Losowe lasy decyzyjne
###OCENA PODELI ORAZ UŻYTYCH PARAMETRÓW
-OCENA SZYBKOŚCI WYKONANIA
-OCENA ZALEŻNIE OD UZUPELNIANIA DANYCH
-OCENA ZALEŻNIE OD DOBRANEJ PARAMERYZACJI :
 - które parametry mają i wpływ i dlaczego:
   - ZALEŻNIE OD METRYKI(SHORT OPIS METRYK)

###  Maszyna wektorów nośnych

###OCENA PODELI ORAZ UŻYTYCH PARAMETRÓW
-OCENA SZYBKOŚCI WYKONANIA
-OCENA ZALEŻNIE OD UZUPELNIANIA DANYCH
-OCENA ZALEŻNIE OD DOBRANEJ PARAMERYZACJI :
 - które parametry mają i wpływ i dlaczego:
   - ZALEŻNIE OD METRYKI(SHORT OPIS METRYK)

###  K-najbliższych sąsiadów

###OCENA PODELI ORAZ UŻYTYCH PARAMETRÓW
-OCENA SZYBKOŚCI WYKONANIA
-OCENA ZALEŻNIE OD UZUPELNIANIA DANYCH
-OCENA ZALEŻNIE OD DOBRANEJ PARAMERYZACJI :
 - które parametry mają i wpływ i dlaczego:
   - ZALEŻNIE OD METRYKI(SHORT OPIS METRYK)


*Porównianie całościowe algorytmów : złożoność czasowa , dokładność , złożoność implementacyjna , wpływ danych wykorzytywanych w modelu*

![Schemat 20](img/22rf_params.png "form"){ width=60% }

![Schemat 20](img/23rf_params_time.png "form"){ width=60% }


Wybrane najlepsze modele klasyfikacji:

[CV 5/15] END C=0.1, cache_size=200, coef0=0.0, degree=1, gamma=scale, kernel=linear, shrinking=False;, score=0.982 total time=   0.0s
[CV 4/15] END C=0.1, cache_size=200, coef0=0.0, degree=1, gamma=scale, kernel=poly, shrinking=True;, score=0.982 total time=   0.0s
[CV 4/15] END C=0.1, cache_size=200, coef0=0.0, degree=1, gamma=scale, kernel=poly, shrinking=False;, score=0.982 total time=   0.0s
[CV 4/15] END C=10, cache_size=500, coef0=0.3, degree=5, gamma=scale, kernel=linear, shrinking=True;, score=0.982 total time=   0.0s
[CV 4/15] END C=10, cache_size=200, coef0=0.3, degree=5, gamma=auto, kernel=rbf, shrinking=True;, score=0.982 total time=   0.0s

Wybrane najgorsze modele klasyfikacji :

[CV 10/15] END C=100, cache_size=200, coef0=0.3, degree=5, gamma=scale, kernel=poly, shrinking=True;, score=0.800 total time=   0.0s
[CV 10/15] END C=100, cache_size=500, coef0=0.3, degree=5, gamma=scale, kernel=poly, shrinking=False;, score=0.800 total time=   0.0s
[CV 10/15] END C=100, cache_size=200, coef0=0.3, degree=5, gamma=scale, kernel=poly, shrinking=False;, score=0.800 total time=   0.0s

Najlepsze modele i wartości dla regresji :

Najgorsze modele i wartości dla regresji :

###  Maszyna wektorów nośnych

![Schemat 20](img/22cv_params.png "form"){ width=60% }

![Schemat 20](img/23cv_params_time.png "form"){ width=60% }


 ![Schemat 20](img/24cvexel.png "form"){ width=60% }

###  K-najbliższych sąsiadów

###OCENA PODELI ORAZ UŻYTYCH PARAMETRÓW

![Schemat 20](img/22knn_params.png "form"){ width=60% }

![Schemat 20](img/23knn_params_time.png "form"){ width=60% }

 ![Schemat 20](img/24knnexel.png "form"){ width=60% }



problem multiklasyfikacji - problem regresji kategrycznej - zwykła regresja , mierzyć będe 
metoda prównania -  tzrea było wprowadzić reguły do float na int -> inne metody do liczenia błędów 
na dzień dobry widzimy nie dokładność ze wględu na klasyfiakcję po przecinku 
regresja kategoryczna -> rzutowanie przedziału wartości na wartość graniczną 



score method of classifiers
Every estimator or model in Scikit-learn has a score method after being trained on the data, usually X_train, y_train.

When you call score on classifiers like LogisticRegression, RandomForestClassifier, etc. the method computes the accuracy score by default (accuracy is #correct_preds / #all_preds). By default, the score method does not need the actual predictions. So, when you call:

clf.score(X_test, y_test)
it makes predictions using X_test under the hood and uses those predictions to calculate accuracy score. Think of score as a shorthand to calculate accuracy since it is such a common metric. It is also implemented to avoid calculating accuracy like this which involves more steps:

from sklearn.metrics import accuracy score

preds = clf.predict(X_test)

accuracy_score(y_test, preds)
When using accuracy_score you need ready predictions, i.e. the function does not generate prediction using the test set under the hood.

For classifiers, accuracy_score and score are both the same - they are just different ways of calculating the same thing.

score method of regressors
When score is called on regressors, the coefficient of determination - R2 is calculated by default. As in classifiers, the score method is simply a shorthand to calculate R2 since it is commonly used to assess the performance of a regressor.

reg.score(X_test, y_test)
As you see, you have to pass just the test sets to score and it is done. However, there is another way of calculating R2 which is:

from sklearn.metrics import r2_score

preds = reg.predict(X_test)

r2_score(y_test, preds)
Unlike the simple score, r2_score requires ready predictions - it does not calculate them under the hood.

So, again the takeaway is r2_score and score for regressors are the same - they are just different ways of calculating the coefficient of determination.score method of classifiers
Every estimator or model in Scikit-learn has a score method after being trained on the data, usually X_train, y_train.

When you call score on classifiers like LogisticRegression, RandomForestClassifier, etc. the method computes the accuracy score by default (accuracy is #correct_preds / #all_preds). By default, the score method does not need the actual predictions. So, when you call:

clf.score(X_test, y_test)
it makes predictions using X_test under the hood and uses those predictions to calculate accuracy score. Think of score as a shorthand to calculate accuracy since it is such a common metric. It is also implemented to avoid calculating accuracy like this which involves more steps:

from sklearn.metrics import accuracy score

preds = clf.predict(X_test)

accuracy_score(y_test, preds)
When using accuracy_score you need ready predictions, i.e. the function does not generate prediction using the test set under the hood.

For classifiers, accuracy_score and score are both the same - they are just different ways of calculating the same thing.

score method of regressors
When score is called on regressors, the coefficient of determination - R2 is calculated by default. As in classifiers, the score method is simply a shorthand to calculate R2 since it is commonly used to assess the performance of a regressor.

reg.score(X_test, y_test)
As you see, you have to pass just the test sets to score and it is done. However, there is another way of calculating R2 which is:

from sklearn.metrics import r2_score

preds = reg.predict(X_test)

r2_score(y_test, preds)
Unlike the simple score, r2_score requires ready predictions - it does not calculate them under the hood.

So, again the takeaway is r2_score and score for regressors are the same - they are just different ways of calculating the coefficient of determination.
+++++++++++
Is it possible that after running the optimization my score won't get better (and even worse?) ?

Yes, theoretically, by pure luck, it is possible that your initial guess, before optimization of hyper-parameters, provides better results than the best of parameter combination found in the parameters grid. However, assuming you have enough data and your parameter grid is wide enough it is rather unlikely that the tuning of hyper-parameters would not be able to find better results. Such behavior rather indicates that something is wrong with your approach or your data.

If understand correctly, the choice of the best parameters is based on the cv results on training data, while in your final run the performance is assessed based on test dataset. If the distribution of training and test data differ significantly it could lead to the situation when the parameters providing the best results on the training data perform poorly on test data.

Where is my mistake?

As already mentioned by others, the parameters you are testing after the tuning were not included in the parameter grid. In this case it is incorrect to talk about the model performance "after running the optimization".

I suggest the following in order to investigate and fix the problem

Instead of using the hard-coded parameters in the XGBClassifier  call, use the optimal parameters found by tuning process, i.e. grid_search.best_params_. Furthermore, if you think that subsample and cilsample_bytree (a typo?) are relevant parameters include them in the parameters grid.
Increase the cv parameter to e.g. 5-10, the results with cv = 3 might be very unstable. You can assess the stability of your current results by using different random seeds and repeating the entire exercise.
Make sure that you use the consistent parameters in tuning process and in the final evaluation, or just include these parameters in the parameters grid if possible. In particular, check early_stopping_rounds and eval_metric.
Are there other parameters that could influence or improve my model?

From your code it is unclear how many rounds you use. Either increase n_estimators or include it in the parameters grid.
Given that you use AUCPR you might need to explicitly set the parameter maximize=True, otherwise in your final run you could minimize the AUCPR, which could explain poor results.
Share
Improve this answer
Follow
edited Sep 28, 2020 at 22:22
answered Sep 28, 2020 at 21:34
user avatar
aivanov
1,43077 silver badges1414 bronze badges
Add a comment

0

This question is a little wrong-worded. You cannot get worse after optimization, otherwise it wouldn't be optimization! (At worst you are at the same performance like before, getting the exact same parameters you already had)

As Grzegorz points out in a comment, first of all your parameter list isn't complete and doesn't contain the values you use later. For example the learning rate, but also max_depth. Secondly, a grid search where you don't really know where to look should contain a much larger variance for the parameters. You check [0.1, 0.01, 0.05] for the learning rate, but did you check [0.0001, 0.001, 1.]? The learning rate might be a bad example here but I hope it gets the point across, you might want to check magnitude/scale first, e.g. powers of ten, before checking small variations.

Depending on your dataset, the difference between runs with the same values might also come from different seeds! Check that you either always set the same seed, or try it enough times with different seeds to get a comparable answer (for example with KFold).

Is your model even converging for every training? Where do you make sure that you train long enough? You can plot the loss for the training and test sample and check if it's converging or not. This can be controlled with n_estimators in xgboost I believe.

Share
Improve this answer
Follow
answered Sep 24, 2020 at 10:24
user avatar
N. Kiefer
55411 silver badge1313 bronze badges
2
@n-kiefer I find your first paragraph presumptuous. The question posed IS the question. How can one think the question is not valid because of wording. This commentary is not helpful to the investigator. I feel it stifles curiosity or expression. Smugness like this is disheartening to me. In limited cases it is possible to find poor testing values after optimization. One, the optimization was not complete but coded correctly, see above. Two, if the sample population is small then even after optimization it is possible to find poor results. – 
mccurcio
 Sep 24, 2020 at 15:39
1
The answer was not intented to be smug, presumptuous or anything like that. It was simply a short take on the question: is it possible to get worse after optimization? I never said it was invalid, and even attempted to give more pointers as to what could be done. I even (like you) thought of the problem of small datasets and recommended a KFold strategy. The question can indeed be read as: why is the performance worse on the test set compared to the training set? But I try to answer what i think the question is as in the title. – 
N. Kiefer
 Sep 24, 2020 at 16:34
my apologies... – 
mccurcio
 Sep 24, 2020 at 16:48
1
The tone of @N.Kiefer answer is a bit off, but he is mostly right, optimization performed in the example given in the question is not broad enough to search the hyperparameter space: optimization done correctly can't give worst results than arbitrary choice of hyperparameters, it will at least give the same result (or slightly different given random effects if a random seed is not set). – 
Pedro Henrique Monforte
 Sep 25, 2020 at 1:20
Add a comment

0

There is nothing wrong in your code or process. Often times in machine learning performance on the test dataset is lower than than performance on the training data set. Your model is not generalizing perfectly to the data it has not seen before (i.e., the test dataset).

Share
Improve this answer
Follow
answered Sep 24, 2020 at 15:08
user avatar
Brian Spiering
16.1k11 gold badge2121 silver badges7979 bronze badges
Add a comment

-2

When you do hyper-parameter tuning, you improve the regularization of the model. Before you did optimization, you could be overfitting. After optimization you regularized your model and now it performs just right.

enter image description here

Then your model score will be worse after optimization on training set. Your model score will also be bad for test set if your model heavily relies on one feature for classification.

You can use learning curve to see how the curve changes when you use optimization vs when you don't. And you can use df.corr() to see the correlation matrix for the correlation between feature values and target values.
++++++++++++++
Spis ilustracji{.unnumbered}
========
[^schemat_wzorowany]:Na podstwie materiałów opublikowanych na [https://www.datacamp.com](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1526288453/index3_souoaz.png)

Spis tabel{.unnumbered}
========

 **Bibliografia**{.unnumbered}
========



