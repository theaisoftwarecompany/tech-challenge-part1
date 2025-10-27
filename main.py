"""
Hauptskript für das Tech Challenge Projekt.
"""

import os
from pathlib import Path
from dotenv import load_dotenv


def load_environment():
    """Lädt Umgebungsvariablen aus der .env Datei."""
    load_dotenv()
    app_name = os.getenv("APP_NAME", "tech-challenge")
    environment = os.getenv("ENVIRONMENT", "development")
    return app_name, environment


def initialize_data_directory():
    """Stellt sicher, dass das Datenverzeichnis existiert."""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    return data_dir


def main():
    """Haupteinstiegspunkt des Programms."""
    app_name, environment = load_environment()
    data_dir = initialize_data_directory()
    
    print(f"Anwendung: {app_name}")
    print(f"Umgebung: {environment}")
    print(f"Datenverzeichnis: {data_dir.absolute()}")
    print("\nBereit für Implementierung...")


if __name__ == "__main__":
    main()

