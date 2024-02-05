import subprocess
import sys
from os import listdir
from os.path import isfile, join
import shutil
from difflib import SequenceMatcher # Pour la compilation d'un seul doc et permettre de taper n'importe quel bout éloigné du nom du fichier, la lib permet de calculer une distance entre mots 
import re

# Impérativement dans l'ordre
liste_lecons = [
	"Exemples de dénombrements dans différentes situations.",
	"Expérience aléatoire, probabilité, probabilité conditionnelle.",
	"Variables aléatoires discrètes.",
	"Variables aléatoires réelles à densité.",
	"Statistique à une ou deux variables, représentation et analyse de données.",
	"Multiples et diviseurs dans N, nombres premiers.",
	"PGCD dans Z.",
	"Congruences dans Z.",
	"Différentes écritures d'un nombre complexe.",
	"Utilisation des nombres complexes en géométrie.",
	"Trigonométrie.",
	"Repérage dans le plan, dans l'espace, sur une sphère.",
	"Droites et plans dans l'espace.",
	"Transformations du plan. Frises et pavages.",
	"Relations métriques et angulaires dans le triangle.",
	"Solides de l'espace : représentations et calculs de volumes.",
	"Périmètres, aires, volumes.",
	"Exemples de résolution de problèmes de géométrie plane à l'aide des vecteurs.",
	"Produit scalaire dans le plan.",
	"Applications de la notion de proportionnalité à la géométrie.",
	"Problèmes de constructions géométriques.",
	"Exemples de problèmes d'alignement, de parallélisme.",
	"Exemples de problèmes d'intersection en géométrie.",
	"Pourcentages et taux d'évolution.",
	"Problèmes conduisant à une modélisation par des équations ou des inéquations.",
	"Problèmes conduisant à une modélisation par des graphes, par des matrices.",
	"Fonctions polynômes du second degré. Équations et inéquations du second degré.",
	"Suites numériques. Limites.",
	"Suites définies par récurrence u_{n+1} = f(u_n).",
	"Détermination de limites de fonctions réelles de variable réelle.",
	"Théorème des valeurs intermédiaires.",
	"Nombre dérivé. Fonction dérivée.",
	"Fonctions exponentielles.",
	"Fonctions logarithmes.",
	"Fonctions convexes.",
	"Primitives, équations différentielles.",
	"Intégrales, primitives.",
	"Exemples de calculs d'intégrales (méthodes exactes, méthodes approchées).",
	"Exemples de résolution d'équations (méthodes exactes, méthodes approchées).",
	"Exemples de modèles d'évolution.",
	"Problèmes dont la résolution fait intervenir un algorithme.",
	"Différents types de raisonnement en mathématiques.",
	"Exemples d'approche historique de notions mathématiques enseignées au collège, au lycée.",
	"Applications des mathématiques à d'autres disciplines."
]

INDEXTEMPLATE = r"""
<div class='doctype'>
	<h2>Leçons</h2>
	<table>
		<thead>
			<th>N°</th>
			<th>État</th>
			<th class='leftaligned'>Intitulé</th>
			<th>Auteur·rice·s</th>
		</thead>
		<tbody>
			$leconshtml
		</tbody>
	</table>
</div>
<div class='doctype'>
	<h2>Développements</h2>
	<table style='margin-left: 15px'>
		<thead>
			<th>Intitulé</th>
			<th>Peut apparaître dans les N°</th>
		</thead>
		<tbody>
			$devshtml
		</tbody>
	</table>
</div>
"""

