<map version="freeplane 1.8.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Baza bibliograficzna (podobna do Polskiej Bibliografii Literackiej)" FOLDED="false" ID="ID_696893020" CREATED="1636035670733" MODIFIED="1636035738762" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="82" RULE="ON_BRANCH_CREATION"/>
<node TEXT="ustalić parametry dla wszystkich odsyłaczy (do listy dokumentów); wpisać to na diagramie interakcji (jednym)" POSITION="right" ID="ID_384302744" CREATED="1635365989602" MODIFIED="1636035723318">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<edge COLOR="#0000ff"/>
<node TEXT="typ wyszukiwania: temat lub ozn. odpowiedzialności" ID="ID_1942771130" CREATED="1635409644807" MODIFIED="1635409665370"/>
<node TEXT="Diagram interakcji:" ID="ID_467377181" CREATED="1635706760440" MODIFIED="1635706765541">
<node TEXT="użytkownik wywołuje trasę na views, views jest aktywowane, w zależności od trasy aktywowana jest konkretna funkcja view etc." ID="ID_688998508" CREATED="1635706765567" MODIFIED="1635706805152"/>
</node>
</node>
<node TEXT="wyszukiwanie pełnotekstowe" POSITION="right" ID="ID_504906659" CREATED="1635710718237" MODIFIED="1636035723321">
<edge COLOR="#00ff00"/>
<node TEXT="Szukanie pełnotekstowe (może oparte na możliwościach MySQL?)." ID="ID_754474006" CREATED="1635709784412" MODIFIED="1635805403964"/>
<node TEXT="chyba powinno mieć własną trasę - przejrzeć dokumentację" ID="ID_1381180607" CREATED="1635805404462" MODIFIED="1635805405656">
<node TEXT="Jeżeli będę robił wyszukiwanie dla wszystkich kategorii rekordów, będzie miało inną trasę. Jak byłoby to zorganizowane:" ID="ID_1223105505" CREATED="1635709916494" MODIFIED="1635709946798">
<node TEXT="Wyniki z dokumentów: skrócona lista dokumentów - np. 5 pozycji; jeżeli jest więcej - dla pozostałych: link &quot;zobacz więcej&quot; odsyłający do listy zawierającej tylko dokumenty (i prawdopodobnie do trasy przeglądania dokumentów - /browse/documents/) --lub-- &quot;rozwiń&quot; i ładowanie kolejnej grupy wierszy (np. kolejnych 5) przy pomocy AJAXa - link aktywny tak długo, jak długo będą dostępne kolejne dokumenty. Dla pozostałych kategorii - tak samo." ID="ID_607194187" CREATED="1635709946819" MODIFIED="1635710264505"/>
</node>
</node>
<node TEXT="Elasticsearch" ID="ID_1737802720" CREATED="1635710727740" MODIFIED="1635710731055">
<node TEXT="posiada paginację i sortowanie tak, jak bazy relacyjne" ID="ID_588009278" CREATED="1635710789238" MODIFIED="1635710798492"/>
</node>
</node>
<node TEXT="wyrazić instrukcje warunkowe w funkcji documents_list na diagramie - tak, żeby kod się nie powtarzał i żeby sprawdzić jak dobrze mi idzie robienie instrukcji warunkowych" POSITION="right" ID="ID_72117529" CREATED="1635423848683" MODIFIED="1636035723322">
<font BOLD="false"/>
<edge COLOR="#ff00ff"/>
</node>
<node TEXT="zrobić dokumentację do parametrów do makr (co oznaczają parametry, jakie przyjmują wartości etc.)" POSITION="right" ID="ID_53596417" CREATED="1635423978804" MODIFIED="1636035723323">
<edge COLOR="#00ffff"/>
</node>
<node TEXT="Można dodać osobną funkcję/klasę/moduł zwracające kwerendy." POSITION="right" ID="ID_1148734699" CREATED="1635413392647" MODIFIED="1636035723324">
<edge COLOR="#7c0000"/>
</node>
<node TEXT="Szablony z listami elementów zrobić podobnie jak szablon listy dokumentów (zmienione makro do paginacji)." POSITION="right" ID="ID_520352425" CREATED="1635355201345" MODIFIED="1636035723326">
<edge COLOR="#00007c"/>
</node>
<node TEXT="Relacje zwrotne - od poszczególnych widoków do listy dokumentów." POSITION="right" ID="ID_32648912" CREATED="1635285678317" MODIFIED="1636035723326">
<edge COLOR="#007c00"/>
</node>
<node TEXT="Na stronach widoków użyć przycisków z hiperłączami do list (zamiast badges) - badges z hiperłączami pozostawić na listach." POSITION="right" ID="ID_1062146301" CREATED="1635284914535" MODIFIED="1636035723328">
<edge COLOR="#7c007c"/>
</node>
<node TEXT="Jeżeli przewijam np. listę osób po tym, jak dostałem się tam z np. widoku oznaczenia odpowiedzialności, chciałbym łatwym sposobem na stronę widoku ozn. odp. wrócić - jak to zrobić? (Zdaje się, że było o tym w podręczniku)." POSITION="right" ID="ID_428121528" CREATED="1635282931718" MODIFIED="1636035723329">
<edge COLOR="#007c7c"/>
</node>
<node TEXT="Aplikacja minimalna (z możliwością rozbudowy)" POSITION="right" ID="ID_394421864" CREATED="1635274763546" MODIFIED="1636035723332">
<font BOLD="true"/>
<richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Będę mógł to gdziekolwiek wystawić, kiedy osiągnie ten status.
    </p>
  </body>
</html>
</richcontent>
<edge COLOR="#7c7c00"/>
<node TEXT="Listy elementów i widoki szczegółów (bez filtrów)." ID="ID_1585874663" CREATED="1635274778488" MODIFIED="1635275124909"/>
<node TEXT="Połączenia zwrotne od widoków szczegółów do list." ID="ID_1572770923" CREATED="1635274790456" MODIFIED="1635274804709"/>
<node TEXT="Wyszukiwanie w bd" ID="ID_30317132" CREATED="1635274806377" MODIFIED="1635274815096"/>
<node TEXT="Logowanie" ID="ID_398581221" CREATED="1635275017369" MODIFIED="1635275020220"/>
<node TEXT="Edycja bd (projektowane osobno)" ID="ID_516648049" CREATED="1635275031784" MODIFIED="1635275045843"/>
</node>
<node TEXT="Usunąć powtarzające się elementy z szablonów i ustalić hierarchię dziedziczenia." POSITION="right" ID="ID_1420613920" CREATED="1635282772738" MODIFIED="1636035723332">
<edge COLOR="#ff0000"/>
</node>
<node TEXT="Do niektórych notatek dopisać &quot;use stories&quot;." POSITION="right" ID="ID_430518307" CREATED="1635259353647" MODIFIED="1636035723333">
<edge COLOR="#0000ff"/>
</node>
<node TEXT="Z widoków szczegółów od liczby dokumentów wyświetlanej na stronie powinno odsyłać: do listy dokumentów - jeżeli jest ich więcej niż 1, do dokumentu - jeżeli jest tylko 1, hiperłącze nieaktywne - jeżeli jest 0." POSITION="right" ID="ID_948933662" CREATED="1634753754227" MODIFIED="1636035723339">
<edge COLOR="#ff00ff"/>
</node>
<node TEXT="Kiedy napiszę w JS skrypt ustawiający klasy dla elementów w szablonie, przejrzeć jeszcze raz strony wyświetlające listy, niektóre zastąpić makrami i usunąć powtarzający/podobny się kod." POSITION="right" ID="ID_1243989412" CREATED="1635177736531" MODIFIED="1636035723340">
<edge COLOR="#00ffff"/>
</node>
<node TEXT="ResponsibilityName.modifiable powinno mieć atr. nullable=False" POSITION="right" ID="ID_1260377471" CREATED="1635157646373" MODIFIED="1636035723341">
<edge COLOR="#7c0000"/>
</node>
<node TEXT="możliwość blokowania/zawieszania konta użytkownika" POSITION="right" ID="ID_971220876" CREATED="1635151459650" MODIFIED="1636035723342">
<edge COLOR="#00007c"/>
</node>
<node TEXT="zapisywanie modyfikacji rekordu" POSITION="right" ID="ID_1277321310" CREATED="1635109528069" MODIFIED="1636035723343">
<edge COLOR="#007c00"/>
<node TEXT="dla dokumentu - osobna tabela z informacjami o modyfikacjach; dla pozostałych rekordów - tylko informacja o aktualizacji rekordu i użytkowniku, który dokonał modyfikacji" ID="ID_1371440234" CREATED="1635109534194" MODIFIED="1635109819044"/>
<node TEXT="utworzenie rekordu" ID="ID_326683102" CREATED="1635109655361" MODIFIED="1635109659614">
<node TEXT="data i czas; informacje o użytkowniku - w polach &quot;aktualizowano&quot; (updated)" ID="ID_1376743720" CREATED="1635109659642" MODIFIED="1635109710170"/>
</node>
</node>
<node TEXT="Rekordu typu miejsce, słowo kluczowe, osoby etc., nie można skasować, jeżeli jest powiązany z jakimkolwiek dokumentem - system ma to blokować (tylko kiedy znikną referencje - wolno skasować)." POSITION="right" ID="ID_708705680" CREATED="1635109840847" MODIFIED="1636035723344">
<edge COLOR="#7c007c"/>
</node>
<node TEXT="kolejna wersja" POSITION="right" ID="ID_1859583935" CREATED="1635107636018" MODIFIED="1636035723346">
<edge COLOR="#007c7c"/>
<node TEXT="Działy" ID="ID_1269708126" CREATED="1630660619735" MODIFIED="1630660622886">
<node TEXT="Zaprojektować to w ten sposób, żeby później można było je w miarę łatwo dodać." ID="ID_1339454882" CREATED="1630660624887" MODIFIED="1630660643848"/>
<node TEXT="Symbole klasyfikacji." ID="ID_1724511651" CREATED="1635107756834" MODIFIED="1635107762724">
<node TEXT="Może: osobna tabela z nazwą klasyfikacji, symbolem klasyfikacji ..." ID="ID_1534655140" CREATED="1635107765304" MODIFIED="1635107889387"/>
</node>
</node>
<node TEXT="elementy z diagramu widoków, które pominąłem:" ID="ID_677728800" CREATED="1635274852297" MODIFIED="1635274866298">
<node TEXT="Filtry w widokach list (w tym dokumentów, osób)." ID="ID_257407989" CREATED="1635274866324" MODIFIED="1635274889690"/>
</node>
</node>
<node TEXT="Interfejs użytkownika (szablony dla tras) opisać diagramami stanów i ewentualnie zastanowić się, co mogę ulepszyć." POSITION="right" ID="ID_128959781" CREATED="1634897110894" MODIFIED="1636035723347">
<edge COLOR="#7c7c00"/>
</node>
<node TEXT="nazwy funkcji (publisher etc.) powinny mieć swoje badge i hiperłącze od dokumentu do strony ze szczegółami" POSITION="right" ID="ID_1576795561" CREATED="1634897789352" MODIFIED="1636035723348">
<edge COLOR="#ff0000"/>
</node>
<node TEXT="lista dokumentów zależnych powinna być taka jak np. lista tematów-ludzi" POSITION="right" ID="ID_515296774" CREATED="1635257588879" MODIFIED="1636035723349">
<edge COLOR="#0000ff"/>
</node>
<node TEXT="w bd dodać check constraint w tabeli self-referential many-to-many między dokumentami: dokument nie może odnosić się sam do siebie (np. czasopismo może być dokumentem nadrzędnym wobec artykułu, artykuł/czasopismo nie może być dok. podrzędnym/nadrzędnym wobec samego siebie)" POSITION="right" ID="ID_920647133" CREATED="1634897961331" MODIFIED="1636035723350">
<edge COLOR="#00ff00"/>
</node>
<node TEXT="Zrobić funkcje które będą automatycznie dodawały klasy do konkretnych elementów (w celu uzyskania odpowiednich stylów na stronach)." POSITION="right" ID="ID_263205327" CREATED="1634721677770" MODIFIED="1636035723353">
<edge COLOR="#ff00ff"/>
<node TEXT="Automatyczne dodawanie klas do elementów w JS." ID="ID_1596444331" CREATED="1634721655869" MODIFIED="1634721669259">
<node TEXT="https://stackoverflow.com/questions/927312/how-to-append-a-css-class-to-an-element-by-javascript/52052493" ID="ID_781362436" CREATED="1634721671261" MODIFIED="1634721671261" LINK="https://stackoverflow.com/questions/927312/how-to-append-a-css-class-to-an-element-by-javascript/52052493"/>
</node>
<node TEXT="przemyśleć jakie klasy powinny mieć elementy do których będę dodawał (klasy Bootstrapa), jak będą wyglądały funkcje etc." ID="ID_1920078552" CREATED="1634722176828" MODIFIED="1634722213218"/>
</node>
<node TEXT="wyszukiwarka nie powinna przeładowywać całej strony - użycie AJAXa" POSITION="right" ID="ID_1509402273" CREATED="1634933366756" MODIFIED="1636035723354">
<edge COLOR="#00ffff"/>
</node>
<node TEXT="W słowach kluczowych, jeżeli żaden dokument nie referencjonuje danego słowa, powinno wyświetlać tylko 0 (bez see list)." POSITION="right" ID="ID_1198991086" CREATED="1634760670501" MODIFIED="1636035723355">
<edge COLOR="#7c0000"/>
</node>
<node TEXT="Porządkowanie elementów na listach (porządek rosnący lub malejący)" POSITION="right" ID="ID_1239304059" CREATED="1634753563582" MODIFIED="1636035723356">
<edge COLOR="#00007c"/>
</node>
<node TEXT="do linków mogę dodać strony bibliotekarskie - np. ISBD" POSITION="right" ID="ID_1636707045" CREATED="1634742036056" MODIFIED="1636035723357">
<edge COLOR="#007c00"/>
</node>
<node TEXT="Jeżeli listy (np. słów kluczowych) są puste, powinno wyświetlić komunikat, że brak elementów do wyświetlenia." POSITION="right" ID="ID_374679143" CREATED="1634723344368" MODIFIED="1636035723358">
<edge COLOR="#7c007c"/>
<node TEXT="na stronie nadrzędnej (abstrakcyjnej?) powinien być opis jakich pól/parametrów wymaga" ID="ID_120377629" CREATED="1634723510471" MODIFIED="1634723532354"/>
<node TEXT="powinno to działać tak jak metoda first_or_404: wyświetlić szablon lub stronę z inf. nt braku elementów" ID="ID_1983601442" CREATED="1634723989232" MODIFIED="1634724039411"/>
</node>
<node TEXT="widok osoby" POSITION="right" ID="ID_643181993" CREATED="1634584384098" MODIFIED="1636035723360">
<edge COLOR="#007c7c"/>
<node TEXT="Niech przy głównych nazwiskach pokazuje też liczbę dokumentów" ID="ID_463832910" CREATED="1634230732120" MODIFIED="1634647352288">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Do szablonu dodać:" ID="ID_1637848329" CREATED="1634582283062" MODIFIED="1634582292950">
<node TEXT="dokumenty, dla których ta osoba jest tematem" ID="ID_1038948802" CREATED="1634582313252" MODIFIED="1634677823197">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="lista odpowiedzialności pełnionych przez tą osobę a przy każdej odpowiedzialności liczba dokumentów" ID="ID_242541737" CREATED="1634584437586" MODIFIED="1634677824946">
<icon BUILTIN="button_ok"/>
<node TEXT="zaprojektować to na diagramach lub pseudokod, muszę dokładnie wiedzieć co chcę osiągnąć" ID="ID_281944813" CREATED="1634589314129" MODIFIED="1634590751868"/>
</node>
<node TEXT="+ przy każdym linku liczba" ID="ID_1945309357" CREATED="1634582342422" MODIFIED="1634582348941"/>
</node>
</node>
<node TEXT="Przy cofaniu się od wpisu do listy dokumentów nie powinno się pytać czy chcę ponownie przesłać formularz." POSITION="right" ID="ID_712342264" CREATED="1636035628759" MODIFIED="1636035723361">
<edge COLOR="#7c7c00"/>
</node>
<node TEXT="Hiperłącza do listy dokumentów z funkcją osoby/dokumentów, w których jest tematem." POSITION="right" ID="ID_688345208" CREATED="1634647357987" MODIFIED="1636035723362">
<edge COLOR="#ff0000"/>
</node>
<node TEXT="w jakim porządku powinny być ułożone funkcje dla tras?" FOLDED="true" POSITION="right" ID="ID_1221608340" CREATED="1634658431582" MODIFIED="1636035723363">
<edge COLOR="#0000ff"/>
<node TEXT="sprawdzić w podręczniku/kodzie aplikacji z podręcznika" ID="ID_630493226" CREATED="1634658443717" MODIFIED="1634658462207"/>
</node>
<node TEXT="W fake.documents: dokument nie może mieć dodanego samego siebie jako dokumentu podrzędnego." POSITION="right" ID="ID_1932536815" CREATED="1634418183047" MODIFIED="1636035723363">
<edge COLOR="#00ff00"/>
</node>
<node TEXT="Dodać sortowanie list w widoku dokumentu." POSITION="right" ID="ID_1155687546" CREATED="1634560752599" MODIFIED="1636035723364">
<edge COLOR="#ff00ff"/>
</node>
<node POSITION="right" ID="ID_1227963654" CREATED="1634500543540" MODIFIED="1636035723365"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Kiedy będę to przenosił do MySQL - kasowanie powiązanych rekordów: dodać 'ondelete cascade' i <b>przetestować</b>&nbsp;kasowanie powiązań (np. kasuję dokument - kasowane są wszystkie wpisy go dotyczące w tabelach asocjacyjnych).
    </p>
  </body>
