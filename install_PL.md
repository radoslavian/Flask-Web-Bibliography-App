# Instalacja:

Aplikacja była budowana na systemie zgodnym z Ubuntu 18.04 (KDE Neon)
z użyciem Python 3.6.9

Po pobraniu repozytorium, w lokalnym katalogu należy utworzyć środowisko
wirtualne:
`$ python3 -m venv ./venv`

i je aktywować:

`$ source ./venv/bin/activate`

W następnej kolejności należy zainstalować wymagane pakiety - ich lista jest
zawarta w pliku requirements.txt (w katalogu requirements aplikacji). Należy
to zrobić przy pomocy instalatora pip:

`$ pip install -r requirements.txt`

Po instalacji, należy ustawić podstawowe zmienne środowiska:
ścieżkę do aplikacji (w tej formie, jeżeli znajduję się wgłównym
katalogu aplikacji):

`$ export FLASK_APP=./main.py`

oraz zmienną wskazującą wybraną konfigurację aplikacji (w tym przypadku
będzie to wersja "rozwojowa" z włączonym trybem debugowania i restartem
serwera testowego w razie wykrycia zmian w plikach źródłowych):

`$ export FLASK_ENV=development`

Pozostałe klasy zawierające konfigurację są wymienione w słowniku config w
module config.py (podczas pisania używałem przeważnie opcji "development"
i "testing").

W celu dalszej konfiguracji należy wywołać interaktywną sesję interpretera
Pythona z podłączoną powłoką Flaska:

`$ flask shell`

Wiersz zachęty interpretera na tym etapie powinien wyglądać z grubsza tak:

```
(venv) [localhost@localdomain:~/Flask-Web-Bibliography-App]$ flask shell
Python 3.6.9 (default, Jan 26 2021, 15:33:00) 
[GCC 8.4.0] on linux
App: app [development]
Instance: /home/user/Flask-Web-Bibliography-App/instance
>>>
```

Aby możliwe było używanie aplikacji, należy zainicjować bazę danych. W tym
celu z pakietu app należy zaimportować obiekt db:
```
>>> from app import db
```
Następnie na obiekcie db należy wywołać metodę inicjującą
tabele (zdefiniowane w modelelach z modułu models.py):
```
>>> db.create_all()
```
Na tym etapie, po wyjściu z interpretera i włączeniu serwera
rozwojowego, aplikację będzie można uruchomić.
Alternatywnie, można pozostawić włączoną sesję powłoki Flaska oraz otworzyć
nowe okno/zakładkę terminala. W tak otwartej nowej sesji powłoki systemowej
powtórzyć kroki polegające na włączeniu środowiska wirtualnego i ustawienia
głównych zmiennych środowiska i tam uruchomić serwer.
```
(venv) localhost@localdomain:~/Flask-Web-Bibliography-App$ flask run
 * Serving Flask app 'main.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 321-185-642
```
Powyżej przykładowe wyjście z terminala po włączeniu serwera rozwojowego - jak
widać, aplikacja jest dostępna lokalnie pod adresem http://127.0.0.1 na
porcie 5000 - co w domyślnej konfiguracji lokalnej pseudo-sieci będzie
równoznaczne z adresem http://localhost:5000

W celu umożliwienia logowania, edycji bazy i nadawania uprawnień innym
użytkownikom aplikacji, trzeba utworzyć konto administratora (w kolejnej
odsłonie administrator ma być rozpoznawany po specjalnej zmiennej środowiska,
ale na razie dodaję go ręcznie). W tym celu w pierwszej kolejności (w powłoce
Flaska) z modułu models należy zaimportować klasę Role i wywołać metodę
insert_roles() w celu dodania ról użytkowników do bazy danych:
```
>>> from app.models import Role
>>> Role.insert_roles()
```
W tej części aplikacji nie ma akurat nic odkrywczego - jest prawie-że
powtórzenie podręcznika (różnica jest w definicjach ról).
Dostępne role można podejrzeć używając kwerendy:
```
>>> Role.query.all()
[<Role: User>, <Role: Editor>, <Role: Administrator>]
```
Jak widać, rola administratora pojawiła się jako trzeci element listy, można
ją w ten sposób przypisać do zmiennej:
```
>>> admin_role = Role.query.all()[2]
```
lub lepiej - uzyskać obiekt roli z kwerendy:
```
>>> admin_role = Role.query.filter_by(name='Administrator').first()
>>> admin_role
<Role: Administrator>
```
Tworzenie użytkownika-administratora:
Należy utworzyć instancję klasy User; ponieważ idziemy na skróty (pomijamy
aktywację użytkownika przez maila etc.), do konstruktora przekazuję wszystkie
parametry, które będą potrzebne do zalogowania, czyli: nazwę użytkownika,
hasło (w bazie danych przechowywany jest tylko hash utworzony przy pomocy
narzędzi z pakietu Flaska), konto od razu ustawiam na "potwierdzone" oraz
dodaję fikcyjny email którym będę się logował do aplikacji:
```
>>> user_admin = User(username='admin', password='admin_password',
... confirmed=True, role=admin_role, email='admin@localhost.localdomain')
```
Jeżeli wszystko poszło dobrze, użytkownika można dodać do bazy:
```
>>> db.session.add(user_admin)
>>> db.session.commit()
```
Oraz zalogować się w aplikacji.

