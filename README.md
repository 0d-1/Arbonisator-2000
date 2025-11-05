# Arbonisator 2000

Arbonisator 2000 est une petite application graphique permettant de générer l'arborescence d'un fichier ZIP. L'interface offre une zone de glisser-déposer : il suffit de déposer un fichier `.zip` pour que l'application génère un fichier texte listant la structure complète de l'archive.

## Fonctionnalités
- Interface graphique simple basée sur Tkinter avec prise en charge du glisser-déposer grâce à `tkinterdnd2`.
- Vérification de l'intégrité et du format du fichier déposé.
- Génération d'un fichier texte `arborescence_<nom_du_zip>.txt` dans le même dossier que l'archive analysée.

## Prérequis
- Python 3.9 ou supérieur.
- Bibliothèques Python :
  - `tkinter` (inclus par défaut avec la plupart des distributions Python).
  - `tkinterdnd2` pour la gestion du glisser-déposer.

Installez `tkinterdnd2` via pip si nécessaire :

```bash
pip install tkinterdnd2
```

Sur certaines distributions Linux, l'installation de Tkinter peut nécessiter des paquets système supplémentaires. Par exemple, sous Debian/Ubuntu :

```bash
sudo apt-get install python3-tk
```

## Lancement de l'application

```bash
python "Arbonisator 2000/arbo.py"
```

Une fenêtre s'ouvrira avec une zone où déposer votre fichier ZIP. Une fois le traitement terminé, un fichier `arborescence_<nom_du_zip>.txt` sera créé aux côtés de l'archive originale.

## Dépannage
- **Fichier non reconnu** : Vérifiez que le fichier déposé possède bien l'extension `.zip`.
- **ZIP corrompu** : Un message d'erreur s'affiche si l'archive ne peut pas être lue.
- **Problèmes d'encodage** : Les fichiers générés sont encodés en UTF-8.

## Licence
Ce projet n'indique pas encore de licence spécifique. Pensez à en ajouter une si nécessaire.
