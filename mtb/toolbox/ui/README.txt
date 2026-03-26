FICHIER .UI CONVERTION EN .PY

TERMINAL COMMANDS
& "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Scripts\pyside6-uic.exe" toto.ui -o ui_toto.py

OU 

& "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Scripts\pyside6-uic.exe"
 "C:\TOOLS_Production\mocaptoolbox\2025\scripts\ui\MenuTab.ui" -o "C:\TOOLS_Production
\mocaptoolbox\2025\scripts\ui\ui_toto.py"


& "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Scripts\pyside6-uic.exe" "C:\TOOLS_Production\mocaptoolbox\toolbox\ui\MenuTabREF.ui" -o "C:\TOOLS_Production\mocaptoolbox\toolbox\ui\menuTab.py"




LANCEMENT DE QT DESIGNER

python -m venv venv_test 
venv_test\Scripts\activate.bat 
pip install pyside6
pip install pyqt6-tools
pyside6-designer