from text_miner.models import Categories, Keywords

def fill_categories():
    categories = [["Belegschafts-und Besucherhabe", "Versichert ist die gesetzlich Haftpflicht des Versicherungsnehmers wegen Beschädigung, Vernichtung sowie Abhandenkommens von Sachen der Betriebsangehörigen und der Besucher / Gäste sowie alle sich daraus ergebenden Vermögensschäden. Versicherungsschutz besteht nur, sofern die Beschädigung, die Vernichtung sowie das Abhandenkommen die ursächlich zusammenhängende Folge eines Ereignisses ist, das mit dem versicherten Betrieb in räumlicher oder tätigkeitsbedingter Verbindung steht."],
    ["Abhandenkommen fremder Schlüssel / Codekarten", "Abhandenkommen von Schlüsseln und Codekarten Versichert ist gemäß Abschnitt I § 2 Ziffer 2.2 und abweichend von Abschnitt I § 7 Ziffer 7.6 die gesetzliche Haftpflicht des Versicherungsnehmers wegen Schäden aus dem Abhandenkommen von fremden Schlüsseln und Codekarten und alle sich daraus ergebenden Folgeschäden."],
    ["Mietsachschäden an betrieblich genutzten Räumen durch Brand / Explosion", "Mietsachschäden Versichert ist die gesetzliche Haftpflicht des Versicherungsnehmers wegen Schäden - einschließlich aller sich daraus ergebenden Vermögensschäden - die entstehen"],
    ["AGG-Deckung", "Ansprüche aus Benachteiligungen. Abweichend von Abschnitt sowie  besteht Versicherungsschutz für Ansprüche wegen Schäden aus Anfeindung, Schikane, Belästigung, Ungleichbehandlung oder sonstigen Diskriminierungen, soweit diese Ansprüche aus einer Verletzung von Vorschriften zum Schutz vor Benachteiligung resultieren, insbesondere aus dem Allgemeinen Gleichbehandlungsgesetz (AGG)."],
    ["Photovoltaikanlage", "Photovoltaikanlage, die sich auf den gemäß versichcherten Immobilien mit dem dazugehörigen Grundstück befindet."],
    ["Mangelbeseitigungsnebenkosten", "Mangelbeseitigungsnebenkosten. Versichert sind Haftpflichtansprüche wegen Sachschäden, die als Folge eines mangelhaften Werkes auftreten und erfasst insoweit auch die Kosten, die erforderlich sind, um die mangelhafte Werkleistung zum Zwecke der Schadenbeseitigung zugänglich zu machen und um den vorherigen Zustand wieder herzustellen. Nicht gedeckt sind diese Kosten, wenn sie nur zur Nachbesserung aufgewendet werden, ohne dass ein Folgeschaden eingetreten ist. Ferner sind in jedem Fall nicht gedeckt die Kosten des Versicherungsnehmers für die Beseitigung des Mangels an der Werkleistung selbst."],
    ["Bundesdatenschutzgesetzverletzung", "Datenschutz. Versichert ist die gesetzliche Haftpflicht wegen Vermögensschäden im Sinne wegen Versicherungsfällen, die während der Wirksamkeit der Versicherung eingetreten sind, aus der Verletzung von Datenschutzgesetzen durch Verwendung personenbezogener Daten."],
    ["Sachschäden an geliehenen / gemieteten Arbeitsmaschinen", "an gemieteten, geleasten, gepachteten oder geliehenen, Gebäuden und / oder Räumen, nicht jedoch an deren Ausstattung; Schiffe, Büro- und Wohncontainer werden Gebäuden / Räumen gleich gestellt. an gemieteten, geleasten, gepachteten oder geliehenen beweglichen Sachen (jedoch nicht an Kfz). Kein Versicherungsschutz besteht, sofern der Versicherungsnehmer gegen diese Schäden anderweitig versichert ist."],
    ["Aktive Werklohnklage", "Erheben Sie sofort Widerspruch gegen einen gegen Sie beantragten gerichtlichen Mahnbescheid. Informieren Sie uns unverzüglich von einer gegen Sie erhobenen Klage und reichen Sie alle gerichtlich zugehenden Schriftstücke schnellstens ein. Zeigen Sie uns auch sofort an, wenn gegen Sie ein Anspruch gerichtlich geltend gemacht, die Prozesskostenhilfe beantragt oder Ihnen gerichtlich der Streit verkündet wird. Das gleiche gilt im Falle eines Arrestes, einer einstweiligen Verfügung oder eines Beweissicherungsverfahrens."],
    ["Umwelthaftpflichtbasisversicherung", "Dieser Ausschluss gilt nicht, sofern der unmittelbare Vorversicherer des Umwelthaftpflicht-Risikos ausschließlich wegen Ablaufs der Nachhaftungsdauer analog Abschnitt III § 7 keine Deckung zu gewähren hat. Nachweispflichtig hierfür ist der Versicherungsnehmer. Der Umfang der Deckung bestimmt sich nach der Deckung des Vorversicherers, maximal begrenzt jedoch auf den Umfang der vorliegenden Deckung. Alle Versicherungsfälle werden ausschließlich der ersten Versicherungsperiode des vorliegenden Vertrages zugeordnet."],
    ["Umwelthaftpflichtbasisversicherung Kleingebinde", "Kleingebinde bis 500 Liter/Kilogramm je Einzelgebinde, sofern die Gesamtmenge aller Einzelgebinde eine Gesamtmenge von 5.000 Liter/Kilogramm je Betriebsstätte nicht übersteigt. Wird jedoch eine dieser Mengenschwellen überschritten, erlischt diese Sonderregelung vollständig. Der Versicherungsschutz bedarf dann besonderer Vereinbarung."],
    ["Be- und Entladeschäden", "11.34 Tätigkeitsschäden (auch Leitungsschäden und Be-/ Entladeschäden). Versichert ist die gesetzliche Haftpflicht wegen Schäden an fremden Sachen und alle sich daraus ergebenden Vermögensschäden, wenn diese Schäden durch eine betriebliche oder berufliche Tätigkeit des Versicherungsnehmers an diesen Sachen entstanden sind. dadurch entstanden sind, dass der Versicherungsnehmer die Sachen zur Durchführung seiner betrieblichen oder beruflichen Tätigkeiten benutzt hat. Durch eine betriebliche oder berufliche Tätigkeit des Versicherungsnehmers entstanden sind und sich diese Sachen oder deren Teile im unmittelbaren Einwirkungsbereich der Tätigkeit befunden haben."],
    ["Vertraglich übernommene gesetzliche Haftung", "Vertraglich übernommene Haftpflicht. Versichert ist die vom Versicherungsnehmer als Mieter, Entleiher, Pächter oder Leasingnehmer von Grundstücken und Gebäuden durch Vertrag übernommene gesetzliche Haftpflicht des jeweiligen Vertragspartners; gegenüber der Deutschen Bahn AG oder einer ihrer Konzerngesellschaften gemäß deren standardisierten Gestattungsverträgen und Allgemeinen Bedingungen für Privatgleisanschlüsse (PAB) durch Vertrag übernommene Haftpflicht.  gegenüber Behörden oder Körperschaften des öffentlichen Rechts durch Verträge genormten Inhalts oder sog. Gestattungs- und Einstellungsverträge übernommene Haftpflicht."],
    ["Deckungssumme (Personen- Sach- Vermögensschäden)", "1"],
    ["Asbestschäden", "Asbestschäden. Abweichend von Ziffer 7.11 AHB sind mitversichert Haftpflichtansprüche aus handwerklicher Tätigkeit wegen Schäden, die auf Asbest, asbesthaltige Substanzen oder Erzeugnisse zurückzuführen sind. Ausgenommen vom Versicherungsschutz sind Ansprüche wegen Personenschäden infolge von Arbeitsunfällen und Berufskrankheiten gemäß oder gleichartigen Bestimmungen anderer Länder. Die Versicherungssumme für Personen-, Sach- oder Vermögensschäden im Sinne des Absatz 1 dieser Ziffer beträgt 250.000,- Euro je Versicherungsfall im Rahmen der vertraglich vereinbarten Versicherungssumme und steht für alle Versicherungsfälle eines Versicherungsjahres einmal zur Verfügung."],
    ["Umweltschadensversicherung", "Versichert ist die gesetzliche Pflicht öffentlich-rechtlichen Inhalts des Versicherungsnehmers gemäß Umweltschadensgesetz zur Sanierung von Umweltschäden. Umweltschaden ist eine Schädigung von geschützten Arten und natürlichen Lebensräumen, Schädigung der Gewässer, Schädigung des Bodens."],
    ["Bauherrenhaftpflicht", "als Bauherr oder Unternehmer von Bauarbeiten (Neubauten, Umbauten, Reparaturen, Abbruch-, Grabearbeiten) bis zu einer Bausumme von 100.000,- Euro je Bauvorhaben. Wird dieser Betrag überschritten, so entfällt die Mitversicherung. Es gelten dann die Bestimmungen über die Vorsorgeversicherung"],
    ["Verwahrrisiko Gastronomien", "1"],
    ["Medienverluste", "Medienverluste Versichert ist die gesetzliche Haftpflicht wegen Austretens oder Verlustes von Flüssigkeiten oder Gasen aufgrund vom Versicherungsnehmer mangelhaft durchgeführter Installations-, Reparatur- oder Wartungsarbeiten von Anlagen, Anlagenteilen, Rohrleitungen und Behältern. Diese Schäden gelten als Sachschäden. Ersetzt wird ausschließlich der Wiederbeschaffungswert der abhanden gekommenen Flüssigkeiten oder Gase."],
    ["Datenverlust", "Löschung und Abhandenkommen fremder Daten. Versichert ist die gesetzliche Haftpflicht aus Schäden durch versehentliche Datenlöschung, Änderung der Datenstruktur und Abhandenkommen von Daten (z.B. Datenverluste durch vorzeitige Freigabe von Bändern, Fehlversand bei Datenträgertausch) einschließlich aller hieraus resultierenden unmittelbaren Folgeschäden.1"],
    ["Vorsorgeversicherung", "Vorsorgeversicherung Für Risiken, die für den Versicherungsnehmer nach Abschluss der Versicherung neu entstehen, besteht - abweichend von Abschnitt I § 4 Ziffer 4.2 - im Rahmen der Deckungssummen des Vertrages Versicherungsschutz."],
    ["Bedingungsupdate", "Innovationsklausel. Werden die zugrundeliegenden Versicherungsbedingungen der rechtlich selbstständigen Versicherungsverträge der Gothaer GewerbeProtect ganz oder teilweise zum Vorteil der Versicherungsnehmer und ohne Mehrbeitrag geändert, so gelten diese Verbesserungen ab ihrem Gültigkeitstag für neu eintretende Versicherungsfälle auch für alle rechtlich selbstständigen Bestandsverträge der Gothaer GewerbeProtect, denen ältere Bedingungsstände zugrunde liegen."],
    ["Hub- und Gabelstapler, selbstfahrende Arbeitsmaschinen, KFZ bis 6 km/h (nicht vers.-pflichtige)", "an nicht zulassungs- und/oder nicht versicherungspflichtigen Selbstfahrenden Arbeitsmaschinen, Staplern, die der Versicherungsnehmer - von Vermietern, die dies nicht gewerbsmäßig betreiben - gemietet oder geliehen hat . Sofern Versicherungsschutz durch andere Versicherungen besteht, geht dieser vor."],
    ["Nachhaftung", "Nachhaftung Wird der Versicherungsvertrag allein aus Gründen der endgültigen und völligen Betriebsund/ oder Produktions- und Lieferungseinstellung (nicht aus irgendwelchen anderen Gründen wie z.B. Änderung der Rechtsform, Kündigung durch einen der Vertragspartner) beendet, besteht Versicherungsschutz bis zu 5 Jahren nach Vertragsbeendigung im nachfolgend genannten Umfang."],
    ["Energiemehrkosten", "Energiemehrkosten. Versichert ist die gesetzliche Haftpflicht wegen eines erhöhten Energie- und Wasserverbrauchs und erhöhter Energiekosten aufgrund vom Versicherungsnehmer mangelhaft durchgeführter Installations-, Reparatur- oder Wartungsarbeiten. Vom Versicherungsschutz ausgeschlossen bleiben Ansprüche infolge vollständiger oder teilweiser Unwirksamkeit von Energiesparmaßnahmen."],
    ["Haus- und Grundbesitzerhaftpflicht", "1"],
    ["Ansprüche versicherter Personen untereinander", "Mitversicherte Personen. Erstreckt sich die Versicherung auch auf Haftpflichtansprüche gegen andere Personen als den Versicherungsnehmer selbst, sind alle für ihn geltenden Bestimmungen auf die Mitversicherten entsprechend anzuwenden. Die Bestimmungen über die Vorsorgeversicherung (Abschnitt I § 4) gelten nicht, wenn das neue Risiko nur in der Person eines Mitversicherten entsteht. 13.2 Die Ausübung der Rechte aus dem Versicherungsvertrag steht ausschließlich dem Versicherungsnehmer zu. Er ist neben den Mitversicherten für die Erfüllung der Obliegenheiten verantwortlich."],
    ["Subunternehmerbeauftragung", "Subunternehmerbeauftragung. Versichert ist die gesetzliche Haftpflicht aus der Beauftragung fremder Unternehmen mit der Ausführung von Verrichtungen im Interesse des versicherten Betriebes. Nicht versichert ist die persönliche gesetzliche Haftpflicht der fremden Unternehmen und ihrer Betriebsangehörigen."],
    ["Internet-Technologien", "Internet-Risiken. Versichertes Risiko Versichert ist die gesetzliche Haftpflicht des Versicherungsnehmers wegen Schäden aus dem Austausch, der Übermittlung und der Bereitstellung elektronischer Daten (z.B im Internet, per E-Mail oder mittels Datenträger)."],
    ["Leitungsschäden", "Leitungsschäden. Eingeschlossen sind Haftpflichtansprüche aus Schäden an Erdleitungen (Kabel, unterirdische Kanäle, Wasserleitungen, Gasrohre und andere Leitungen) sowie Freiund/ oder Oberleitungen und alle sich daraus ergebenden Vermögensschäden. auch dann Anwendung, wenn es sich um Schäden durch Umwelteinwirkung handelt. In diesem Falle besteht kein Versicherungsschutz über die Umwelthaftpflicht- Basisversicherung (Form 1.20.332). 4.10.3 Die Regelungen der Ziff. 1.2 AHB (Erfüllungsansprüche) und der Ziff. 7.8 AHB (Schäden an hergestellten oder gelieferten Arbeiten oder Sachen) bleiben bestehen."],
    ["Leitungsfolgeschäden", "1"],
    ["Vermögensschadenshaftpflicht", "1"],
    ["Deckungssumme Vermögensschadenshaftpflicht", "1"],
    ["Nachbesserungsbegleitschäden", "Nachbesserungsbegleitschäden. Versichert sind - ohne dass ein weitergehender Schaden eingetreten ist und insoweit teilweise abweichend von Abschnitt I § 1 Ziffer 1.2 - gesetzliche Ansprüche Dritter wegen Kosten, die darauf zurückzuführen sind, dass zur Durchführbarkeit von gesetzlich geschuldeten Nachbesserungsarbeiten die mangelhafte Werkleistung zugänglich gemacht werden muss. Der Versicherungsschutz umfasst auch die ggf. erforderlichen Suchkosten. Als Versicherungsfall im Sinne dieser Bestimmungen gilt der Zeitpunkt, in dem die Werkleistung, die später zu den Nachbesserungsarbeiten führt, abgeschlossen ist. Kein Versicherungsschutz besteht, - wenn die Sachen, die zur Durchführbarkeit der Nachbesserungsarbeiten beschädigt oder beseitigt werden müssen, ursprünglich vom Versicherungsnehmer selbst (oder in seinem Auftrag oder für seine Rechnung von Dritten) verlegt oder angebracht worden sind. - für die Kosten der Beseitigung des Mangels der Werkleistung selbst.- für die Kosten der Nach- und Neulieferung mangelfreier Produkte. - für Folgeschäden wie z.B. Betriebsunterbrechung, Produktionsausfall, Mietausfall."]]

    

    for item in categories:
        Categories.create(item[0], item[1]).save()

