import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import zipfile
import os


def generer_arborescence_zip(chemin_zip, status_label):
    """
    Traite le fichier ZIP déposé et met à jour l'interface.
    Le fichier .txt est créé dans le même dossier que le .zip.
    """

    # 1. Réinitialiser le statut
    status_label.config(text="Traitement en cours...", fg="blue")
    root.update_idletasks()  # Forcer la mise à jour de l'interface

    try:
        # 2. Vérifier si c'est bien un .zip (double vérification)
        if not chemin_zip.lower().endswith('.zip'):
            raise ValueError("Le fichier n'est pas un .zip")

        # 3. Déterminer les noms de fichiers
        dossier_parent = os.path.dirname(chemin_zip)
        nom_zip = os.path.basename(chemin_zip)
        nom_base, _ = os.path.splitext(nom_zip)
        fichier_sortie = os.path.join(dossier_parent, f"arborescence_{nom_base}.txt")

        # 4. Logique de lecture du ZIP (identique au script précédent)
        with zipfile.ZipFile(chemin_zip, 'r') as zf:
            liste_fichiers = sorted(zf.namelist())

            with open(fichier_sortie, 'w', encoding='utf-8') as f:
                f.write(f"Arborescence de : {nom_zip}\n")
                f.write("=" * (18 + len(nom_zip)) + "\n\n")

                if not liste_fichiers:
                    f.write("(Ce fichier ZIP est vide)\n")
                else:
                    for chemin in liste_fichiers:
                        if not chemin: continue
                        parties = chemin.split('/')
                        nom_item = ""
                        profondeur = 0

                        if chemin.endswith('/'):
                            nom_item = parties[-2] + "/"
                            profondeur = len(parties) - 2
                        else:
                            nom_item = parties[-1]
                            profondeur = len(parties) - 1

                        indentation = "    " * profondeur
                        f.write(f"{indentation}{nom_item}\n")

        # 5. Afficher le succès
        status_label.config(text=f"Succès ! Fichier '{os.path.basename(fichier_sortie)}' créé.", fg="green")

    except zipfile.BadZipFile:
        status_label.config(text="Erreur : Fichier ZIP corrompu ou invalide.", fg="red")
    except (ValueError, PermissionError) as e:
        status_label.config(text=f"Erreur : {e}", fg="red")
    except Exception as e:
        status_label.config(text=f"Erreur inattendue : {e}", fg="red")


def on_drop(event):
    """
    Fonction appelée lorsque quelque chose est déposé sur la zone.
    """
    # event.data contient le chemin du fichier (ou des fichiers)
    # Nettoyage du chemin (tkinterdnd2 ajoute des {} s'il y a des espaces)
    chemin_fichier = event.data.strip('{}')

    # On passe le chemin et le label de statut à la fonction de traitement
    generer_arborescence_zip(chemin_fichier, status_label)


# --- Configuration de la fenêtre principale ---

# 1. Initialiser la fenêtre avec TkinterDnD (au lieu de tk.Tk())
root = TkinterDnD.Tk()
root.title("Analyseur d'arborescence ZIP")
root.geometry("450x250")

# 2. Créer la zone de "dépôt"
drop_zone_label = tk.Label(
    root,
    text="Glissez-déposez votre fichier .zip ici",
    font=("Arial", 14),
    relief="groove",  # Style de bordure
    borderwidth=2,
    bg="lightgray",
    padx=20,
    pady=20
)
drop_zone_label.pack(fill="both", expand=True, padx=20, pady=20)

# 3. Créer un label pour afficher le statut (succès ou erreur)
status_label = tk.Label(
    root,
    text="En attente d'un fichier...",
    font=("Arial", 11),
    pady=10
)
status_label.pack()

# --- Liaison des événements ---

# 4. Enregistrer la zone comme cible de dépôt pour les fichiers
drop_zone_label.drop_target_register(DND_FILES)

# 5. Lier l'événement <<Drop>> (lorsque le fichier est lâché)
#    à notre fonction 'on_drop'
drop_zone_label.dnd_bind('<<Drop>>', on_drop)

# 6. Lancer la boucle principale de l'interface
root.mainloop()