</html>
</richcontent>
<edge COLOR="#00ffff"/>
</node>
<node TEXT="w widoku dokumentu, w wierszu z typem dokumentu - typ dokumentu powinien być linkiem do strony dla tego typu dokumentu" POSITION="right" ID="ID_1760205770" CREATED="1634555783510" MODIFIED="1636035723365">
<icon BUILTIN="button_ok"/>
<edge COLOR="#7c0000"/>
</node>
<node TEXT="wspólny szablon dla collectivity_details i person_record_details" POSITION="right" ID="ID_529136222" CREATED="1634745348952" MODIFIED="1636035723368">
<icon BUILTIN="button_cancel"/>
<edge COLOR="#00007c"/>
<node TEXT="za:&#xa;  + oba są w miarę podobne&#xa;  przeciw:&#xa;  + jeżeli w przyszłości będę chciał wprowadzić dodatkowe elementy,&#xa;  w jednym a nie w drugim widoku (osoby/ciała zbiorowego),&#xa;  będzie to utrudnione i sprawi, że kod stanie się mało&#xa;  przejrzysty&#xa;  + wymagałoby to upchania pól z obiektu z rekordami w słowniku,&#xa;  liście lub innej strukturze a później przetwarzanie tego&#xa;  w szablonie, co mogłoby się okazać później trudne w utrzymaniu" ID="ID_284402006" CREATED="1634745408427" MODIFIED="1634745410180"/>
</node>
<node TEXT="dodać self referential relation dla dokumentu typu seria" POSITION="right" ID="ID_361873261" CREATED="1634393396920" MODIFIED="1636035723368">
<edge COLOR="#007c00"/>
</node>
<node TEXT="Role (responsibilities) osób/ciał zbiorowych w dokumencie" POSITION="right" ID="ID_1680901782" CREATED="1633460790504" MODIFIED="1636035723369">
<font BOLD="false"/>
<edge COLOR="#7c007c"/>
<node TEXT="Podstawowe - dodane do bazy tak jak role użytkowników - w ten sposób będzie to można wykorzystać w interfejsie." ID="ID_1874436952" CREATED="1633460800885" MODIFIED="1634305082443">
<icon BUILTIN="button_ok"/>
<node TEXT="metoda add_basic_responsibilities w models.py" ID="ID_356482532" CREATED="1633982620575" MODIFIED="1634152796141">
<font BOLD="false"/>
</node>
<node TEXT="autor, tłumacz etc." ID="ID_199733821" CREATED="1633460888535" MODIFIED="1633460892859"/>
</node>
<node TEXT="Inne - dodawane/zmieniane z poziomu aplikacji." ID="ID_31238353" CREATED="1633981629719" MODIFIED="1633981649039"/>
</node>
<node TEXT="edytor ról osób/ciał zbiorowych w aplikacji - jak to zrobić?" POSITION="right" ID="ID_1187607858" CREATED="1634304594527" MODIFIED="1636035723370">
<edge COLOR="#007c7c"/>
</node>
<node TEXT="Zaprojektować interakcje w widoku przeglądania nazw osoby." POSITION="right" ID="ID_410401384" CREATED="1633981527625" MODIFIED="1636035723370">
<font BOLD="false"/>
<edge COLOR="#7c7c00"/>
<node TEXT="na podstawie diagramów" ID="ID_929126477" CREATED="1634072116928" MODIFIED="1634072125055"/>
</node>
<node TEXT="testy dla widoków" POSITION="right" ID="ID_665735923" CREATED="1633631241937" MODIFIED="1636035723371">
<edge COLOR="#ff0000"/>
</node>
<node TEXT="kolejność pracy" POSITION="right" ID="ID_1868652500" CREATED="1633981398760" MODIFIED="1636035723371">
<edge COLOR="#0000ff"/>
<node TEXT="Sprawy zw. z użytkownikami - na końcu." ID="ID_1178698675" CREATED="1633981405529" MODIFIED="1633981423147"/>
</node>
<node TEXT="bugtracker" POSITION="right" ID="ID_524977360" CREATED="1634300796153" MODIFIED="1636035723372">
<edge COLOR="#00ff00"/>
<node TEXT="Login manager nie działa" ID="ID_1314422306" CREATED="1633631167236" MODIFIED="1633631171445"/>
</node>
<node TEXT="dodać osobną trasę z listą linków prowadzących do rekordów które można przeglądać (&quot;browse&quot;) - szczegóły w diagramach widoków" POSITION="right" ID="ID_1229959108" CREATED="1634135358907" MODIFIED="1636035723373">
<edge COLOR="#ff00ff"/>
</node>
<node TEXT="strony z błędami" POSITION="right" ID="ID_929969456" CREATED="1633687276556" MODIFIED="1636035723373">
<edge COLOR="#00ffff"/>
<node TEXT="dodać strony błędów (403, 404) spójne z resztą (stron)" ID="ID_982863066" CREATED="1634149669477" MODIFIED="1634149690838"/>
</node>
<node TEXT="zaprojektować ogólne interakcje (na pdstw. use-cases - np. gdzie po danej interakcji aplikacja powinna mnie odesłać - np. po zmodyfikowaniu i zapisaniu opisu bibliograficznego na stronę wyświetlającą ten opis lub wyświetlić komunikat niepowodzenia modyfikacji [etc.])" POSITION="right" ID="ID_1006816947" CREATED="1630965034139" MODIFIED="1636035723375">
<edge COLOR="#7c0000"/>
<node TEXT="tworzenie konta" ID="ID_519157732" CREATED="1632949869890" MODIFIED="1632949906381"/>
<node TEXT="widoki interfejsu przedstawić na diagramie interakcji jako &quot;view&quot;, np. &quot;base view&quot;" ID="ID_49992338" CREATED="1633814583641" MODIFIED="1633814629935"/>
</node>
<node TEXT="Dodać do bd listę zapisanych przez użytkownika pozycji" POSITION="right" ID="ID_761561780" CREATED="1632998613361" MODIFIED="1636035723376">
<edge COLOR="#00007c"/>
</node>
<node TEXT="po zaprojektowaniu interakcji, dodać odpowiednie metody do modelów w bd" POSITION="right" ID="ID_312195761" CREATED="1632328462661" MODIFIED="1636035723377">
<edge COLOR="#007c00"/>
<node TEXT="projektować klasy" ID="ID_321241912" CREATED="1630964813112" MODIFIED="1631307684460"/>
</node>
<node TEXT="model użytkownika/ról/uwierzytelnianie chyba najlepiej wydzielić z models.py" POSITION="right" ID="ID_1041156449" CREATED="1632770887909" MODIFIED="1636035723378">
<edge COLOR="#7c007c"/>
</node>
<node TEXT="pola w bd powinny mieć maksymalnie 30 znaków - sprawdzić czy tyle mają" POSITION="right" ID="ID_1857624967" CREATED="1634504369369" MODIFIED="1636035723379">
<edge COLOR="#007c7c"/>
</node>
<node TEXT="W stopce dodać m.in. Githuba etc." POSITION="right" ID="ID_1979427547" CREATED="1633979286053" MODIFIED="1636035723380">
<edge COLOR="#7c7c00"/>
</node>
<node TEXT="Zaprojektować stronę z rezultatami szybkiego wyszukiwania." POSITION="right" ID="ID_1627936475" CREATED="1633725425644" MODIFIED="1636035723381">
<edge COLOR="#ff0000"/>
<node TEXT="Szukanie zaprojektować dopiero gdy przyjrzę się narzędziom do wyszukiwania." ID="ID_1140692085" CREATED="1635259116926" MODIFIED="1635259134522"/>
</node>
<node TEXT="blokowanie rekordów do edycji" POSITION="right" ID="ID_222293649" CREATED="1634117528225" MODIFIED="1636035723384">
<edge COLOR="#0000ff"/>
<node TEXT="Record locking strategies" ID="ID_735266412" CREATED="1631298262727" MODIFIED="1631298284796">
<node TEXT="źródła" ID="ID_1582640380" CREATED="1631298702721" MODIFIED="1631298705517">
<node TEXT="Gray, Jim &amp; Reuter, Andreas (1993), Distributed Transaction Processing: Concepts and Techniques, Morgan Kaufmann, pp. 375–437, ISBN 1-55860-190-2" ID="ID_1243386771" CREATED="1631298593687" MODIFIED="1631298595113"/>
<node TEXT="http://www.agiledata.org/essays/concurrencyControl.html" ID="ID_1640762898" CREATED="1631299104653" MODIFIED="1631299104653" LINK="http://www.agiledata.org/essays/concurrencyControl.html"/>
</node>
<node TEXT="In database management theory, locking is used to implement isolation among multiple database users. This is the &quot;I&quot; in the acronym ACID." ID="ID_870206224" CREATED="1631298709010" MODIFIED="1631298710461"/>
</node>
<node TEXT="wylogowanie użytkownika powinno również powodować odblokowanie rekordu wpisanego w tabeli blokującej" ID="ID_1000627189" CREATED="1631699090998" MODIFIED="1631699112883"/>
</node>
<node TEXT="Program umożliwia tworzenie/przeglądanie spisów literatury:" POSITION="right" ID="ID_401959053" CREATED="1629194996806" MODIFIED="1636035723385">
<edge COLOR="#00ff00"/>
<node TEXT="książek" ID="ID_320972248" CREATED="1629195020949" MODIFIED="1629195022880"/>
<node TEXT="czasopism" ID="ID_585815184" CREATED="1629195023268" MODIFIED="1629195025508"/>
<node TEXT="artykułów z czasopism" ID="ID_111652460" CREATED="1629195031748" MODIFIED="1629195044206">
<node TEXT="powiązane z czasopismem (relacja - foreign key)" ID="ID_1959714360" CREATED="1629195465256" MODIFIED="1629195557484"/>
</node>
<node TEXT="Fragmentów z dzieł zbiorowych" ID="ID_1519424892" CREATED="1629996487036" MODIFIED="1629996492009"/>
</node>
<node TEXT="Może zamiast słów kluczowych użyć deskryptorów?" POSITION="right" ID="ID_1679966855" CREATED="1630931806665" MODIFIED="1636035723386">
<edge COLOR="#ff00ff"/>
<node TEXT="w pierwszej wersji słowa kluczowe, jeżeli będę nad tym pracował - deskryptory" ID="ID_645268082" CREATED="1630931901530" MODIFIED="1630931921368"/>
</node>
<node TEXT="Administrator rozpoznawany jest po emailu przechowywanym w zmiennej środowiska; kiedy aktywuje konto, natychmiast przyznane mu zostają odpowiednie uprawnienia." POSITION="right" ID="ID_961083289" CREATED="1631640761289" MODIFIED="1636035723387">
<edge COLOR="#00ffff"/>
</node>
<node TEXT="Tworzenie listy rekordów do wydruku." POSITION="right" ID="ID_977062956" CREATED="1629284704904" MODIFIED="1636035723388">
<edge COLOR="#7c0000"/>
<node TEXT="Osobny szablon/strona." ID="ID_1789753802" CREATED="1629284740985" MODIFIED="1629284745094"/>
<node TEXT="Możliwość dodawania/usuwania wpisów z listy." ID="ID_1969836780" CREATED="1629284722384" MODIFIED="1629284740358"/>
<node TEXT="Możliwość wyczyszczenia listy rekordów." ID="ID_1908485921" CREATED="1629284746890" MODIFIED="1629284755672"/>
</node>
<node TEXT="konta użytkowników" POSITION="right" ID="ID_1696552146" CREATED="1629214145825" MODIFIED="1636035723393">
<edge COLOR="#00007c"/>
<node TEXT="uprawnienia/role" ID="ID_999960712" CREATED="1629214179567" MODIFIED="1629724490928">
<node TEXT="zwykły użytkownik" ID="ID_562901859" CREATED="1629214190154" MODIFIED="1629218651063">
<node TEXT="zapisywanie opisów (dodawanie listy do konta)" ID="ID_1247820478" CREATED="1629214154128" MODIFIED="1629214169328"/>
<node TEXT="Przeglądanie rekordów w szablonach bibliografii." ID="ID_1138732" CREATED="1629723452997" MODIFIED="1629723481752"/>
</node>
<node TEXT="redaktor" ID="ID_1732590653" CREATED="1629216927835" MODIFIED="1629216948153">
<node TEXT="Uprawnienia użytkownika plus ..." ID="ID_167971989" CREATED="1629723487695" MODIFIED="1629723494570">
<node TEXT="modyfikacja + dodawanie rekordów / haseł etc. w odpowiednich szablonach" ID="ID_1414415893" CREATED="1629723498048" MODIFIED="1629723540055"/>
</node>
<node TEXT="Osoba wprowadzająca, modyfikująca rekordy." ID="ID_54836329" CREATED="1629216948163" MODIFIED="1629216967639"/>
</node>
<node TEXT="administrator" ID="ID_445063501" CREATED="1629214195533" MODIFIED="1629214200570">
<node TEXT="Redaktor plus ..." ID="ID_1353087511" CREATED="1629723521793" MODIFIED="1629723526078">
<node TEXT="aktywowanie kont innych użytkowników, zarządzanie kontami" ID="ID_254744942" CREATED="1629216969019" MODIFIED="1629723583381"/>
<node TEXT="Uważać, żeby nie było możliwe, że nieaktywny administrator może sobie sam aktywować konto!" ID="ID_225877015" CREATED="1629723583792" MODIFIED="1629723609299">
<node TEXT="Możliwe rozwiązania:" ID="ID_1204152169" CREATED="1630586826100" MODIFIED="1630586834757">
<node TEXT="Uprawnienia administratora muszą zostać nadane ręcznie przez innego administratora (potrzebny bezpośredni kontakt - np. email z prośbą)." ID="ID_1873609884" CREATED="1630586834780" MODIFIED="1630586894982"/>
</node>
</node>
</node>
</node>
<node TEXT="Uważnie przejrzeć jak to jest rozwiązane w podręczniku do aplikacji internetowych - ew. zrobić diagram." ID="ID_1133464010" CREATED="1629724491692" MODIFIED="1630586925763"/>
</node>
<node TEXT="uwierzytelnienie" ID="ID_1235131982" CREATED="1629218630934" MODIFIED="1629218638279">
<node TEXT="Hashowanie/porównywanie hashy haseł wg. podręcznika (i notatek)." ID="ID_254383866" CREATED="1629218681686" MODIFIED="1629218752793"/>
<node TEXT="Użycie TLS (Transport Layer Security)" ID="ID_638970744" CREATED="1630355290421" MODIFIED="1630355310175">
<node TEXT="https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https" ID="ID_1601120161" CREATED="1630355359228" MODIFIED="1630355359228" LINK="https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https"/>
</node>
</node>
<node TEXT="Aplikacja rejestruje czas:" ID="ID_113538527" CREATED="1629726352891" MODIFIED="1629726367402">
<node TEXT="Rejestracji konta" ID="ID_33329792" CREATED="1629726367412" MODIFIED="1629726373006"/>
<node TEXT="Ostatniego logowania" ID="ID_214886097" CREATED="1629726373242" MODIFIED="1629726377282"/>
</node>
</node>
<node TEXT="kopie zapasowe" POSITION="right" ID="ID_946007255" CREATED="1630417726567" MODIFIED="1636035723394">
<edge COLOR="#007c00"/>
<node TEXT="Osobny skrypt zrzucający co pewien czas bazę danych." ID="ID_1208707766" CREATED="1630417784813" MODIFIED="1630417801143"/>
</node>
<node TEXT="Strony wyświetlające wpisy są paginowane - żeby nie zawiesić przeglądarki, jeżeli wpisów będzie zbyt wiele." POSITION="right" ID="ID_78722230" CREATED="1629214323611" MODIFIED="1636035723394">
<icon BUILTIN="button_ok"/>
<edge COLOR="#7c007c"/>
</node>
<node TEXT="Czy należy rozdzielić klasy opisujące model użytkownika, uprawnień etc. od pozostałej części bd?" POSITION="right" ID="ID_580236929" CREATED="1632413399013" MODIFIED="1636035723395">
<edge COLOR="#007c7c"/>
</node>
<node TEXT="Logowanie/rejestracja użytkownika" POSITION="right" ID="ID_585407159" CREATED="1629284944354" MODIFIED="1636035723400">
<edge COLOR="#7c7c00"/>
<node TEXT="w przypadku redaktora: dostęp do stron edycji rekordów, haseł etc." ID="ID_1466036761" CREATED="1629284972466" MODIFIED="1629285074800"/>
<node TEXT="w przypadku administratora: uprawnienia redaktora + możliwość aktywowania/blokowania kont użytkowników" ID="ID_1078301124" CREATED="1629285075119" MODIFIED="1629285123837"/>
<node TEXT="Logowanie tylko na daną sesję (do zamknięcia przeglądarki) lub na dłuższy czas - &apos;Keep me logged in&apos; (wg. podręcznika Flaska)." ID="ID_1771218270" CREATED="1629285159195" MODIFIED="1629285256143"/>
<node TEXT="Jeżeli użytkownik niezalogowany chciał dostać się do strony z której został przekierowany na formularz logowania, po zalogowaniu ma zostać przeniesiony na powrót do tej strony." ID="ID_429220750" CREATED="1629382316633" MODIFIED="1629382371495">
<node TEXT="funkcja login() (linia 949) we flask.py i odpowiedni fragment z podręcznika" LOCALIZED_STYLE_REF="defaultstyle.details" ID="ID_760156330" CREATED="1629382379256" MODIFIED="1629382528425"/>
</node>
<node TEXT="bezpieczeństwo" ID="ID_1489321758" CREATED="1629383164422" MODIFIED="1629383168529">
<node TEXT="rejestracja konta" ID="ID_378428254" CREATED="1629384536971" MODIFIED="1629384544093">
<node TEXT="Podczas rejestracji, aplikacja sprawdza, czy użytkownik użył dozwolonych w nazwie użytkownika znaków (liter, liczb, podkreśleń)." ID="ID_1314007710" CREATED="1629383234851" MODIFIED="1629384534575"/>
</node>
<node TEXT="potwierdzenie konta" ID="ID_1387370552" CREATED="1629713598000" MODIFIED="1629713602032">
<node TEXT="link aktywacyjny wysyłany na pocztę - wg. podręcznika" ID="ID_1832238324" CREATED="1629713602043" MODIFIED="1629713619312"/>
</node>
<node TEXT="formularz rejestracyjny - wg podręcznika i notatek (flask.py, 1008 linia)" ID="ID_413464894" CREATED="1629384579997" MODIFIED="1629384598745"/>
</node>
</node>
<node TEXT="API" POSITION="right" ID="ID_694480213" CREATED="1630354946930" MODIFIED="1636035723401">
<edge COLOR="#ff0000"/>
<node TEXT="Pozostawić możliwość budowy API (do wykorzystania np. przez aplikacje z tradycyjnym GUI, np. w tkinter/pyQt)" ID="ID_566713098" CREATED="1630354949970" MODIFIED="1630354983868"/>
</node>
<node TEXT="modyfikacja rekordów" POSITION="right" ID="ID_1016743517" CREATED="1629719000594" MODIFIED="1636035723403">
<edge COLOR="#0000ff"/>
<node TEXT="Aplikacja uniemożliwia otwarcie rekodu do modyfikacji jeżeli został on już otwarty do modyfikacji (np. w formularzu w innej zakładce, przez innego użytkownika na etc.)." ID="ID_1354421201" CREATED="1629718909234" MODIFIED="1629719521565">
<node TEXT="Wersje:" ID="ID_628302854" CREATED="1629719120515" MODIFIED="1629719125360">
<node TEXT="Otwarcie rekordu powoduje jego zablokowanie, np. przed otwarciem sprawdzana jest inna tabela - zawierająca listę zablokowanych rekordów." ID="ID_1784190644" CREATED="1629719125620" MODIFIED="1629719444487">
<node TEXT="Rozpisać dokładnie procedurę, np. w formie diagramu." LOCALIZED_STYLE_REF="defaultstyle.details" ID="ID_1818761668" CREATED="1629719444696" MODIFIED="1629719465659"/>
</node>
<node TEXT="Można otworzyć rekord, ale przy próbie zapisu porównywane są pola ze stemplem czasowym i użytkownikiem który wprowadził ostatnie zmiany - jeżeli się różnią, wyświetlany jest komunikat o modyfikacji rekordu." ID="ID_309335567" CREATED="1629719193029" MODIFIED="1629719387221"/>
<node TEXT="Może istnieją jakieś wzorce postępowania w takich okolicznościach? Sprawdzić czy istnieją gotowe rozwiązania." ID="ID_590884942" CREATED="1629719389096" MODIFIED="1629720076391"/>
</node>
</node>
</node>
<node TEXT="Raportowanie" POSITION="right" ID="ID_23432694" CREATED="1630416982740" MODIFIED="1636035723405">
<edge COLOR="#00ff00"/>
<node TEXT="np. podsumowania o dodanych/zmodyfikowanych rekordach" ID="ID_1608795255" CREATED="1629218105642" MODIFIED="1630589950431"/>
<node TEXT="Szczegółowa lista zmian wprowadzanych w rekordach (użytkownik, data wprowadzenia zmiany)." ID="ID_1653897457" CREATED="1630417155009" MODIFIED="1630417196517"/>
<node TEXT="Czy należy rejestrować ile razy dany rekord był wyświetlany przez użytkowników innych niż redaktorzy i administratorzy?" ID="ID_991503088" CREATED="1630417203125" MODIFIED="1630590250324">
<icon BUILTIN="button_cancel"/>
</node>
<node TEXT="wysyłanie poczty" ID="ID_1008878082" CREATED="1629218102072" MODIFIED="1629218105623">
<node TEXT="nowi użytkownicy" ID="ID_283366037" CREATED="1629218123287" MODIFIED="1629218130503"/>
<node TEXT="powiadomienia o raportach (np. &quot;wprowadzono zmiany w bd&quot;)" ID="ID_1063612012" CREATED="1630416992936" MODIFIED="1630417014341"/>
</node>
</node>
<node TEXT="Anonimowy użytkownik/uż. bez uprawnień/uż. konta nie aktywowanego, który będzie chciał wejść np. na stronę edycji rekordu zostanie przekierowany na inną stronę (szczegóły techniczne w pliku ze źródłami-notatkami i notatkach we Freeplane)." POSITION="right" ID="ID_123252507" CREATED="1629284097575" MODIFIED="1636035723407">
<icon BUILTIN="xmag"/>
<edge COLOR="#ff00ff"/>
<node TEXT="stronę logowania" ID="ID_1091888054" CREATED="1629379887272" MODIFIED="1629379890672"/>
<node TEXT="wyświetlenie przycisku/linku &quot;zaloguj&quot;/&quot;wyloguj&quot; wg. instrukcji warunkowej w szablonie" ID="ID_654999847" CREATED="1629379926823" MODIFIED="1629379957999"/>
</node>
<node TEXT="Aplikacja umożliwia wyszukiwanie:" POSITION="right" ID="ID_390525456" CREATED="1629214377066" MODIFIED="1636035723408">
<edge COLOR="#00ffff"/>
<node TEXT="osób" ID="ID_1702011960" CREATED="1629214386024" MODIFIED="1629214389592"/>
<node TEXT="opisów bibliograficznych" ID="ID_105939168" CREATED="1629214395416" MODIFIED="1629214412627"/>
<node TEXT="haseł przedmiotowych/nazw działów" ID="ID_1408531268" CREATED="1629214412775" MODIFIED="1629214424681"/>
</node>
<node TEXT="listy (np. wyszukiwania) są paginowane" POSITION="right" ID="ID_759138296" CREATED="1630348186687" MODIFIED="1636035723409">
<edge COLOR="#7c0000"/>
</node>
<node TEXT="wyświetlanie:" POSITION="right" ID="ID_937475074" CREATED="1629213336376" MODIFIED="1636035723411">
<edge COLOR="#00007c"/>
<node TEXT="następujących list:" ID="ID_641650752" CREATED="1629973504148" MODIFIED="1629973511652">
<node TEXT="" ID="ID_58330203" CREATED="1629213915080" MODIFIED="1629213915080">
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="listy osób" ID="ID_864984014" CREATED="1629213342472" MODIFIED="1629213902803"/>
<node TEXT="działów" ID="ID_1023638043" CREATED="1629213522027" MODIFIED="1629213524777"/>
<node TEXT="haseł przedmiotowych/deskryptorów/słów kluczowych" ID="ID_958747022" CREATED="1629213525402" MODIFIED="1629213540534"/>
<node TEXT="listy czasopism" ID="ID_816681391" CREATED="1629213708706" MODIFIED="1629213712109"/>
<node TEXT="" ID="ID_590104910" CREATED="1629213915047" MODIFIED="1629213915080">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="wraz z linkami do podczepionych pod nie opisów; wyświetlanie liczb określających ilość podpiętych opisów" ID="ID_757527901" CREATED="1629213915080" MODIFIED="1630420099229"/>
</node>
<node TEXT="listy książek" ID="ID_713537805" CREATED="1629213712528" MODIFIED="1629213717296"/>
<node TEXT="artykułów z prac zbiorowych/czasopism" ID="ID_1894289249" CREATED="1629973551511" MODIFIED="1629973559844"/>
</node>
<node TEXT="Listy są paginowane (wyświetlane na wielu stronach)." ID="ID_1169067340" CREATED="1629973578121" MODIFIED="1629973611415"/>
</node>
<node TEXT="etapy projektowania" POSITION="right" ID="ID_235516252" CREATED="1629195216884" MODIFIED="1636035723415">
<edge COLOR="#007c00"/>
<node TEXT="wymogi" ID="ID_907043232" CREATED="1629215139908" MODIFIED="1629215143560">
<node TEXT="Przepisać na sformalizowany SRS." ID="ID_301634918" CREATED="1629379821142" MODIFIED="1629379833266">
<node TEXT="SRS (wg. przykładów i zasad - m.in. dot. wymogów shall/should etc. - po angielsku)" ID="ID_1788588999" CREATED="1629304290862" MODIFIED="1629304329742"/>
</node>
<node TEXT="nieformalnie - notatki w mapie myśli" ID="ID_1411443799" CREATED="1629304283265" MODIFIED="1630590563531"/>
</node>
<node TEXT="use cases" ID="ID_1804998358" CREATED="1629211072857" MODIFIED="1629211075291"/>
<node TEXT="Zaprojektować interfejs - strony" ID="ID_528852427" CREATED="1629195220095" MODIFIED="1629195443384">
<node TEXT="do przeglądania" ID="ID_458219140" CREATED="1629195225814" MODIFIED="1629195229633"/>
<node TEXT="tworzenia spisów" ID="ID_1625228362" CREATED="1629195229860" MODIFIED="1629195235118"/>
<node TEXT="mock-views (np. w Gimp w formie uproszczonej - np. siatki lub napisać ręcznie wstępne strony, które będę mógł użyć przy projektowaniu szablonów)" ID="ID_1001097402" CREATED="1629726019065" MODIFIED="1630590660588"/>
</node>
<node TEXT="Zaprojektować bazę danych" ID="ID_558142081" CREATED="1629195536776" MODIFIED="1629195542871">
<node TEXT="od razu w MySQL czy w SQLight?" ID="ID_966482938" CREATED="1629213663360" MODIFIED="1629213676207"/>
<node TEXT="Diagramy ER" ID="ID_1526177758" CREATED="1629218958935" MODIFIED="1629218964795"/>
<node TEXT="zaprojektować modele w SQLAlchemy" ID="ID_679305043" CREATED="1629218946073" MODIFIED="1629218957428"/>
<node TEXT="relacje obustronne w bd" ID="ID_688448788" CREATED="1629195595863" MODIFIED="1629218787625"/>
</node>
<node TEXT="zaprojektować ścieżki (routes)" ID="ID_1681145262" CREATED="1629217743639" MODIFIED="1629217753032"/>
<node TEXT="diagramy" ID="ID_1283931739" CREATED="1629211083592" MODIFIED="1629211103322">
<node TEXT="klasy" ID="ID_1930809417" CREATED="1629211103334" MODIFIED="1629211105594"/>
<node TEXT="interakcje" ID="ID_1556994505" CREATED="1629211112185" MODIFIED="1629211130762"/>
<node TEXT="aktywności" ID="ID_1408554484" CREATED="1629211131048" MODIFIED="1629211135125"/>
<node TEXT="Czy view functions można zorganizować w diagramie pakietu (jako części modułu?)" ID="ID_597518745" CREATED="1629744284484" MODIFIED="1629744311891">
<icon BUILTIN="help"/>
</node>
</node>
<node TEXT="Pisanie kodu" ID="ID_43728689" CREATED="1629213238230" MODIFIED="1629213241289">
<node TEXT="testy jednostkowe" ID="ID_850093597" CREATED="1629211140889" MODIFIED="1629211146283">
<node TEXT="pisane razem z kodem (lub nawet przed)" ID="ID_691969416" CREATED="1629213245045" MODIFIED="1629388245538" COLOR="#ff0000">
<icon BUILTIN="yes"/>
</node>
<node TEXT="Zastanowić się co mogę przetestować" ID="ID_448082679" CREATED="1629211153336" MODIFIED="1629211162586"/>
<node TEXT="fałszywa baza danych" ID="ID_548587259" CREATED="1629213643536" MODIFIED="1629213647375">
<node TEXT="przy pomocy Faker" ID="ID_1642251820" CREATED="1629388264292" MODIFIED="1629388269129"/>
</node>
</node>
</node>
</node>
<node TEXT="Software Requirements Specification Document" FOLDED="true" POSITION="right" ID="ID_299391823" CREATED="1629994945727" MODIFIED="1636035723426"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Zachować kolejność punktów/podpunktów.
    </p>
    <p>
      Nie modyfikować tego - zmiany wprowadzać w dokumencie (na dysku Google).
    </p>
  </body>
