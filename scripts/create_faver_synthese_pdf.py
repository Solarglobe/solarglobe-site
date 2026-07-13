from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


OUT = "output/pdf/DOSSIER-SYNTHESE-FAVER-2026-07-06.pdf"

CLIENT = "Didier FAVER"
DATE = "6 juillet 2026"

DATA = [
    {
        "scenario": "7 kWc + 1 batterie",
        "role": "Recommandation principale",
        "panneaux": "14 - 28 m2",
        "production": "6 733 kWh",
        "rendement": "962 kWh/kWc",
        "couverture": "29 %",
        "eco1": "893 EUR",
        "tri": "8,2 %",
        "lcoe": "0,082 EUR/kWh",
        "amort": "12 ans",
        "invest": "13 900 EUR",
        "gain": "25 211 EUR",
        "evite": "39 111 EUR",
        "pv_place": "68 %",
        "ref": "SGS-2026-0138",
    },
    {
        "scenario": "7 kWc + 2 batteries",
        "role": "Plus de couverture en 7 kWc",
        "panneaux": "14 - 28 m2",
        "production": "6 733 kWh",
        "rendement": "962 kWh/kWc",
        "couverture": "32 %",
        "eco1": "999 EUR",
        "tri": "7,3 %",
        "lcoe": "0,101 EUR/kWh",
        "amort": "13 ans",
        "invest": "17 000 EUR",
        "gain": "26 067 EUR",
        "evite": "43 067 EUR",
        "pv_place": "76 %",
        "ref": "SGS-2026-0139",
    },
    {
        "scenario": "9 kWc + 1 batterie",
        "role": "Production superieure, bon compromis",
        "panneaux": "18 - 36 m2",
        "production": "8 804 kWh",
        "rendement": "978 kWh/kWc",
        "couverture": "32 %",
        "eco1": "996 EUR",
        "tri": "7,5 %",
        "lcoe": "0,076 EUR/kWh",
        "amort": "13 ans",
        "invest": "16 780 EUR",
        "gain": "27 097 EUR",
        "evite": "43 877 EUR",
        "pv_place": "58 %",
        "ref": "SGS-2026-0122",
    },
    {
        "scenario": "9 kWc + 2 batteries",
        "role": "Maximum production et gain net",
        "panneaux": "18 - 36 m2",
        "production": "8 804 kWh",
        "rendement": "978 kWh/kWc",
        "couverture": "36 %",
        "eco1": "1 126 EUR",
        "tri": "7,1 %",
        "lcoe": "0,088 EUR/kWh",
        "amort": "14 ans",
        "invest": "19 520 EUR",
        "gain": "29 143 EUR",
        "evite": "48 663 EUR",
        "pv_place": "66 %",
        "ref": "SGS-2026-0135",
    },
]


