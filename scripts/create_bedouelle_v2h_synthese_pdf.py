from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle


OUT = "output/pdf/DOSSIER-SYNTHESE-BEDOUELLE-12kWc-V2H-2026-07-06.pdf"
CLIENT = "Charles Bedouelle"
DATE = "6 juillet 2026"

GOLD = colors.HexColor("#c8943f")
DARK = colors.HexColor("#17191c")
TEXT = colors.HexColor("#222222")
MUTED = colors.HexColor("#555555")
PAPER = colors.white
SOFT = colors.HexColor("#fbf6ec")
GRID = colors.HexColor("#dfcda9")


styles = getSampleStyleSheet()
styles.add(ParagraphStyle("Brand", fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=GOLD, spaceAfter=0))
styles.add(ParagraphStyle("Meta", fontName="Helvetica", fontSize=8.5, leading=11, textColor=MUTED, alignment=TA_LEFT))
styles.add(ParagraphStyle("DocTitle", fontName="Helvetica-Bold", fontSize=21, leading=25, textColor=DARK, spaceAfter=2))
styles.add(ParagraphStyle("Subtitle", fontName="Helvetica", fontSize=12.5, leading=16, textColor=MUTED, spaceAfter=8))
styles.add(ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=15.5, leading=19, textColor=GOLD, spaceBefore=8, spaceAfter=7))
styles.add(ParagraphStyle("H1Dark", fontName="Helvetica-Bold", fontSize=15.5, leading=19, textColor=DARK, spaceBefore=8, spaceAfter=7))
styles.add(ParagraphStyle("Body", fontName="Helvetica", fontSize=9.7, leading=13.2, textColor=TEXT, spaceAfter=6))
styles.add(ParagraphStyle("BodyTight", fontName="Helvetica", fontSize=9.2, leading=12.2, textColor=TEXT, spaceAfter=4))
styles.add(ParagraphStyle("Small", fontName="Helvetica", fontSize=7.6, leading=9.6, textColor=MUTED))
styles.add(ParagraphStyle("Note", fontName="Helvetica-Oblique", fontSize=8, leading=10.5, textColor=MUTED))
styles.add(ParagraphStyle("Cell", fontName="Helvetica", fontSize=8.2, leading=10.2, textColor=TEXT))
styles.add(ParagraphStyle("CellSmall", fontName="Helvetica", fontSize=7.6, leading=9.3, textColor=TEXT))
styles.add(ParagraphStyle("CellBold", fontName="Helvetica-Bold", fontSize=8.2, leading=10.2, textColor=DARK))
styles.add(ParagraphStyle("Header", fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=DARK))
styles.add(ParagraphStyle("Center", fontName="Helvetica", fontSize=8.2, leading=10.2, alignment=TA_CENTER, textColor=TEXT))
styles.add(ParagraphStyle("CenterBold", fontName="Helvetica-Bold", fontSize=8.2, leading=10.2, alignment=TA_CENTER, textColor=DARK))
styles.add(ParagraphStyle("MetricValue", fontName="Helvetica-Bold", fontSize=16, leading=18, alignment=TA_CENTER, textColor=DARK))
styles.add(ParagraphStyle("MetricLabel", fontName="Helvetica", fontSize=7.5, leading=9, alignment=TA_CENTER, textColor=MUTED))


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def page_header(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 14)
    canvas.setFillColor(GOLD)
    canvas.drawString(18 * mm, h - 16 * mm, "S O L A R G L O B E")
    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(w - 18 * mm, h - 15 * mm, f"Client : {CLIENT}")
    canvas.drawRightString(w - 18 * mm, h - 20 * mm, f"Dossier de synthèse - {DATE}")
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1)
    canvas.line(18 * mm, h - 24 * mm, w - 18 * mm, h - 24 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(18 * mm, 13 * mm, "Document explicatif non contractuel - le devis détaillé de la configuration retenue fera foi.")
    canvas.drawRightString(w - 18 * mm, 13 * mm, f"Page {doc.page} / 7")
    canvas.restoreState()


def metric(value, label):
    return Table(
        [[p(value, "MetricValue")], [p(label, "MetricLabel")]],
        colWidths=[43 * mm],
        rowHeights=[12 * mm, 13 * mm],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), SOFT),
            ("BOX", (0, 0), (-1, -1), 0.8, GOLD),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]),
    )


