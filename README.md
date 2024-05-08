# Automatyczne Usuwanie Plików

Program umożliwia automatyczne planowanie i usuwanie(przenoszenia do kosza) plików lub folderów w określonym czasie.

## Opis

Ten projekt implementuje funkcję automatycznego usuwania (przenoszenia do kosza) plików lub folderów w czasie podanym przez użytkownika. Użytkownik może wybrać, czy chce usunąć element na podstawie daty i godziny, lub wprowadzić liczbę dni, godzin i minut do usunięcia (czasu liczonego od momentu wprowadzenia danych).
#### Uwaga: Na chwilę obecną program musi być uruchomiony od momentu wpisania daty do momentu przeniesienia danego elementu.

## Użycie

1. Uruchomienie programu spowoduje wyświetlenie menu z opcjami:
   - Wybierz opcję 1, aby określić datę i godzinę usunięcia.
   - Wybierz opcję 2, aby określić liczbę dni, godzin i minut do usunięcia.
   - Wpisz 's', aby przerwać operację usuwania.
   - Wpisz 'q', aby wyjść z programu.

2. Wprowadź ścieżkę do pliku lub folderu.

3. Wybierz odpowiednią opcję z menu.

4. Plik lub folder zostanie usunięty zgodnie z wybranym terminem.

## Wymagania

Aby uruchomić ten program, wymagane są następujące biblioteki:
- os
- time
- send2trash
- threading
- keyboard

***

# Automatic File Deletion

The program enables automatic scheduling and deletion (moving to the trash) of files or folders at specified times.

## Description

This project implements a feature for automatically deleting (moving to the trash) files or folders at predefined times. The user can choose whether to delete an item based on a date and time or enter the number of days, hours, and minutes until deletion.
#### Note: Currently, the program must be running from the moment the date is entered until the item is moved.

## Usage

1. Running the program will display a menu with options:
   - Choose option 1 to specify the deletion date and time.
   - Choose option 2 to specify the number of days, hours, and minutes until deletion.
   - Enter 's' to interrupt the deletion operation.
   - Enter 'q' to exit the program.

2. Enter the path to the file or folder.

3. Choose the appropriate option from the menu.

4. The file or folder will be deleted according to the selected deadline.

## Requirements

To run this program, the following libraries are required:
- os
- time
- send2trash
- threading
- keyboard