</html>
</richcontent>
<font BOLD="true"/>
<edge COLOR="#7c007c"/>
<node TEXT="Introduction" FOLDED="true" ID="ID_703548230" CREATED="1629994960267" MODIFIED="1630603527534">
<icon BUILTIN="full-1"/>
<node TEXT="Purpose" FOLDED="true" ID="ID_1604722274" CREATED="1629994985383" MODIFIED="1629994988909">
<node TEXT="The purpose of this document is to build a web application for bibliography management." ID="ID_1424567010" CREATED="1629995014531" MODIFIED="1629995257166"/>
</node>
<node TEXT="Document conventions" FOLDED="true" ID="ID_1780829747" CREATED="1629995259286" MODIFIED="1629995263987">
<node ID="ID_492452859" CREATED="1629995293909" MODIFIED="1630603607927"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      This document uses the following conventions:
    </p>
    <table border="0" style="width: 80%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 0; border-right-width: 0; border-bottom-width: 0; border-left-width: 0">
      <tr>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            DB
          </p>
        </td>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Database
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            app
          </p>
        </td>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            application
          </p>
        </td>
      </tr>
    </table>
  </body>
</html>
</richcontent>
</node>
<node TEXT="Authority record - is a record which gives the authoritative form (the form selected for a heading) of a personal name, corporate name, family name, place name, uniform or preferred title, series title, subject, etc. in the library catalogue or the file of bibliographic records, and are listed in an authority file containing headings of library items." FOLDED="true" ID="ID_285659762" CREATED="1630415716682" MODIFIED="1630603660454">
<node TEXT="https://www.librarianshipstudies.com/2016/02/authority-record.html" ID="ID_976107514" CREATED="1630415878793" MODIFIED="1630415878793" LINK="https://www.librarianshipstudies.com/2016/02/authority-record.html"/>
</node>
<node TEXT="Subject Heading - defined as the most specific word or group of words that captures the essence of the subject or one of the subjects of a book or other library material (e.g. serial, sound recording, moving image, cartographic material, manuscript, computer file, e-resource etc.) which is selected from a subject heading list containing the preferred subject access terms (controlled vocabulary) and assigned as an added entry in the bibliographic record which works as an access point and enables the work to be searched and retrieved by subject from the library catalog database." FOLDED="true" ID="ID_165717161" CREATED="1630416090006" MODIFIED="1630416098075">
<node TEXT="https://www.librarianshipstudies.com/2015/09/subject-heading.html" ID="ID_379737497" CREATED="1630416102067" MODIFIED="1630416102067" LINK="https://www.librarianshipstudies.com/2015/09/subject-heading.html"/>
</node>
</node>
<node TEXT="Project scope" FOLDED="true" ID="ID_1566418594" CREATED="1629995408749" MODIFIED="1629995413020">
<node TEXT="The purpose of the application is to facilitate making bibliographies of the following materials: books, periodicals, articles from periodicals and from collective works (published as books). The application uses a relational database, allows browsing bibliographic records using the web browser and has separate views for editing bibliographic information." ID="ID_631739371" CREATED="1629995439276" MODIFIED="1630603785927"/>
</node>
<node TEXT="References" FOLDED="true" ID="ID_1235978600" CREATED="1629995855900" MODIFIED="1629995858987">
<node TEXT="Grinberg, Miguel. Flask Web Development: Developing Web Applications with Python. O&apos;Reilly Media, Inc., 2018.&#xa;SQLALchemy documentation website: https://docs.sqlalchemy.org/en/14/ [accessed: August 26th, 2021]." ID="ID_1626080204" CREATED="1629995885085" MODIFIED="1629996079103"/>
</node>
</node>
<node TEXT="Overall Description" FOLDED="true" ID="ID_347509695" CREATED="1629996164356" MODIFIED="1630603529503">
<icon BUILTIN="full-2"/>
<node TEXT="Product perspective" FOLDED="true" ID="ID_1099714129" CREATED="1629996171651" MODIFIED="1629996178791">
<node ID="ID_272966455" CREATED="1629996208626" MODIFIED="1630605965953"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      A bibliographic database stores the following information:
    </p>
    <ul>
      <li>
        <b>Bibliographic records&nbsp;</b>of book, periodicals, articles from periodicals and parts (for ex. essays published within a single volume) of collective works (collective works are usually published as books).
      </li>
      <li>
        <b>Personal data</b>&nbsp;(information about individuals): authors, editors, translators
      </li>
      <li>
        <b>Organisations:</b>&nbsp;publishing houses, collective (institutional) bodies
      </li>
      <li>
        <b>Subject headings</b>&nbsp;to be attached to bibliographic records, describing thematic content of referenced materials.
      </li>
      <li>
        Bibliography should also have<b>&nbsp;classification symbols (divisions)</b>&nbsp;with symbols to represent content of the document; symbols should be organised into sections and subsections (two or three levels deep).
      </li>
    </ul>
    <p>
      Data from the database should be made available using web (browser) interface.
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="Product features" FOLDED="true" ID="ID_203363755" CREATED="1629997653789" MODIFIED="1629997659038">
<node TEXT="The major features of bibliographic database are shown below in the entity-relationship model (ER model)." ID="ID_1637063024" CREATED="1629997670319" MODIFIED="1629997736941"/>
<node TEXT="(dodać model ER bazy danych)" LOCALIZED_STYLE_REF="defaultstyle.details" ID="ID_952973766" CREATED="1629997659597" MODIFIED="1629997801016"/>
</node>
<node TEXT="User class and characteristics" FOLDED="true" ID="ID_400749864" CREATED="1629999090026" MODIFIED="1629999100337">
<node TEXT="Browsing and searching options" FOLDED="true" ID="ID_1071794335" CREATED="1630000410417" MODIFIED="1630000429819">
<node ID="ID_1118266210" CREATED="1629999112060" MODIFIED="1630003418619"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Users of the applications should be able to retrieve bibliographic information by browsing hypertext lists:
    </p>
    <ul>
      <li>
        Individual (personal) entry list - clickable list of individuals referenced by bibliographic records - that is, clicking on an individual-personal-entry from the list should display another list of attached bibliographic records to which that person is related - as an author, translator or editor.
      </li>
      <li>
        List of organisations referenced by bibliographic records.
      </li>
      <li>
        List of articles attached to a periodical.
      </li>
      <li>
        List of fragments attached to collective work.<br/>
      </li>
    </ul>
    <p>
      Clicking on a bibliographic entry in an application should redirect to the detailed bibliographic description and list of materials referencing a given item.
    </p>
    <p>
      
    </p>
    <p>
      Users of the application should also be able to search the database using following criteria:
    </p>
    <ul>
      <li>
        Personal name
      </li>
      <li>
        Collective body name (institution, eg. publishing house)
      </li>
      <li>
        Title (book, periodical, article, fragment)
      </li>
      <li>
        Topic - subject keyword
      </li>
    </ul>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="User classes and permissions" FOLDED="true" ID="ID_838442886" CREATED="1630002064372" MODIFIED="1630003309827">
