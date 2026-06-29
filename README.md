## Instruktioner<br><br>


### Controls:<br>
Use WASD to move<br>
Use J+W/A/S/D to jump<br>
Use T to disarm trap<br>
Use I to show inventory<br>
Use C to open controls<br>
Use G to dig<br>
Use Q/X to quit <br>
<br>


### Symbols:<br>
Inactive bomb = 'b'<br>
Active bomb = 'B'<br>
Chest = '±'<br>
Key = '¬'<br>
Shovel = 'Î'<br>
Trap = '#'<br>
Wall = '■'<br>
Way out = 'E'<br>
Vegetables = '?'<br>
You = '@'<br>
<br>
<br>
Plocka upp alla grönsaker och ta dig till utgången!


---


## Starta projektet

För att starta mitt projekt skriver man följande i terminalen, medan man står i projektets rotmapp.

```commandline
python -m src.game
```

## Vad jag har gjort
Jag har arbetat med följande krav:

| Version 1 | Status | Detaljer                                                                                                                                                              |
|:---------:|:------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     A     |   ✅    | Spelaren ska börja nära mitten av rummet.                                                                                                                             |
|     B     |   ✅    | Förflyttningar i alla 4 riktningar. (Med tangenterna WASD.)                                                                                                           |
|     C     |   ✅    | Man ska inte kunna gå igenom väggar.                                                                                                                                  |
|     D     |   ✅    | Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.                                                                                                  |
|     E     |   ✅    | Inventory - alla saker som man plockar upp ska sparas i en lista.                                                                                                     |
|     F     |   ✅    | Nytt kommando: "i", skriver ut innehållet i spelarens inventory.                                                                                                      |
|     G     |   ✅    | The floor is lava - för varje steg man går ska man tappa 1 poäng.                                                                                                     |
|     H     |   ✅    | Använd for-loopar för att skapa flera, sammanhängande väggar på kartan. Se till att det inte skapas några rum som man inte kan komma in i. Gör detta i filen grid.py. |

| Version 2 | Status | Detaljer                                                                                                                                                                                                                                                                                                                            |
|:---------:|:------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     I     |   ✅    | Fällor - introducera valfri fälla till spelplanen. Om man går på en ruta med en fälla ska man förlora 10 poäng. Fällan ska ligga kvar så att man kan falla i den flera gånger.                                                                                                                                                      |
|     J     |   ✅    | Spade - en ny sak man kan plocka upp. När man går in i en vägg nästa gång, förbrukas spaden för att ta bort väggen.                                                                                                                                                                                                                 |
|     K     |   ✅    | Nycklar och kistor - slumpa minst en nyckel och lika många kistor på spelplanen. När man går på en ruta med en nyckel plockar man upp den i sitt inventory. Om man kommer till en kista och har minst en nyckel, öppnar man kistan och plockar upp en skatt som är värd 100 poäng. (Nyckeln är förbrukad.)                          |
|     L     |   ✅    | Bördig jord - efter varje 25:e drag skapas en ny frukt/grönsak någonstans på kartan.                                                                                                                                                                                                                                                |
|     M     |   ✅    | Exit - slumpa ett "E" på kartan. När man har plockat upp alla ursprungliga saker, kan man gå till exit för att vinna spelet. Men innan man tagit upp alla har inte Exit någon effekt.                                                                                                                                               |
|     N     |   ✅    | Jump - om man skriver ett "J" innan något av "WASD", ska spelaren hoppa över en ruta. (Exempel: "JW" → två steg uppåt.) Man förflyttar sig alltså två steg, men kan förstås bara plocka upp eller interagera med saker där man landar. Hoppar man in i en vägg blir det samma effekt som om man hade gått ett steg på vanligt sätt. |

| Version 3 | Status | Detaljer                                                                                                                                                                                                                                                                                                                                            |
|:---------:|:------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     O     |   ✅    | Grace period - efter man har tagit plockat upp något, kan man gå 5 steg utan att det dras några poäng.                                                                                                                                                                                                                                              |
|     P     |   ❌    | AI-fiender - placera 1-3 fiender på kartan. För varje steg spelaren tar ska ska varje fiende ha en slumpmässig chans att flytta sig ett steg närmare spelaren. Minus 20 poäng om en fiende hinner ifatt. (Inte diagonalt, dvs. samma rörelsemönster som spelaren. Fienderna ska vara lite "långsammare" så att det är lagom svårt att undvika dem.) |
|     Q     |   ✅    | Tryck "B" för att placera en bomb. Efter 3 drag smäller bomben och förstör allt på sin ruta och de åtta som gränsar till den. (fällor, väggar, m.m.) Om spelaren är kvar förlorar man poäng.                                                                                                                                                        |
|     R     |   ✅    | Ett nytt kommando ("T" för trap) för att desarmera fällor.                                                                                                                                                                                                                                                                                          |
|     S     |   ❌    | Använd TDD för att testa några av funktionerna i koden.                                                                                                                                                                                                                                                                                             |
|     T     |   ❌    | Använd paketet curses för bättre hantering av terminalen, exempelvis getkey i stället för input.                                                                                                                                                                                                                                                    |
