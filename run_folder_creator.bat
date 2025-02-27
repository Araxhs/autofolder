@echo off
echo Paste your folder structure, then press Ctrl+Z and Enter when done:
copy con folder_structure.txt

echo Creating folders and files...
python folder_creator.py

echo Done! Press any key to exit.
pause
