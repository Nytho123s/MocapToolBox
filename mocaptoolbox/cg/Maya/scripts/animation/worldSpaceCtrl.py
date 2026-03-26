from tkinter import Scale
import maya.cmds as cmds

from cg.Maya.scripts                import actionsMaya
from cg.Maya.scripts.animation      import bake
from cg.Maya.scripts.utilities      import finder
from cg.Maya.scripts.utilities      import constraint

class WORLDSPACE(object):

    def __init__(self):
          pass

    def worldSpaceParentConstraint(self, offset):

        # 1. On commence le bloc d'annulation
        cmds.undoInfo(openChunk=True)

        # 1. Récupérer la sélection actuelle
        target_selection = cmds.ls(selection=True)

        # Check if an object is selected
        if not target_selection:
            cmds.warning("Hey buddy! Select an object first!")
            return

        # Create a locator
        loc = cmds.spaceLocator(name="WSC_loc")[0]

        # This moves the locator to the target's position and orientation
        cmds.matchTransform(loc, target_selection)

        if offset == True:

            # 2. Make sure the locator is selected
            cmds.select(loc, replace=True)
            print("ALLO")
            # 'runOnce=True' est CRUCIAL : le job se supprime tout seul dès qu'il a fini sa tâche une fois
            cmds.scriptJob(event=["SelectionChanged", lambda: finder.FINDPARENT.check_selection('', loc, target_selection)], runOnce=True)
            

        else:
            cmds.parentConstraint(target_selection, loc)
            bake.BAKING.bake_selected_objects('', loc, '')
            cmds.parentConstraint(loc, target_selection)
            




    # This function deletes the selected temp ctrl
    def bakeDelete(self):
        
        finder.FINDPARENT.findreturn()
        toBake = cmds.ls(selection=True)

        bake.BAKING.bake_selected_objects('', toBake, '')

        target_pattern = "WSC*"
        # We find the shapes first to ensure they are actually locators
        all_locators = cmds.ls(target_pattern, type='locator', long=True)
    
        # We also check transforms in case the transform itself is named WSC
        # but the shape inside is just 'locatorShape1'
        transforms = cmds.ls(target_pattern, type='transform', long=True)
        locators_by_name = [t for t in transforms if cmds.listRelatives(t, s=True, type='locator')]

        # Combine and remove duplicates
        to_delete = list(set(all_locators + locators_by_name))

        if not to_delete:
            print("No locators starting with 'WSC' were found.")
            return

        # Delete the objects
        cmds.delete(to_delete)


    def bakeDeleteSelected(self):
            listObj, listLoc = finder.FINDPARENT.get_object_from_selected_wsc()
            bake.BAKING.bake_selected_objects('','', listObj)
            cmds.delete(listLoc)