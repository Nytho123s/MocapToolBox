# -*- coding: utf-8 -*-
from PySide6 import QtWidgets
import importlib
import os
import getpass
import datetime

from cg.Maya.scripts.animation   import worldSpaceCtrl
from cg.Maya.scripts.animation   import bake
from cg.Maya.scripts.utilities   import constraint

class ANIMATION(object):

    def __init__(self):
        pass

    # CALL THE FONCTION TO APPLY A WORLD CONTROLLER
    def parentConstraint(self, offset):
        worldSpaceCtrl.WORLDSPACE.worldSpaceParentConstraint('', offset)

    #def parentConstraintOffset(self, offset):
    #    worldSpaceCtrl.WORLDSPACE.worldSpaceParentConstraint('', offset)

    def bakeOperation(self, selObj, listObj):
        bake.BAKING.bake_selected_objects('', selObj, listObj)


class RETARGETING(object):

    def __init__(self):
        pass

class EXPORT(object):

    def __init__(self):
        pass