<node ID="ID_695543555" CREATED="1630002262090" MODIFIED="1630606144231"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      The application defines following user classes:
    </p>
    <ul>
      <li>
        Anonymous users (unregistered) - can only display, browse and search database.
      </li>
      <li>
        Regular users - can display, browse, search database and add entries to a personal list of bibliographic items.
      </li>
      <li>
        Editors - have regulars user's permissions + permission to edit bibliographic information (bibliographic records, personal/collective names, subject keywords)
      </li>
      <li>
        Administrators - can activate and change user accounts.
      </li>
    </ul>
    <p>
      Each user class is defined by user permissions (which in turn can be modified by administrators).
    </p>
    <table border="0" style="width: 80%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 0; border-right-width: 0; border-bottom-width: 0; border-left-width: 0">
      <tr>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Anonymous users
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Regular users
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Editors
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Administrators
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            display bibliography
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            browse/search database
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            save bib. items to a list
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Edit bibliographic information
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Activate user accounts
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Modify user accounts
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            no
          </p>
        </td>
        <td valign="top" style="width: 25%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            yes
          </p>
        </td>
      </tr>
    </table>
    <p>
      As specified above, some functionality is available only after registering a user account and logging in.
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
</node>
<node TEXT="Operating environment" FOLDED="true" ID="ID_382944654" CREATED="1630413665905" MODIFIED="1630413672907">
<node TEXT="SQL database system (like MySQL)" ID="ID_1004681306" CREATED="1630413776706" MODIFIED="1630413785928"/>
<node TEXT="Client/server system" ID="ID_1721813564" CREATED="1630413789762" MODIFIED="1630606384313"/>
<node TEXT="browser-based application on client side, Linux on server side (or any other compatible, tested with the app OS)" ID="ID_53517557" CREATED="1630413828642" MODIFIED="1630606400573"/>
<node TEXT="platform: Python/Flask/SQLAlchemy (server side), html+css+Bootstrap+JavaScript (on client side)" ID="ID_255615844" CREATED="1630413884514" MODIFIED="1630414171357"/>
</node>
</node>
<node TEXT="System Features" FOLDED="true" ID="ID_1045746108" CREATED="1630414361478" MODIFIED="1630603532347">
<icon BUILTIN="full-3"/>
<node TEXT="Functional Requirements" FOLDED="true" ID="ID_1328785665" CREATED="1630414760553" MODIFIED="1630414767124">
<node TEXT="Stimulus/response sequence" FOLDED="true" ID="ID_1338530144" CREATED="1630414915611" MODIFIED="1630414923897">
<node TEXT="The system shall allow users to add/remove/modify:" FOLDED="true" ID="ID_114510338" CREATED="1630414958142" MODIFIED="1630415294235">
<node TEXT="personal records in the database" ID="ID_1951084773" CREATED="1630415012873" MODIFIED="1630415058458"/>
<node TEXT="bibliographic records in the database" ID="ID_433601973" CREATED="1630415062859" MODIFIED="1630415076175"/>
</node>
<node TEXT="The system shall restrict some actions to certain categories of users - as specified in the section &quot;User class and characteristics&quot;." ID="ID_625967086" CREATED="1630415090604" MODIFIED="1630415299662"/>
<node TEXT="The system shall record data about entry modifications and users modifying records (date, time and login names of users who modified entries)." ID="ID_1433612875" CREATED="1630415566592" MODIFIED="1630607278218"/>
<node TEXT="The system shall have easy to navigate, web-based interface that allows users to query for information (bibliographic records, authority names)." ID="ID_885075482" CREATED="1630416224902" MODIFIED="1630606555918"/>
<node TEXT="Each database item displayed in a view template shall contain information about referenced records and number of attached records (records referencing this item). For instance, each item in search results of periodicals shall display number of articles attached (referencing) this item. Each authority name shall link to a view page for that authority and in turn - authority view page shall link to a paginated list of items referencing this authority. Each periodical details view template shall display paginated list of articles attached to this periodical.&#xa;Details are specified in attachments." ID="ID_256618443" CREATED="1630420280603" MODIFIED="1630607160275"/>
<node TEXT="The system shall allow users (as specified in &quot;User classes and permissions&quot;) to edit database through a web-based user interface." ID="ID_234859612" CREATED="1630416440904" MODIFIED="1630607292151"/>
<node TEXT="The system shall allow users to register as regular users. Application shall notify users to activate their accounts - activation shall be automated by sending an email with a confirmation link to the user. Application administrator shall be able to change individual user permissions (change user category, for instance from a regular user to an editor)." ID="ID_1205085453" CREATED="1630418094972" MODIFIED="1630607693992"/>
<node TEXT="Anonymous user/user with an unconfirmed account attempting to enter part of the application requiring logging-in shall be redirected to the registration site (anonymous u.) or displayed the site notifying that his account has not yet been activated and offering to resend confirmation email to a given email address.&#xa;User attempting to enter part of the application requiring lifted permissions shall be displayed notification about insufficient permissions and informed that they can ask the system administrator to lift their permissions." ID="ID_1439953139" CREATED="1630419012917" MODIFIED="1630421935880"/>
<node TEXT="User registration time+date as well as the &quot;last seen&quot; time+date shall be recorded in the database." ID="ID_1289631213" CREATED="1630587027501" MODIFIED="1630587100951"/>
<node FOLDED="true" ID="ID_248344212" CREATED="1630587453853" MODIFIED="1630608680009"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      The application shall prevent:
    </p>
    <ul>
      <li>
        editing a single record by more than one user at the same time
      </li>
      <li>
        opening a record for modification in more than one edit form at the same time
      </li>
    </ul>
    <p>
      The record should be locked when opened for modification, unlocked after completing edition. The view-form with record opened for editing shall be automatically disabled (&quot;greyed-out&quot;) after a given amount of time of user idleness: if that happens, the button for subsequent unlocking the entry shall be enabled. If clicked, the app will check the db if another person hadn't, in the meantime, opened the entry for editing or if the entry had been modified. If modified, the app shall ask to reload it but warn that by doing so all changes introduced locally will be lost. The app shall also allow to save modified record as a new one and merge records manually later.
    </p>
  </body>
</html>
</richcontent>
<node TEXT="use story:" FOLDED="true" ID="ID_1585003974" CREATED="1630587958228" MODIFIED="1630587962420">
<node TEXT="Halinka is a librarian who wants to edit an entry in a bibliography. She logs into her account in the Flask-Bibliography-App (which is being used at the library she works in), finds the entry she wants to modify and clicks &quot;modify&quot;. The app flashes a notification saying that this particular entry was locked for modification by another user, bozenka_123 and for this sake it cannot be opened for modification until bozenka_123 unlocks the entry - that is, she either saves changes she introduced and closes the editing form or discards them by explicitly clicking on &quot;discard (changes)&quot; - or closes the web-browser tab/window in which the editing form was displayed." ID="ID_757144542" CREATED="1630587962437" MODIFIED="1630608944467"/>
</node>
<node TEXT="Wymagany diagram activity." ID="ID_946381763" CREATED="1630588518244" MODIFIED="1630588527792"/>
</node>
<node TEXT="Detailed interactions are described in attached interaction diagrams." ID="ID_500506142" CREATED="1630414924971" MODIFIED="1630417552257">
<font BOLD="true"/>
</node>
<node TEXT="User interface details and view-templates shall be implemented in accordance with the attachments." ID="ID_563394135" CREATED="1630418727908" MODIFIED="1630419518788">
<font BOLD="true"/>
</node>
</node>
<node TEXT="Other system features" FOLDED="true" ID="ID_474986793" CREATED="1630415313773" MODIFIED="1630609258752">
<node TEXT="The application shall display ISBD formatted bibliography information after selecting detailed entry view." ID="ID_928205460" CREATED="1630588764356" MODIFIED="1630588822020"/>
</node>
<node TEXT="Optional features" FOLDED="true" ID="ID_1354301464" CREATED="1630609250611" MODIFIED="1630609256683">
<node TEXT="The system should expose database bibliographic and authority records through an API." ID="ID_1763351266" CREATED="1630415448783" MODIFIED="1630416692491"/>
<node TEXT="The system should record how many times a given bibliographic record was displayed in an online bibliography (views by editors and administrators should be excluded)." ID="ID_1683082895" CREATED="1630417284105" MODIFIED="1630417410908"/>
<node TEXT="The system should daily report modifications to the database and email notification about new report being generated." ID="ID_1643444478" CREATED="1630416860250" MODIFIED="1630608878141"/>
</node>
</node>
<node TEXT="Non-functional requirements" FOLDED="true" ID="ID_330497115" CREATED="1630414772298" MODIFIED="1630414777157">
<node TEXT="The application shall have general scripts for backups (and shall inform the administrator of the need to customize them)." ID="ID_479191159" CREATED="1630417926567" MODIFIED="1630421085590"/>
<node TEXT="The application shall securely confirm user account by sending an email with a confirmation link to the email address given at the registration." ID="ID_1574720932" CREATED="1630420888706" MODIFIED="1630587438605"/>
<node TEXT="The application shall check if user, during registration, used only allowed characters for a username and if a user password meets security requirements." ID="ID_1729539910" CREATED="1630420803394" MODIFIED="1630422080621"/>
</node>
</node>
<node TEXT="External interface requirements" FOLDED="true" ID="ID_252873559" CREATED="1630591107608" MODIFIED="1630603534861">
<icon BUILTIN="full-4"/>
<node TEXT="User interface" FOLDED="true" ID="ID_134179306" CREATED="1630591118200" MODIFIED="1630591124288">
<node TEXT="Front-end software: bootstrap+vanilla JS for AJAX" ID="ID_973791939" CREATED="1630591127222" MODIFIED="1630591163936"/>
<node TEXT="Back-end software: Flask, SQLAlchemy" ID="ID_605341370" CREATED="1630591164087" MODIFIED="1630591186359"/>
</node>
<node TEXT="Software interfaces" FOLDED="true" ID="ID_39229246" CREATED="1630591279430" MODIFIED="1630591283462">
<node ID="ID_1706925623" CREATED="1630591293368" MODIFIED="1630591709594"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <table border="0" style="width: 80%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 0; border-right-width: 0; border-bottom-width: 0; border-left-width: 0">
      <tr>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            <b>Software used</b>
          </p>
        </td>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            <b>Description</b>
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Server operating system
          </p>
        </td>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            I chose Ubuntu-based OS for its customizability, availability of various developer tools such as containers, Python-related tools and its CLI.
          </p>
        </td>
      </tr>
      <tr>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            Database software and libraries/frameworks
          </p>
        </td>
        <td valign="top" style="width: 50%; border-top-style: solid; border-right-style: solid; border-bottom-style: solid; border-left-style: solid; border-top-width: 1; border-right-width: 1; border-bottom-width: 1; border-left-width: 1">
          <p style="margin-top: 1; margin-right: 1; margin-bottom: 1; margin-left: 1">
            For database I decided to use SQLite (for development version), MySQL (for deployment) and SQLAlchemy ORM.
          </p>
        </td>
      </tr>
    </table>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="Communication interfaces" FOLDED="true" ID="ID_1551484358" CREATED="1630591719465" MODIFIED="1630591730721">