PLOTTEMPLATE = r"""
\documentclass{standalone}
\usepackage{../../../utilities}
\begin{document}
\begin{tikzpicture}
	\begin{axis}[
		grid = major,
		axis line style = very thick,
		grid style={line width=1pt, draw=gray!50},
		axis equal image,
		xmin=$XMIN,xmax=$XMAX,
		ymin=$YMIN,ymax=$YMAX,
		xtick = {$XMIN,...,$XMAX},
		ytick = {$YMIN,...,$YMAX},
		axis lines=middle,
		axis line style={-Latex},
		ticks=none]
			$PLOTDATA
	\end{axis}
\end{tikzpicture}
\end{document}
"""
PLOTCURVETEMPLATE = r"""
\addplot[
	domain=$XMIN:$XMAX,
	samples=200,
	color=blue,
	thick
	] {$EXPR};
"""








# Pre-processeur
def convert_md(f_name, file_path):
	print(f'\nConstruction du document {f_name}')
	markdown = None
	
	with open(file_path, encoding='utf-8') as f:
		markdown = f.read()
	
	# Remplacement automatique de certains débuts de lignes par des codes clefs.
	markdown = markdown.replace('\nDéfinition', '\n\\shortcutDefinition{}')
	markdown = markdown.replace('\nPropriétés', '\n\\shortcutProprietes{}')
	markdown = markdown.replace('\nPropriété',  '\n\\shortcutPropriete{}')
	markdown = markdown.replace('\nProposition', '\n\\shortcutProposition{}')
	markdown = markdown.replace('\nThéorème',   '\n\\shortcutTheoreme{}')
	markdown = markdown.replace('\nLemme',      '\n\\shortcutLemme{}')
	markdown = markdown.replace('\nCorollaire', '\n\\shortcutCorollaire{}')
	markdown = markdown.replace('\nMéthode',    '\n\\shortcutMethode{}')
	markdown = markdown.replace('\nExemples',   '\n\\shortcutExemples{}')
	markdown = markdown.replace('\nExemple',    '\n\\shortcutExemple{}')
	markdown = markdown.replace('\nApplications',    '\n\\shortcutApplications{}')
	markdown = markdown.replace('\nApplication',    '\n\\shortcutApplication{}')
	
	# Surcharge de l'implémentation du package markdown pour les citations.
	# La surcharge est écrite en Python par flemme, je trouve cela pour le
	# moment beaucoup plus simple et plus facile à éditer.
	
	comment_styles = [
						['🧩', 'puzzle-piece', 'shadeGreen'],
						['🚨', 'police-car-light', 'shadeRed'],
						['💶', 'euro-banknote', 'shadeBlue'],
					]
	
	print('Pré-processing du markdown.')
	
	# "Pre-processor"
	
	plotnum = 1
	
	lines = markdown.split('\n')
	for li in range(len(lines)):
		if len(lines[li]) > 2 and lines[li][0] == '|' and lines[li][2] == ' ':
			emoji = lines[li][1]
			for comment_style in comment_styles:
				if comment_style[0] == emoji:
					lines[li] = r'\begin{boitecitation}['+comment_style[2]+r']\tikz[overlay]{\node at (-0.7,0.1) {\emoji{'+comment_style[1]+'}}}' + lines[li][3:] + r'\end{boitecitation}'
		elif len(lines[li]) > 2 and lines[li][0:2] == '! ':
			lines[li] = r'\docpart{'+lines[li][2:]+'}'
		elif len(lines[li]) > 1 and lines[li][0] == '📈':
			plotparams = lines[li][1:].split(';')
			plot_expr = plotparams[0]
			plot_xmin = plotparams[1]
			plot_xmax = plotparams[2]
			plot_ymin = plotparams[3]
			plot_ymax = plotparams[4]
			
			# TODO : plusieurs courbes sur un même schéma.
			latex_curve_form = PLOTCURVETEMPLATE.replace('$EXPR', plot_expr).replace('$XMIN', plot_xmin).replace('$XMAX', plot_xmax)
			latex_plot_form = PLOTTEMPLATE.replace('$PLOTDATA', latex_curve_form).replace('$XMIN', plot_xmin).replace('$XMAX', plot_xmax).replace('$YMIN', plot_ymin).replace('$YMAX', plot_ymax)
			
			fname = f'plot{plotnum}.tex'
			plotnum += 1
			
			with open('plots/'+fname, 'w+', encoding='utf-8') as f:
				f.write(latex_plot_form)
			
			lines[li] = r'\begin{figure}[H] \center \includegraphics{plots/'+fname+r'} \end{figure}'
	
	markdown = '\n'.join(lines)
	
	with open('PROCESSED.md', 'w', encoding='utf-8') as f:
		f.write(markdown)
	
	print('Compilation du LaTeX.')
	
	# Compilation
	subprocess.run(['lualatex','--output-directory=./output/', '--interaction=batchmode', 'main.tex'])
	
	print('Déplacement du pdf.')
	# Déplacement du résultat vers le dossier hôte des pdfs
	shutil.move(f'./output/main.pdf', f'../lecons pdfs/{f_name}.pdf')




