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
**Variabel:** let
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
1. Ladda ner Selenium IDE tillägget till Firefox, Chrome eller Edge (Chromium)
1. Öppna tillägget och tryck på Open an existing project
1. Navigera till mappen Selenium i Git repot och välj filen Fantastic 4.side
1. För att starta ett test så måste man först välja ett test och sedan trycka på Run current test knappen 
1. För att köra alla tester så trycker man på knappen till vänster om den förra knappen “Run all tests” 
1. För att spara ändringar i projektet så trycker du på Ctrl+S och navigerar sedan till mappen Selenium i repot och tryck på Save för att ersätta Fantastic 4.side med den nya filen

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
1. Går in i **\scripts\validators**
1. Starta kommand prompt i den mappen
1. Skriv in **./runValidators.sh** för att starta filen
1. Sedan resultat visas i fönstret av valideringen
