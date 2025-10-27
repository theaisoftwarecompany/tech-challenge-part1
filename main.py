"""
Hauptskript für das Tech Challenge Projekt.
"""

import os
from pathlib import Path
from dotenv import load_dotenv


def load_environment():
    """Lädt Umgebungsvariablen aus der .env Datei."""
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key


def main():
    """Haupteinstiegspunkt des Programms."""
    load_environment()

    ## program logic here
    

if __name__ == "__main__":
    main()