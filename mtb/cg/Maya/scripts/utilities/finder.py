import maya.cmds as cmds

from cg.Maya.scripts.animation  import bake

class FINDPARENT(object):

    def __init__(self):
        pass

    def findreturn():
        # 1. On récupère TOUTES les parentConstraints de la scène
        all_constraints = cmds.ls(type='parentConstraint')
    
        objets_a_selectionner = []

        for constraint in all_constraints:
            # 2. On demande à la contrainte la liste de ses cibles (les objets qui la pilotent)
            targets = cmds.parentConstraint(constraint, query=True, targetList=True)
        
            if targets:
                # 3. On vérifie si une des cibles commence par "WSC"
                for t in targets:
                    if t.startswith("WSC"):
                        # 4. On trouve l'objet qui est piloté par cette contrainte
                        # (Le parent de la contrainte dans l'Outliner)
                        parent = cmds.listRelatives(constraint, parent=True, fullPath=True)
                        if parent:
                            objets_a_selectionner.append(parent[0])
                            break # On a trouvé une cible WSC, pas besoin de vérifier les autres pour cet objet

        # 5. Sélection finale
        if objets_a_selectionner:
            # On enlève les doublons
            objets_a_selectionner = list(set(objets_a_selectionner))
            cmds.select(objets_a_selectionner, replace=True)
            print(f"Succès ! Objets trouvés : {objets_a_selectionner}")
        else:
            cmds.select(clear=True)
            print("Aucun objet piloté par une cible 'WSC' n'a été trouvé.")

        return objets_a_selectionner


    def get_object_from_selected_wsc():
        # 1. On récupère TOUTE la sélection (noms longs pour la précision)
        selection = cmds.ls(selection=True, long=True)

        if not selection:
            cmds.warning("Veuillez sélectionner au moins un locator WSC.")
            return []
    
        # 2. On récupère toutes les parentConstraints de la scène une seule fois (optimisation)
        all_constraints = cmds.ls(type='parentConstraint')
    
        if not all_constraints:
            print("Aucune parentConstraint trouvée dans la scène.")
            return []

        found_driven_objects = []

        # 3. On boucle sur chaque locator sélectionné
        for selected_item in selection:
            short_name = selected_item.split('|')[-1]
        
            # Pour chaque locator, on cherche s'il est une cible dans une contrainte
            for constraint in all_constraints:
                targets = cmds.parentConstraint(constraint, query=True, targetList=True)
            
                # Si le locator est dans la liste des targets de cette contrainte
                if targets and any(short_name in t for t in targets):
                    # On trouve l'objet piloté
                    driven = cmds.listRelatives(constraint, parent=True, fullPath=True)
                    if driven:
                        found_driven_objects.append(driven[0])
                        # Une fois trouvé pour ce locator, on peut passer au locator suivant
                        break 

        # 4. Nettoyage final (on enlève les doublons si plusieurs locators pilotent le même objet)
        final_list = list(set(found_driven_objects))

        if final_list:
            print(f"Succès ! {len(final_list)} objet(s) trouvé(s) : {final_list}")
        else:
            print("Aucun objet piloté trouvé pour la sélection actuelle.")

        return final_list, selection


    def get_selected_locators():
        # 1. On récupère TOUTE la sélection (noms longs pour la précision)
        selection = cmds.ls(selection=True, long=True)

        if not selection:
            cmds.warning("Veuillez sélectionner au moins un locator WSC.")
            return []

    def check_selection(self, loc, trg):
                """
                Vérifie si le locator est toujours dans la sélection.
                """
                cmds.parentConstraint(trg, loc, maintainOffset=True)
                selection = cmds.ls(selection=True)

                if loc not in selection:
                    # 1. On arrête de surveiller pour ne pas boucler à l'infini
                    # Le scriptJob s'auto-détruit grâce à l'argument 'runOnce=True' dans la création
        
                    # 2. On lance la suite pour le bake
                    bake.BAKING.bake_selected_objects('', loc, '')
                    cmds.parentConstraint(loc, trg, maintainOffset=True)
                else:
                    return