def table_style(header=True, highlight_rows=None):
    cmds = [
        ("GRID", (0, 0), (-1, -1), 0.45, GRID),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    if header:
        cmds.append(("BACKGROUND", (0, 0), (-1, 0), SOFT))
        cmds.append(("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"))
    if highlight_rows:
        for r in highlight_rows:
            cmds.append(("BACKGROUND", (0, r), (-1, r), colors.HexColor("#fff3dd")))
            cmds.append(("FONTNAME", (0, r), (-1, r), "Helvetica-Bold"))
    return TableStyle(cmds)


def callout(text):
    return Table(
        [[p(text, "BodyTight")]],
        colWidths=[172 * mm],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), SOFT),
            ("BOX", (0, 0), (-1, -1), 0.8, GOLD),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]),
    )


story = []

# Page 1
story += [
    Spacer(1, 12 * mm),
    p("Votre projet photovoltaïque", "DocTitle"),
    p("12 kWc en pose lestée sur toiture plate · stockage V2H voiture + batterie virtuelle · investissement optimisé sans batterie physique dédiée", "Subtitle"),
    Spacer(1, 8 * mm),
]
story.append(Table(
    [[
        metric("12 kWc", "PUISSANCE INSTALLÉE - 24 panneaux"),
        metric("83 %", "DE VOS BESOINS COUVERTS"),
        metric("68 269 €", "GAIN NET ESTIMÉ SUR 25 ANS"),
        metric("10 ans", "AMORTISSEMENT - TRI 12,3 %"),
    ]],
    colWidths=[43 * mm] * 4,
    style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]),
))
story += [
    Spacer(1, 9 * mm),
    p("Notre recommandation", "H1"),
    p("La configuration <b>12 kWc avec voiture V2H + batterie virtuelle</b> devient l'option la plus pertinente de votre projet : elle conserve le bon dimensionnement solaire, valorise la grande capacité de stockage déjà présente dans le véhicule, évite l'achat d'une batterie physique dédiée et améliore fortement la rentabilité.", "Body"),
    p("Le résultat est très net : investissement plus bas, meilleur TRI, amortissement plus rapide et gain net supérieur. La batterie physique garde un intérêt pour un besoin de secours dédié, mais elle n'est plus le meilleur choix économique si le V2H est disponible dans les conditions prévues.", "Body"),
    p("Les quatre configurations étudiées", "H1"),
]
rows = [
    ["Configuration", "Tarif TTC", "Besoins\ncouverts", "Gain net\n25 ans", "TRI", "Positionnement"],
    ["9 kWc + 1 batterie", "19 060 €", "64 %", "46 565 €", "9,7 %", "Référence étudiée - écartée"],
    ["12 kWc + 1 batterie", "24 100 €", "86 %", "60 525 €", "9,8 %", "Ancienne recommandation"],
    ["12 kWc + 2 batteries", "27 800 €", "85 %", "59 105 €", "8,8 %", "Option résilience"],
    ["12 kWc + V2H + batterie virtuelle", "20 400 €", "83 %", "68 269 €", "12,3 %", "Nouvelle recommandation - meilleure rentabilité globale"],
]
story.append(Table([[p(c, "Header" if i == 0 else ("CellBold" if i == 4 else "CellSmall")) for c in row] for i, row in enumerate(rows)], colWidths=[39 * mm, 23 * mm, 22 * mm, 25 * mm, 18 * mm, 45 * mm], style=table_style(highlight_rows=[4])))
story += [
    Spacer(1, 2 * mm),
    p("Tarifs TTC, valables selon les conditions de l'offre correspondante.", "Small"),
    Spacer(1, 4 * mm),
    callout("<b>Comment se déroule la suite :</b> ce dossier compare maintenant les quatre configurations étudiées pour votre site. Dès que la configuration qui vous convient est arrêtée, le devis détaillé correspondant vous est adressé sous 24 heures."),
    Spacer(1, 5 * mm),
    p("Les fondations du chiffrage : votre courbe de consommation Enedis réelle (13 195 kWh/an), la géométrie réelle de votre toiture, une modélisation énergétique fondée sur le profil de consommation du site, et l'évolution du prix de l'électricité intégrée aux projections. Les coûts du dispositif V2H + batterie virtuelle sont intégrés dans l'étude dédiée.", "BodyTight"),
    PageBreak(),
]