<node TEXT="This project aims to support major up-to-date browsers such as gecko- (Firefox) and webkit-based (Chromium/Chrome, Edge)." ID="ID_343392940" CREATED="1630591758633" MODIFIED="1630592593681"/>
</node>
</node>
<node TEXT="Safety requirements" FOLDED="true" ID="ID_720464886" CREATED="1630592097245" MODIFIED="1630603537256">
<icon BUILTIN="full-5"/>
<node TEXT="The deployed application database shall have a regular backup copy stored on archival storage (different than the main server). The backup copy shall allow for database restoration after a critical failure: for instance hardware malfunction or data loss due to malicious acts of individuals - crackers breaking into a system and corrupting data." ID="ID_1000263588" CREATED="1630592113758" MODIFIED="1630592578466"/>
</node>
<node TEXT="Uwagi" FOLDED="true" ID="ID_550280387" CREATED="1629997845522" MODIFIED="1629997846896">
<node TEXT="Wzorowane na:" FOLDED="true" ID="ID_836817365" CREATED="1629997774977" MODIFIED="1629997783814">
<node TEXT="https://krazytech.com/projects/sample-software-requirements-specificationsrs-report-airline-database" ID="ID_1169901196" CREATED="1629997784421" MODIFIED="1629997784421" LINK="https://krazytech.com/projects/sample-software-requirements-specificationsrs-report-airline-database"/>
</node>
<node TEXT="Pilnować, żeby było to zgrane z opisem powyżej (w gałęzi &quot;Projekt&quot;)" ID="ID_1919624111" CREATED="1629997849169" MODIFIED="1630609968580"/>
<node TEXT="Jeżeli będę kiedyś robił swoją stronę, przekształcić ten węzeł na dokument w formacie do wydruku (tekst+schematy) i zamieścić tam do wglądu - np. w formacie pdf." ID="ID_93012923" CREATED="1630591939722" MODIFIED="1630591989805"/>
</node>
</node>
<node TEXT="opisy bibliograficzne:" POSITION="right" ID="ID_413907243" CREATED="1633201192930" MODIFIED="1636035723427">
<edge COLOR="#007c7c"/>
<node TEXT="z PBL" ID="ID_1535798366" CREATED="1633201198386" MODIFIED="1633201200136"/>
<node TEXT="API Biblioteki Kongresu" ID="ID_1831754446" CREATED="1633201200396" MODIFIED="1633201210028"/>
<node TEXT="API Biblioteki Narodowej" ID="ID_1887344515" CREATED="1633201210193" MODIFIED="1633201215592"/>
</node>
<node TEXT="testy" POSITION="right" ID="ID_1401736301" CREATED="1629383005379" MODIFIED="1636035723429">
<edge COLOR="#7c7c00"/>
<node TEXT="zasady" ID="ID_1111186491" CREATED="1630936650178" MODIFIED="1630936651734">
<node TEXT="Na potrzeby testów należy wypełnić bazę danymi wygenerowanymi przez moduł faker." LOCALIZED_STYLE_REF="defaultstyle.details" ID="ID_1986445917" CREATED="1629383013175" MODIFIED="1634931622597">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Testy pisać razem z kodem (po zrobieniu projektu)." ID="ID_1129021365" CREATED="1630408184273" MODIFIED="1630408200273"/>
<node TEXT="Korzystać referencyjnie z jakiejś książki na temat testowania aplikacji w Python." ID="ID_115322150" CREATED="1630408153106" MODIFIED="1630408173693"/>
</node>
<node TEXT="testy bazy danych" ID="ID_1146073976" CREATED="1630936654644" MODIFIED="1630936665680">
<node TEXT="Jak będą działały klucze kompozytowe? Czy unikatowa musi być wartość obu pól czy wartości każdego pola osobno?" ID="ID_1029459100" CREATED="1630936666133" MODIFIED="1630936668685"/>
</node>
</node>
<node TEXT="uwagi" POSITION="right" ID="ID_1932769928" CREATED="1629215781400" MODIFIED="1636035723435">
<edge COLOR="#ff0000"/>
<node TEXT="Skąd wziąć dane do tej bazy?" ID="ID_933458772" CREATED="1629215783916" MODIFIED="1629215793865">
<node TEXT="Pracowicie powprowadzać samemu." ID="ID_1916821586" CREATED="1629215828460" MODIFIED="1629215835225"/>
<node TEXT="Poszukać w sieci gotowe zbiory (autorów, czasopism etc.)" ID="ID_1834697997" CREATED="1629215836125" MODIFIED="1629215869608"/>
</node>
<node TEXT="Pisać wg. rozwiązań przedstawionych w podręczniku do Flaska (blueprints, factory function etc.)" ID="ID_1201784246" CREATED="1629218232088" MODIFIED="1629218256245"/>
<node TEXT="pola opisów wg. ISBD i MARC-a" ID="ID_1138904124" CREATED="1629213476826" MODIFIED="1629213487128"/>
<node TEXT="wygląd z samym Bootstrapem (moduły dostarczone z Flaskiem)" ID="ID_484553024" CREATED="1629380143790" MODIFIED="1629380163216"/>
<node TEXT="szczegóły obsługi błędów - w pliku flask.py (w pobliżu ValidationError)" ID="ID_874962225" CREATED="1629882546041" MODIFIED="1629882577024"/>
<node TEXT="Rozmiary pól muszą być udostępniane szablonom html - tak, żeby w razie zmiany rozmiaru pola w modelu było to odzwierciedlon w kodzie html z szablonu: ograniczenie długości wprowadzanych danych." ID="ID_1872531727" CREATED="1630952945536" MODIFIED="1630953280369"/>
<node TEXT="Serię można dodać jako osobny dokument w relacji lub zapisać w polu &quot;series&quot;." ID="ID_1328673962" CREATED="1630963940307" MODIFIED="1630963970997"/>
<node TEXT="Wyświetlanie komunikatów, zmiany w interfejsie (na stronach, reakcje programu na wybór poszczególnych opcji, kliknięcia przycisków, linków etc.) - opisać na diagramie automatu skończonego." ID="ID_1053619492" CREATED="1629380606296" MODIFIED="1629380653976"/>
<node TEXT="Napisać use stories." ID="ID_1473096723" CREATED="1629979628688" MODIFIED="1629979640485"/>
<node TEXT="Czego będę potrzebował" ID="ID_132245771" CREATED="1629979799667" MODIFIED="1629979805176">
<node TEXT=".query.count()" ID="ID_1411578835" CREATED="1629979807027" MODIFIED="1629979814948">
<node TEXT="liczy rekordy" ID="ID_1975222968" CREATED="1629979814955" MODIFIED="1629979818665"/>
</node>
<node TEXT="tabele asocjacyjne w relacjach many-to-many (w pliku źródłowym z notatkami)" ID="ID_424109971" CREATED="1629980053593" MODIFIED="1629980078462"/>
</node>
<node TEXT="Pilnować, żeby długość pól na formularzach była taka sama jak w bd - być może należy ją w strukturach danych z których będą korzystały i konstruktory modelów i view-functions?" ID="ID_989139041" CREATED="1630609546666" MODIFIED="1630609753958"/>
<node TEXT="prototyp wireframe zrobić przy pomocy programu do diagramów, np. Yed" ID="ID_391195122" CREATED="1631217692147" MODIFIED="1631217715081"/>
</node>
<node TEXT="Pod koniec pracy gałąź z opisem projektu wyeksportować do podkatalogu design w katalogu design." POSITION="right" ID="ID_822833738" CREATED="1630938363382" MODIFIED="1636035723436">
<edge COLOR="#0000ff"/>
</node>
<node TEXT="uporządkowanie funkcji dla tras: wg alfabetu a w ramach grup (np. dla detali języka i listy języków) - najpierw lista, potem detale" POSITION="right" ID="ID_1749744190" CREATED="1634920713423" MODIFIED="1636035723437">
<edge COLOR="#00ff00"/>
<node TEXT="warto też oddzielić funkcje interfejsu ogólniedostępnego od tras dla edytorów" ID="ID_1832321193" CREATED="1634920769709" MODIFIED="1634920804891"/>
</node>
<node TEXT="wrócić do projektowania - diagramy stanów dla widoków: gdzie przechodzę po kliknięciu elementu etc." FOLDED="true" POSITION="right" ID="ID_1890833320" CREATED="1634236008566" MODIFIED="1636035723439">
<edge COLOR="#ff00ff"/>
<node TEXT="niektóre notatki wyrazić w use-cases, use stories i diagramach" ID="ID_1872060402" CREATED="1635109626770" MODIFIED="1635273262428">
<font BOLD="false"/>
</node>
<node TEXT="Strona z trasy responsibility_details odsyła do list osób/ciał zbiorowych zawierających te oznaczenia odpowiedzialności. Od trasy responsibility_details do tych stron (osób i ciał zbiorowych) powinny być wywoływane funkcje tworzące te listy, co wymaga zmiany tych funkcji - żeby w kwerendach pobierały tylko listy osób/ciał zbiorowych zawierające te oznaczenia odpowiedzialności (responsibilities)." ID="ID_1631830890" CREATED="1635156993927" MODIFIED="1635242959938">
<icon BUILTIN="button_ok"/>
<node TEXT="Zaprojektować przejścia diagramem stanów, ew. interakcji oraz zaprojektować zmiany w tych funkcjach." ID="ID_1531008171" CREATED="1635157134769" MODIFIED="1635157159218"/>
<node TEXT="Strona dla listy osób musi dziedziczyć z &quot;base.html&quot; i mieć własną paginację." ID="ID_1197785861" CREATED="1635201052923" MODIFIED="1635242943430">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Podobna zależność między ciałami zbiorowymi &lt; -- &gt; oznaczeniami odpowiedzialności." ID="ID_608736603" CREATED="1635244662981" MODIFIED="1635244684995"/>
</node>
<node TEXT="Jak mógłbym zrobić listę szeregowaną alfabetycznie od A lub w dół od końca?" ID="ID_350553436" CREATED="1635200142366" MODIFIED="1635200170743">
<node TEXT="Jakieś parametry musiałbym przekazać do hiperłączy w dolnej paginacji. Jakie?" ID="ID_367683664" CREATED="1635200172751" MODIFIED="1635200237275">
<node TEXT="Można te parametry przekazywać do makra robiącego paginację." ID="ID_883809692" CREATED="1635200827406" MODIFIED="1635200839509"/>
</node>
</node>
<node TEXT="use-cases powinny być w formie: &quot;użytkownik przegląda listę dokumentów&quot; -&gt; interakcje do wyświetlenia listy etc.; &quot;użytkownik przegląda rekord: dokumentu etc&quot; -&gt; diagramy stanu/sekwencyjne co w tym widoku się dzieje (i w tej formie dodać)" ID="ID_157932975" CREATED="1635107906782" MODIFIED="1635108102464"/>
<node TEXT="projekt hiperłączy dla liter alfabetu" ID="ID_95889094" CREATED="1635244753955" MODIFIED="1635285523429">
<font BOLD="false"/>
</node>
</node>
<node TEXT="draft - aktualne zadanie:" POSITION="left" ID="ID_1122590423" CREATED="1631875920852" MODIFIED="1636035723316">
<font BOLD="true"/>
<edge COLOR="#ff0000"/>
<node TEXT="zaprojektować listę dokumentów" ID="ID_27005830" CREATED="1634932507217" MODIFIED="1635505194090">
<font BOLD="false"/>
<node TEXT="Jak resetować filtr dokumentów (w widoku listy dokumentów) przy przechodzeniu między stronami? (jeżeli nie jest to paginacja)." ID="ID_1510763130" CREATED="1636040460608" MODIFIED="1636041238857">
<font BOLD="true"/>
<node TEXT="Ręcznie poprzez przycisk na stronie" ID="ID_1640878452" CREATED="1636041227412" MODIFIED="1636041235484"/>
<node TEXT="zapisać argumenty kargs - jeżeli się różnią," ID="ID_1873386970" CREATED="1636041467663" MODIFIED="1636041485993"/>
<node TEXT="zapisanie id typów dokumentów w URL" ID="ID_847683826" CREATED="1636041903672" MODIFIED="1636041917426"/>
</node>
<node TEXT="Jak aplikacja ma zachowywać pozycje które były zaznaczone na liście typów dokumentów (formularzu) przy przechodzeniu pomiędzy stronami paginacji?" ID="ID_423374964" CREATED="1635878017947" MODIFIED="1636039906084">
<font BOLD="false"/>
<node TEXT="" ID="ID_658749521" CREATED="1635879002592" MODIFIED="1635879002593">
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="użycie jakichś obiektów globalnych?" ID="ID_823816640" CREATED="1635880005749" MODIFIED="1635880006580">
<node TEXT="session" ID="ID_321620381" CREATED="1635880620203" MODIFIED="1636039904778">
<font BOLD="false"/>
<node TEXT="ciastka mogę kasować przy wejściu na stronę - jeżeli w url nie ma ?page= (chyba przy pomocy JS)" ID="ID_575133979" CREATED="1635886036355" MODIFIED="1635886068468"/>
</node>
</node>
<node TEXT="Po stronie serwera." ID="ID_1692476151" CREATED="1635878776837" MODIFIED="1635878782111"/>
<node TEXT="Po stronie przeglądarki: ciastka." ID="ID_1136742078" CREATED="1635878783314" MODIFIED="1635878791571"/>
<node TEXT="" ID="ID_459123520" CREATED="1635879002568" MODIFIED="1635879002592">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="nie można odróżnić przejść między stronami przy pomocy dolnej paginacji od wyjścia ze strony - przez co zaznaczenia zostaną zapamiętane nawet jak wrócę tam po pewnym czasie (a powinny zostać zapamiętane tylko kiedy przechodzę pomiędzy stronami przy pomocy dolnej paginacji)" ID="ID_1538447759" CREATED="1635879002593" MODIFIED="1635879188369"/>
</node>
<node TEXT="Użycie AJAX-a" ID="ID_40865297" CREATED="1635878974732" MODIFIED="1635878980250">
<node TEXT="wymagałoby przebudowy paginacji" ID="ID_957130091" CREATED="1635878980284" MODIFIED="1635878985745"/>
<node TEXT="mogę to zrobić w późniejszej wersji" ID="ID_26862344" CREATED="1635879216787" MODIFIED="1635879224692"/>
</node>
<node TEXT="Użycie metody GET i czytanie URL" ID="ID_1982594876" CREATED="1635880083888" MODIFIED="1635880145660">
<node TEXT="będzie przesyłało tokeny etc." ID="ID_792435614" CREATED="1635880237791" MODIFIED="1635880245658"/>
<node TEXT="Czy da się w ten sposób przesłać tylko część danych?" ID="ID_1327428292" CREATED="1635880245854" MODIFIED="1635880257991"/>
</node>
</node>
<node TEXT="dopisywać kolejne kwerendy (wg. schematu interakcji) wraz z testami tych tras: każda nowa kwerenda - test" ID="ID_1716623346" CREATED="1635975150407" MODIFIED="1635975210562"/>
<node TEXT="poprawić funkcję wyświetlającą listę dokumentów i kwerendy w niej (refactoring)" ID="ID_1195185219" CREATED="1635874224975" MODIFIED="1635877994293">
<node TEXT="które elementy w funkcji wyświetlającej listę dokumentów będą się powtarzały - do klasy abstrakcyjnej" ID="ID_238175533" CREATED="1635854646578" MODIFIED="1635860243486">
<font BOLD="false"/>
</node>
</node>
<node TEXT="pisać testy dla widoków - inaczej pisanie pozostałych elementów i poprawianie kodu będzie bardzo trudne" ID="ID_140828065" CREATED="1635444751407" MODIFIED="1635874035252">
<font BOLD="false"/>
</node>
<node TEXT="interakcje między trasami a listą dokumentów:" ID="ID_1041189173" CREATED="1635341910972" MODIFIED="1635878750932">
<font BOLD="false"/>
<node TEXT="Odsyłacze ze stron prowadzące do listy dokumentów - diagramy interakcji z parametrami wejścia/wyjścia:" ID="ID_1122914884" CREATED="1635341949704" MODIFIED="1635341949704">
<node TEXT="typ dokumentu (document type) - szczegóły:" ID="ID_1989357902" CREATED="1635341949704" MODIFIED="1635364545706">
<font BOLD="false"/>
<node TEXT="- dokumenty (określonego typu dokumentu, np. typu &quot;book&quot; - entry_type=&apos;document_type&apos;)" ID="ID_1289212153" CREATED="1635341949704" MODIFIED="1635409591143">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="parametry:" ID="ID_1017957855" CREATED="1635343979254" MODIFIED="1635343983328">
<node TEXT="id typu dokumentu (nazwa typu - jeżeli są unikatowe)" ID="ID_491287142" CREATED="1635344115467" MODIFIED="1635345098528"/>
</node>
</node>
<node TEXT="ciało zbiorowe - szczegóły:" ID="ID_611848888" CREATED="1635341949704" MODIFIED="1635364510490">
<font BOLD="false"/>
<node TEXT="- dokumenty dla których ciało zbiorowe jest tematem" FOLDED="true" ID="ID_293334386" CREATED="1635341949704" MODIFIED="1635363564292">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="parametry:" ID="ID_1982943015" CREATED="1635342122446" MODIFIED="1635342127476">
<node TEXT="id ciała zbiorowego -&gt; &apos;documents_topics&apos;" ID="ID_40562216" CREATED="1635342112973" MODIFIED="1635346130654"/>
</node>
</node>
<node TEXT="- responsibility (dokumenty w których to ciało zbiorowe pełni określoną funkcję-responsibility)" ID="ID_1277858373" CREATED="1635341949704" MODIFIED="1635342101195">
<node TEXT="parametry:" ID="ID_1184627384" CREATED="1635342060542" MODIFIED="1635342064916">
<node TEXT="id funkcji-oznaczenia odpowiedzialności (responsibility id)" ID="ID_585524161" CREATED="1635342102813" MODIFIED="1635342328981"/>
<node TEXT="id ciała zbiorowego" ID="ID_760843563" CREATED="1635342112973" MODIFIED="1635342308738"/>
</node>
<node TEXT="osobna funkcja ?" ID="ID_956133937" CREATED="1635345884082" MODIFIED="1635345955085"/>
</node>
</node>
<node TEXT="+ lokalizacje geograficzne (geographic locations) - lista i strona szczegółów:" ID="ID_126012620" CREATED="1635341949704" MODIFIED="1635345333519">
<node TEXT="- dokumenty opublikowane w danej lokalizacji (documents published)" ID="ID_1403634393" CREATED="1635341949704" MODIFIED="1635345220134">
<node TEXT="parametry:" ID="ID_1638873033" CREATED="1635345438625" MODIFIED="1635345441385">
<node TEXT="id lokalizacji" ID="ID_264455061" CREATED="1635345447635" MODIFIED="1635345450862"/>
</node>
</node>
<node TEXT="- dokumenty dla których dana lokalizacja jest tematem (documents-topic)" ID="ID_1154558088" CREATED="1635341949704" MODIFIED="1635345213057">
<node TEXT="parametry:" ID="ID_1593616814" CREATED="1635345702803" MODIFIED="1635345705748">
<node TEXT="id lokalizacji -&gt; &apos;documents_topics&apos;" ID="ID_1389253584" CREATED="1635345705776" MODIFIED="1635345728449"/>
</node>
</node>
</node>
<node TEXT="+ słowa kluczowe: lista i szczegóły:" FOLDED="true" ID="ID_982302896" CREATED="1635341949704" MODIFIED="1635341949704">
<node TEXT="- dokumenty dla których dane słowo jest" FOLDED="true" ID="ID_1505023372" CREATED="1635341949704" MODIFIED="1635341949704">
<node TEXT="tematem" ID="ID_936285502" CREATED="1635341949704" MODIFIED="1635341949704"/>
</node>
</node>
<node TEXT="+ Języki - szczegóły:" FOLDED="true" ID="ID_1474663104" CREATED="1635341949704" MODIFIED="1635341949704">
<node TEXT="- dokumenty opublikowane w danym języku" ID="ID_1946420597" CREATED="1635341949704" MODIFIED="1635341949704"/>
<node TEXT="- dokumenty dla których jest to język oryg." ID="ID_1789115459" CREATED="1635341949704" MODIFIED="1635341949704"/>
<node TEXT="- dokumenty dla których dany język jest" FOLDED="true" ID="ID_227171231" CREATED="1635341949704" MODIFIED="1635341949704">
<node TEXT="tematem" ID="ID_1084123011" CREATED="1635341949704" MODIFIED="1635341949704"/>
</node>
</node>
<node TEXT="+ Nazwy osobowe - szczegóły:" FOLDED="true" ID="ID_1696639014" CREATED="1635341949704" MODIFIED="1635341949704">
<node TEXT="- responsibility (dokumenty w których osoba" FOLDED="true" ID="ID_236843257" CREATED="1635341949704" MODIFIED="1635341949704">
<node TEXT="pełni określoną funkcję -" ID="ID_1257786119" CREATED="1635341949704" MODIFIED="1635341949704"/>
<node TEXT="parametrem jest id funkcji i osoby)" ID="ID_1098066145" CREATED="1635341949704" MODIFIED="1635341949704"/>
</node>
<node TEXT="- dokumenty, w których dana osoba jest" FOLDED="true" ID="ID_574207488" CREATED="1635341949704" MODIFIED="1635341949704">
<node TEXT="tematem dokumentu" ID="ID_1381342430" CREATED="1635341949704" MODIFIED="1635341949704"/>
</node>
</node>
</node>
<node TEXT="czy poszczególne kwerendy mogą mieć własne view-functions?" ID="ID_121689746" CREATED="1635342659768" MODIFIED="1635342889735">
<node TEXT="jeżeli nie będę powtarzał w nich zbyt wiele kodu" ID="ID_245631512" CREATED="1635342685257" MODIFIED="1635342695472"/>
<node TEXT="Niektóre mogą mieć ale nie wszystkie." ID="ID_1165093271" CREATED="1635345373718" MODIFIED="1635345382536">
<node TEXT="prostsze kwerendy mogą być przetwarzane w jednej funkcji" ID="ID_920240721" CREATED="1635345840276" MODIFIED="1635345850857"/>
<node TEXT="bardziej złożone - w wielu" ID="ID_682400309" CREATED="1635345851203" MODIFIED="1635345857594"/>
</node>
<node TEXT="jedna funkcja dla wielu wyszukiwań:" ID="ID_1557895668" CREATED="1635345488421" MODIFIED="1635345495234">
<node TEXT="pobiera wartości dla wszystkich parametrów i używa wzorca dopasowań, np. w słowniku dla utworzenia konkretnej kwerendy" ID="ID_967763757" CREATED="1635345495261" MODIFIED="1635345549624"/>
</node>
</node>
<node TEXT="oryginał notatki:" FOLDED="true" ID="ID_441910303" CREATED="1635341964221" MODIFIED="1635341968592">
<node TEXT="Odsyłacze ze stron prowadzące do listy dokumentów - diagramy interakcji z parametrami wejścia/wyjścia:&#xa; + ciało zbiorowe - szczegóły:&#xa;   - responsibility (dokumenty w których to&#xa;     ciało zbiorowe pełni określoną funkcję -&#xa;     parametrem jest id funkcji i c.zbiorowego)&#xa;   - dokumenty dla których ciało zbiorowe jest&#xa;     tematem&#xa; + typ dokumentu (document type) - szczegóły:&#xa;   - dokumenty (określonego typu dokumentu,&#xa;     np. typu &quot;book&quot;)&#xa; + lokalizacje geograficzne (geographic&#xa;   locations) - lista:&#xa;   - dokumenty opublikowane w danej lokalizacji&#xa;     (documents published)&#xa;   - dokumenty dla których dana lokalizacja&#xa;     jest tematem (documents-topic)&#xa; + lokalizacje geograficzne (geographic&#xa;   locations) - szczegóły lokalizacji:&#xa;   - j.w. (powtórzenie linków)&#xa; + słowa kluczowe: lista i szczegóły:&#xa;   - dokumenty dla których dane słowo jest&#xa;     tematem&#xa; + Języki - szczegóły:&#xa;   - dokumenty opublikowane w danym języku&#xa;   - dokumenty dla których jest to język oryg.&#xa;   - dokumenty dla których dany język jest&#xa;     tematem&#xa; + Nazwy osobowe - szczegóły:&#xa;   - responsibility (dokumenty w których osoba&#xa;     pełni określoną funkcję -&#xa;     parametrem jest id funkcji i osoby)&#xa;   - dokumenty, w których dana osoba jest&#xa;     tematem dokumentu" ID="ID_1546401452" CREATED="1635341930317" MODIFIED="1635341938399"/>
</node>
</node>
<node TEXT="poszczególne hiperłącza z widoków, np. języków, powinny odsyłać do listy dokumentów - funkcja wyświetlająca listę powinna przyjmować odpowiednie argumenty" ID="ID_772507477" CREATED="1634932525312" MODIFIED="1634932760283">
<node TEXT="wszystkie opcje rozpisać na diagramach" ID="ID_287786279" CREATED="1634932760306" MODIFIED="1634932769469"/>
</node>
<node TEXT="Lista dokumentów" ID="ID_568001826" CREATED="1634497996440" MODIFIED="1634498000606">
<node TEXT="jakie parametry powinna przyjmować funkcja tworząca listę dokumentów:" ID="ID_623761250" CREATED="1634650086080" MODIFIED="1634658283658">
<node TEXT="hiperłącze z widoku osoby" ID="ID_388018853" CREATED="1634650105512" MODIFIED="1634650143358">
<node TEXT="wg. funkcji" ID="ID_1149865242" CREATED="1634650144333" MODIFIED="1634650145158">
<node TEXT="id osoby, id funkcji" ID="ID_1395696714" CREATED="1634650125857" MODIFIED="1635270835568"/>
</node>
<node TEXT="wg. tematu (dokumenty dla których osoba jest tematem)" ID="ID_1462891490" CREATED="1634650147566" MODIFIED="1634650217707"/>
</node>
<node TEXT="słowa kluczowe" ID="ID_1452758786" CREATED="1634672368281" MODIFIED="1634672370386">
<node TEXT="widok słowa kluczowego" ID="ID_625786113" CREATED="1634651628897" MODIFIED="1634651633555">
<node TEXT="odsyła do listy dokumentów do których to słowo przypisano" ID="ID_615401112" CREATED="1634651633578" MODIFIED="1634669007006"/>
</node>
<node TEXT="widok listy słów kluczowych" ID="ID_1576422645" CREATED="1634672337638" MODIFIED="1634672345656">
<node TEXT="obok każdego słowa - dodać link do referencjonowanych dokumentów" ID="ID_538274096" CREATED="1634672345679" MODIFIED="1634672365232"/>
</node>
</node>
</node>
<node TEXT="Jak zaprojektuję pozostałe widoki, zrobić funkcję, która będzie tworzyła odpowiednią kwerendę z argumentów którą ta lista otrzyma." ID="ID_1345568748" CREATED="1634647267761" MODIFIED="1634647295068"/>
<node TEXT="Jeżeli wyświetlę profil osoby i w tym widoku będę miał hiperłącze z listą dokumentów w których: ta osoba jest przedmiotem; posiada funkcję (autor etc.). Po kliknięciu przeniosę się na listę tych dokumentów. Czy dla tych list (i listy wszystkich dokumentów z &apos;Browse/documents&apos;) da się zrobić: jeden szablon i jedną view function?" ID="ID_1620901373" CREATED="1634575203460" MODIFIED="1634583324828">
<node TEXT="rozpisać to na diagramie" ID="ID_418475903" CREATED="1634575386228" MODIFIED="1634575392204"/>
<node TEXT="Funkcja dla trasy musi pobierać odpowiednie parametry dla kwerendy (z URL - generowany funkcją url_for; parametr pobierany przy pomocy request.args.get) - na podstawie tych parametrów powstanie odpowiednia kwerenda a potem te parametry trzeba przekazać do makra tworzącego paginację." ID="ID_1140698634" CREATED="1634635786809" MODIFIED="1635271120240"/>
<node TEXT="można zastosować odpowiednie filtry w kwerendzie i dynamiczne części kwerendy, np. tworzone z użyciem funkcji" ID="ID_665430857" CREATED="1635265777706" MODIFIED="1635265813277"/>
<node TEXT="interakcje:" ID="ID_1767833985" CREATED="1634637856780" MODIFIED="1634637859709">
<node TEXT="hiperłącze z responsibility na stronie osoby (np. author) odsyła na listę dokumentów (z parametrem dla kwerendy)" ID="ID_1092621047" CREATED="1634637803589" MODIFIED="1634637855808"/>
</node>
</node>
<node TEXT="Co się stanie, jeżeli będę chciał wyświetlić na liście dokumentów dokument, który nie ma przypisanego typu?" ID="ID_1824182255" CREATED="1635887032652" MODIFIED="1635887054375"/>
<node TEXT="Kryteria wyświetlania (artykuły, książki etc.) mają być pobierane z listy typów dokumentów; to jak będą przetwarzane na paginowaną listę powinno zostać uogólnione i możliwe do zastosowania w innych szablonach." ID="ID_1239270300" CREATED="1634299255167" MODIFIED="1634299322064">
<node TEXT="Tadzik jest studentem literaturoznawstwa i chciałby skorzystać z aplikacji bibliograficznej w celu wyszukania wśród skatalogowanych książek egzemplarzy wydanych w latach 1995-1996. W tym celu korzysta z listy dokumentów. W filtrach zaznacza interesujący go zakres lat wydania oraz typ dokumentu &quot;książka&quot; (book). W celu uzupełnienia wyszukiwania, może skorzystać z dodatkowych filtrów: wybrać osoby pełniące w dokumencie określoną funkcję (np. autora); instytucję - np. wydawcę; temat dokumentu - słowo kluczowe, instytucję, osobę itd. - spośród kategorii, które mogą stać się tematem. Wyboru dokonuje w okienkach modalnych umożliwiających wyszukanie interesujących go terminów." ID="ID_583863172" CREATED="1635269606214" MODIFIED="1635270702747">
<node TEXT="interfejs zaprojektować diagramem stanów" ID="ID_602873862" CREATED="1635270436092" MODIFIED="1635270442853"/>
</node>
</node>
</node>
<node TEXT="dopisać typy dokumentów do szablonu listy dokumentów" ID="ID_1404569177" CREATED="1635860244801" MODIFIED="1635873519424">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
</node>
</node>
<node TEXT="napisać testy" ID="ID_1252667547" CREATED="1634676737843" MODIFIED="1634931662537" LINK="#ID_1401736301">
<node TEXT="widoki" FOLDED="true" ID="ID_773548487" CREATED="1635973028732" MODIFIED="1635973032233">
<node TEXT="dla wszystkich" ID="ID_725839855" CREATED="1635973383808" MODIFIED="1635973386625">
<node TEXT="sprawdzić czy wyskakują pod określonymi trasami strony (200)" ID="ID_1066228768" CREATED="1634720912962" MODIFIED="1635973418532"/>
<node TEXT="czy w wypadku podania błędnej trasy (np. id poza zakresem) wyskakuje 404" ID="ID_1622901513" CREATED="1634720925029" MODIFIED="1634720942308"/>
</node>
<node TEXT="osoby" ID="ID_1448106474" CREATED="1634676744996" MODIFIED="1635972736792">
<node TEXT="Testy dla listy:" ID="ID_556699425" CREATED="1634232029410" MODIFIED="1634232078013"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Wprowadzić tu jakie testy będę przeprowadzał.
    </p>
  </body>
