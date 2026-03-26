import sys
import os
import maya.cmds as cmds
from PySide6 import QtWidgets, QtCore


# --- 1. CONFIGURATION DU CHEMIN ---
path_to_folder = "C:/TOOLS_Production/mocaptoolbox"
if path_to_folder not in sys.path:
    sys.path.insert(0, path_to_folder)


# Import du fichier de UI
from cg.Maya.scripts                     import reloadScripts
from cg.Maya.scripts.animation           import worldSpaceCtrl
from cg.Maya.scripts.utilities           import locator
from toolbox.ui                          import menuTab
import importlib
importlib.reload(menuTab)

from cg.Maya.scripts            import actionsMaya



def get_maya_main_window():
    return QtWidgets.QApplication.activeWindow()

# --- 2. LA CLASSE (Hérite de QWidget car ton UI est un 'Form') ---
class TOOLBOX(QtWidgets.QWidget):
    
    def __init__(self):
        
        # On met la fenêtre principale de Maya comme parent
        super().__init__(parent=get_maya_main_window())
        
        # On initialise l'interface Ui_Form
        self.ui = menuTab.Ui_Form()
        

        # Le self.ui devient lui-même le UI, On appel la fonction qui setup le ui
        self.ui.setupUi(self)
        
        # Configuration de la fenêtre avec fonction de Pyside6
        self.setWindowTitle("Mocap Tool Box")
        
        # Fenêtre flottante (faire en sorte d'avoir fenêtré)
        self.setWindowFlags(QtCore.Qt.Window)
        
        # --- 3. CONNEXIONS DES BOUTONS ---
        
        # (pushButton) Make WorldTransformCtrl
        self.ui.worldSpaceBtn.clicked.connect(lambda: actionsMaya.ANIMATION.parentConstraint('', False))
        
        # (pushButton) Make WorldTransformCtrlOffset
        self.ui.worldSpaceOffsetBtn.clicked.connect(lambda: actionsMaya.ANIMATION.parentConstraint('', True))

        # (pushButton) Refresh Script
        self.ui.refreshBtn.clicked.connect(lambda: reloadScripts.reloadAll(''))

        # (pushButton) Bake all and delete all Temp Controls
        self.ui.bakeAllBtn.clicked.connect(lambda: worldSpaceCtrl.WORLDSPACE.bakeDelete(''))
        
        # (pushButton) Bake only selected Temp ctrls
        self.ui.bakeSelectedBtn.clicked.connect(lambda: worldSpaceCtrl.WORLDSPACE.bakeDeleteSelected(''))

        # (pushButton) Make Locator size bigger
        self.ui.locSizeMaxBtn.clicked.connect(lambda: locator.LOCATOR.sizeUp(''))

        # (pushButton) Make Locator size smaller
        self.ui.locSizeMinBtn.clicked.connect(lambda: locator.LOCATOR.sizeDown(''))

        # (pushButton) Create a locator on an object and parent it to it
        self.ui.createlocatorBtn.clicked.connect(lambda: locator.LOCATOR.createLocator(''))

        # (pushButton) Make Locator size smaller
        #self.ui.createIKchainBtn.clicked.connect(lambda: locator.LOCATOR.sizeDown(''))

# LAUNCH
def run():
    global tool_app
    
    # Correction de la logique de fermeture
    try:
        if tool_app is not None:
            tool_app.close()
            tool_app.deleteLater()
    except:
        pass

    # Lancement
    tool_app = TOOLBOX()
    tool_app.show()
