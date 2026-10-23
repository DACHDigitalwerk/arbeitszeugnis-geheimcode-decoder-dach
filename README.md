# Arbeitszeugnis Geheimcode Decoder DACH 🇩🇪 🇨🇭 🇦🇹

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![DACH Compliance](https://img.shields.io/badge/DACH_Law-DE_§109_GewO_|_CH_Art._330a_OR_|_AT_§39_AngG-emerald.svg)](https://dach-digitalwerk.netlify.app/arbeitszeugnis/)
[![Live App](https://img.shields.io/badge/Web_App-Live_&_Kostenlos-purple.svg)](https://dach-digitalwerk.netlify.app/arbeitszeugnis/)
[![Status](https://img.shields.io/badge/Status-100%25_Lokal_&_Offline_Datenschutz-brightgreen.svg)](https://dach-digitalwerk.netlify.app/arbeitszeugnis/)

> 🔍 **Open-Source DACH Arbeitszeugnis-Decoder, Formulierungsscanner & Zeugnis-Prüfer.**  
> Entschlüsselt 140+ codierte HR-Phrasen, Notenstufen (1–5), versteckte Warnhinweise (Red Flags) und beredtes Schweigen nach deutschem (§ 109 GewO), schweizerischem (Art. 330a OR) und österreichischem (§ 39 AngG) Arbeitsrecht.

---

### 🌐 Interaktive Live-Web-App (Sofort im Browser nutzen)

**Ohne Anmeldung, ohne Upload zu externen Servern, 100% vertraulich im Browser:**  
👉 **[https://dach-digitalwerk.netlify.app/arbeitszeugnis/](https://dach-digitalwerk.netlify.app/arbeitszeugnis/)**

---

## Inhaltsverzeichnis
1. [Hintergrund: Warum HR-Geheimcodes existieren](#hintergrund-warum-hr-geheimcodes-existieren)
2. [Die 30 wichtigsten Arbeitszeugnis-Geheimcodes (Übersichtstabelle)](#die-30-wichtigsten-arbeitszeugnis-geheimcodes-übersichtstabelle)
3. [Rechtliche Grundlagen im DACH-Raum (DE / CH / AT)](#rechtliche-grundlagen-im-dach-raum-de--ch--at)
4. [Kritische Red Flags & "Beredtes Schweigen"](#kritische-red-flags--beredtes-schweigen)
5. [Verwendung der Standalone-Tools (CLI / Python / JavaScript)](#verwendung-der-standalone-tools-cli--python--javascript)
6. [Muster-Widerspruch & Berichtigung einfordern](#muster-widerspruch--berichtigung-einfordern)
7. [Mitwirken & Lizenz](#mitwirken--lizenz)

---

## Hintergrund: Warum HR-Geheimcodes existieren

Im gesamten DACH-Raum gilt das rechtliche Gebot, dass Arbeitszeugnisse **wohlwollend** formuliert sein müssen und dem Arbeitnehmer das weitere berufliche Fortkommen nicht ungerechtfertigt erschweren dürfen. Gleichzeitig gilt jedoch der Grundsatz der **Zeugniswahrheit**.

Aus diesem Spannungsverhältnis hat die HR-Praxis eine codierte Fachsprache ("Zeugnissprache") entwickelt: Vordergründig freundliche und positive Formulierungen transportieren für geschulte Personaler klare Noten und mitunter vernichtende Beurteilungen.

Wer den Code nicht kennt, hält eine Formulierung wie *„Er zeigte stets großes Engagement und war wegen seiner Geselligkeit bei Kollegen beliebt“* für ein Kompliment – in Wahrheit signalisiert dies oft Überforderung und problematischen Alkoholkonsum oder Geschwätzigkeit.

---

## Die 30 wichtigsten Arbeitszeugnis-Geheimcodes (Übersichtstabelle)

Die folgende Referenztabelle fasst die 30 am häufigsten verwendeten Codierungen im DACH-Raum zusammen:

| # | Zeugnisformulierung | Schulnote | Wahre HR-Bedeutung | Kategorie / Warnstufe | Korrekturvorschlag |
|---|---------------------|-----------|--------------------|-----------------------|-------------------|
| **1** | *„...hat die ihm übertragenen Aufgaben stets zu unserer vollsten Zufriedenheit erledigt.“* | **Note 1 (Sehr gut)** | Höchste Leistungsbeurteilung ohne jede Einschränkung. | Gesamtzufriedenheit 🟢 | Beibehalten |
| **2** | *„...stets zu unserer vollen Zufriedenheit...“* | **Note 2 (Gut)** | Solide, gute Leistung ohne Mängel. | Gesamtzufriedenheit 🟢 | „vollsten Zufriedenheit“ fordern |
| **3** | *„...zu unserer vollen Zufriedenheit...“* | **Note 3 (Befriedigend)** | Durchschnittliche Leistung. Es fehlt das Temporaladverb *„stets“* oder *„jederzeit“*. | Gesamtzufriedenheit 🟡 | *„stets zu unserer vollen...“* |
| **4** | *„...zu unserer Zufriedenheit...“* | **Note 4 (Ausreichend)** | Unterdurchschnittlich. Unter den Erwartungen geblieben. | Gesamtzufriedenheit 🟠 | Dringend nachbessern |
| **5** | *„...hat sich bemüht, den Anforderungen zu entsprechen.“* | **Note 5 (Mangelhaft)** | Völliges Scheitern. Bemühen ohne Erfolg. | Leistung 🔴 Red Flag | Streichen lassen |
| **6** | *„...zeigte für seine Arbeit stets großes Verständnis und Interesse.“* | **Note 5 (Mangelhaft)** | Reine Faulheit. Hat nichts geleistet, nur zugeschaut. | Arbeitsbereitschaft 🔴 | *„setzte sein fundiertes Fachwissen stets äußerst erfolgreich ein.“* |
| **7** | *„Er war stets bemüht, den an ihn gestellten Erwartungen gerecht zu werden.“* | **Note 5 (Mangelhaft)** | Der Klassiker für völlige Unfähigkeit. | Leistung 🔴 Red Flag | Sofort korrigieren |
| **8** | *„Sein Verhalten gegenüber Vorgesetzten und Kollegen war stets einwandfrei.“* | **Note 1 (Sehr gut)** | Vorbildliches Sozialverhalten. Rangfolge Vorgesetzte vor Kollegen ist korrekt. | Verhalten 🟢 | Beibehalten |
| **9** | *„Sein Verhalten gegenüber Kollegen und Vorgesetzten war stets einwandfrei.“* | **Note 4 (Ausreichend)** | Umgekehrte Reihenfolge! Probleme mit Autorität und Vorgesetzten. | Verhalten 🔴 Red Flag | Vorgesetzte zwingend an erste Stelle setzen! |
| **10** | *„Er trug durch seine Geselligkeit zur Verbesserung des Betriebsklimas bei.“* | **Note 5 (Mangelhaft)** | Verdacht auf übermäßigen Alkoholkonsum während oder nach der Arbeit. | Red Flag 🔴 | Vollständig streichen lassen |
| **11** | *„Sie galt im Kollegenkreis als umgängliche und tolerante Kollegin.“* | **Note 5 (Mangelhaft)** | Niemand mochte sie; schwierig im Team. | Verhalten 🔴 | *„wurde von Vorgesetzten und Kollegen gleichermaßen sehr geschätzt.“* |
| **12** | *„Er trat engagiert für die Interessen seiner Kollegen ein.“* | **Note 4 (Ausreichend)** | Unbequeme Gewerkschafts- oder Betriebsratsaktivität; Unruhestifter. | Red Flag 🟠 | Nur neutrales Teamverhalten erwähnen |
| **13** | *„Er zeichnete sich durch seine Pünktlichkeit aus.“* | **Note 5 (Mangelhaft)** | Alibi-Lob: Mehr gab es nicht Positives zu berichten. | Selbstverständlichkeit 🔴 | Streichen oder in Arbeitsstil integrieren |
| **14** | *„Er zeigte stets ein gesundes Selbstvertrauen.“* | **Note 4 (Ausreichend)** | Arrogant, überschätzte sich selbst, unbelehrbar. | Persönlichkeit 🟠 | *„überzeugte durch hohe Fachkompetenz und Souveränität.“* |
| **15** | *„Er verstand es, seine Meinungen mit Nachdruck zu vertreten.“* | **Note 4 (Ausreichend)** | Streitlustig, kompromissunfähig, mangelnde Teamfähigkeit. | Verhalten 🟠 | *„überzeugte durch lösungsorientierte und kooperative Haltung.“* |
| **16** | *„Sie erledigte alle Aufgaben ordnungsgemäß und pflichtbewusst.“* | **Note 4 (Ausreichend)** | Bürokratisch, Dienst nach Vorschrift, keine Eigeninitiative. | Arbeitsstil 🟠 | *„mit herausragender Eigeninitiative und Weitsicht.“* |
| **17** | *„Er war mit großem Eifer bei der Sache.“* | **Note 4 (Ausreichend)** | Übereifrig, chaotisch, machte viele Fehler. | Arbeitsweise 🟠 | *„arbeitete stets zielgerichtet, hochpräzise und effizient.“* |
| **18** | *„Er verfügte über Fachwissen und zeigte ein gesundes Auffassungsvermögen.“* | **Note 4 (Ausreichend)** | Schwache Fachkenntnisse, nur das Allernötigste vorhanden. | Fachwissen 🟠 | *„verfügt über ein exzellentes, stets aktuelles Expertenwissen.“* |
| **19** | *„Wir lernten ihn als umgänglichen Mitarbeiter kennen.“* | **Note 5 (Mangelhaft)** | *„Kennenlernen“*-Floskel signalisiert: Der Eindruck täuschte gewaltig. | Red Flag 🔴 | *„Er war ein jederzeit geschätzter und loyaler Mitarbeiter.“* |
| **20** | *„Er war für die ihm übertragenen Arbeiten umfassend vorbereitet.“* | **Note 5 (Mangelhaft)** | Hat viel geplant, aber nie etwas zu Ende gebracht. | Arbeitserfolg 🔴 | *„setzte Projekte stets termingerecht und mit höchster Qualität um.“* |
| **21** | *„Sie hat alle Aufgaben im Großen und Ganzen zu unserer Zufriedenheit gelöst.“* | **Note 4 (Ausreichend)** | Mängel und Fehler in der Ausführung. | Einschränkung 🟠 | *„im Großen und Ganzen“* zwingend tilgen! |
| **22** | *„Er stand den Kunden jederzeit beratend zur Seite.“* | **Note 4 (Ausreichend)** | Konnte keine Abschlüsse erzielen, schwache Vertriebskraft. | Kundenorientierung 🟠 | *„gewann Neukunden und baute Kundenbeziehungen höchst erfolgreich aus.“* |
| **23** | *„Er führte die Abteilung mit starker Hand.“* | **Note 5 (Mangelhaft)** | Autoritärer Führungsstil, hohe Mitarbeiterfluktuation. | Führung 🔴 | *„führte sein Team kooperativ, motivierend und zielorientiert.“* |
| **24** | *„Wir bedauern sein Ausscheiden sehr, danken ihm für die stets hervorragende Mitarbeit und wünschen ihm für die Zukunft weiterhin viel Erfolg und alles Gute.“* | **Note 1 (Sehr gut)** | Vollständige 4-teilige Schlussformel: Bedauern + Dank + Zukunftswünsche + Beruflicher Erfolg. | Schlussformel 🟢 | Ideale Formulierung! |
| **25** | *„Wir bedauern sein Ausscheiden und wünschen ihm für die Zukunft alles Gute.“* | **Note 3 (Befriedigend)** | Es fehlt der Dank für die Leistungen und der Wunsch nach *„weiterhin“* Erfolg. | Schlussformel 🟡 | Um Dank und *„weiterhin viel Erfolg“* ergänzen |
| **26** | *„Er verlässt unser Unternehmen zum [Datum]. Wir wünschen ihm für die Zukunft alles Gute, insbesondere Erfolg.“* | **Note 4 (Ausreichend)** | *„insbesondere Erfolg“* bedeutet: Bisher hatte er keinen Erfolg! Kein Bedauern, kein Dank. | Schlussformel 🔴 Red Flag | Formulierung anfechten |
| **27** | *„Er verlässt uns auf eigenen Wunsch.“* | **Neutral / Positiv** | Eigenkündigung des Mitarbeiters (keine arbeitgeberseitige Kündigung). | Kündigungsinitiator 🟢 | Beibehalten bei Eigenkündigung |
| **28** | *„Das Arbeitsverhältnis endete im gegenseitigen Einvernehmen.“* | **Note 4 (Ausreichend)** | Typische Aufhebungsvertrag-Chiffre; Kündigung drohte oder Konflikt. | Trennungsgrund 🟠 | Sofern möglich auf eigenen Wunsch abändern |
| **29** | *„Für die Zukunft wünschen wir ihm viel Glück.“* | **Note 5 (Mangelhaft)** | Wer *„Glück“* braucht, hat kein Können. Im Zeugnis fatal. | Schlussformel 🔴 | *„weiterhin viel Erfolg und persönlich alles Gute“* |
| **30** | *„Frau Müller war stets ehrlich und genoss vollstes Vertrauen.“* (ohne Kassenbezug) | **Note 5 (Mangelhaft)** | Verdacht auf Diebstahl oder Unregelmäßigkeiten (außer bei expliziten Kassierern). | Red Flag 🔴 | Nur bei Berufsgruppen mit Geldverantwortung zulässig! |

---

## Rechtliche Grundlagen im DACH-Raum (DE / CH / AT)

### 🇩🇪 Deutschland: § 109 GewO & BAG-Rechtsprechung
* **Gesetzliche Basis:** Gemäß [§ 109 Abs. 2 Gewerbeordnung (GewO)](https://www.gesetze-im-internet.de/gewo/__109.html) muss das Zeugnis klar und verständlich formuliert sein. Es darf keine Merkmale oder Formulierungen enthalten, die den Zweck haben, eine andere als die aus der äußeren Form oder dem Wortlaut ersichtliche Aussage über den Arbeitnehmer zu treffen.
* **Beweislast (BAG):**
  * Note 3 („befriedigend“) gilt laut Bundesarbeitsgericht (BAG, Urteil vom 18.11.2014 – 9 AZR 584/13) als Durchschnitt.
  * Begehrt der Arbeitnehmer ein besseres Zeugnis (Note 1 oder 2), trägt **er** die Darlegungs- und Beweislast für überdurchschnittliche Leistungen.
  * Erteilt der Arbeitgeber ein schlechteres Zeugnis (Note 4 oder 5), trägt der **Arbeitgeber** die Beweislast für unterdurchschnittliche Leistungen.
* **Verjährung & Verwirkung:** Zeugnisansprüche verjähren nach der regelmäßigen Frist von 3 Jahren (§ 195 BGB), können jedoch schon nach 5 bis 10 Monaten verwirken, wenn der Arbeitnehmer untätig bleibt.

### 🇨🇭 Schweiz: Art. 330a OR & Bundesgericht
* **Gesetzliche Basis:** Nach [Art. 330a Obligationenrecht (OR)](https://www.fedlex.admin.ch/eli/cc/27/317_321_377/de#art_330_a) kann der Arbeitnehmer jederzeit vom Arbeitgeber ein Zeugnis verlangen, das sich über die Art und die Dauer des Arbeitsverhältnisses sowie über seine Leistungen und sein Verhalten ausspricht (Vollzeugnis / qualifiziertes Zeugnis).
* **Grundsätze:** Wahrheit, Klarheit und Wohlwollen. Negative Punkte dürfen nur erwähnt werden, wenn sie für das Gesamtbild des Arbeitnehmers und für die zukünftige Anstellung wesentlich sind.
* **Beredtes Schweigen:** Das Weglassen wesentlicher Zeugniselemente (z. B. keine Erwähnung des Verhaltens zu Vorgesetzten) verstößt gegen Art. 330a OR.
* **Verjährungsfrist:** 10 Jahre nach Beendigung des Arbeitsverhältnisses (Art. 127 OR).

### 🇦🇹 Österreich: § 39 AngG & § 1163 ABGB
* **Gesetzliche Basis:** [§ 39 Angestelltengesetz (AngG)](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008069) und [§ 1163 Allgemeines bürgerliches Gesetzbuch (ABGB)](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001622).
* **Erschwerungsverbot:** Das Zeugnis darf keine Eintragungen oder Anmerkungen enthalten, die dem Angestellten die Erlangung einer neuen Stelle erschweren würden.
* Grundsätzlich besteht in Österreich Anspruch auf ein einfaches Zeugnis; ein qualifiziertes Zeugnis kann kollektivvertraglich oder einzelvertraglich geregelt sein.

---

## Kritische Red Flags & "Beredtes Schweigen"

Neben Notencodierungen existieren HR-Verhaltensmuster, die von Personalern sofort bemerkt werden:

1. **Reihenfolgen-Tausch (Hierarchie-Verstoß):**  
   *„Sein Verhalten zu Kollegen und Vorgesetzten war vorbildlich.“*  
   ➡️ Die Nennung der Kollegen vor den Vorgesetzten bedeutet: Respektlosigkeit gegenüber Chefs oder interne Cliquenbildung.
2. **Beredtes Schweigen (Qualifiziertes Auslassen):**  
   Wird eine Kernkompetenz nicht erwähnt (z. B. keine Erwähnung von Ehrlichkeit beim Kassierer, keine Erwähnung von Führungsverhalten bei Abteilungsleitern), signalisiert dies Totalversagen in diesem Bereich.
3. **Passive Konstruktionen:**  
   *„Die Aufgaben wurden ihm übertragen.“* statt *„Er übernahm eigenverantwortlich...“*  
   ➡️ Mangelnde Eigeninitiative, reiner Befehlsempfänger.
4. **Alibi-Lob & Selbstverständlichkeiten:**  
   Ausführliches Lob für Pünktlichkeit, Sauberkeit oder Erscheinen am Arbeitsplatz deutet darauf hin, dass fachlich nichts Positives zu berichten war.

---

## Verwendung der Standalone-Tools (CLI / Python / JavaScript)

Dieses Repository liefert vollständige, unabhängige Skripte zur lokalen Analyse ohne Cloud-Zwang.

### Node.js / JavaScript
```bash
# Analyse eines kurzen Textes via CLI
node decoder.js "Frau Schmidt hat alle Aufgaben stets zu unserer vollsten Zufriedenheit erledigt. Ihr Verhalten gegenüber Vorgesetzten und Kollegen war stets vorbildlich."
```

### Python 3
```bash
# Zeugnisdatei analysieren
py decoder.py sample_zeugnis_sehr_gut.txt --jurisdiction DE

# Mit detaillierter JSON-Ausgabe
py decoder.py sample_zeugnis_red_flags.txt --json
```

### Programmatische Einbindung in eigene Projekte
```javascript
const { analyzeZeugnis } = require('./decoder.js');

const result = analyzeZeugnis("Er war stets bemüht den Anforderungen gerecht zu werden.");
console.log(`Ermittelte Gesamtnote: ${result.overallGrade} (${result.gradeLabel})`);
console.log(`Erkannte Red Flags: ${result.redFlags.length}`);
```

---

## Muster-Widerspruch & Berichtigung einfordern

Sollte Ihr Arbeitszeugnis unberechtigte Codierungen oder eine mangelhafte Note enthalten, sollten Sie schriftlich binnen 2 bis 4 Wochen Widerspruch einlegen.

Ein kostenloses, anwaltlich geprüftes Musterschreiben finden Sie direkt hier:  
📄 **[Musterbrief Arbeitszeugnis-Berichtigung (Online-Vorlage)](https://dach-digitalwerk.netlify.app/arbeitszeugnis-berichtigung-fordern-muster.html)**

---

## Mitwirken & Lizenz

Beiträge, Ergänzungen weiterer Formulierungen und Pull Requests sind herzlich willkommen!  
Erstelle einfach ein Issue oder einen PR mit neuen Phrasen für `codes.json`.

Lizenziert unter der **MIT Lizenz** – freie Verwendung für Entwickler, Betriebsräte, HR-Abteilungen und Arbeitnehmer.  
Entwickelt von [DACH Digitalwerk](https://dach-digitalwerk.netlify.app).
