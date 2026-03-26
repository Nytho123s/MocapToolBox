import maya.cmds as cmds

from cg.Maya.scripts.animation  import bake

class LOCATOR(object):

    def __init__(self):
        pass

     # This fonction create a locator on a selected object or ctrl
    def createLocator(self):

        # Makes a list of the selected objects
        selection = cmds.ls(sl=True, type='transform')
    
        # Makes sure we got at least one selected
        if not selection:
            cmds.warning("Aucun objet sélectionné !")
            return

        # Boucle to place a locator and parent it to the selected object
        for obj in selection:

            # Creation of the locator
            loc = cmds.spaceLocator(name=f"WSC_ik_loc")[0]

            # Match the spostion of the object
            cmds.matchTransform(loc, obj, pos=True, rot=True)
                
            # Apply a constraint
            cmds.parentConstraint(loc, obj, maintainOffset=True)

    def sizeUp(self):
        facteur = 2
        # 1. Récupérer la sélection actuelle
        selection = cmds.ls(sl=True, type='transform')

        for obj in selection:
            # On cherche spécifiquement la shape de type 'locator'
            shapes = cmds.listRelatives(obj, shapes=True, type='locator')
        
            if shapes:
                loc_shape = shapes[0]
            
                # 2. Récupérer le localScale actuel sur la SHAPE
                # localScale est un attribut composé, on récupère le premier index
                current_l_scale = cmds.getAttr(f"{loc_shape}.localScale")[0]
            
                # 3. Calculer le nouveau local scale
                new_lx = current_l_scale[0] * facteur
                new_ly = current_l_scale[1] * facteur
                new_lz = current_l_scale[2] * facteur
            
                # 4. Appliquer les nouvelles valeurs sur la SHAPE
                cmds.setAttr(f"{loc_shape}.localScale", new_lx, new_ly, new_lz, type="double3")

    def sizeDown(self):
        facteur = 0.5
        # 1. Récupérer la sélection actuelle
        selection = cmds.ls(sl=True, type='transform')

        for obj in selection:
            # On cherche spécifiquement la shape de type 'locator'
            shapes = cmds.listRelatives(obj, shapes=True, type='locator')
        
            if shapes:
                loc_shape = shapes[0]
            
                # 2. Récupérer le localScale actuel sur la SHAPE
                # localScale est un attribut composé, on récupère le premier index
                current_l_scale = cmds.getAttr(f"{loc_shape}.localScale")[0]
            
                # 3. Calculer le nouveau local scale
                new_lx = current_l_scale[0] * facteur
                new_ly = current_l_scale[1] * facteur
                new_lz = current_l_scale[2] * facteur
            
                # 4. Appliquer les nouvelles valeurs sur la SHAPE
                cmds.setAttr(f"{loc_shape}.localScale", new_lx, new_ly, new_lz, type="double3")