W podobny sposób można dodawać użytkowników-edytorów bibliografii (przy czym,
konta potwierdzać, aktywować i zmieniać im uprawnienia może administrator):
```
>>> editor = User(username='editor', password='editor_password',
... email='editor@localhost.localdomain')
>>> db.session.add(editor)
>>> db.session.commit()
```
Aplikacja umożliwia wysyłanie użytkownikom maili z linkami do strony
potwierdzającej konto, ale tak jak wspomniałem - jest to zrobione według
podręcznika i nie zawiera wielu oryginalnych rozwiązań, a wymaga ustawienia
zmiennych środowiska z:
* adresem serwera pocztowego
* nazwą i hasłem użytkownika (na serwerze)

Testowałem to z Gmailem, no i działa (i w zasadzie tyle w tym temacie).
Przy czym taką aktywację dodałem w celu nauczenia się i dość ogólnego
zrozumienia uwierzytelniania/logowania etc. - potwierdzanie kont przez mail
ma większy sens w przypadku aplikacji typu społecznościowego; w przypadku
systemów bibliotecznych (i tym podobnych) - aktywacją i zarządzaniem kontami
powinien zajmować się (właśnie) administrator lub np. w bibliotekach - tzw.
"bibliotekarz systemowy".

Baza danych, jak na razie, jest pusta. W zamyśle: powinna zostać zapełniona
ręcznie opisami dokumentów. Jednakże aby ułatwić pracę wyobrażonym
bibliografom, postanowiłem do niej dodać pewne predefiniowane wpisy. Są to:
* początkowa lista typów dokumentów (Document Types) - statycznie wpisane do
  klasy DocumentType
* języki - pochodzą z modułu pycountry znalezionego w repozytorium PyPI
(który wymieniłem w requirements.txt)

Podstawowe typy dokumentów dodaje się w powłoce Flaska przy pomocy metody
klasy DocumentType (są one potrzebne do generowania losowych wpisów w bazie):
```
>>> from app.models import DocumentType
>>> DocumentType.add_basic_document_types()
```
Typ dokumentu posiada pole określające, czy jest on wbudowany
i tylko-do-odczytu czy też można go edytować/usuwać. Obecnie nie ma ono
odzwierciedlenia nigdzie w logice programu i to rozróżnienie zamierzam
skasować, gdyż wydaje mi się ono zbędne.

Przed zapełnieniem pozostałych tabel należy zainstalować (wg. instrukcji na
stronie projektu) i włączyć Elasticsearch:
```
$ sudo systemctl start elasticsearch
```
oraz w środowisku wirtualnym, w którym jest uruchamiany serwer ustawić
zmienną z adresem usługi - która domyślnie jest włączona na porcie 9200 -
zatem po instalacji na lokalnym komputerze:
```
$ export ELASTICSEARCH_URL=localhost:9200
```
Aby utworzyć bazę danych z fałszywymi wpisami, należy skonfigurować
Elasticsearch (tak jak przedstawiono powyżej), następnie w środowisku
wirtualnym, w którym ustawiono zmienną `ELASTICSEARCH_URL`
(jest to ważne - inaczej baza danych się nie zaindeksuje) uruchomić powłokę
Flaska, zaimportować moduł fake i wykonać procedurę tworzącą wpisy:
```
>>> from app import fake
>>> fake.create_all()
```

# Uwagi:

Jeżeli Elasticsearch nie był uruchomiony podczas tworzenia bazy danych,
dodawania/usuwania lub modyfikacji rekordów, tabele można
zreindeksować/zaindeksować ręcznie (w celu zsynchronizowania bazy ES z bazą
danych aplikacji). Aby tego dokonać, dla klas z modułu models.py,
posiadających atrybut `__searchable__`, w powłoce Flaska należy wykonać
np. taką instrukcję:
```
>>> from app import models
>>> for model_name in models.__all__:
...  model = getattr(models, model_name, None)
...  if getattr(model, '__searchable__', None):
...   model.reindex()
```

[wideo z działającą instalacją](https://youtu.be/QaYa7rLCeNw)