</html>
</richcontent>
<node TEXT="sprawdza czy trasa istnieje (kod 200)" ID="ID_1788097683" CREATED="1635972556627" MODIFIED="1635972568325">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="czy wszystkie osoby i warianty ich nazw zostaną zwrócone przez kwerendę (prawidłowa liczba wpisów na liście paginowanej - suma osób i wariantów nazw)" ID="ID_1331395732" CREATED="1634635434343" MODIFIED="1635522729200">
<icon BUILTIN="button_ok"/>
<node TEXT="czy nazwa się nigdy nie powtarza" ID="ID_1597749098" CREATED="1635513441409" MODIFIED="1635522730652">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="zrobić kwerendę tylko dla osób; czy lista zwróci listę wszystkich osób (tylko osób)" ID="ID_1793470990" CREATED="1635971741642" MODIFIED="1635971784823"/>
<node TEXT="zrobić kwerendę tylko dla wariantów; czy lista zwróci wszystkie warianty" ID="ID_575846585" CREATED="1635971761543" MODIFIED="1635971795346"/>
</node>
<node TEXT="sprawdzić czy lista wyświetla imiona i nazwiska (a nie np. puste pola)" ID="ID_1943921624" CREATED="1635972488933" MODIFIED="1635972502355">
<node TEXT="wylosować paru ludzi" ID="ID_903156282" CREATED="1635972598597" MODIFIED="1635972620661"/>
<node TEXT="wyszukać ich na liście wg. formatu wyświetlania (nazwisko, imię)" ID="ID_49095528" CREATED="1635972622647" MODIFIED="1635972637216"/>
</node>
<node TEXT="Czy w hiperłączu od oznaczenia odpowiedzialności (&quot;responsibility&quot;), na liście osób zostaną wyświetlone wszystkie osoby z danym oznaczeniem odpowiedzialności (w tym - taka sama liczba)?" ID="ID_1092998055" CREATED="1635243609377" MODIFIED="1635243656193">
<node TEXT="Utworzyć responsibilities, parę osób" ID="ID_1203429095" CREATED="1635969929646" MODIFIED="1635970263362"/>
<node TEXT="utworzyć dokument" ID="ID_1715758074" CREATED="1635970263822" MODIFIED="1635970290544">
<node TEXT="dodać do niego jedno oznaczenie odpowiedzialności" ID="ID_878049597" CREATED="1635970249800" MODIFIED="1635970456953"/>
<node TEXT="pobrać od oznaczania odpowiedzialności osobę" ID="ID_1113752498" CREATED="1635970292762" MODIFIED="1635970396766"/>
<node TEXT="sprawdzić czy trasa dla browse_people z id tego ozn. odpowiedzialności wykaże tą osobę i będzie to jedyna osoba" ID="ID_1710442296" CREATED="1635970397211" MODIFIED="1635971179304"/>
</node>
<node TEXT="utworzyć dokument" ID="ID_1751824048" CREATED="1635970559755" MODIFIED="1635971268629">
<node TEXT="dodać do niego kilka różnych osób z tym samym oznaczeniem odpowiedzialności" ID="ID_1035753158" CREATED="1635971273351" MODIFIED="1635971496772"/>
<node TEXT="pobrać to oznaczenie odpowiedzialności" ID="ID_464129131" CREATED="1635971309333" MODIFIED="1635971316113"/>
<node TEXT="sprawdzić czy lista osób z linkiem (z id tego oznaczenia odpowiedzialności) zostanie wyświetlona przez trasę (oraz tylko ta lista oraz czy każda osoba wystąpi tylko raz)" ID="ID_62104505" CREATED="1635971501654" MODIFIED="1635971685425"/>
</node>
</node>
</node>
</node>
<node TEXT="ciała zbiorowe" ID="ID_1551264746" CREATED="1635971890954" MODIFIED="1635972748742">
<node TEXT="lista" ID="ID_1653591893" CREATED="1635972750296" MODIFIED="1635972752322">
<node TEXT="testy podobne do listy osób" ID="ID_898596990" CREATED="1635971898949" MODIFIED="1635971902900"/>
</node>
<node TEXT="szczegóły" ID="ID_376250986" CREATED="1635974305138" MODIFIED="1635974308032">
<node TEXT="zawiera nazwę, id" ID="ID_1445153325" CREATED="1635974313765" MODIFIED="1635974318736"/>
<node TEXT="właściwe hiperłącza" ID="ID_1856504334" CREATED="1635974368997" MODIFIED="1635974373186"/>
</node>
</node>
<node TEXT="typy dokumentów" ID="ID_135892517" CREATED="1635972700357" MODIFIED="1635972704269">
<node TEXT="lista typów dokumentów" ID="ID_1138787835" CREATED="1635972043068" MODIFIED="1635972069627">
<node TEXT="czy wyświetla wszystkie typy dokumentów" ID="ID_1885343884" CREATED="1635972089405" MODIFIED="1635972096169"/>
<node TEXT="czy linki od typu dokumentów prowadzą do właściwych stron ze szczegółami" ID="ID_1007801017" CREATED="1635972688821" MODIFIED="1635972729335"/>
</node>
<node TEXT="szczegóły" ID="ID_110573553" CREATED="1635972783401" MODIFIED="1635972787111">
<node TEXT="czy na stronie ze szczegółami znajdują się nazwa typu i numer id" ID="ID_490441251" CREATED="1635972787140" MODIFIED="1635972834404"/>
</node>
</node>
<node TEXT="lokalizacje geograficzne" ID="ID_139144295" CREATED="1635973046346" MODIFIED="1635973051142">
<node TEXT="lista" ID="ID_870608590" CREATED="1635973123196" MODIFIED="1635973124545">
<node TEXT="czy wyświetla nazwy w odpowiednim formacie" ID="ID_1247305421" CREATED="1635973128683" MODIFIED="1635973169827"/>
<node TEXT="czy zawiera hiperłącza i czy hiperłącza prowadzą do właściwych stron ze szczegółami" ID="ID_657693295" CREATED="1635973170124" MODIFIED="1635973189274"/>
</node>
<node TEXT="szczegóły" ID="ID_1446758087" CREATED="1635973244859" MODIFIED="1635973247263">
<node TEXT="czy strona zawiera nazwę lokalizacji i id" ID="ID_1885415045" CREATED="1635973247287" MODIFIED="1635973261085"/>
</node>
</node>
<node TEXT="słowa kluczowe" ID="ID_987266010" CREATED="1635973765540" MODIFIED="1635973769219">
<node TEXT="lista" ID="ID_654028530" CREATED="1635973841458" MODIFIED="1635973842738">
<node TEXT="czy lista wyświetla słowa kluczowe w odpowiednim formacie" ID="ID_1370995388" CREATED="1635973769251" MODIFIED="1635973832191"/>
</node>
<node TEXT="szczegóły" ID="ID_1929840595" CREATED="1635973852948" MODIFIED="1635973854956">
<node TEXT="czy strona zawiera nazwę i id słowa" ID="ID_1808459002" CREATED="1635973855811" MODIFIED="1635973861809"/>
</node>
</node>
<node TEXT="języki" ID="ID_1367937479" CREATED="1635973886916" MODIFIED="1635973889349">
<node TEXT="lista" ID="ID_1436752548" CREATED="1635973889376" MODIFIED="1635973890496">
<node TEXT="czy wpisy na liście są wyświetlane w odpowiednim formacie" ID="ID_418562392" CREATED="1635973893795" MODIFIED="1635973906417"/>
</node>
<node TEXT="szczegóły" ID="ID_1536215784" CREATED="1635973890787" MODIFIED="1635973892638">
<node TEXT="czy strona zawiera nazwę języka i id" ID="ID_1898407359" CREATED="1635973947188" MODIFIED="1635973954131"/>
</node>
</node>
<node TEXT="oznaczenia odpowiedzialności" ID="ID_1014789026" CREATED="1635974013299" MODIFIED="1635974018676">
<node TEXT="lista" ID="ID_1730595307" CREATED="1635974018706" MODIFIED="1635974020077">
<node TEXT="czy wyświetla elementy" ID="ID_1828715482" CREATED="1635974052195" MODIFIED="1635974061039"/>
</node>
<node TEXT="szczegóły" ID="ID_606719817" CREATED="1635974020390" MODIFIED="1635974022275">
<node TEXT="nazwa i id" ID="ID_55326008" CREATED="1635974106374" MODIFIED="1635974109877"/>
<node TEXT="czy przycisk obok &quot;Number of collective bodies with this responsibility:&quot; oraz &quot;Number of individuals...&quot; zawiera odpowiednie hiperłącza" ID="ID_1645875210" CREATED="1635974237139" MODIFIED="1635974277150"/>
</node>
</node>
</node>
<node TEXT="języki" ID="ID_387573057" CREATED="1634762145651" MODIFIED="1634766133727">
<node TEXT="losuje języki (1-3 - zapamiętuje liczbę)" ID="ID_1099156413" CREATED="1634762189713" MODIFIED="1634762207069"/>
<node TEXT="tworzy dokument bez języka jako tematu (test: 0 tematów-języków); losuje język, dodaje jako temat do dokumentu - test: 1 temat-język;" ID="ID_1263940716" CREATED="1634913260657" MODIFIED="1634913316093"/>
<node TEXT="dodaje je jako temat dokumentu" ID="ID_693906824" CREATED="1634762207410" MODIFIED="1634762213817"/>
<node TEXT="sprawdza, czy znajdują się w tematach dokumentu" ID="ID_39035674" CREATED="1634762249267" MODIFIED="1634762259655"/>
<node TEXT="sprawdza, czy od języka można dojść do dokumentu/ów (w których język jest tematem)" ID="ID_308756596" CREATED="1634762291170" MODIFIED="1634762318201"/>
<node TEXT="usuwa języki" FOLDED="true" ID="ID_1630978794" CREATED="1634762259891" MODIFIED="1634762290002">
<node TEXT="powinno kasować tylko wpisy w tabeli asocjacyjnej" ID="ID_1160533751" CREATED="1634766242841" MODIFIED="1634766253744"/>
</node>
</node>
<node TEXT="czy w dokumencie wszystkie elementy w &apos;relationship&apos; wskazują to, co wyświetlają (sprawdzić czy zgadza się wyświetlana nazwa albo inne pole not null, ale nie będące id)" ID="ID_1357381012" CREATED="1634897409441" MODIFIED="1634897560015"/>
<node TEXT="co się dzieje jeżeli brak jest elementów na liście do wyświetlenia?" FOLDED="true" ID="ID_1870566124" CREATED="1634758296631" MODIFIED="1634758317788">
<node TEXT="wyświetla szablon bez danych" ID="ID_1577514883" CREATED="1634759984782" MODIFIED="1634760002023"/>
</node>
<node TEXT="dokumenty" ID="ID_1358985312" CREATED="1635354962170" MODIFIED="1635354967719">
<node TEXT="czy dobrze będzie paginowało listę powstałą po odesłaniu od widoku szczegółów ciała zbiorowego do listy dokumentów dla których to ciało zb. jest tematem?" ID="ID_1783662983" CREATED="1635354968154" MODIFIED="1635355078929"/>
<node TEXT="czy lista paginowana zawiera tyle samo elementów co wyświetlane elementy na stronach szczegółów" ID="ID_1935188300" CREATED="1635366052993" MODIFIED="1635366133542"/>
<node TEXT="dla poszczególnych części funkcji documents_list" ID="ID_548993893" CREATED="1635443936132" MODIFIED="1635443952380"/>
<node TEXT="porównać listę dokumentów dla określonej funkcji jaką dane: osoba, ciało zbiorowe pełnią (w relacji-relationship) z listą dokumentów wygenerowaną przez funkcję documents_list" ID="ID_360930823" CREATED="1635444810992" MODIFIED="1635445065840"/>
</node>
<node TEXT="przypadki graniczne w testach - np. maksymalna liczba dokumentów/wpisów, 0 dokumentów/wpisów etc." ID="ID_1626676668" CREATED="1635366144419" MODIFIED="1635366169197"/>
<node TEXT="słowa kluczowe" FOLDED="true" ID="ID_512583578" CREATED="1634676821589" MODIFIED="1634676825002">
<node TEXT="czy prawidłowo referencjonuje dokumenty (liczba dokumentów ze słowem kluczowym)" ID="ID_1910755119" CREATED="1634677043765" MODIFIED="1634677064346"/>
</node>
<node TEXT="Jak projektować testy:" ID="ID_1970934263" CREATED="1635973064444" MODIFIED="1635973070874">
<node TEXT="najpierw ustalam co mam przetestować" ID="ID_155506756" CREATED="1635973070899" MODIFIED="1635973077630"/>
<node TEXT="piszę jak ten test ma wyglądać (opis w języku naturalnym lub pseudokodzie)" ID="ID_1169191315" CREATED="1635973078203" MODIFIED="1635973116364"/>
<node TEXT="jeżeli będę coś sprawdzał ręcznie - zapisać (co sprawdzam ręcznie) i napisać test automatyczny" ID="ID_325597234" CREATED="1635974146018" MODIFIED="1635974163784"/>
</node>
</node>
</node>
<node TEXT="paginacja widoku przeglądania" POSITION="left" ID="ID_1692035509" CREATED="1634201956980" MODIFIED="1636035723338">
<edge COLOR="#00ff00"/>
<node TEXT="osoby" ID="ID_1935367177" CREATED="1634294640028" MODIFIED="1634294643637"/>
<node TEXT="nazwy geograficzne" ID="ID_1877642994" CREATED="1634294645021" MODIFIED="1634294651924"/>
<node TEXT="słowa kluczowe" ID="ID_667584056" CREATED="1634294662097" MODIFIED="1634294671764"/>
<node TEXT="nazwy ciał zbiorowych" ID="ID_1996224387" CREATED="1634294677697" MODIFIED="1634294682146"/>
<node TEXT="dokumenty" ID="ID_1215632252" CREATED="1634294714194" MODIFIED="1634294717255"/>
<node TEXT="Zamiast filtra, pozostawić tylko listę liter z hiperłączami." ID="ID_71345221" CREATED="1634294525594" MODIFIED="1634297078957"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      zrobić to po dokumentach
    </p>
  </body>