styles = getSampleStyleSheet()
styles.add(ParagraphStyle("Brand", fontName="Helvetica-Bold", fontSize=13, leading=16, tracking=4, textColor=colors.HexColor("#15221f")))
styles.add(ParagraphStyle("Kicker", fontName="Helvetica", fontSize=8.5, leading=11, textColor=colors.HexColor("#66736e")))
styles.add(ParagraphStyle("DocTitle", fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=colors.HexColor("#10211d"), spaceAfter=8))
styles.add(ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=17, leading=21, textColor=colors.HexColor("#10211d"), spaceAfter=8))
styles.add(ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=colors.HexColor("#10211d"), spaceBefore=7, spaceAfter=4))
styles.add(ParagraphStyle("Body", fontName="Helvetica", fontSize=9.3, leading=12.6, textColor=colors.HexColor("#26332f"), spaceAfter=5))
styles.add(ParagraphStyle("Small", fontName="Helvetica", fontSize=7.8, leading=10.2, textColor=colors.HexColor("#5c6965")))
styles.add(ParagraphStyle("Note", fontName="Helvetica-Oblique", fontSize=8, leading=10.5, textColor=colors.HexColor("#5c6965")))
styles.add(ParagraphStyle("MetricValue", fontName="Helvetica-Bold", fontSize=15, leading=17, alignment=TA_CENTER, textColor=colors.HexColor("#10211d")))
styles.add(ParagraphStyle("MetricLabel", fontName="Helvetica", fontSize=6.8, leading=8.5, alignment=TA_CENTER, textColor=colors.HexColor("#5c6965")))
styles.add(ParagraphStyle("Cell", fontName="Helvetica", fontSize=7.5, leading=9, textColor=colors.HexColor("#26332f")))
styles.add(ParagraphStyle("CellBold", fontName="Helvetica-Bold", fontSize=7.5, leading=9, textColor=colors.HexColor("#10211d")))
styles.add(ParagraphStyle("CenterCell", fontName="Helvetica", fontSize=7.4, leading=8.8, alignment=TA_CENTER, textColor=colors.HexColor("#26332f")))
styles.add(ParagraphStyle("CenterBold", fontName="Helvetica-Bold", fontSize=7.4, leading=8.8, alignment=TA_CENTER, textColor=colors.HexColor("#10211d")))
styles.add(ParagraphStyle("HeaderCell", fontName="Helvetica-Bold", fontSize=7.4, leading=8.8, alignment=TA_CENTER, textColor=colors.white))


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def euro_text(text):
    return text.replace("EUR", "€")


def on_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(colors.HexColor("#fbfaf6"))
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setStrokeColor(colors.HexColor("#d9ded8"))
    canvas.setLineWidth(0.6)
    canvas.line(18 * mm, h - 18 * mm, w - 18 * mm, h - 18 * mm)
    canvas.setFillColor(colors.HexColor("#10211d"))
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(18 * mm, h - 14 * mm, "S O L A R G L O B E")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#66736e"))
    canvas.drawRightString(w - 18 * mm, h - 14 * mm, f"Client : {CLIENT}")
    canvas.drawString(18 * mm, 12 * mm, "Document explicatif non contractuel - le devis detaille de la configuration retenue fera foi.")
    canvas.drawRightString(w - 18 * mm, 12 * mm, f"Page {doc.page} / 7")
    canvas.restoreState()


def metric_box(value, label):
    return Table(
        [[p(euro_text(value), "MetricValue")], [p(label, "MetricLabel")]],
        colWidths=[38 * mm],
        rowHeights=[10 * mm, 12 * mm],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#eef3ee")),
            ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#cfd8d0")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]),
    )


def card(title, body, accent="#1f6f58"):
    return Table(
        [[p(title, "H2")], [p(body, "Body")]],
        colWidths=[78 * mm],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#d9ded8")),
            ("LINEBEFORE", (0, 0), (0, -1), 3, colors.HexColor(accent)),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]),
    )


