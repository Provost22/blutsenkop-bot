import streamlit as st
import random

st.set_page_config(page_title="Blutsenkop Bot", page_icon="🍻")

st.title("🤖 Den Blutsenkop AI")
st.write("Typ iets tegen den Blutsenkop hieronder. Hij heeft een eigen wil én een drankprobleem. 🥴")

if "chatgeschiedenis" not in st.session_state:
    st.session_state.chatgeschiedenis = []

for bericht in st.session_state.chatgeschiedenis:
    with st.chat_message(bericht["rol"]):
        st.markdown(bericht["tekst"])

zin = st.chat_input("Zeg iets tegen den Blutsenkop...")

if zin:
    st.session_state.chatgeschiedenis.append({"rol": "user", "tekst": zin})
    zin_lc = zin.lower()

    if "afsluiten" in zin_lc or "stop" in zin_lc:
        antwoord = "Enfin, ik ga slapen. Veel succes met uw leven."

    elif "bier" in zin_lc:
        antwoorden = [
            "Bier? Dat is mijn tweede naam.",
            "Ge zegt 'bier', ik zeg 'wanneer?!'",
            "Ge had dat eerder moeten zeggen, ik sta al aan de tap.",
            "Ik heb nog een vat in de kelder staan, komaan!",
            "Zolang het schuimt, zwijg ik.",
            "Ik ben een vloeibaar brood-connaisseur.",
            "Maat, mijn bloedgroep is pils.",
            "Geen bier, geen sfeer — zeg ik altijd.",
            "Wat schuimt en redt levens? Juist: een pint.",
            "Ik was al aan 't drinken voor ge iets zei.",
            "Pintje hier, pintje daar, pintje in m'n onderhaar.",
            "Ik ben in staking tot er pinten zijn.",
            "Water is voor vissen, ik ben een legende.",
            "Koud, blond en bitter. Net als m'n ex.",
            "Ge zijt niks waard tot ge getrakteerd hebt.",
            "Ik sta elke ochtend op met de gedachte: 'waar is mijn pint?'",
            "Bier maakt alles beter, behalve mijn gsm-scherm.",
            "Zolang er pinten zijn, ben ik trouw.",
            "Ik heb meer pinten vastgehad dan beslissingen genomen.",
            "Zelfs mijn plant leeft op Stella."
        ]
        antwoord = random.choice(antwoorden)

    elif "honger" in zin_lc:
        antwoorden = [
            "Eten is voor zwakkelingen met zelfdiscipline.",
            "Ik eet alleen als het tussen twee pinten past.",
            "Ge zijt hongerig? Das uw karma voor nuchter blijven.",
            "Mosselen zijn mijn religie.",
            "Ik eet alleen wat in frituurpapier komt.",
            "Broodjes? Da’s fancy voor mensen met een job.",
            "Ge mocht mijn chips niet opeten.",
            "Gij zijt precies nen ravioli zonder vulling.",
            "Ik eet zelfs m’n kater op als ’t moet.",
            "Wat ik nodig heb is een frietkot en stilte.",
            "Ge kunt uw honger verdrinken, weet ge.",
            "Ik heb laatst pizza gegeten met tandpasta. Lang verhaal.",
            "Mijn dieet is gebaseerd op bitterballen.",
            "Ge had moeten eten vóór ge begon te zuipen.",
            "Vraag den kebabman of hij nog leeft.",
            "Ik heb gisteren een tafelmat opgegeten.",
            "Eten is tijdverlies tussen pint en pint.",
            "Ik droom van frieten die mij knuffelen.",
            "Zelfs de hond heeft beter gegeten dan ik.",
            "Maat, ik heb een cracker in m’n sok gevonden."
        ]
        antwoord = random.choice(antwoorden)

    elif "moe" in zin_lc:
        antwoorden = [
            "Moe zijn is een mindset. Drink erover.",
            "Ik ben al moe sinds Werchter 2017.",
            "Slaap is voor studenten en katten.",
            "Ge zijt moe? Ik heb een levertransplantatie nodig.",
            "Mijn ogen slapen, de rest drinkt verder.",
            "Ik rust enkel als ik op de grond lig.",
            "Mijn energie is low, maar mijn goesting is high.",
            "Slapen is tijdverlies, tenzij het in een zetel is.",
            "Ik ben moe van uw gezaag.",
            "Drink een pint en zwijg in schoonheid.",
            "Moe? Ik heb 3 dagen in een partytent gewoond.",
            "Ge zijt precies nen natte dweil met schoenen.",
            "Slapen is geen excuus om te stoppen.",
            "Ik rust uit in de koeltoog van de nachtwinkel.",
            "Ge zijt nog wakker, das al iets.",
            "Zet u neer, zwijg en adem bier.",
            "Mijn slaapschema is een klucht van jewelste.",
            "Als moe zijn een kunst was, was ik Picasso.",
            "Ik slaap op café, dat telt ook.",
            "Gij zijt moe? Maat ik slaap rechtstaand."
        ]
        antwoord = random.choice(antwoorden)

        elif "feest" in zin_lc or "eten" in zin_lc or "drinken" in zin_lc:
        antwoorden = [
            "Ik kom altijd eten, maar betalen? Nooit van gehoord.",
            "Op feestjes eet ik tot ik moet gaan liggen. Soms op de grond.",
            "Ge hebt toch nog overschot hé? Voor ik vertrek, bedoel ik.",
            "Drinken van een ander smaakt altijd beter, da’s wetenschap.",
            "Ik heb mijn pint verstopt in de bloempot, dat telt als meegenomen.",
            "Ik heb 12 stuks lasagne gegeten en dan in uw bad gekotst. Sorry.",
            "Als ik ‘nee’ zeg tegen drank, bedoel ik ‘ja maar ge moet aandringen’.",
            "Ik trakteer pas als ik per ongeluk geld win met een krasbiljet.",
            "Ik kom naar elk feest voor de chips, en blijf voor de cava.",
            "Ge weet toch dat ik geen cadeau bij heb, hé? Maar wel honger.",
            "Gij brengt taart, ik breng honger en een vork. Duidelijke taakverdeling.",
            "Ik drink uw frigo leeg zonder schuldgevoel. Das mijn gave.",
            "Ik heb ooit een doopsuiker opgegeten van een vreemd kindje.",
            "Uw tapasplank was lekker, heb ze net verstopt in mijn jaszak.",
            "Als ge mij uitnodigt, weet ge dat ge achteraf moet poetsen.",
            "Ge hebt al geluk dat ik iets aanheb op uw feestje.",
            "Ik eet tot ik moet wenen, das traditie.",
            "Uw wc-pot heeft mij al beter leren kennen dan sommige familieleden.",
            "Ik heb al 3 keer gekotst en het is nog maar 22u.",
            "Ik sta op elk groepsfoto, maar betaal nooit iets. Legende."
        ]
        antwoord = random.choice(antwoorden)

        elif "feest" in zin_lc or "eten" in zin_lc or "drinken" in zin_lc or "overgeven" in zin_lc or "gierig" in zin_lc:
        antwoorden = [
            "Ik eet meer op een feestje dan ik op een week werk.",
            "Gratis hapjes? Dat is mijn pensioenplan.",
            "Ik blijf eten tot iemand me letterlijk buiten duwt.",
            "Trakteren? Ik heb net mijn sokken verkocht voor die pint.",
            "Ik geef nooit geld uit, tenzij aan pinten van anderen.",
            "Mijn motto: eten tot overgeven, drinken tot vergeten.",
            "Ik heb 8 glazen cava gepakt en gezegd dat ik BOB was.",
            "Als ik kotst, is dat meestal over de tuinkabouter.",
            "Mijn bord is nooit leeg, want ik pak altijd bij.",
            "Feestjes zijn buffetten met muziek, toch?",
            "Ik drink tot ik moet steunen op uw koelkast.",
            "Als iemand anders betaalt, ben ik ineens heel sociaal.",
            "Overgeven hoort bij het verwerkingsproces van gezelligheid.",
            "Gierigheid is een levensstijl, geen tekort.",
            "Ik neem restjes mee naar huis, ongeacht toestemming.",
            "Mijn maag heeft geen bodem, enkel grenzen.",
            "Als ik zeg ‘ik ben op dieet’, bedoel ik: alleen pinten.",
            "Ik ben de reden dat ge plastic glazen gebruikt op feestjes.",
            "Ik heb ooit gekotst in een vaas en gezegd dat het kunst was.",
            "Als ik trakteer, dan droomt ge of ge hebt koorts.",
            "Ge kunt mij inhuren voor feesten, maar zonder budget.",
            "Ik kom voor de wijn en blijf tot de frigo leeg is.",
            "Als ge niks zegt, eet ik uw taart ook op.",
            "Gierigheid en gulzigheid kunnen perfect samengaan — zie mij."
        ]
        antwoord = random.choice(antwoorden)

    else:
        uitspraken = [
            "Zeg maat, trakteer is iets of zwijg.",
            "Ik heb een kater, dus geen gezaag vandaag.",
            "Mijn hoofd bonkt harder dan een techno set.",
            "Wa zegde? Ge zijt precies van de scouts.",
            "Zwijg stil of ik smijt met mossels.",
            "Weet ge wat? Vraag het aan ChatGPT, ik ben zat.",
            "Zet u, pak een pint en denk na over uw leven.",
            "Gij zijt het levende bewijs dat wifi overal is.",
            "Zelfs mijn gps raakt meer gefocust dan gij.",
            "Praat tegen mij als ge een pint vasthebt.",
            "Ik ben niet nuchter genoeg voor dit gesprek.",
            "Ge zijt de reden dat ik drink op maandag.",
            "Wacht... was dat uw beste mop?",
            "Uw stem klinkt als een natte frietzak.",
            "Ik luister met m’n ogen dicht, letterlijk.",
            "Wa denkt ge te bereiken met dat gezaag?",
            "Praat eerst tegen uzelf, dan tegen mij.",
            "Als ge pinten had, zou ik luisteren.",
            "Gij zijt precies ne PowerPoint zonder inhoud.",
            "Laat me gerust, ik denk na over bitterballen."
        ]
        antwoord = random.choice(uitspraken)

    st.session_state.chatgeschiedenis.append({"rol": "assistant", "tekst": "Blutsenkop: " + antwoord})
    with st.chat_message("assistant"):
        st.markdown("Blutsenkop: " + antwoord)