# Page 2
story += [
    Spacer(1, 12 * mm),
    p("Pourquoi 12 kWc, et pas 9 ?", "H1Dark"),
    p("Le dimensionnement reste calé sur votre consommation réelle. La nouvelle étude ne remet pas en cause la puissance solaire : elle confirme que <b>12 kWc</b> reste le bon point d'arrêt. Ce qui change, c'est la manière de stocker et de valoriser l'énergie produite.", "Body"),
]
rows = [
    ["", "9 kWc + 1 batterie", "12 kWc + 1 batterie", "12 kWc + V2H"],
    ["Production annuelle", "8 636 kWh", "11 516 kWh", "11 516 kWh"],
    ["Part de vos besoins couverte", "64 %", "86 %", "83 %"],
    ["Économies la 1re année", "1 266 €", "1 576 €", "1 684 €"],
    ["Gain net sur 25 ans", "46 565 €", "60 525 €", "68 269 €"],
    ["Rentabilité (TRI)", "9,7 %", "9,8 %", "12,3 %"],
    ["Investissement TTC", "19 060 €", "24 100 €", "20 400 €"],
]
story.append(Table([[p(c, "Header" if i == 0 else ("CellBold" if j == 0 else "Center")) for j, c in enumerate(row)] for i, row in enumerate(rows)], colWidths=[50 * mm, 38 * mm, 42 * mm, 42 * mm], style=table_style(highlight_rows=[0])))
story += [
    Spacer(1, 7 * mm),
    p("La lecture est simple : le 12 kWc garde le plafond utile du site. Par rapport au 9 kWc, il produit 2 880 kWh de plus par an et va chercher une part beaucoup plus importante de vos besoins.", "Body"),
    p("La nouveauté, c'est que le V2H permet d'obtenir un meilleur résultat économique que la batterie physique : <b>3 700 € de moins que l'option 12 kWc + 1 batterie</b>, un gain net supérieur de <b>7 744 €</b>, et un amortissement ramené à <b>10 ans</b>.", "Body"),
    p("Ce plafond existe toujours : votre production solaire annuelle reste inférieure à votre consommation, et production et consommation ne coïncident jamais parfaitement. À 83 % de besoins couverts, le V2H s'approche du maximum utile tout en améliorant la rentabilité.", "Body"),
    p("Et votre toiture le permet : 24 panneaux en pose lestée occupent 48 m² de votre toiture-terrasse, sans perforation de l'étanchéité.", "Body"),
    PageBreak(),
]

# Page 3
story += [
    Spacer(1, 12 * mm),
    p("Pourquoi le V2H change l'équation économique", "H1Dark"),
    p("Dans l'ancienne lecture, le stockage reposait sur une batterie physique dédiée, complétée par une batterie virtuelle. La nouvelle étude utilise un actif déjà présent : la batterie du véhicule. Sa capacité est sans commune mesure avec une batterie résidentielle classique, tout en laissant la réserve mobilité prioritaire.", "Body"),
    p("Le point important est la lecture en cascade : les volumes ci-dessous ne s'additionnent pas deux fois. Les 10 912 kWh correspondent au total valorisé sur l'année : direct + V2H + batterie virtuelle.", "BodyTight"),
]
rows = [
    ["Étage", "Ce qu'il fait", "Énergie solaire valorisée / an"],
    ["1. Autoconsommation directe", "La production couvre la consommation du moment, en journée.", "4 486 kWh"],
    ["2. Voiture V2H", "Quand elle est branchée, la voiture restitue une partie de l'énergie à la maison.", "3 501 kWh"],
    ["3. Batterie virtuelle", "Le surplus restant est converti en crédit kWh et utilisé plus tard.", "2 925 kWh"],
    ["Total", "Énergie couverte sans achat réseau", "10 912 kWh"],
]
story.append(Table([[p(c, "Header" if i == 0 else ("CellBold" if i == 4 or j == 0 else "Cell")) for j, c in enumerate(row)] for i, row in enumerate(rows)], colWidths=[42 * mm, 91 * mm, 39 * mm], style=table_style(highlight_rows=[4])))
story += [
    Spacer(1, 7 * mm),
    p("Les paramètres qui font la différence", "H1"),
]
rows = [
    ["Capacité batterie véhicule", "85 kWh"],
    ["Réserve mobilité prioritaire", "30 % - environ 26 kWh"],
    ["Disponible maison théorique", "59 kWh"],
    ["Heures branchées retenues", "149 h/semaine"],
    ["Puissance de décharge", "5,0 kW"],
    ["Stockage valorisé par la cascade V2H + crédit", "6 426 kWh/an inclus dans les 10 912 kWh"],
]
story.append(Table([[p(a, "CellBold"), p(b, "Cell")] for a, b in rows], colWidths=[82 * mm, 90 * mm], style=table_style(header=False)))
story += [
    Spacer(1, 6 * mm),
    p("Facture résiduelle : les 2 283 kWh restant à acheter représentent environ 446 € d'énergie. La facture annuelle estimée à 892 € intègre aussi les coûts liés au stockage virtuel et à la restitution ; elle ne correspond donc pas au seul prix des kWh achetés au réseau.", "BodyTight"),
    p("La conclusion est logique : quand le véhicule est compatible et suffisamment présent à domicile, il devient plus pertinent d'utiliser cette grande capacité de stockage que d'acheter une batterie physique supplémentaire.", "Body"),
    PageBreak(),
]

