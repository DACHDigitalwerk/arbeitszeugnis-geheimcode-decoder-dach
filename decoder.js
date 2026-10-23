/**
 * Arbeitszeugnis Geheimcode Decoder (DACH)
 * Standalone Node.js & Browser Engine
 * Copyright (c) 2026 DACH Digitalwerk (MIT License)
 */

const fs = require('fs');
const path = require('path');

// Load database
let CODES = [];
try {
  const raw = fs.readFileSync(path.join(__dirname, 'codes.json'), 'utf8');
  CODES = JSON.parse(raw);
} catch (e) {
  console.warn('codes.json could not be loaded via fs, using fallback.');
}

function normalize(text) {
  return String(text || '')
    .toLowerCase()
    .replace(/ß/g, 'ss')
    .replace(/[„“"»«]/g, '"')
    .replace(/\s+/g, ' ');
}

function analyzeZeugnis(text, jurisdiction = 'DE') {
  const normText = normalize(text);
  const matches = [];
  const redFlags = [];
  let totalGradeWeight = 0;
  let gradeCount = 0;

  for (const item of CODES) {
    const normPhrase = normalize(item.phrase);
    if (normText.includes(normPhrase)) {
      matches.push(item);
      if (item.isRedFlag || item.grade >= 4) {
        redFlags.push(item);
      }
      totalGradeWeight += item.grade;
      gradeCount += 1;
    }
  }

  // Check for closing formula components
  const hasBedauern = /bedauer/i.test(text);
  const hasDank = /dank/i.test(text);
  const hasErfolg = /erfolg/i.test(text);
  const hasZukunft = /zukunft|weiter/i.test(text);

  const missingClosingParts = [];
  if (!hasBedauern) missingClosingParts.push('Bedauern über das Ausscheiden');
  if (!hasDank) missingClosingParts.push('Dank für geleistete Dienste');
  if (!hasErfolg) missingClosingParts.push('Wunsch nach weiterhin beruflichem Erfolg');

  const calculatedGrade = gradeCount > 0 ? (totalGradeWeight / gradeCount).toFixed(1) : '3.0';
  let gradeLabel = 'Befriedigend';
  const numericGrade = parseFloat(calculatedGrade);
  if (numericGrade <= 1.5) gradeLabel = 'Sehr gut';
  else if (numericGrade <= 2.5) gradeLabel = 'Gut';
  else if (numericGrade <= 3.5) gradeLabel = 'Befriedigend';
  else if (numericGrade <= 4.5) gradeLabel = 'Ausreichend';
  else gradeLabel = 'Mangelhaft';

  return {
    jurisdiction,
    overallGrade: numericGrade,
    gradeLabel,
    totalPhrasesMatched: matches.length,
    matchedItems: matches,
    redFlags,
    closingFormulaAudit: {
      hasBedauern,
      hasDank,
      hasErfolg,
      hasZukunft,
      missingClosingParts,
      isComplete: missingClosingParts.length === 0
    }
  };
}

module.exports = { analyzeZeugnis, normalize };

if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.log('Usage: node decoder.js "<Zeugnistext>" [DE|CH|AT]');
    process.exit(1);
  }
  const sample = args[0];
  const juris = args[1] || 'DE';
  const result = analyzeZeugnis(sample, juris);
  console.log('=== DACH ARBEITSZEUGNIS ANALYSE ===');
  console.log(`Rechtsraum: ${result.jurisdiction}`);
  console.log(`Ermittelte Gesamtnote: ${result.overallGrade} (${result.gradeLabel})`);
  console.log(`Gefundene codierte Phrasen: ${result.totalPhrasesMatched}`);
  console.log(`Gefundene Red Flags: ${result.redFlags.length}`);
  if (result.redFlags.length > 0) {
    console.log('\n[WARNUNG] Gefundene kritische Codes:');
    result.redFlags.forEach(rf => {
      console.log(`- Note ${rf.grade} [${rf.category}]: "${rf.phrase}" -> ${rf.meaning}`);
    });
  }
}
