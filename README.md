# FileToMarkdown


### Description

FileToMarkdown est un outil qui permet de convertir des fichiers personnalisés au format .tmd en fichiers Markdown standards (.md).
Ce projet vise à simplifier la rédaction de contenu structuré en utilisant une syntaxe légère et extensible.

### Fonctionnalités

- Conversion de fichiers .tmd vers .md
- Support des titres (h1 à h6)
- Texte en gras et en italique
- Listes simples
- Liens et images
- Blocs de code
- Tableaux personnalisés


### Format du fichier .tmd

Le fichier .tmd utilise une syntaxe basée sur des balises de la forme balise{contenu.}
Chaque balise correspond à un élément Markdown.

#### Exemples


title{Mon document
## Introduction

**Texte important**
*Texte en italique*
- élément 1
- élément 2
- élément 3

Google | https://google.com
logo | https://example.com/logo.png
}

### Syntaxes disponibles


#### Titres

- title{...
 : Titre principal (h1) | # ...
 : Titre niveau 1 | ## ...
 : Titre niveau 2 | ### ...
 : Titre niveau 3 | #### ...
 : Titre niveau 4 | ##### ...
 : Titre niveau 5 | ###### ...
 : Titre niveau 6}

#### Texte

- bold{...
 ou **...** : Texte en gras | *...* ou *...* : Texte en italique | ~~...~~ : Texte barré}

#### Listes

- list{item1
- item2
- item3
 : Liste à puces | - item1
- item2
 : Variante de liste}

#### Liens et images

- link{texte
- url
 : Lien cliquable | alt | url : Image}

#### Code

- code{...
 : Code inline | ... : Bloc de code multi-lignes}

#### Autres

- quote{...
 : Citation | ------ : Ligne horizontale}

#### Tableaux

Les tableaux sont définis avec la balise table en utilisant thead et row.

table{
thead: Nom | Age | Pays;
row: John | 25 | USA;
row: Anna | 30 | France

}

### Installation

Clonez le projet depuis le dépôt GitHub.

git clone https://github.com/ItokianaIZ07/FileToMarkdown.git


### Utilisation

Exécutez le programme en passant un fichier .tmd en argument.

python main.py fichier.tmd


### Exemple de conversion

Entrée (.tmd)

title{Exemple
**Bonjour** *monde*
}

Sortie (.md)
```

# Exemple
**Bonjour** *monde*

```


### Objectif du projet

Ce projet est conçu comme un exercice pour apprendre la manipulation de fichiers, les expressions régulières et la conception de petits langages.

### Licence

Projet libre d'utilisation à des fins éducatives.