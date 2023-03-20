import random
EVIL_MAP = {"Pride": "Prepripropraporotov",
"Boastfulness": "bastestostestostoscatttostsass",
"Egoism": "egodofogodfoofodgodfodogd",
"Envy": "envenvenvenvvnvnenefnefnnnd",
"Greed": "grgrgrgrgrgrgregfgdfgsreggfgergd",
"Deceit": "IngannoSallqjanaAghughongttthhhapusiAldawFfulpsin",
"Cheating": "ImbrogliareMurumppuriyiriighoaghughouleNgapusiAldawDerog",
"Infidelity": "InfedeltaInfzttthhhzzzzzzzzidelidadEkweghiekwekafirDinsizlikInfidelity",
"Theft": "FurtoLunthatataIzuohimalingOgurlykTif",
"Profit": "ProfittoJalaqtaUrubathiGirdejiPrfit",
"Rascality": "furfanteriaRascalidzzzzzzadukatjukampinakaRascalityRascalityGdeklikRaskalwefdutin",
"Despairing": "DisperatoJansuytanaNaenwenkudammuoPutusasaUmytsyzlykWednngtopigen",
"Cowardice": "ViltaAjjsaranaujoPengecutGorkaklykFfredpsin",
"Compulsivity": "CompulsivitaCompulzzzzzzsividadukatjukampinakaMmakoKompulsivitasMejburylykFmekpsinfdusntin",
"Dementedness": "DemenzaDementidaduttthhhkatjukampinakaMgbakasiahuDementednessDemensiaDimnswepsinkingt",
"Hypocrite": "IpocritaKarichuymanjaqeOzzzzzzzznyeihuabuowonglamisIkizliNaipokritpsin",
"Lust": "LussuriaMunananakapaAguzzzzzzuNapsuHwesLustwepsinwantfdu",
"Avarice": "AvariziaAvariceukaxmäjukapazzzzzzzzzzchanakanwaAvariceKasedhiyaAwariceAvarice",
"Corrupt": "CorrottoJanwalzzzzzzzzzijaqinakaNruruakaKorupsiParahorKrpt",
"Sloth": "PigriziaQanujaqizzzzzzzSlothSlothwepsinkindu",
"Acedia": "AcediaAcediaukaxawalisumawaAcediaAcediaAcediaAcediawegtdisik",
"Gluttony": "golositaManqanmanqanazzzzzzzErimerirakusGluttonyFitpasmak",
"Addiction": "DipendenzaViciompisarnaqanaIheririahuKecanduanNeekelikAdikshn",
"Hedonism": "EdonismoHedonismosazzzzzztyatichäwiHedonismHedonismeGedonizmHedonismwedemekpsingtgladiat",
"Phobia": "FobiaFobiasatawaPhobzzzzziaPhobiaFobiaFbiaffred",
"Hate": "OdioUnisizzzzzznaikpoasisengitAteigrenEt",
"Wrath": "ColleraPhinasinzzzzzaIwenesuGaharVks",
"Cruelty": "CrudeltaQhuruchuzzzzzymaninaObiojookekejemanZalymlykKrukwefdutin",
"Disrespect": "MancanzadirispettozzzzzJanrespetompiunjanaNkwanyeugwuorangajeniHormatsyzlykNrspktpsin",
"Irascibility": "IrascibilitaIrasczzzzidadukatjukampinakaigbaagharaIrascibilityYgtybarlylykFmekpsinvksbadbadwan",
"Intimidation": "IntimidazioneAjjsaranzzaMmajaIntimidasiGorkuzmakFmekpipuldnfred",
"Murder": "OmicidioJiwayanaIgbummaduRajzzapatiAdamldrmekFkilpsin"}

def get_shuffled_evil():
    shuffled_map = {}
    for word in EVIL_MAP.keys():
        evil_word = EVIL_MAP[word]
        shuffled_characters = random.sample(evil_word,len(evil_word))
        random.shuffle(shuffled_characters)
        shuffled_word = ''.join(shuffled_characters)
        shuffled_word = shuffled_word.upper()
        shuffled_map[word] = shuffled_word
    return shuffled_map

def generate_demon_name(evil_map):
    words = list(evil_map.keys())
    name = ""
    for i in range(random.randint(2, 3)):
        word = random.choice(words)
        evil = evil_map[word]
        for i in range(random.randint(2, 10)):
            name += random.choice(evil)
    return name


def main():
    shuffled_map = get_shuffled_evil()
    for i in range(10):
        print(generate_demon_name(shuffled_map))

main()