# Lister les documents à exporter
# Patch pour utilisateurs mac (avec le .DS_Store)
md_files = [f for f in listdir('../lecons brutes/') if isfile(join('../lecons brutes/', f)) and not ".DS" in f]

lecons_existantes = list()
developpements_existants = list()

# On les compile tous
for fname in md_files:
	
	if fname.startswith('lecon '):
		#no = ''.join(fname.split(' ')[1].split('.')[:-1]) # pas de test, peut poser pb ici si noms de fichiers pas parfaits - BUG POSSIBLE ICI
		no = re.search("lecon [0-9]+ de", fname)[0].split(' ')[1]
		#auteurrices = ' '.join(re.search("de [a-zA-Z ]+\\.md", fname)[0].split(' ')[1:]).split('.')[:-1]
		auteurrices = re.search("de [a-zA-Z ]+\\.md", fname)[0][3:-3]
		lecons_existantes.append((int(no),auteurrices,fname)) # pareil /\, bug possible ici
	elif fname.startswith('dev '):
		nom = ''.join(' '.join(fname.split(' ')[1:]) .split(' casage ')[0]) # pas de test, peut poser pb ici si noms de fichiers pas parfaits - BUG POSSIBLE ICI
		casages = ''.join(fname[fname.index(' ')+1:].split(' casage ')[1].split('.')[:-1])
		developpements_existants.append((nom, casages, fname))
	
	convert_md('.'.join(fname.split('.')[:-1]),join('../lecons brutes/', fname))

# Construction de l'index.html

print(f"\nConstruction de l'index")

html = ''
with open('./index template.html', encoding='utf-8') as f:
	html = f.read()

mod_table = INDEXTEMPLATE

# toucher à mod_table
lecons_rows = ''
devs_rows = ''

for n in range(len(liste_lecons)):
	lname = liste_lecons[n]
	# sale, très sale
	lecon_trouvee = None
	for leconex in lecons_existantes:
		if leconex[0] == n+1:
			lecon_trouvee = leconex
	lecons_rows += f"<tr> <td>{n+1}</td> <td>{"🟢" if lecon_trouvee != None else "🔴"}</td> <td class='leftaligned'>{ (f"<a href='./lecons pdfs/{'.'.join(lecon_trouvee[2].split('.')[:-1])}.pdf'>{lname}</a>") if lecon_trouvee != None else lname }</td> <td>{lecon_trouvee[1] if lecon_trouvee != None else ""}</td> </tr>"
mod_table = mod_table.replace('$leconshtml', lecons_rows)


for dev in developpements_existants:
	devs_rows += f"<tr> <td class='leftaligned'>{ (f"<a href='./lecons pdfs/{'.'.join(dev[2].split('.')[:-1])}.pdf'>{dev[0]}</a>")}</td> <td>{dev[1]}</td> </tr>"
mod_table = mod_table.replace('$devshtml', devs_rows)

html = html.replace('$content', mod_table)

with open('../index.html', 'w', encoding='utf-8') as f:
	f.write(html)


print(lecons_existantes)