</html>
</richcontent>
<node TEXT="Grupowanie wg. liter" ID="ID_1693062899" CREATED="1634294572603" MODIFIED="1634294608547">
<node TEXT="Grupowanie wpisów na stronie/w szablonie wg. liter alfabetu:&#xa;&#xa;+ pętla drukująca listę powinna drukować literę:&#xa; - na początku strony (jeżeli na poprzedniej nie ma wpisów na tą literę)&#xa; - przy przejściu od jednej litery do drugiej&#xa;&#xa;+ linki: hiperłącze od każdej litery powinno mnie odesłać do odpowiedniej strony na liście paginowanej&#xa; - kod funkcji powinien przeglądać/sprawdzać od której strony rozpoczyna się dana litera&#xa;&#xa;+ lista liter:&#xa; - moduł string, lista string.ascii_uppercase&#xa;&#xa;sprawdzić:&#xa;+ jak mogę przeglądać listę paginowaną&#xa;+ dokumentację tej metody" ID="ID_1333784630" CREATED="1634297065363" MODIFIED="1634297376758"/>
</node>
<node TEXT="Tadzik poszukuje informacji o książkach autora: Jana Nowaka-Kowalskiego. W tym celu w aplikacji bibliograficznej wybiera z menu: przeglądaj (browse) -&gt; nazwy osobowe (personal names). Wyświetla się stronicowana lista nazwisk w alfabetycznym porządku nazwisk, domyślnie rosnącym (A-Z). W górnej części listy znajduje się grupa hiperłączy w postaci liter alfabetu, odsyłających do konkretnej lokalizacji na liście: strony, gdzie nazwiska autorów rozpoczynają się od konkretnej litery. Aby ułatwić sobie przeglądanie, Tadzik klika na &quot;N&quot; po czym wyświetla mu się strona, na której rozpoczynają się nazwiska osób na tą literę." ID="ID_1130692478" CREATED="1635265917629" MODIFIED="1635268704674"/>
<node TEXT="Linki od litery powinny odsyłać do określonej grupy." ID="ID_244576480" CREATED="1634294577977" MODIFIED="1634294605142"/>
</node>
</node>
<node TEXT="gotowe" FOLDED="true" POSITION="left" ID="ID_269536781" CREATED="1631029724333" MODIFIED="1636035723453">
<icon BUILTIN="button_ok"/>
<edge COLOR="#00ffff"/>
<node TEXT="baza danych: role - pdr Flaska, 127-128" ID="ID_1658180478" CREATED="1632424641913" MODIFIED="1632482427427">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Uzupełnić o Role Assignment (s. 131) i przetestować." ID="ID_1374559586" CREATED="1632424641913" MODIFIED="1632482427426">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="+ dodać pozostałe pola do tabel (wg. ISDB)" ID="ID_708701964" CREATED="1630955928849" MODIFIED="1631029732312">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="+ dodać katalog projektu do Git-a" ID="ID_40277462" CREATED="1630955928849" MODIFIED="1631306677734">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="+ zaprojektować use-cases" FOLDED="true" ID="ID_1527010077" CREATED="1630955928850" MODIFIED="1631306679690">
<icon BUILTIN="button_ok"/>
<node TEXT="Projektować wg. tego, co mam w bazie danych (np. &quot;przeszukiwanie bd wg. tematu-nazwy geograficznej będącej przedmiotem dokumentu&quot;, &quot;wyświetlenie liczby lokalizacji&quot; -&gt; &quot;wyświetlenie lokalizacji użytych jako tematy + liczba dokumentów dla każdej lokalizacji&quot;" ID="ID_1423201180" CREATED="1630955954060" MODIFIED="1630956100121"/>
</node>
<node TEXT="+ zmienić nazwy pól w tabelach bibliografii: comments -&gt; note" ID="ID_673552379" CREATED="1630955928849" MODIFIED="1631307489197">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="w join tables pola łączące tabele powinny tworzyć klucz kompozytowy" ID="ID_58755640" CREATED="1630935954127" MODIFIED="1632315559644">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="wprowadzić bazę danych do aplikacji i napisać jej testy (kwerendy, dodawanie rekordów etc.)" FOLDED="true" ID="ID_1077153561" CREATED="1631307547014" MODIFIED="1632315530478">
<icon BUILTIN="button_ok"/>
<node TEXT="+ Jak będą działały klucze kompozytowe? Czy unikatowa musi być wartość obu pól czy wartości każdego pola osobno?" FOLDED="true" ID="ID_241903909" CREATED="1630955938810" MODIFIED="1630955938810">
<node TEXT="Z samymi kluczami głównymi/kompozytowymi nic nie musi być unikatowe, trzeba do pól dodać UniqueConstraint, żeby uzyskać ten efekt." ID="ID_1670541810" CREATED="1632315469663" MODIFIED="1632315513869"/>
</node>
</node>
<node TEXT="dodać indeksy do wybranych pól" ID="ID_1559249374" CREATED="1632134778722" MODIFIED="1632335290393">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Dodać blueprints do aplikacji" FOLDED="true" ID="ID_364481577" CREATED="1632424686877" MODIFIED="1632479274283">
<icon BUILTIN="button_ok"/>
<node TEXT="podstawowa struktura" ID="ID_1798113744" CREATED="1632479284324" MODIFIED="1632479295158"/>
</node>
<node TEXT="+ Dodać skrypt do migracji bazy." ID="ID_1056818720" CREATED="1632482436885" MODIFIED="1632765768851">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="sprawdzić czy w momencie skasowania relacji w many-to-many, zostanie skasowany wpis z tabeli join" FOLDED="true" ID="ID_931242815" CREATED="1632329856879" MODIFIED="1632770721892">
<icon BUILTIN="button_ok"/>
<node TEXT="w razie czego - opcja cascade=&apos;all, delete-orphan&apos; w relationship()" ID="ID_1408027558" CREATED="1632331264533" MODIFIED="1632331287736"/>
</node>
<node TEXT="Sprawdzić diagram nt. blokowania modyfikowanego rekordu: po zablokowaniu formularza (w wyniku braku aktywności użytkownika) i przy próbie jego odblokowania, aplikacja sprawdza: czy rekord dalej istnieje, stemple modyfikacji (może jakieś md5? - tabele będą wymagały dodania pola na taki stempel), jeżeli podczas zablokowania formularza rekord został zmodyfikowany - informuje użytkownika, umożliwia wyświetlenie nowej wersji rekordu i wczytanie nowej wersji-porzucenie zmian lub nadpisanie rekordu (+zapis kopii)." ID="ID_460785322" CREATED="1632778026866" MODIFIED="1634582161181">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Czy da się Emacsa dostosować do budowania aplikacji we Flasku? Środowiska wirtualne etc." ID="ID_867309965" CREATED="1631100735675" MODIFIED="1632257634974">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="zaprojektować interfejs" FOLDED="true" ID="ID_1153646168" CREATED="1631029703707" MODIFIED="1633631161088">
<icon BUILTIN="button_ok"/>
<node TEXT="zrobić widoki interfejsu i diagram zmian stanów między nimi (np. widok rekordu książki -- kliknięcie osoby-autora etc. --&gt; widok rekordu osoby --&gt; -- kliknięcie linku np. &quot;rekordy bibliograficzne powiązane z...&quot; --&gt; wyświetlenie listy rekordów (np. książek)" FOLDED="true" ID="ID_1658949302" CREATED="1632770509236" MODIFIED="1632770708388">
<node TEXT="najlepiej w ogólny programie do diagramów - np. Yed" ID="ID_771120133" CREATED="1632770792622" MODIFIED="1632770814402"/>
<node TEXT="korzystać z tutoriala/dokumentacji Bootstrapa" ID="ID_1211618925" CREATED="1632954869885" MODIFIED="1632954888291"/>
<node TEXT="Korzystać z Bootstrap 4" FOLDED="true" ID="ID_961479988" CREATED="1632955719685" MODIFIED="1632955726055">
<node TEXT="bootstrap-flask" ID="ID_1760633400" CREATED="1632955794486" MODIFIED="1632955799708"/>
</node>
<node TEXT="referencyjnie:" FOLDED="true" ID="ID_678957145" CREATED="1632955318016" MODIFIED="1632955323456">
<node TEXT="use-cases" ID="ID_114097684" CREATED="1632955323474" MODIFIED="1632955326839"/>
<node TEXT="baza danych (models.py)" ID="ID_168461473" CREATED="1632956419421" MODIFIED="1632956428291"/>
<node TEXT="dokument SRS" ID="ID_320044953" CREATED="1632955327361" MODIFIED="1632955336214"/>
</node>
</node>
<node TEXT="wyszukiwanie" FOLDED="true" ID="ID_1655442957" CREATED="1633012004586" MODIFIED="1633012006780">
<node TEXT="szybkie/pełnotekstowe przeszukiwanie (quick search)" FOLDED="true" ID="ID_1994974242" CREATED="1633012009049" MODIFIED="1633012022235">
<node TEXT="wyniki wyszukiwania pod kolejnymi nagówkami:" FOLDED="true" ID="ID_1948628818" CREATED="1633012062185" MODIFIED="1633012134680">
<node TEXT="tematy (subject keywords-słowa kluczowe)" ID="ID_1493030343" CREATED="1633012134702" MODIFIED="1633012164017"/>
<node TEXT="oznaczenia odpowiedzialności" ID="ID_1085707086" CREATED="1633012140730" MODIFIED="1633012147265"/>
<node TEXT="dokumenty wg. tytułów dokumentów" ID="ID_486895389" CREATED="1633012147576" MODIFIED="1633012383028"/>
<node TEXT="osoby" ID="ID_136575092" CREATED="1633012166857" MODIFIED="1633012191053"/>
<node TEXT="ciała zbiorowe" ID="ID_656363819" CREATED="1633012191479" MODIFIED="1633012194584"/>
<node TEXT="nazwy geograficzne" ID="ID_1902066239" CREATED="1633012275128" MODIFIED="1633012280043"/>
</node>
</node>
<node FOLDED="true" ID="ID_1762076809" CREATED="1633011077129" MODIFIED="1633109623263"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      wyszukiwanie opisów bibliograficznych (dokumentów) wg. zaznaczonych kryteriów (<i>Search multiple fields</i>)
    </p>
  </body>
