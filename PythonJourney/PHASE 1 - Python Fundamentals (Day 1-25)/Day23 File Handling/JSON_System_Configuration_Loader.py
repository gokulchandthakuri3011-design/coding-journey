"""
### Assignment 3: JSON System Configuration Loader (Medium)

Create a program that:
1. Reads a JSON config file (`config.json`) containing app settings
2. Displays all settings to the user
3. Allows the user to update a setting
4. Saves the updated settings back to the JSON file

**Sample `config.json`:**
```json
{
    "app_name": "MyApp",
    "version": "1.0.0",
    "theme": "dark",
    "font_size": 14,
    "auto_save": true
}
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def reading_json():
    with open(os.path.join(BASE_DIR, "config.json"), "r") as file:
        app_settings = json.load(file)

        # Printing app settings
        print(f"App settings: {app_settings}")

        # For user choice to update setting
        for i, key in enumerate(app_settings.keys(), start=1):
            print(f"{i}. {key}")
        choice = input("Enter the choice (1-5) to update them: ")
        if choice == "1":
            name = input("Enter the app name: ")
            app_settings["app_name"] = name
        elif choice == "2":
            version = input("Enter the version number: ")
            app_settings["version"] = version
        elif choice == "3":
            theme = input("Enter the theme of your choice: ")
            app_settings["theme"] = theme
        elif choice == "4":
            font_size = int(input("Enter the font size of your liking: "))
            app_settings["font_size"] = font_size
        elif choice == "5":
            auto_save = input("Enter True/False: ")
            app_settings["auto_save"] = auto_save
        else: 
            print("Wrong Choice! Please choose (1-5).")
            return
    updating_json(app_settings)

def updating_json(app_settings):
    with open(os.path.join(BASE_DIR,"config.json"), "w") as file:
        json.dump(app_settings, file, indent=4)

    # To verify if the app setting is updated or not
    with open(os.path.join(BASE_DIR, "config.json"), "r") as file:
        print(file.read())

reading_json()