def table_style(header_rows=1, highlight_col=None):
    cmds = [
        ("BACKGROUND", (0, 0), (-1, header_rows - 1), colors.HexColor("#10211d")),
        ("TEXTCOLOR", (0, 0), (-1, header_rows - 1), colors.white),
        ("FONTNAME", (0, 0), (-1, header_rows - 1), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#d9ded8")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, header_rows), (-1, -1), [colors.white, colors.HexColor("#f4f6f2")]),
    ]
    if highlight_col is not None:
        cmds += [
            ("BACKGROUND", (highlight_col, header_rows), (highlight_col, -1), colors.HexColor("#e7f1ea")),
            ("BOX", (highlight_col, 0), (highlight_col, -1), 1.0, colors.HexColor("#1f6f58")),
        ]
    return TableStyle(cmds)


story = []

# Page 1
story += [
    p(f"Dossier de synthese - {DATE}", "Kicker"),
    p("Votre projet photovoltaïque", "DocTitle"),
    p("Quatre propositions etudiees - 7 kWc ou 9 kWc - une ou deux batteries physiques - raccordement monophasé 9 kVA", "Body"),
    Spacer(1, 7 * mm),
]
story.append(Table(
    [[
        metric_box("7 kWc + 1", "CHOIX LE PLUS PERTINENT"),
        metric_box("8,2 %", "MEILLEUR TRI"),
        metric_box("12 ans", "AMORTISSEMENT LE PLUS COURT"),
        metric_box("9 kWc + 2", "MAXIMUM GAIN ET COUVERTURE"),
    ]],
    colWidths=[40 * mm] * 4,
    style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]),
))
story += [
    Spacer(1, 10 * mm),
    p("À quoi sert ce dossier", "H1"),
    p("Vous avez reçu quatre études détaillées pour le même site : 7 kWc avec une batterie, 7 kWc avec deux batteries, 9 kWc avec une batterie et 9 kWc avec deux batteries. Elles reposent sur la même consommation annuelle, le même raccordement et une architecture technique comparable ; elles diffèrent par la puissance installée et la capacité de stockage physique.", "Body"),
    p("Ce document sert à lire les chiffres avec recul. Il ne remplace pas le devis, mais il explique quel scénario est le plus rationnel à recommander et quel scénario maximise la production, la couverture des besoins et le gain net.", "Body"),
    Spacer(1, 4 * mm),
    p("Lecture directe", "H1"),
]
story.append(Table(
    [[
        card("1 - Recommandation principale : 7 kWc + 1 batterie", "C'est le scénario le plus pertinent économiquement : investissement le plus bas, meilleur TRI, amortissement le plus court. Il fait travailler chaque euro au mieux."),
        card("2 - Option volume : 9 kWc + 2 batteries", "C'est le scénario qui produit le plus et qui génère le gain net le plus élevé. Il couvre davantage de besoins, mais demande plus de capital et s'amortit plus lentement.", "#b6852b"),
    ]],
    colWidths=[82 * mm, 82 * mm],
    style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]),
))
story += [
    Spacer(1, 6 * mm),
    p("Chiffres issus des études annexées : SGS-2026-0138, 0139, 0122 et 0135. Consommation de reference : 16 000 kWh/an.", "Note"),
    PageBreak(),
]

# Page 2
story += [
    p(f"Dossier de synthese - {DATE}", "Kicker"),
    p("Comment lire les quatre propositions", "H1"),
    p("Les indicateurs ne racontent pas tous la même chose. Certains mesurent l'efficacité économique de l'argent investi ; d'autres mesurent le volume d'énergie et d'économies générées.", "Body"),
]
defs = [
    ["Indicateur", "Ce qu'il mesure", "Ce qu'il faut chercher"],
    ["TRI", "Rentabilite annuelle de l'argent investi.", "Plus il est haut, mieux chaque euro travaille."],
    ["Amortissement", "Nombre d'annees necessaires pour rembourser le projet.", "Plus il est court, plus le retour est rapide."],
    ["Investissement TTC", "Capital engage au depart.", "Plus il est bas, plus le risque financier est contenu."],
    ["Besoins couverts", "Part de la consommation annuelle prise en charge par le solaire.", "Plus il est haut, plus la dependance au reseau baisse."],
    ["Gain net 25 ans", "Gain cumule apres remboursement de l'investissement.", "Plus il est haut, plus le projet rapporte en euros."],
    ["LCOE", "Cout moyen du kWh solaire produit.", "Plus il est bas, plus l'energie produite est competitive."],
]
story.append(Table([[p(c, "HeaderCell") for c in row] if i == 0 else [p(c, "Cell") for c in row] for i, row in enumerate(defs)], colWidths=[35 * mm, 74 * mm, 58 * mm], style=table_style()))
story += [
    Spacer(1, 8 * mm),
    p("Deux façons de gagner", "H1"),
    p("<b>Rentabilité pure</b> : on privilégie le TRI, l'amortissement et l'investissement de départ. Sur ce critère, le 7 kWc + 1 batterie est devant.", "Body"),
    p("<b>Volume et autonomie</b> : on privilégie la production, la couverture des besoins, les économies cumulées et le gain net. Sur ce critère, le 9 kWc + 2 batteries est devant.", "Body"),
    Spacer(1, 4 * mm),
    p("Socle commun des études", "H1"),
]
common = [
    ["Consommation annuelle", "16 000 kWh/an"],
    ["Raccordement", "9 kVA monophasé"],
    ["Architecture", "Panneaux photovoltaïques + micro-onduleurs ATMOCE MI-500"],
    ["Stockage", "Batterie physique : une ou deux unités selon le scénario"],
    ["Orientation", "Ouest / Sud-Ouest, environ 256-257°"],
]
story.append(Table([[p(a, "CellBold"), p(b, "Cell")] for a, b in common], colWidths=[52 * mm, 115 * mm], style=table_style(header_rows=0)))
story += [PageBreak()]

