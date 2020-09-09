# Pizza Website

Backlogg: https://docs.google.com/spreadsheets/d/131Dxy4QplduNJaxo41rS0nOelqbk0bQTxoG1y0TOsho/edit#gid=0

Hemsida: https://fantastic4group.gitlab.io/pizza-website
**(För att hosta HTML sida används GitLab Pages, därför behövs .gitlab-ci.yml filen.)**

**Viktigt! Installera Node.js från https://nodejs.org/en/ . Sedan navigera till pizza-website foldern i valfri kommandoprompt och skriv in "npm install" . Detta krävs för att allt ska funka som det ska.**

# Kodningsstandard
**Spaces:** 4
<br>
**Kommentarer:** Engelska över funktionen, mellanslag mellan "//" och meningen, stor bokstav
<br>
**Namngivning:** Engelska
<br>
**Variabel:** let, stor bokstav som delar upp flera ord i en variabel som "pizzaFooter"
<br>
**Funktioner:** non lambda functions
<br>
Ingen css i html-filer

# Programmeringsspråk
HTML 5
<br>
CSS 3
<br>
Javascript (ECMAScript 2018)

# Utvecklingsmiljöstandard
**Editor** - Visual Studio Code 1.48.2
<br>
Plugins för VSCode: 
- Live Server
- Beautify
- Beautify css/sass/scss/less
- Live Share
- Code Spell Checker
- Swedish - Code Spell Checker

**Fildelning** - GitLab
<br>
**OS** - Windows 10 1909
<br>
**Browsers** - Edge 85 / Chrome 85
<br>
**Skärmupplösning** - 2560x1440, 1920x1080
<br>
**Tester** - Selenium IDE Chrome
<br>
**Validering** - HTML Validator, CSS Validator
<br>
**Dokumentation** - Svenska, kortfattat med bilder
<br>
**Annat** - node.js v.14.9.0, npm v.6.14.8


# Definition of Done
Godkänd av gruppen.
<br>
Bearbetat feedback från gruppmedlemmar.
<br>
Ska klara av tester
<br>
Överens med gruppens kodningsstandard
<br>
Koden ska vara kommenterad och dokumenterad
<br>
Koden ska gå igenom valideringen





# Tester Dokumentation
**Hur man sätter upp Selenium IDE för tester**
1. Klona/pulla filerna från Gitlab repot Pizza Website
1. Öppna Git Bash och kör kommandot **cd tests && ./setup.sh**
1. Sedan kör kommandot **python run.py**
1. Skriv antingen in 1 för den lokala hostningen av index.html med **VSCode Live Server** eller 2 för hemsidan på GitLab
1. Om allting dyker upp utan errors så hittar testerna allting

**Hur man skapar ett test i Selenium IDE**
1. Se till att du har den senaste versionen av filerna genom att pulla dem från Gitlab.
1. Öppna Selenium IDE och skapa ett projekt eller välj ett existerande projekt om du redan har ett.
1. Klicka på + knappen under projekt rubriken och välj ett namn på testet du vill skapa.
1. Skriv in eller välj “open” från listan på fältet där det står command 
1. Skriv in url:et  på sidan du vill testa i target fältet på samma rad.
1. Observera att du måste skriva in hela url:et på sidan du vill testa så du inte glömmer http/https delen. Är sidan lokal måste du skriva in localhost adressen med den rätta porten till din lokala server (VSCode Live Server).
1. Därefter, skriv på raden/raderna under vad du vill testa. I command inputtar du vad du vill göra, t.ex att klicka eller att selecta en rad text. Sedan på Target så inputtar du vad det är på sidan du vill testa, t.ex h1 tagg osv.  

# Screenshots av websidan
**För att använda**
1.  Gå in i "shot.json" via VSCode.
1.  Under rubriken "urls" kan man skriva in det adress man vill.
1.  Under rubriken "sizes" kan man skriva in det upplösning man vill.
1.  Starta "takeScreenshot.sh"
1.  Sedan alla screenshots ska sparas i scripts/screenshots

# HTML och CSS Validering
Koden valideras automatiskt via CI när man har pushat den. Annars kan man validera den lokalt genom att:
1. Starta Git Bash i **/scripts/validators mappen**
1. Skriv in **./runValidators.sh** för att starta filen
1. Sedan resultat visas i fönstret av valideringen

# Innehåll från internet

- Typsnitt är licensierat under Open Font License(OFL) http://scripts.sil.org/OFL
- Bild under titeln är licensierat under Pixabay License, gratis för kommersiellt bruk https://pixabay.com/sv/photos/pizza-mat-italian-bakad-ost-3007395/
- Bild i footer är från våran Product Owner
