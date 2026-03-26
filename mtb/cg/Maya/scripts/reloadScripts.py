import sys
import maya.cmds as cmds

def reloadAll(self):

    print("MOCAP_TOOL_BOX: ----------­> Mocap Tool Box as been refreshed")

    # --- 1. SET THE ROOT PATH ---
    root_path = r"C:/TOOLS_Production/mocaptoolbox"

    if root_path not in sys.path:
        sys.path.insert(0, root_path)

    import importlib

    from cg.Maya.scripts                   import actionsMaya
    importlib.reload(actionsMaya)

    from cg.Maya.scripts.animation         import worldSpaceCtrl
    importlib.reload(worldSpaceCtrl)

    from cg.Maya.scripts.animation         import bake
    importlib.reload(bake)

    from cg.Maya.addons.mocaptoolbox       import mocaptoolbox
    importlib.reload(mocaptoolbox)

    from cg.Maya.scripts                   import reloadScripts
    importlib.reload(reloadScripts)

    from cg.Maya.scripts.utilities         import finder
    importlib.reload(finder)

    from cg.Maya.scripts.utilities         import constraint
    importlib.reload(constraint)

    from cg.Maya.scripts.utilities           import locator
    importlib.reload(locator)