# Page 3
story += [
    p(f"Dossier de synthese - {DATE}", "Kicker"),
    p("Les quatre propositions, côte à côte", "H1"),
    p("Voici les mêmes indicateurs pour les quatre scénarios, à conditions comparables. La colonne verte correspond à la recommandation principale.", "Body"),
]
headers = ["Indicateur"] + [d["scenario"] for d in DATA]
rows = [
    ["Priorité"] + [d["role"] for d in DATA],
    ["Panneaux - surface"] + [d["panneaux"] for d in DATA],
    ["Production annuelle"] + [d["production"] for d in DATA],
    ["Rendement par kWc"] + [d["rendement"] for d in DATA],
    ["Besoins couverts"] + [d["couverture"] for d in DATA],
    ["Production PV utilisée"] + [d["pv_place"] for d in DATA],
    ["Économies année 1"] + [d["eco1"] for d in DATA],
    ["TRI"] + [d["tri"] for d in DATA],
    ["Coût kWh solaire"] + [d["lcoe"] for d in DATA],
    ["Amortissement"] + [d["amort"] for d in DATA],
    ["Investissement TTC"] + [d["invest"] for d in DATA],
    ["Dépenses évitées 25 ans"] + [d["evite"] for d in DATA],
    ["Gain net 25 ans"] + [d["gain"] for d in DATA],
]
table_data = [[p(c, "HeaderCell") for c in headers]]
for r in rows:
    table_data.append([p(euro_text(r[0]), "CellBold")] + [p(euro_text(c), "CenterCell") for c in r[1:]])
story.append(Table(table_data, colWidths=[34 * mm, 33 * mm, 33 * mm, 33 * mm, 33 * mm], repeatRows=1, style=table_style(highlight_col=1)))
story += [
    Spacer(1, 7 * mm),
    p("Lecture rapide", "H1"),
    p("Le 7 kWc + 1 batterie gagne sur les critères de rentabilité : TRI de 8,2 %, amortissement en 12 ans et investissement limité à 13 900 €. Le 9 kWc + 2 batteries gagne sur le volume : 36 % des besoins couverts, 8 804 kWh produits et 29 143 € de gain net sur 25 ans.", "Body"),
    PageBreak(),
]

