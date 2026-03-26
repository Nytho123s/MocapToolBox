import maya.cmds as cmds

from cg.Maya.scripts.animation      import worldSpaceCtrl

class BAKING(object):

    def __init__(self):
          pass

    def bake_selected_objects(self, selObj, listObj):

        # Set the timeline as start and ending of the bake
        start_frame = cmds.playbackOptions(query=True, minTime=True)
        end_frame = cmds.playbackOptions(query=True, maxTime=True)

        attrs_to_bake = ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"]
       
        if selObj:

            cmds.bakeResults(
            selObj,
            simulation=True,               # Actually calculates the physics/constraints
            attribute=attrs_to_bake,
            time=(start_frame, end_frame), # The frame range to bake
            sampleBy=1,                    # Bakes on every 1 frame (put 2 for every other frame)
            disableImplicitControl=False,  # Mutes the constraints after baking so keyframes take over
            preserveOutsideKeys=True,      # Doesn't delete keys outside your time range
            sparseAnimCurveBake=False      # Forces a key on every single frame
            )
        else:
            cmds.bakeResults(
            listObj,
            simulation=True,               # Actually calculates the physics/constraints
            attribute=attrs_to_bake,
            time=(start_frame, end_frame), # The frame range to bake
            sampleBy=1,                    # Bakes on every 1 frame (put 2 for every other frame)
            disableImplicitControl=False,  # Mutes the constraints after baking so keyframes take over
            preserveOutsideKeys=True,      # Doesn't delete keys outside your time range
            sparseAnimCurveBake=False      # Forces a key on every single frame
            )

  