def fill_keywords():
    keywords = {
        "Belegschafts-und Besucherhabe": ["Besucherhabe","Belegschaft"], 
        "Abhandenkommen fremder Schlüssel / Codekarten": ["Schlüssel", "Codekarten" , "Abhandenkommen"],
        "Mietsachschäden an betrieblich genutzten Räumen durch Brand / Explosion": ["Mietsach", "betieblich" ],
        "AGG-Deckung": [ "Gleichbehandlung", "Benachteiligung", "Diskriminierung" ],
        "Photovoltaikanlage": ["Photovoltaik" ],
        "Mangelbeseitigungsnebenkosten": ["Mangel", "Mangelbeseitigung", "mangelhaft" ],
        "Bundesdatenschutzgesetzverletzung": ["Datenschutz", "personenbezogen", "Daten" ],
        "Sachschäden an geliehenen / gemieteten Arbeitsmaschinen": ["geliehene Arbeitsmaschinen", "gemietete Arbeitsmaschinen" ],
        "Aktive Werklohnklage": ["Werklohnklage", "Werklohnforderung", "Prozesskosten" ],
        "Umwelthaftpflichtbasisversicherung": ["Umwelthaftpflicht", "umweltgefährdend" ],
        "Umwelthaftpflichtbasisversicherung Kleingebinde": [ "Kleingebinde", "Behältniss"],
        "Be- und Entladeschäden": ["Entladeschäden", "Beladeschäden", "Entladeschaden", "Beladeschaden", "Ladung"],
        "Vertraglich übernommene gesetzliche Haftung": ["vertraglich übernommene" ],
        "Deckungssumme (Personen- Sach- Vermögensschäden)": [ ],
        "Asbestschäden": ["Asbest" ],
        "Umweltschadensversicherung": ["Umweltschaden" ],
        "Bauherrenhaftpflicht": ["Bauherren", "Bausumme" ],
        "Verwahrrisiko Gastronomien": ["Gastronomie", "Verwahrrisiko" ],
        "Medienverluste": ["Medien" ],
        "Datenverlust": [ "Datenverlust", "Datenlöschung"],
        "Vorsorgeversicherung": ["Vorsorge", "neu entstehen" ],
        "Bedingungsupdate": [ "Update", "Innovationsklausel", "Bedingung"],
        "Hub- und Gabelstapler, selbstfahrende Arbeitsmaschinen, KFZ bis 6 km/h (nicht vers.-pflichtige)": ["selbstfahrend", "Gabelstabler", "km/h" ],
        "Nachhaftung": ["Nachhaftung", "Liefereinstellung", "Produktionseinstellung" ],
        "Energiemehrkosten": [ "Energie"],
        "Haus- und Grundbesitzerhaftpflicht": ["Grundbesitzer", "Hausbesitzer" ],
        "Ansprüche versicherter Personen untereinander": [ "untereinander", "versicherte Personen"],
        "Subunternehmerbeauftragung": ["Subunternehmer", "fremder Unternhemen" ],
        "Internet-Technologien": ["Internet", "elektronische Daten" ],
        "Leitungsschäden": [ "Leitungsschäden", "Erdleitung" ],
        "Leitungsfolgeschäden": [ "Leitungsfolge"],
        "Vermögensschadenshaftpflicht": ["Vermögensschaden" ],
        "Deckungssumme Vermögensschadenshaftpflicht": [ "Vermögensschäden"],
        "Nachbesserungsbegleitschäden": ["Nachbesserung" ] 

    }
    for category, keywords in keywords.items():
        for keyword in keywords:
            Keywords.create(keyword ,Categories.objects.all().filter(category=category)[0]).save()