# Page 4
story += [
    p(f"Dossier de synthese - {DATE}", "Kicker"),
    p("Pourquoi le 7 kWc + 1 batterie est le plus pertinent", "H1"),
    p("La recommandation ne doit pas seulement chercher le plus gros gain final. Elle doit aussi tenir compte du capital à engager, du temps de retour et de la rentabilité de chaque euro investi.", "Body"),
]
story.append(Table(
    [[
        card("Meilleur TRI", "8,2 %. C'est le niveau le plus haut des quatre scénarios, donc le meilleur rendement annuel de l'argent engagé."),
        card("Retour le plus court", "12 ans. Le projet revient plus vite à l'équilibre que les trois autres scénarios, qui s'amortissent en 13 ou 14 ans."),
    ],
     [
        card("Investissement le plus bas", "13 900 €. Le ticket d'entrée est inférieur de 2 880 € au 9 kWc + 1 batterie et de 5 620 € au 9 kWc + 2 batteries."),
        card("Choix facile à défendre", "29 % des besoins couverts et 25 211 € de gain net : le scénario reste solide sans surdimensionner le stockage ni le budget."),
     ]],
    colWidths=[82 * mm, 82 * mm],
    style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]),
))
story += [
    p("Comparaison utile : 7 kWc + 1 batterie contre 7 kWc + 2 batteries", "H1"),
    p("La deuxième batterie ajoute 3 points de couverture et 106 € d'économie la première année, mais elle augmente l'investissement de 3 100 €, allonge l'amortissement d'un an et fait baisser le TRI de 8,2 % à 7,3 %. Le gain net à 25 ans ne progresse que de 856 €. Pour une recommandation rationnelle, ce surcoût est donc difficile à privilégier en premier choix.", "Body"),
    p("Comparaison utile : 7 kWc + 1 batterie contre 9 kWc + 1 batterie", "H1"),
    p("Le 9 kWc + 1 batterie produit plus et affiche un gain net supérieur de 1 886 € sur 25 ans. Mais il demande 2 880 € de plus au départ, couvre seulement 3 points de besoins supplémentaires et s'amortit en 13 ans au lieu de 12. Il reste intéressant, mais moins prioritaire si le client cherche le meilleur équilibre financier.", "Body"),
    Spacer(1, 3 * mm),
    p("<b>Conclusion :</b> le 7 kWc + 1 batterie est le scénario à recommander en premier, car il combine rentabilité, prudence budgétaire et lisibilité commerciale.", "Body"),
    PageBreak(),
]

# Page 5
story += [
    p(f"Dossier de synthese - {DATE}", "Kicker"),
    p("Pourquoi le 9 kWc + 2 batteries arrive en deuxième choix", "H1"),
    p("Ce scénario n'est pas le meilleur en rentabilité pure, mais il est le plus fort en volume. Il s'adresse à un client qui accepte d'investir davantage pour produire plus, couvrir plus de consommation et obtenir le gain net le plus élevé.", "Body"),
]
volume_rows = [
    ["Critère", "9 kWc + 2 batteries", "Meilleur autre scénario", "Écart"],
    ["Production annuelle", "8 804 kWh", "6 733 kWh en 7 kWc", "+2 071 kWh"],
    ["Besoins couverts", "36 %", "32 %", "+4 points"],
    ["Économies année 1", "1 126 €", "999 €", "+127 €"],
    ["Dépenses évitées 25 ans", "48 663 €", "43 877 €", "+4 786 €"],
    ["Gain net 25 ans", "29 143 €", "27 097 €", "+2 046 €"],
]
story.append(Table([[p(euro_text(c), "HeaderCell") for c in row] if i == 0 else [p(euro_text(c), "CenterCell") for c in row] for i, row in enumerate(volume_rows)], colWidths=[42 * mm, 42 * mm, 43 * mm, 40 * mm], style=table_style()))
story += [
    Spacer(1, 8 * mm),
    p("Le bon positionnement commercial", "H1"),
    p("Il faut le présenter comme une option premium, pas comme le choix le plus rentable. Le message est simple : si la priorité est de maximiser l'autonomie et le gain net en euros, le 9 kWc + 2 batteries est le plus ambitieux. Si la priorité est le meilleur retour sur investissement, le 7 kWc + 1 batterie reste devant.", "Body"),
    p("Le point de vigilance", "H1"),
    p("Le scénario 9 kWc + 2 batteries exige 19 520 € TTC, soit 5 620 € de plus que la recommandation principale. Son amortissement passe à 14 ans et son TRI descend à 7,1 %. Il est donc excellent en production, mais moins efficace en rentabilité.", "Body"),
    PageBreak(),
]

