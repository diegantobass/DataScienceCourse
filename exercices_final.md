
# Exercices

### Qui suis-je ?

__Le but de l'exercice est de récupérer des informations basiques sur l'utilisateur (nom, âge, origine géographique) en écrivant le programme qui permettra l'échange ci-dessous avec la machine__

~~~
- Bonjour, comment vous appelez-vous ?
- Camille
- Bonjour Camille, quel âge avez-vous ?
- 23 ans
- Vous êtes majeur.e. Dans quel département êtes-vous né.e ?
- Le Var
- Joli coin.
~~~

__Step by step :__
- Demander son prénom utilisateur avec la question apropriée, sans oublier de stocker le résultat dans une variable
- Utiliser cette variable pour demander sont âge à l'utilisateur en l'appelant par son prénom. Le stocker dans une variable
- La variable qui contient l'âge est une string. La transformer en un integer
- Construire un bloc de conditions pour proposer une réponse à l'utilisateur selon qu'il est majeur, mineur ou un bon blagueur (âge négatif !)
- Demander le département de naissance et le stocker

### Nos députés

__Le but est d'importer une liste de député.e.s récupérée sur data.gouv et d'en extraire quelques statistiques descriptives.__

__1) Importer un fichier__
- Récupérer la liste de députés [à cette adresse](https://www.data.gouv.fr/fr/datasets/listes-de-personnalites-issues-de-wikidata-1/)
- L'inclure dans votre espace repl.it
- Importer le paquet _csv_ et construire un _reader_

__2) Créer une fonction__
- Définir une fonction qui calcule l'âge d'une personne en se basant sur la date de naissance passée en paramètre

__3) Parcourir un fichier__
- Stocker les entêtes de colonne dans une variable à l'aide de la fonction _next()_
- Utiliser une boucle _for_ pour parcourir les lignes du fichier
- Calculer et stocker l'âge de chacun des député.e.s à l'aide de la fonction

__4) Reporting statistiques__
- Compter à l'aide de variables _compteur\__ déclarées avant la boucle _for_ les individus correspondants aux descriptions suivantes :
    - Hommes agés de plus de 50 ans
    - Femmes
    - Député.e.s de moins de 40 ans
    - Nombre de député.e.s ayant le même prenom que l'utilisateur de l'exercice 1
    - Député.e.s du département de naissance de l'utilisateur de l'exo 1
    - Député.e.s né.e.s dans des [villes de moins de 100k habitants](http://france.ousuisje.com/villes/classement/population-100000.php) 

### Scraper l'INSEE

__Un chercheur m'a demandé vendredi à 16h45 de scraper des données de [l'adresse suivante](https://www.insee.fr/fr/statistiques/2044109?sommaire=2131811&geo=DEP-01) parce que télécharger les données à la main était long et fastidieux...__

__Les paquets nécessaires sont _requests_ et _from bs4 import BeautifulSoup___

Pour chacun des départements français il existe une page similaire qui contient des informations sur ce département. En construire l'url en ajoutant la partie d'URL générique au numéro du département. Cette url doit être passée à la fonction _requests.get(url)_. Le contenu HTML de la page peut ensuite être parsé grace à BeautifulSoup, et il est possible de rechercher des morceaux de html dedans.

~~~python
import requests
from bs4 import BeautifulSoup

url_2009 = "https://www.insee.fr/fr/statistiques/2044109?sommaire=2131811&geo=DEP-"

for departement in range(1, 96):
  departement = str(departement).zfill(2)
  url_departement = url_2009 + departement
  response = requests.get(url_departement)
  soup = BeautifulSoup(response.content, "html.parser")
  table = soup('table', attrs={"id" : "produit-tableau-IMG1A_ENS"})
  print(table)
~~~

Attention tout de même : le site de l'INSEE a peut-être une protection anti robot-scraper... Lorsque vous lancez _requests.get()_ vous accédez aux serveurs qui hébergent le site.