</html>
</richcontent>
<node TEXT="jeden termin wyszukiwany w różnych polach" ID="ID_955259742" CREATED="1633012594273" MODIFIED="1633012651739"/>
<node TEXT="w tym - wyszukiwanie wg. tematów (topics/subjects):" FOLDED="true" ID="ID_194284039" CREATED="1633009962971" MODIFIED="1633011922878">
<node TEXT="klikam na &quot;topics&quot;" FOLDED="true" ID="ID_820323825" CREATED="1633009981971" MODIFIED="1633009990265">
<node TEXT="Na nowej stronie wybieram które tematy mnie interesują (lista wielokrotnego wyboru - np. słowa kluczowe, osoby - wg. tabel, których rekordy mogą być tematami)." FOLDED="true" ID="ID_1652961093" CREATED="1633010029449" MODIFIED="1633010126259">
<node TEXT="Wyniki są wyświetlane na liście paginowanej, oddzielone nagłówkami - np. tematy-osoby, tematy-słowa kluczowe etc." ID="ID_323512591" CREATED="1633010128887" MODIFIED="1633010181564"/>
<node TEXT="Możliwość zaznaczenia wszystkich pól jedną opcją." ID="ID_1862730898" CREATED="1633010202116" MODIFIED="1633010233620"/>
</node>
</node>
<node TEXT="dodać schemat z przejściami" ID="ID_1839328047" CREATED="1633010419936" MODIFIED="1633010427605"/>
</node>
<node TEXT="wyszukiwanie wg. wielu kryteriów (wg. zaznaczenia)" ID="ID_1835003676" CREATED="1633011892613" MODIFIED="1633011916845"/>
<node TEXT="przycisk czyszczenia formularza (odznaczenie wszystkich zaznaczeń)" ID="ID_610745309" CREATED="1633011924152" MODIFIED="1633011947452"/>
<node TEXT="wybór typu dokumentu" ID="ID_1434657336" CREATED="1633012234552" MODIFIED="1633012258687"/>
</node>
<node TEXT="wyszukiwanie zawansowane (opisów bibliograficznych)" FOLDED="true" ID="ID_303462792" CREATED="1633012581236" MODIFIED="1633108864194">
<node TEXT="dodaję/usuwam kolejne kryteria wyszukiwania i zaznaczam przeszukiwane pole" ID="ID_1196588074" CREATED="1633012586275" MODIFIED="1633108999896"/>
</node>
<node TEXT="Na diagramach widoków stron zaznaczać powtarzające się elementy." ID="ID_1372117389" CREATED="1633034475109" MODIFIED="1633034499656"/>
</node>
<node TEXT="przeglądanie (browse)" FOLDED="true" ID="ID_1234615094" CREATED="1633035734624" MODIFIED="1633035741536">
<node TEXT="przeglądanie listy osób" FOLDED="true" ID="ID_1016489776" CREATED="1633010562683" MODIFIED="1633034466245">
<icon BUILTIN="button_ok"/>
<node TEXT="lista paginowana w układzie tabelarycznym: osoba (nazwisko, imię); liczba zapisów (dokumentów) gdzie osoba występuje w oznaczeniu odpowiedzialności (1. ozn. odp., późniejsze; inne funkcje); liczba z. gdzie osoba jest tematem." FOLDED="true" ID="ID_867237977" CREATED="1633010742284" MODIFIED="1633034462325">
<node TEXT="podobnie z:" FOLDED="true" ID="ID_987387138" CREATED="1633011014306" MODIFIED="1633011338150">
<node TEXT="ciała zbiorowe" ID="ID_1053733343" CREATED="1633011338169" MODIFIED="1633011342308"/>
<node TEXT="nazwy geograficzne" FOLDED="true" ID="ID_64115055" CREATED="1633011370060" MODIFIED="1633011376998">
<node TEXT="pola:" FOLDED="true" ID="ID_784267505" CREATED="1633011377022" MODIFIED="1633011382367">
<node TEXT="miejsca wydania" ID="ID_160890480" CREATED="1633011382386" MODIFIED="1633011384845"/>
<node TEXT="tematy geograficzne" ID="ID_1493580137" CREATED="1633011385004" MODIFIED="1633011388144"/>
</node>
</node>
</node>
<node TEXT="w górnej części - wyszukiwarka osób" ID="ID_169813476" CREATED="1633011707827" MODIFIED="1633011721207"/>
<node TEXT="pierwotne plany, ostatecznie zmienione - szczegóły w diagramie widoku" ID="ID_443269527" CREATED="1633032089640" MODIFIED="1633032106350"/>
</node>
</node>
<node TEXT="przeglądanie listy ciał zbiorowych" FOLDED="true" ID="ID_542232070" CREATED="1633036049074" MODIFIED="1633036057071">
<node TEXT="podobne do listy osób" ID="ID_1926820805" CREATED="1633036057571" MODIFIED="1633036062504"/>
</node>
</node>
<node TEXT="uwagi" FOLDED="true" ID="ID_1090061654" CREATED="1633009955143" MODIFIED="1633009962954">
<node TEXT="przeglądanie listy dokumentów (browse/documents)" FOLDED="true" ID="ID_1932508512" CREATED="1633024450491" MODIFIED="1633024461801">
<node TEXT="Na stronie widoku listy dokumentów mogę ograniczyć typ wyświetlanych dokumentów - ODZNACZYĆ jedno z pól typu (czyli jeżeli są wszystkie zaznaczone w kwerendzie nie uwzględnia typu dokumentu)." ID="ID_737802379" CREATED="1633024462376" MODIFIED="1633024650642"/>
</node>
<node TEXT="najpierw zaprojektować elementy dostępne dla wszystkich użytkowników, potem - dodać widoki wymagające logowania" ID="ID_1227286328" CREATED="1633013347595" MODIFIED="1633013392896"/>
<node TEXT="zaznaczyć elementy wspólne dla kilku widoków i je zgeneralizować - zdefiniować widoki &quot;abstrakcyjne&quot; i dziedziczące" ID="ID_81770304" CREATED="1633038047636" MODIFIED="1633038087543"/>
<node TEXT="uwzględnić uwagi-komentarze z diagramów" ID="ID_1423388493" CREATED="1632924575267" MODIFIED="1632924592521"/>
</node>
<node TEXT="zrobić mock-pages dla poszczególnych use-cases i punktów z dokumentu SRS" ID="ID_132827153" CREATED="1631307603373" MODIFIED="1631307604770"/>
</node>
<node TEXT="nad poszczególnymi wpisami w menu powinny wyskakiwać hinty" ID="ID_1298324452" CREATED="1633689310234" MODIFIED="1633713247725">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
</node>
<node TEXT="Jak zaimplementować formularz wyszukiwania we wszystkich trasach?" FOLDED="true" ID="ID_132924019" CREATED="1633953912826" MODIFIED="1634931606104">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="sprawdzić we flask megatutorial (fragmencie dot. wyszukiwania)" ID="ID_1389988403" CREATED="1633953932073" MODIFIED="1633953948086"/>
<node TEXT="formularz może być w makrze" ID="ID_1424120688" CREATED="1633965126938" MODIFIED="1633965981849"/>
<node TEXT="Zamiast WTF Forms, może lepiej użyć obiektu request?" FOLDED="true" ID="ID_1337135256" CREATED="1633965552002" MODIFIED="1633968358888">
<icon BUILTIN="button_ok"/>
<node TEXT="I&apos;m personally not a big fan of using form objects for search forms in my projects.&#xa;&#xa;&lt;form action=&quot;{{ url_for(&apos;search.search_page&apos;) }}&quot; method=&quot;get&quot;&gt;&#xa;  &lt;input type=&quot;search&quot; placeholder=&quot;Search&quot; name=&quot;q&quot;&gt;&#xa;  &lt;button type=&quot;submit&quot;&gt;Search&lt;/button&gt;&#xa;&lt;/form&gt;&#xa;This will result in a URL like /search?q=search+terms which will also make it linkable. Your search.search_page route can just use request.args.get(&quot;q&quot;) without involving WTForms at all.&#xa;&#xa;Edit: I forgot to mention that having a search endpoint that accepts a q query param is a pretty widespread practice." FOLDED="true" ID="ID_887322777" CREATED="1633965696481" MODIFIED="1633965698188">
<node TEXT="https://www.reddit.com/r/flask/comments/f1nvub/search_bar_in_layouthtml_template/" ID="ID_702301143" CREATED="1633965934975" MODIFIED="1633965934975" LINK="https://www.reddit.com/r/flask/comments/f1nvub/search_bar_in_layouthtml_template/"/>
<node TEXT="czy jest to bezpieczne?" ID="ID_1522621962" CREATED="1633967794602" MODIFIED="1633967800561"/>
</node>
</node>
<node TEXT="Przejrzeć notatki tn Flaska." ID="ID_714779877" CREATED="1633954084972" MODIFIED="1633954091644"/>
</node>
<node TEXT="Trasa dla szczegółów osoby (hasła) - projekt-diagram." ID="ID_290045842" CREATED="1634023385317" MODIFIED="1634027658468">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
</node>
<node TEXT="Dodać fałszywe nazwy osób (wg. podręcznika przy pomocy fakera - do bazy deweloperskiej)." FOLDED="true" ID="ID_1054916900" CREATED="1634072163692" MODIFIED="1634931603799">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node ID="ID_537788284" CREATED="1634931601681" MODIFIED="1634931601681"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      napisać testy
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="ustawić identyfikatory które będą eksportowane z models.py instrukcją from models import *" ID="ID_1796793853" CREATED="1634161965330" MODIFIED="1634307810777">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Dodać podstawowe typy dokumentów do bd" ID="ID_487148717" CREATED="1634299040685" MODIFIED="1634307935621">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Skasowanie wszystkich dokumentów nie kasuje wpisów w tablicach asocjacyjnych." FOLDED="true" ID="ID_160156099" CREATED="1634414307645" MODIFIED="1634483484606">
<font BOLD="false"/>
<node TEXT="sprawdzić opcje dla cascade:" FOLDED="true" ID="ID_96381509" CREATED="1634414429566" MODIFIED="1634414436320">
<node TEXT="Co powinno się stać, jeżeli skasuję wszystkie dokumenty:" FOLDED="true" ID="ID_1930182142" CREATED="1634464595514" MODIFIED="1634464609194">
<node TEXT="wszystkie powiązane rekordy w tablicach asocjacyjnych powinny zostać skasowane" ID="ID_1751023416" CREATED="1634464609214" MODIFIED="1634464627319"/>
</node>
<node TEXT="sprawdzić jeszcze raz:" FOLDED="true" ID="ID_168607576" CREATED="1634414484529" MODIFIED="1634414491714">
<node TEXT="wykasować zaw. tablic asocjacyjnych" ID="ID_800523689" CREATED="1634414499393" MODIFIED="1634415482439">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="co się stanie, jeżeli będę pojedynczo kasował rekordy?" FOLDED="true" ID="ID_626290188" CREATED="1634414521439" MODIFIED="1634415498898">
<node TEXT="bez zmian" ID="ID_1899739053" CREATED="1634464587558" MODIFIED="1634464590286"/>
</node>
</node>
<node TEXT="Podręcznik na temat cascades" ID="ID_910990514" CREATED="1634419301758" MODIFIED="1634419310065"/>
<node TEXT="materiały" FOLDED="true" ID="ID_820872730" CREATED="1634419883328" MODIFIED="1634419885398">
<node TEXT="SQLAlchemy ORM Cascade" FOLDED="true" ID="ID_1839213670" CREATED="1634419895423" MODIFIED="1634419896036">
<node TEXT="https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/" ID="ID_1473064217" CREATED="1634419886847" MODIFIED="1634419886847" LINK="https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/"/>
</node>
<node TEXT="cascade delete (SQLAlchemy)" FOLDED="true" ID="ID_522256829" CREATED="1634470790275" MODIFIED="1634470796760">
<node TEXT="https://dev.to/zchtodd/sqlalchemy-cascading-deletes-8hk" ID="ID_1349661016" CREATED="1634470797355" MODIFIED="1634470797355" LINK="https://dev.to/zchtodd/sqlalchemy-cascading-deletes-8hk"/>
</node>
</node>
<node TEXT="po której stronie relacji to powinno być" FOLDED="true" ID="ID_1714301396" CREATED="1634414436341" MODIFIED="1634414445541">
<node TEXT="https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_deleting_related_objects.htm" ID="ID_771490805" CREATED="1634414563459" MODIFIED="1634414563459" LINK="https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_deleting_related_objects.htm"/>
</node>
<node TEXT="Sprawdzić czy działa to w przykładowej aplikacji z podręcznika." ID="ID_358674462" CREATED="1634473133303" MODIFIED="1634473144874"/>
</node>
<node TEXT="Możliwe rozwiązania:" FOLDED="true" ID="ID_723724691" CREATED="1634475119060" MODIFIED="1634475124643">
<node TEXT="kasowanie obiektów rekordów w SQLAlchemy przez metodę (która najpierw wyczyści wszystkie powiązania)" ID="ID_1268476700" CREATED="1634475124661" MODIFIED="1634475142877"/>
<node TEXT="Jeżeli w MySQL wszystko działa, być może trzeba użyć opcji" ID="ID_130501374" CREATED="1634482417468" MODIFIED="1634482433571"/>
</node>
<node TEXT="czy w MySQL będzie ten sam problem?" FOLDED="true" ID="ID_905499012" CREATED="1634414582497" MODIFIED="1634414590333">
<node TEXT="utworzyć tabele" ID="ID_825600732" CREATED="1634414690915" MODIFIED="1634414695526"/>
<node TEXT="dodać fałszywe wpisy" ID="ID_626031883" CREATED="1634414695826" MODIFIED="1634414716009"/>
<node TEXT="spróbować wykasować rekordy z tabeli &apos;documents&apos;" ID="ID_1174666519" CREATED="1634414716274" MODIFIED="1634414731559"/>
<node TEXT="Próba skasowania dokumentu powoduje błąd integralności bd (Referential Integrity) spowodowany przez klucze zewnętrzne. Aby usunąć dokument należy wszystkie pola referencyjne ustawić na None lub pustą listę [] (w SQLAlchemy)." ID="ID_1535572883" CREATED="1634481316264" MODIFIED="1634481425882"/>
</node>
<node TEXT="uwagi:" FOLDED="true" ID="ID_545679125" CREATED="1634470870533" MODIFIED="1634470872196">
<node TEXT="Wszystko chyba jest dobrze, bo kasowanie relacji z tabeli asocjacyjnej następuje kiedy do pola utworzonego przez relationship np. przypiszę []." ID="ID_887644477" CREATED="1634474487670" MODIFIED="1634475052482"/>
<node TEXT="FOREIGN_KEY jest domyślnie wyłączony w SQLite" ID="ID_1104333679" CREATED="1634471802827" MODIFIED="1634471814674"/>
</node>
<node TEXT="Będę analizował dwie tabele: documents i jedną z tabel asocjacyjnych (i sprawdzę czy ew. rekordy z innych tabel nie zostały skasowane)." FOLDED="true" ID="ID_750357383" CREATED="1634420095428" MODIFIED="1634420175654">
<node TEXT="i zaprojektuję do tego testy: to radykalnie przyspiesza pracę" ID="ID_971863772" CREATED="1634420222532" MODIFIED="1634420237852"/>
</node>
<node TEXT="podręcznik Flaska" FOLDED="true" ID="ID_1680851992" CREATED="1634420720731" MODIFIED="1634420727123">
<node TEXT="s 176" ID="ID_1262595662" CREATED="1634420727593" MODIFIED="1634420757276"/>
</node>
<node TEXT="w MySQL być może trzeba użyć ondelete=&quot;cascade&quot;, sprawdzić jak to będzie działało" ID="ID_630628492" CREATED="1634484362385" MODIFIED="1634484451211"/>
<node TEXT="wyszukiwanie" FOLDED="true" ID="ID_1952333845" CREATED="1634420788907" MODIFIED="1634420792569">
<node TEXT="delete rows from associative table" ID="ID_1898169589" CREATED="1634420792590" MODIFIED="1634420806125"/>
<node TEXT="delete items from association" ID="ID_628671837" CREATED="1634420806313" MODIFIED="1634420812305"/>
</node>
<node TEXT="przyjrzeć się relacji Document.collectivity_subjects" FOLDED="true" ID="ID_116218743" CREATED="1634421045739" MODIFIED="1634421063317">
<node TEXT="dodać tam opcję cascade" ID="ID_835871251" CREATED="1634421159661" MODIFIED="1634421169329"/>
<node TEXT="kasuję collective body o id 2, sprawdzam, czy usunęło wpis z tabeli subjects_collectivities_join i nie usunęło dokumentu o id 25" FOLDED="true" ID="ID_756117033" CREATED="1634465936448" MODIFIED="1634465983627">
<node TEXT="w tabeli asocjacyjnej nic się nie zmienia" ID="ID_1363203988" CREATED="1634466321058" MODIFIED="1634466328101"/>
</node>
<node TEXT="kasuję dok.id=2, z tabeli responsibilities_people powinien zniknąć wiersz o id=1" FOLDED="true" ID="ID_540735217" CREATED="1634467903075" MODIFIED="1634467926737">
<node TEXT="w MySQL foreign_key nie pozwala na skasowanie" ID="ID_365660359" CREATED="1634479333207" MODIFIED="1634479362066"/>
</node>
<node TEXT="sprawdzić czy w razie wykasowania wiersza z tablicy asocjacyjnej nie zostaną skasowane wpisy z powiązanych tablic" FOLDED="true" ID="ID_1416777663" CREATED="1634465167911" MODIFIED="1634467803695">
<icon BUILTIN="button_ok"/>
<node TEXT="z responsibilities_collectivities usuwam id=1, sprawdzić czy nie usunie: responsibility_id=8, collectivity_id=12, document_id=1" FOLDED="true" ID="ID_184824593" CREATED="1634467005288" MODIFIED="1634467244567">
<icon BUILTIN="button_ok"/>
<node TEXT="W konfiguracji tych tabel wszystko działa." ID="ID_1841541825" CREATED="1634467252774" MODIFIED="1634467307149"/>
</node>
</node>
<node TEXT="jak to działa w tabeli asocjacyjnej z tylko dwoma polami?" ID="ID_1340635678" CREATED="1634467807202" MODIFIED="1634467816674"/>
<node TEXT="napisać testy" ID="ID_760262806" CREATED="1634465194274" MODIFIED="1634465197379"/>
</node>
<node TEXT="sprawdzić czy w którejś innej tabeli to działa" ID="ID_1377804906" CREATED="1634470048139" MODIFIED="1634470056341"/>
<node TEXT="Jeżeli: document.keywords = [] - wówczas wpisy z tablic asocjacyjnych działają -&gt; sprawdzić jak usuwa się wpisy wg. foreign keys" FOLDED="true" ID="ID_1862655884" CREATED="1634468947373" MODIFIED="1634468983079">
<node TEXT="w innym wypadku przed skasowaniem każdego dokumentu będę musiał ręcznie czyścić wszystkie powiązania" ID="ID_754723216" CREATED="1634469020288" MODIFIED="1634469037825"/>
</node>
</node>
<node TEXT="Widok dokumentu (z osobami/rolami)" ID="ID_104156341" CREATED="1634152378383" MODIFIED="1634582136035">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Zaprojektować widok &quot;osoby&quot; (wg. diagramu)" FOLDED="true" ID="ID_1705333739" CREATED="1634074206279" MODIFIED="1634300781292">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="trasa dla szczegółów (name variant)" FOLDED="true" ID="ID_1158159375" CREATED="1634141531011" MODIFIED="1634149651966">
<icon BUILTIN="button_ok"/>
<node TEXT="w dwie strony ma to działać: zwrotny link do strony osoby (person)" ID="ID_377253215" CREATED="1634146119338" MODIFIED="1634146246882"/>
</node>
<node TEXT="Zrobić makro do pola z wariantami nazwy." ID="ID_650558486" CREATED="1634139792468" MODIFIED="1634142133455">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Utworzyć fałszywe dokumenty" FOLDED="true" ID="ID_1295819536" CREATED="1634307952013" MODIFIED="1634414286698">
<icon BUILTIN="button_ok"/>
<node TEXT="Dowiązać osoby do dokumentów" ID="ID_1553753603" CREATED="1634152196011" MODIFIED="1634152208052"/>
<node TEXT="relacja many-to-many w dokumentach (m.in. powiązanie czasopism z artykułami):" FOLDED="true" ID="ID_814303946" CREATED="1634382546438" MODIFIED="1634382571829">
<node TEXT="Zrobić fake-dokumenty i zobaczyć jak to będzie wyglądało w BD." ID="ID_363870987" CREATED="1634382571851" MODIFIED="1634382615564"/>
</node>
<node TEXT="Jeżeli w czasie ich dodawania dojdzie do nieprzewidzianych błędów w bazie danych (które nie powinny wystąpić), sprawdzić je i ewentualnie dodać do testów." ID="ID_695100241" CREATED="1634394298691" MODIFIED="1634414286696" HGAP_QUANTITY="10.250000111758705 pt"/>
</node>
</node>
<node TEXT="zrobić widok słowa kluczowego" ID="ID_1709040204" CREATED="1634658339196" MODIFIED="1634669022996">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
</node>
<node TEXT="dodać trasę od dokumentu do słowa kluczowego" ID="ID_947958089" CREATED="1634670600488" MODIFIED="1634673662864">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
</node>
<node TEXT="Widok przeglądania listy osób." FOLDED="true" ID="ID_618575998" CREATED="1634149931007" MODIFIED="1634676756417">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="Do kwerendy dodać warianty nazwy, powinny odsyłać do właściwego hasła osobowego, powinny być wyświetlane inaczej niż właściwe nazwy." ID="ID_1114448270" CREATED="1634209954771" MODIFIED="1634234931517">
<icon BUILTIN="button_ok"/>
</node>
</node>
<node TEXT="geographic locations" FOLDED="true" ID="ID_151705417" CREATED="1634676690661" MODIFIED="1634726320242">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="w details dodać dokumenty w których jest to miejsce wydania i temat dokumentu" ID="ID_943153969" CREATED="1634721337621" MODIFIED="1634726316225">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="widok i lista" ID="ID_785410371" CREATED="1634726325842" MODIFIED="1634726330414">
<icon BUILTIN="button_ok"/>
</node>
</node>
<node TEXT="collective names" FOLDED="true" ID="ID_560109887" CREATED="1634677234760" MODIFIED="1634753852999">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="lista chyba podobna do listy osób" ID="ID_863043333" CREATED="1634726360372" MODIFIED="1634726369629"/>
</node>
<node TEXT="Languages" FOLDED="true" ID="ID_355191777" CREATED="1634752898195" MODIFIED="1634921863011">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="Język powinien też móc być przedmiotem dokumentu." ID="ID_876813045" CREATED="1634324408122" MODIFIED="1634762144400">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="dodać fałszywe wpisy z językami jako tematami dokumentu (od 0 do ...)" ID="ID_1723328546" CREATED="1634762572710" MODIFIED="1634895116404">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="Zaktualizować widok dokumentu (żeby wyświetlał języki jako tematy)" ID="ID_944510698" CREATED="1634896328779" MODIFIED="1634909762135">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="widok strony języka" ID="ID_1776495270" CREATED="1634762618103" MODIFIED="1634913849057">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="widok listy języków" FOLDED="true" ID="ID_1568830868" CREATED="1634762633220" MODIFIED="1634921858614">
<icon BUILTIN="button_ok"/>
<node TEXT="spróbować zrobić listę polimorficzną dla języków i nazw ciał zbiorowych" ID="ID_1153135632" CREATED="1634913855360" MODIFIED="1634913891685"/>
</node>
</node>
<node TEXT="zrobić dokumentację do makr" ID="ID_528903028" CREATED="1634907173997" MODIFIED="1634912418715">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="przycisk-badge z listą dokumentów powinien być komponentem" ID="ID_22127658" CREATED="1634841725182" MODIFIED="1634931559858">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="responsibilities" FOLDED="true" ID="ID_367710586" CREATED="1634934212650" MODIFIED="1635158773477">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="lista" ID="ID_732912182" CREATED="1634934216745" MODIFIED="1634934223106"/>
<node TEXT="widok" ID="ID_1612459998" CREATED="1634934223352" MODIFIED="1634934224644"/>
</node>
<node TEXT="Dodać linki do nazw oznaczeń odpowiedzialności od stron: ze szczegółami osoby, ciała zbiorowego." ID="ID_398703700" CREATED="1635158664204" MODIFIED="1635161618391">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="w odpowiednich miejscach użyć makra see_documents_list_badge" ID="ID_1220483096" CREATED="1634920466060" MODIFIED="1635256507712">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="W funkcjach collective_body_resp_list i person_responsibility_list trzeba dwa razy dodać ResponsibilityRow - w obu przypadkach jest to ta sama instrukcja. Czy można to poprawić?" FOLDED="true" ID="ID_1663906102" CREATED="1635160662253" MODIFIED="1635168849565">
<icon BUILTIN="button_ok"/>
<node TEXT="Kwerenda jest przekazywana jako funkcja anonimowa." ID="ID_728673565" CREATED="1635168833544" MODIFIED="1635168846675"/>
</node>
<node TEXT="Zaprojektować interakcje dla przejścia od strony oznaczenia odpowiedzialności do listy ciał zbiorowych (referencjonowanych przez oznaczenie odpowiedzialności)." ID="ID_1478702722" CREATED="1635275142426" MODIFIED="1635282811727">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
</node>
<node TEXT="see_list_badge ma stać się przyciskiem i blokować się jeżeli brak hiperłącza (endpoint)." ID="ID_68748648" CREATED="1635446802805" MODIFIED="1635449134038">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="zmienić sposób w jaki funkcja documents_list dowiaduje się jaką kwerendę przeprowadzić" FOLDED="true" ID="ID_413274273" CREATED="1635364546895" MODIFIED="1635365710180">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="parametr entry_type=&apos;collective_body&apos; or &apos;person&apos; etc.&#xa;parametr id_number" ID="ID_605534072" CREATED="1635364586737" MODIFIED="1635364874374"/>
</node>
<node TEXT="Zrobić kwerendę dla dokumentów z filtrem wg. typu dokumentu" FOLDED="true" ID="ID_1067046675" CREATED="1635874035826" MODIFIED="1635878001070">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
<node TEXT="Podstawowa wersja kwerendy wygląda tak:" FOLDED="true" ID="ID_602910021" CREATED="1635876253318" MODIFIED="1635876262109">
<node TEXT="Document.query.filter(Document.document_type_id.in_([3, 4])).all()" ID="ID_1933829602" CREATED="1635876262741" MODIFIED="1635876263979"/>
</node>
</node>
<node TEXT="lista wszystkich dokumentów" ID="ID_1898039390" CREATED="1635346562264" MODIFIED="1635353263497">
<icon BUILTIN="button_ok"/>
<font BOLD="false"/>
</node>
</node>
</node>
</map>