# Page 6
story += [
    p(f"Dossier de synthese - {DATE}", "Kicker"),
    p("Comprendre la batterie physique", "H1"),
    p("Les quatre études reposent sur une batterie physique. Elle sert à stocker une partie du surplus solaire produit en journée pour le restituer plus tard, notamment le soir ou pendant les périodes où la maison consomme alors que les panneaux produisent peu ou pas.", "Body"),
    p("Le principe, en trois temps", "H1"),
    p("1. Les panneaux alimentent d'abord les usages du moment. 2. Le surplus disponible charge la batterie. 3. Quand la production baisse, la batterie restitue l'énergie stockée afin de réduire les achats sur le réseau.", "Body"),
    p("Pourquoi deux batteries ne sont pas automatiquement meilleures", "H1"),
    p("Une deuxième batterie augmente la capacité de stockage, mais elle n'est intéressante que si le surplus disponible et les usages différés permettent de l'exploiter suffisamment. Dans ce dossier, elle améliore bien la couverture, mais elle dégrade le TRI et allonge le retour sur investissement.", "Body"),
]
bat_rows = [
    ["Scénario", "Restitution batterie", "Pertes batterie", "Énergie autoconsommée"],
    ["7 kWc + 1 batterie", "1 260 kWh", "65 kWh", "4 574 kWh"],
    ["7 kWc + 2 batteries", "1 803 kWh", "93 kWh", "5 117 kWh"],
    ["9 kWc + 1 batterie", "1 411 kWh", "74 kWh", "5 103 kWh"],
    ["9 kWc + 2 batteries", "2 076 kWh", "107 kWh", "5 768 kWh"],
]
story.append(Table([[p(c, "HeaderCell") for c in row] if i == 0 else [p(c, "CenterCell") for c in row] for i, row in enumerate(bat_rows)], colWidths=[51 * mm, 39 * mm, 36 * mm, 41 * mm], style=table_style()))
story += [
    Spacer(1, 8 * mm),
    p("Point d'honnêteté", "H1"),
    p("La batterie physique apporte un confort réel d'autoconsommation, mais elle a un coût. Le meilleur projet n'est donc pas automatiquement celui qui stocke le plus : c'est celui dont le stockage supplémentaire est suffisamment valorisé par les économies générées.", "Body"),
    PageBreak(),
]

# Page 7
story += [
    p(f"Dossier de synthese - {DATE}", "Kicker"),
    p("Décision recommandée et étapes", "H1"),
    p("La décision peut être formulée très simplement au client : nous recommandons le 7 kWc + 1 batterie comme scénario principal, et nous gardons le 9 kWc + 2 batteries comme variante ambitieuse si l'objectif prioritaire est de maximiser la couverture des besoins et le gain net.", "Body"),
]
story.append(Table(
    [[
        card("Choix conseillé", "<b>7 kWc + 1 batterie</b><br/>Le plus pertinent : meilleur TRI, amortissement le plus court, investissement le plus bas et rentabilité la plus lisible."),
        card("Choix maximum", "<b>9 kWc + 2 batteries</b><br/>Le plus puissant : production maximale, couverture maximale et gain net le plus élevé sur 25 ans.", "#b6852b"),
    ]],
    colWidths=[82 * mm, 82 * mm],
    style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]),
))
story += [
    Spacer(1, 8 * mm),
    p("Formulation commerciale proposée", "H1"),
    p("\"Le scénario que nous recommandons est le 7 kWc avec une batterie : c'est celui qui offre le meilleur retour sur investissement et l'amortissement le plus rapide. Si votre priorité est plutôt de couvrir davantage de consommation et de maximiser le gain net à long terme, l'option 9 kWc avec deux batteries est la plus performante en volume.\"", "Body"),
    p("Les étapes de votre projet", "H1"),
    p("1. Validation de la puissance retenue et du devis. 2. Déclaration préalable en mairie. 3. Commande du matériel selon disponibilité. 4. Installation et raccordement. 5. Contrôle Consuel, mise en service et paramétrage du suivi de production.", "Body"),
    p("Hypothèses et réserves", "H1"),
    p("Montants TTC. Économies calculées sur le profil de consommation du site, prix de l'électricité indexé et production issue des études annexées. La facture résiduelle reste estimative et hors évolutions contractuelles futures. Le devis détaillé de la configuration retenue fera foi.", "Small"),
]


doc = BaseDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=24 * mm,
    bottomMargin=18 * mm,
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=on_page)])
doc.build(story)
print(OUT)
