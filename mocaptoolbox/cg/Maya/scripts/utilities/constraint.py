import maya.cmds as cmds

from cg.Maya.scripts        import actionsMaya

class CONSTRAINT(object):

    def __init__(self):
        pass

    def constraintBake(self, trg, loc):

        #Make the locator copy the targets movement
        cmds.parentConstraint(trg, loc)

        # Bake the animation
        actionsMaya.ANIMATION.bakeOperation('', loc, '')
        
        # Delete the current constraints
        relatives = cmds.listRelatives(loc, type="constraint")
        if relatives:
            cmds.delete(relatives)

        # Parenting operation     
        cmds.parentConstraint(loc, trg)

        # Select the new locator
        cmds.select(loc)

        # 1. On termine le bloc d'annulation
        cmds.undoInfo(closeChunk=True)