# Page 4
story += [
    Spacer(1, 12 * mm),
    p("Votre décision : batterie physique ou V2H ?", "H1Dark"),
    p("Les options ne répondent plus exactement à la même philosophie. La batterie physique reste une solution dédiée à la résilience. Le V2H devient la meilleure solution économique, parce qu'il utilise une capacité de stockage déjà disponible.", "Body"),
]
rows = [
    ["", "12 kWc + 1 batterie", "12 kWc + 2 batteries", "12 kWc + V2H"],
    ["Investissement TTC", "24 100 €", "27 800 €", "20 400 €"],
    ["Stockage utile", "7 kWh - 3,5 kW", "14 kWh - 7 kW", "Voiture 85 kWh - réserve mobilité prioritaire"],
    ["Économies la 1re année", "1 576 €", "1 672 €", "1 684 €"],
    ["Gain net sur 25 ans", "60 525 €", "59 105 €", "68 269 €"],
    ["Rentabilité (TRI)", "9,8 %", "8,8 %", "12,3 %"],
    ["Coût de votre kWh solaire", "0,083 €/kWh", "0,096 €/kWh", "0,070 €/kWh"],
    ["Amortissement", "12 ans", "Non prioritaire économiquement", "10 ans"],
]
story.append(Table([[p(c, "Header" if i == 0 else ("CellBold" if j == 0 else "Center")) for j, c in enumerate(row)] for i, row in enumerate(rows)], colWidths=[45 * mm, 42 * mm, 42 * mm, 43 * mm], style=table_style(highlight_rows=[0])))
story += [
    Spacer(1, 7 * mm),
    p("Comment lire ce tableau", "H1"),
    p("La batterie physique ne disparaît pas parce qu'elle serait mauvaise : elle garde un rôle clair si la priorité absolue est d'avoir un stockage résidentiel dédié. Mais économiquement, la voiture V2H fait mieux : elle baisse l'investissement, améliore le TRI, raccourcit l'amortissement et augmente le gain net.", "Body"),
    p("<b>Notre recommandation devient donc le V2H.</b> La bonne question n'est plus « une batterie ou deux ? », mais « le véhicule peut-il jouer correctement son rôle de stockage domestique ? ». Si oui, c'est le meilleur choix.", "Body"),
    PageBreak(),
]

# Page 5
story += [
    Spacer(1, 12 * mm),
    p("Un choix plus intelligent : utiliser le stockage déjà disponible", "H1Dark"),
    p("La force du V2H, c'est de transformer la voiture en actif énergétique. Le client ne paie pas deux fois une batterie : la capacité embarquée du véhicule sert aussi à mieux valoriser la production solaire de la maison.", "Body"),
    p("Concrètement, cela change la nature du projet :", "Body"),
    p("• La puissance en toiture reste le vrai choix structurant : 12 kWc, 24 panneaux, 48 m².", "BodyTight"),
    p("• Le stockage quotidien est assuré par le véhicule quand il est branché et au-dessus de la réserve mobilité.", "BodyTight"),
    p("• La batterie virtuelle complète le V2H pour le surplus résiduel et le décalage dans le temps.", "BodyTight"),
    p("• La batterie physique devient une option de résilience dédiée, pas l'optimum économique.", "BodyTight"),
    Spacer(1, 4 * mm),
    callout("<b>En résumé :</b> choisir le V2H aujourd'hui ne diminue pas l'ambition solaire. Au contraire, il garde le 12 kWc, réduit l'investissement de départ et améliore la rentabilité globale du projet."),
    Spacer(1, 8 * mm),
    p("Le point d'honnêteté", "H1"),
    p("Les gains V2H dépendent fortement des heures de présence du véhicule à domicile. L'étude retient 149 heures branchées par semaine et une réserve mobilité prioritaire de 30 %. Si les usages de mobilité changent fortement, le bilan devra être réajusté.", "Body"),
    p("La recharge nécessaire aux trajets est suivie à part : elle ne gonfle pas artificiellement les économies de la maison. C'est un point important, car le bilan présenté mesure bien la performance énergétique du logement, pas un transfert caché depuis la voiture.", "Body"),
    PageBreak(),
]

