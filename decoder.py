#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arbeitszeugnis Geheimcode Decoder (DACH: DE / CH / AT)
Standalone Python CLI & Engine
Copyright (c) 2026 DACH Digitalwerk (MIT License)
"""

import os
import sys
import json
import re
import argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CODES_PATH = os.path.join(SCRIPT_DIR, "codes.json")

def load_codes():
    if os.path.exists(CODES_PATH):
        with open(CODES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def normalize_text(text: str) -> str:
    text = (text or "").lower()
    text = text.replace("ß", "ss")
    text = re.sub(r'[„“”«»"]', '"', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def analyze_certificate(text: str, jurisdiction: str = "DE") -> dict:
    codes = load_codes()
    norm_text = normalize_text(text)
    
    matches = []
    red_flags = []
    total_grade = 0
    grade_count = 0

    for item in codes:
        norm_phrase = normalize_text(item["phrase"])
        if norm_phrase in norm_text:
            matches.append(item)
            if item.get("isRedFlag") or item.get("grade", 3) >= 4:
                red_flags.append(item)
            total_grade += item.get("grade", 3)
            grade_count += 1

    overall_grade = round(total_grade / grade_count, 1) if grade_count > 0 else 3.0
    
    if overall_grade <= 1.5:
        grade_label = "Sehr gut (Note 1)"
    elif overall_grade <= 2.5:
        grade_label = "Gut (Note 2)"
    elif overall_grade <= 3.5:
        grade_label = "Befriedigend (Note 3)"
    elif overall_grade <= 4.5:
        grade_label = "Ausreichend (Note 4)"
    else:
        grade_label = "Mangelhaft (Note 5)"

    # Closing formula analysis
    has_bedauern = bool(re.search(r"bedauer", text, re.IGNORECASE))
    has_dank = bool(re.search(r"dank", text, re.IGNORECASE))
    has_erfolg = bool(re.search(r"erfolg", text, re.IGNORECASE))
    has_zukunft = bool(re.search(r"zukunft|weiter", text, re.IGNORECASE))

    missing = []
    if not has_bedauern:
        missing.append("Bedauern über das Ausscheiden fehlt")
    if not has_dank:
        missing.append("Dank für Mitarbeit/Leistung fehlt")
    if not has_erfolg:
        missing.append("Wunsch nach weiterhin beruflichem Erfolg fehlt")

    return {
        "jurisdiction": jurisdiction,
        "overallGrade": overall_grade,
        "gradeLabel": grade_label,
        "totalPhrasesMatched": len(matches),
        "matches": matches,
        "redFlags": red_flags,
        "closingFormula": {
            "hasBedauern": has_bedauern,
            "hasDank": has_dank,
            "hasErfolg": has_erfolg,
            "hasZukunft": has_zukunft,
            "missingComponents": missing,
            "isComplete": len(missing) == 0
        }
    }

def main():
    parser = argparse.ArgumentParser(description="DACH Arbeitszeugnis Geheimcode Decoder")
    parser.add_argument("file_or_text", help="Dateipfad zu einem Zeugnis (.txt) oder Rohtext")
    parser.add_argument("--jurisdiction", "-j", choices=["DE", "CH", "AT"], default="DE", help="Rechtsraum (DE, CH, AT)")
    parser.add_argument("--json", action="store_true", help="Ergebnis als JSON ausgeben")
    
    args = parser.parse_args()

    content = args.file_or_text
    if os.path.exists(content):
        with open(content, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

    result = analyze_certificate(content, args.jurisdiction)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    print("=" * 65)
    print(" 🔍 DACH ARBEITSZEUGNIS DECODER & GEHEIMCODE-ANALYSE")
    print(f" Rechtsraum: {result['jurisdiction']} | Gesamtnote: {result['overallGrade']} ({result['gradeLabel']})")
    print("=" * 65)
    print(f"\nErkannte Phrasen: {result['totalPhrasesMatched']}")
    print(f"Gefundene Red Flags: {len(result['redFlags'])}")

    if result["redFlags"]:
        print("\n⚠️ KRITISCHE BEURTEILUNGEN & RED FLAGS:")
        for rf in result["redFlags"]:
            print(f"  • [Note {rf['grade']}] \"{rf['phrase']}\"")
            print(f"    Bedeutung: {rf['meaning']}")
            print(f"    Empfehlung: {rf['replacement']}\n")

    print("📋 PRÜFUNG DER SCHLUSSFORMEL:")
    cf = result["closingFormula"]
    if cf["isComplete"]:
        print("  ✅ Vollständige 4-teilige Schlussformel vorhanden (Bedauern, Dank, Zukunftswünsche, Erfolg).")
    else:
        print("  ⚠️ Unvollständige Schlussformel (Beredtes Schweigen):")
        for m in cf["missingComponents"]:
            print(f"    - {m}")

    print("\n👉 Interaktiven Web-Decoder nutzen: https://dach-digitalwerk.netlify.app/arbeitszeugnis/")

if __name__ == "__main__":
    main()
