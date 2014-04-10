Zadanie 2 laboratoryjne

Należy przygotować w Django aplikację służącą do rezerwacji miejsc w pokojach konferencyjnych.

Każdy pokój ma:

nazwę (np. pokój biały),
pojemność (np. 20),
i opis (np. jakiś tekst).
Z każdym pokojem powinny być związane (ForeignKey) wolne terminy, które składają się z

daty (np. 2014-04-01)
godziny od której pokój jest wolny (np. 10),
godziny do której pokój jest wolny (np. 16)
Aplikacji używają wyłącznie zalogowani użytkownicy.

Wiele osób jednocześnie może korzystać z aplikacji, więc trzeba uważać żeby nie powstały błędy z tym związane.

Pokoje i wolne terminy powinno się dać wprowadzać za pomocą django.admin. Gdy dopisuje się wolny termin należy sprawdzać czy termin ten nie zachodzi na inny termin i nie pozwolić na dopisanie w przypadku zachodzących terminów.

Aplikacja powinna pozwalać na wybranie pokoju (formularz 1), a następnie daty i godzin (formularz 2) i zarezerwowaniu ich (formularz 3 z potwierdzeniem danych). Nie obsługujemy anulowania rezerwacji, ale obsługujemy błędy (np. pokój jest już zajęty). Nie obsługujemy "scalania" wolnych terminów, czyli jeśli jest wolne od 10 do 12 i od 12 do 14 to nie można zarezerwować od 10 do 14.

Do wybrania pokoju należy przygotować przeglądarkę pokojów, która powinna:

wyświetlać pokoje po kilka na stronie (np. 10),
pozwalać sortować według nazwy lub pojemności,
pozwalać wyszukiwać pokoje w oparciu o jedną wprowadzoną frazę (np. 100 znajdzie zarówno pokoje mające pojemność 100 jak i takie, które mają napis 100 w nazwie lub opisie),
z wyszukiwarki powinno dać się przejść od razu do drugiego formularza rezerwacji.
Rezerwacja powinna posiadać:

pokój, datę, godziny od-do,
użytkownika który ją dokonał.
Jeśli pokój był wolny od 10 do 16 a rezerwujemy go od 12 do 14, to powinno się go wciąż dać zarezerwować od 10 do 12 i od 14 do 16.
Rezerwacje powinno się dać przeglądać za pomocą django.admin, ale zwykli użytkownicy nie widzą rezerwacji.

Aplikacja powinna posiadać automatyczne testy modeli przygotowane za pomocą django.test.