# Page 6
story += [
    Spacer(1, 12 * mm),
    p("Les conditions de réussite du V2H", "H1Dark"),
    p("Le scénario V2H est le meilleur choix économique dans le cadre de cette étude. Pour qu'il reste cohérent en pratique, quatre conditions doivent être validées lors de la préparation technique.", "Body"),
]
rows = [
    ["Condition", "Pourquoi c'est important"],
    ["Compatibilité V2H du véhicule et de l'équipement", "Le véhicule, la borne et l'architecture électrique doivent permettre la restitution vers la maison."],
    ["Présence régulière à domicile", "Le V2H fonctionne quand la voiture est branchée. Les 149 h/semaine retenues expliquent une grande partie de la performance."],
    ["Réserve mobilité prioritaire", "La maison ne doit jamais prendre l'énergie nécessaire aux trajets. La réserve de 30 % reste séparée du bilan maison."],
    ["Paramétrage et validation technique", "Puissance de décharge, protection électrique, contrat de stockage et règles réseau doivent être confirmés avant pose."],
]
story.append(Table([[p(c, "Header" if i == 0 else ("CellBold" if j == 0 else "Cell")) for j, c in enumerate(row)] for i, row in enumerate(rows)], colWidths=[57 * mm, 115 * mm], style=table_style()))
story += [
    Spacer(1, 8 * mm),
    p("Et en cas de coupure ?", "H1"),
    p("La synthèse initiale détaillait le secours assuré par la batterie physique ATMOCE et le boîtier de bascule. Ce point reste une information utile pour les options avec batterie physique. Pour le scénario V2H, il ne faut pas promettre le même comportement sans validation dédiée : la capacité à alimenter la maison en coupure dépend du matériel V2H, du mode de bascule, de la réglementation anti-îlotage et des circuits retenus.", "Body"),
    p("La bonne formulation est donc prudente et professionnelle : <b>le V2H est retenu comme meilleur choix économique ; le niveau précis de secours en coupure sera validé techniquement selon le matériel et l'architecture finale.</b>", "Body"),
    PageBreak(),
]

# Page 7
story += [
    Spacer(1, 12 * mm),
    p("Votre toiture, l'installation électrique, les garanties", "H1Dark"),
    p("Pose sur toiture-terrasse", "H1"),
    p("Toiture support : plate, 0°. Modules photovoltaïques : orientation sud, inclinaison 10° sur structure lestée K2. Aucune perforation de l'étanchéité : le système tient par lestage. Le dimensionnement définitif du lestage est validé par l'outil de calcul du fabricant et confirmé lors de la préparation technique.", "Body"),
    p("Architecture électrique", "H1"),
    p("24 panneaux pilotés par 12 micro-onduleurs ATMOCE MI1000 (1 pour 2 panneaux), raccordés sur votre compteur 18 kVA triphasé à raison de 4 micro-onduleurs par phase, avec protections dédiées par branche. La répartition des branches, les sections de câble et le coffret de protection sont validés en préparation technique, conformément aux prescriptions du fabricant.", "Body"),
    p("Garanties", "H1"),
]
rows = [
    ["Équipement", "Garantie / information"],
    ["Panneaux photovoltaïques", "25 ans produit - 30 ans sur la production"],
    ["Micro-onduleurs ATMOCE MI1000", "25 ans avec extension de garantie incluse"],
    ["Batterie ATMOCE", "15 ans - information valable pour les options avec batterie physique"],
    ["Boîtier de secours ATMOCE MC 100", "Selon conditions fabricant - information valable si l'option secours dédié est retenue"],
    ["Équipement V2H / véhicule", "Selon matériel, compatibilité et garanties fabricant à valider dans l'offre finale"],
]
story.append(Table([[p(c, "Header" if i == 0 else ("CellBold" if j == 0 else "Cell")) for j, c in enumerate(row)] for i, row in enumerate(rows)], colWidths=[62 * mm, 110 * mm], style=table_style()))
story += [
    Spacer(1, 7 * mm),
    p("Les étapes de votre projet", "H1"),
    p("1. Choix de la configuration et validation du devis -> 2. Déclaration préalable en mairie -> 3. Validation technique V2H, stockage virtuel et architecture électrique -> 4. Commande du matériel -> 5. Installation -> 6. Contrôle Consuel, mise en service et activation des contrats.", "BodyTight"),
    p("Hypothèses et réserves", "H1"),
    p("Montants TTC ; économies calculées sur votre courbe de consommation réelle, prix de l'électricité indexé ; facture résiduelle estimée hors abonnement compteur ; primes, garanties, compatibilités V2H et conditions contractuelles sous réserve de validation à la mise en service. Le détail complet figure dans les études annexées.", "Small"),
]


doc = BaseDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=28 * mm,
    bottomMargin=18 * mm,
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=page_header)])
doc.build(story)
print(OUT)
