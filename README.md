## Introduction
Metadata Extractor est une application web Flask conçue pour l'extraction de métadonnées de fichiers multimédias, office et pdf. Elle offre une interface conviviale pour les utilisateurs souhaitant obtenir des informations détaillées sur leurs fichiers audio, vidéo, images, documents office et PDF.

## Fonctionnalités
- Extraction de métadonnées de fichiers multimédias.
- Interface utilisateur intuitive pour le téléchargement de fichiers.
- Affichage détaillé des métadonnées.
- Option pour télécharger les métadonnées en format CSV.

## Installation
1. Clonez le dépôt Git `git clone https://github.com/INESNDJANA/realmetadata`
2. Installez les dépendances avec `pip install -r requirements.txt`.
3. Lancez l'application avec `python app.py`.
4. Ouvrez votre navigateur à l'adresse `http://127.0.0.1:5000`.

## Utilisation
1. Sur la page d'accueil, cliquez sur *"Choisir des fichiers"* pour sélectionner les fichiers à analyser.
2. Une fois les fichiers sélectionnés, cliquez sur *"Upload Folder"* pour les télécharger sur le serveur.
3. L'application traitera les différents fichiers contenus dans le repertoire et affichera les métadonnées.

## Captures d'écran
- Page d'accueil où l'utilisateur peut choisir des fichiers à télécharger.
![Page d'accueil](/static/Page_d'acceuil.png)

- Dialogue de sélection du répertoire.
![Dialogue de sélection](/static/Dialogue_de_selection.png)

- Répertoire sélectionné prêt à être chargé.
![Répertoire sélectionnés](/static/Repertoire_selectionné.png)

- Affichage des métadonnées extraites avec l'option de télécharger en CSV.
![Métadonnées extraites 1](/static/Affichage_MetaData_1.png)
![Métadonnées extraites 2](/static/Affichage_MetaData_2.png)

## Choix Techniques
- Utilisation de **JavaScript** pour améliorer l'interaction côté client.
- **Flask** a été choisi pour sa légèreté et sa facilité d'utilisation dans le développement d'applications web.
- **Bibliothèques de traitement des fichiers** telles que `PyPDF2`, `python-docx`, `openpyxl`, `python-pptx`, `pillow`, `moviepy`, `mutagen` pour manipuler divers formats de fichiers.
- **Bootstrap** pour un design responsive et moderne.
- **PyPDF2** : Pour manipuler les fichiers PDF.
- **python-docx** : Pour manipuler les documents Word (.docx).
- **openpyxl** : Pour manipuler les fichiers Excel (.xlsx).
- **python-pptx** : Pour manipuler les présentations PowerPoint (.pptx).
- **Pillow** : Une bibliothèque de traitement d'images.
- **moviepy** : Pour l'édition vidéo.
- **mutagen** : Pour manipuler les métadonnées audio.


## Problèmes Rencontrés
- La gestion des différents formats de fichiers a nécessité une recherche approfondie pour trouver les bonnes bibliothèques.
- Assurer une extraction des métadonnées cohérente pour différents types de fichiers a été un défi.

## Améliorations Futures
- Ajout de la prise en charge d'autres formats de fichiers.
- Amélioration de l'interface utilisateur pour une meilleure expérience mobile.
- Intégration d'une API pour permettre l'utilisation du service par d'autres applications.

## Conclusion
Metadata Extractor est un outil polyvalent pour quiconque a besoin d'accéder rapidement et facilement aux métadonnées de fichiers multimédias et documents. Avec son interface simple et ses fonctionnalités robustes, il s'adresse aussi bien aux professionnels qu'aux amateurs.
