#!/usr/bin/env python3
"""
YouTube Clip Extractor - Language Launcher
Lanceur pour choisir la langue de l'application
"""

import os
import sys
import subprocess

def main():
    print("🎞️ YouTube Clip Extractor")
    print("=" * 40)
    print("Choose your language / Choisissez votre langue:")
    print("1. 🇺🇸 English")
    print("2. 🇫🇷 Français")
    print("3. ❌ Exit / Quitter")
    print("=" * 40)
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            print("🚀 Launching English version...")
            subprocess.run([sys.executable, "app_en.py"])
            break
        elif choice == "2":
            print("🚀 Lancement de la version française...")
            subprocess.run([sys.executable, "app_fr.py"])
            break
        elif choice == "3":
            print("👋 Goodbye! / Au revoir!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
            print("❌ Choix invalide. Veuillez entrer 1, 2 ou 3.")

if __name__ == "__main__":
    main() 