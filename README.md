# Uppgift 2 - Skapa en funktion för att avgöra om en sekvens är en "viss grad" av palindrom

## Beskrivning:

I denna uppgift ska du skapa en funktion med namnet `palindromish` i filen [uppgift2.py](uppgift2.py) som bestämmer om en given sekvens (sträng eller lista) är ett palindrom till en viss grad. En sekvens anses vara ett [palindrom](https://sv.wikipedia.org/wiki/Palindrom) om den är likadan bakifrån som framtill. Denna funktion ska dock tillåta en viss flexibilitet genom att definiera en "grad" av palindrom, baserat på hur många tecken i början och slutet av sekvensen som måste matcha.

### Funktionsspecifikation:

- **Funktionsnamn:** `palindromish`
- **Argument:**
  - **sekvens (str eller list):** Den sekvens som ska undersökas.
  - **grad (int, optional):** Ett heltal som anger hur många tecken från början och slutet av sekvensen som måste vara lika för att sekvensen ska anses vara ett palindrom till den angivna graden. Om detta värde är högre än halva längden av sekvensen, justeras det automatiskt till halva sekvensens längd. Om inget värde anges, antas halva sekvensens längd.
- **Returvärde:** Funktionen ska returnera en boolsk värde (`True` eller `False`), som indikerar om sekvensen är ett palindrom till den angivna graden.

### Exempel:

1. **Exempel 1:**
   - **Input:** `palindromish("radar", 2)`
   - **Förväntat resultat:** `True`
   - **Förklaring:** De första två och de sista två tecknen är lika ("ra" och "ar"), så sekvensen är ett palindrom till graden 2.

2. **Exempel 2:**
   - **Input:** `palindromish([1, 2, 3, 50, 60, 3, 2, 1], 3)`
   - **Förväntat resultat:** `True`
   - **Förklaring:** De första tre och de sista tre elementen matchar (1, 2, 3), så listan är ett palindrom till graden 3.

3. **Exempel 3:**
   - **Input:** `palindromish([1, 2, 3, 50, 60, 3, 2, 1], 4)`
   - **Förväntat resultat:** `False`
   - **Förklaring:** De första fyra och de sista fyra elementen matchar inte då de är (1, 2, 3, 50) respektive (1, 2, 3, 60), så listan är *inte* ett palindrom till graden 4.

4. **Exempel 4:**
   - **Input:** `palindromish("example", 3)`
   - **Förväntat resultat:** `False`
   - **Förklaring:** Sekvensen är inte ett palindrom till graden 3 eftersom de första tre och de sista tre tecknen inte matchar.

5. **Exempel 5:**
   - **Input:** `palindromish("Naturrutan")`
   - **Förväntat resultat:** `True`
   - **Förklaring:** Sekvensen är ett palindrom i sin helhet.

6. **Exempel 6:**
   - **Input:** `palindromish("")`
   - **Förväntat resultat:** `True`
   - **Förklaring:** En tom sträng får anses vara ett kortaste palindromet, då den startar och slutar med "den tomma strängen".

### Inlämningsinstruktioner:

Din lösning ska innehålla funktionen `palindromish` komplett med den beskrivna funktionaliteten. Se till att din funktion hanterar både strängar och listor som input och korrekt justerar graden om den överstiger halva sekvensens längd.

Inkludera kommentarer i din kod för att förklara din logik där det är nödvändigt. Testa din funktion med flera olika input för att säkerställa att den fungerar som förväntat och inkludera minst tre exempelkörningar (som de ovan) i din inlämning.
