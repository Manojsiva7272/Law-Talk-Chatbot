import csv


def generate_variations(base_query, response_en, response_ta, article_num, usage_en, usage_ta):
    return [
        (base_query, response_en, article_num, usage_en, "English"),
        (base_query.replace("India", "இந்தியாவில்"), response_ta, article_num, usage_ta, "Tamil")
    ]


categories = {
    "Theft Law": [
        ("What is considered theft under Indian law?", 
         "Theft in India is defined as dishonestly taking any movable property out of the possession of another person without their consent.",
         "இந்திய சட்டத்தின் படி திருட்டு என்பது மற்றொரு நபரின் உடமையை அவர்களின் ஒப்புதலின்றி தூண்டுதலுடன் எடுத்தல் ஆகும்.",
         "Section 378, Indian Penal Code", 
         "Section 378 of the Indian Penal Code defines theft and provides the legal framework for prosecuting theft offenses.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 378 திருட்டை வரையறுக்கிறது மற்றும் திருட்டு குற்றங்களைப் பற்றி சட்டப்பூர்வமான கட்டமைப்பை வழங்குகிறது."
        ),
        ("What are the punishments for theft in India?", 
         "The punishment for theft in India is imprisonment for a term that may extend up to 3 years, or a fine, or both.",
         "இந்தியாவில் திருட்டிற்கான தண்டனை 3 ஆண்டுகள் வரை சிறைவாசம், அல்லது அபராதம் அல்லது இரண்டும் ஆகியவற்றைக் கொண்டுள்ளது.",
         "Section 379, Indian Penal Code", 
         "Section 379 of the Indian Penal Code specifies the punishment for theft, including imprisonment and fines.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 379, திருட்டிற்கு சிறைத்தண்டனை மற்றும் அபராதம் போன்ற தண்டனைகளை குறிப்படுகிறது."
        ),
        ("What is the difference between theft and robbery under Indian law?", 
         "Theft involves taking property without consent, while robbery involves the use of force or threat to commit the theft.",
         "திருட்டு என்பது உடமையை ஒப்புதலின்றி எடுத்தல், அந்நியமீடு என்பது அந்தத் திருட்டைச் செய்ய சக்தி அல்லது மிரட்டலின் பயன்பாட்டை உள்ளடக்கியது.",
         "Section 390, Indian Penal Code", 
         "Section 390 of the Indian Penal Code defines robbery and distinguishes it from theft by including the element of force or threat.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 390 அந்நியமீட்டை வரையறுக்கிறது மற்றும் அதில் சக்தி அல்லது மிரட்டலின் கூறுகளை உட்கொள்கிறது."
        ),
        ("What is the punishment for robbery in India?", 
         "The punishment for robbery in India is rigorous imprisonment which may extend up to 10 years and also includes fines.",
         "இந்தியாவில் அந்நியமீட்டிற்கான தண்டனை கடுமையான சிறைத்தண்டனையாகும், இது 10 ஆண்டுகள் வரை நீடிக்கலாம் மற்றும் அபராதங்களையும் உள்ளடக்கியது.",
         "Section 392, Indian Penal Code", 
         "Section 392 of the Indian Penal Code outlines the punishment for robbery, which may include imprisonment and fines.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 392, அந்நியமீட்டிற்கான தண்டனையை விவரிக்கிறது, இதில் சிறைத்தண்டனையும் அபராதங்களும் அடங்கும்."
        ),
        ("What is dacoity under Indian law?", 
         "Dacoity is when five or more persons commit or attempt to commit robbery, and it is a more serious offense than robbery.",
         "நான்கு அல்லது அதற்கு மேற்பட்ட நபர்கள் அந்நியமீடு செய்வதற்கு முயன்றால், அது அந்நியமாக்கம் ஆகும், மற்றும் இது அந்நியமீட்டைவிட அதிகமான குற்றமாகும்.",
         "Section 391, Indian Penal Code", 
         "Section 391 of the Indian Penal Code defines dacoity as an aggravated form of robbery involving five or more persons.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 391, அந்நியமீட்டையைச் சிறப்பிக்கிறது, இது 5 அல்லது அதற்கு மேற்பட்ட நபர்கள் பங்கேற்கும் அந்நியமீட்டு ஆகும்."
        ),
        ("What are the punishments for dacoity in India?", 
         "The punishment for dacoity in India is rigorous imprisonment for a term that may extend up to life imprisonment or ten years and also includes fines.",
         "இந்தியாவில் அந்நியமாக்கத்திற்கான தண்டனை கடுமையான சிறைத்தண்டனையாகும், இது ஆயுள் தண்டனை அல்லது 10 ஆண்டுகள் வரை நீடிக்கலாம் மற்றும் அபராதங்களையும் உள்ளடக்கியது.",
         "Section 395, Indian Penal Code", 
         "Section 395 of the Indian Penal Code prescribes punishment for dacoity, which can include life imprisonment or a term up to 10 years.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 395, அந்நியமாக்கத்திற்கான தண்டனையைத் திருத்துகிறது, இதில் ஆயுள் தண்டனை அல்லது 10 ஆண்டுகள் வரை சிறைத்தண்டனை அடங்கும்."
        )
    ],

    "Family Law": [
        ("What are the grounds for divorce in India?", 
         "The grounds for divorce in India include cruelty, desertion, conversion, adultery, mental disorder, and irretrievable breakdown of marriage.",
         "இந்தியாவில் விவாகரத்திற்கு அடிப்படைகள் கடுமையாக நடந்து கொள்வது, விலகல், மதம் மாற்றுதல், தனிவாழ்வு, மன நோய், மற்றும் விவாகரத்தைத் தவிர்க்க முடியாத உடன்படையாக இருக்கலாம்.",
         "Section 13, Hindu Marriage Act, 1955", 
         "Section 13 of the Hindu Marriage Act, 1955, lays down various grounds for divorce, including cruelty, desertion, and irretrievable breakdown of marriage.",
         "இந்திய திருமண சட்டம், 1955 இன் பிரிவு 13 விவாகரத்திற்கு பல்வேறு அடிப்படைகளை வழங்குகிறது, இதில் கொடூரம், விலகல் மற்றும் விவாகரத்தைத் தவிர்க்க முடியாத உடன்பாடு அடங்கும்."
        ),
        ("How can I file for child custody in India?", 
         "To file for child custody in India, you need to file a petition in the family court, and the court will decide based on the child's welfare.",
         "இந்தியாவில் குழந்தை காவலர் உரிமை பெற, நீங்கள் குடும்ப நீதிமன்றத்தில் ஒரு மனுவை தாக்கல் செய்ய வேண்டும், மற்றும் நீதிமன்றம் குழந்தையின் நலத்தை அடிப்படையாகக் கொண்டு முடிவு செய்யும்.",
         "Section 26, Hindu Marriage Act, 1955", 
         "Section 26 of the Hindu Marriage Act, 1955, provides for the custody, maintenance, and education of minor children.",
         "இந்திய திருமண சட்டம், 1955 இன் பிரிவு 26 சிறார்களின் காவல், பராமரிப்பு மற்றும் கல்வியைப் பற்றிய விதிகளைக் குறிப்பிடுகிறது."
        ),
        ("What is the concept of mutual consent divorce in India?", 
         "Mutual consent divorce in India allows both parties to agree to dissolve the marriage, provided they have lived separately for at least one year.",
         "இந்தியாவில் பரஸ்பர ஒப்புதலுடன் விவாகரத்து என்பது இருபுறமும் விவாகரத்தை ஒப்புக்கொள்வதை அறிகிறது, குறைந்தது ஒரு வருடத்திற்கு வெவ்வேறாக வாழ்ந்திருந்தால்.",
         "Section 13B, Hindu Marriage Act, 1955", 
         "Section 13B of the Hindu Marriage Act, 1955, permits divorce by mutual consent if the parties have lived separately for at least one year.",
         "இந்திய திருமண சட்டம், 1955 இன் பிரிவு 13B, குறைந்தது ஒரு வருடம் வெவ்வேறாக வாழ்ந்திருந்தால், பரஸ்பர ஒப்புதலுடன் விவாகரத்தை அனுமதிக்கிறது."
        ),
        ("What are the rights of a wife in a divorce case in India?", 
         "A wife has the right to maintenance, alimony, and her share in the marital property depending on the circumstances of the case.",
         "இந்தியாவில் விவாகரத்து வழக்கில் மனைவிக்கு பராமரிப்பு, கழிவுத் தொகை, மற்றும் திருமண சொத்தில் பங்குக்கான உரிமை உள்ளது.",
         "Section 25, Hindu Marriage Act, 1955", 
         "Section 25 of the Hindu Marriage Act, 1955, provides for permanent alimony and maintenance for either spouse, including the wife, based on the circumstances of the case.",
         "இந்திய திருமண சட்டம், 1955 இன் பிரிவு 25, வழக்கின் சூழ்நிலைகளின் அடிப்படையில், மனைவிக்கு நிரந்தர பராமரிப்பு மற்றும் வாழ்வாதாரத்திற்கான உரிமையை வழங்குகிறது."
        ),
        ("What is the procedure for adoption under Indian law?", 
         "In India, adoption can be done through the legal process under the Hindu Adoption and Maintenance Act, 1956, or the Juvenile Justice (Care and Protection of Children) Act, 2015.",
         "இந்தியாவில், தத்தெடுக்கும் செயல்முறை, 1956 இல் இந்திய தத்தெடுப்பு மற்றும் பராமரிப்பு சட்டம் அல்லது 2015 இன் குழந்தைகள் பராமரிப்பு மற்றும் பாதுகாப்பு சட்டத்தின் கீழ் சட்ட செயல்முறையை அடிப்படையாகக் கொண்டு செய்யலாம்.",
         "Hindu Adoption and Maintenance Act, 1956", 
         "The Hindu Adoption and Maintenance Act, 1956, governs the process of adoption for Hindus, covering eligibility, consent, and the legal effects of adoption.",
         "இந்திய தத்தெடுப்பு மற்றும் பராமரிப்பு சட்டம், 1956, இந்துக்களுக்கான தத்தெடுப்பின் செயல்முறையை நிர்ணயிக்கிறது, இதில் தகுதி, ஒப்புதல் மற்றும் தத்தெடுத்த பிறகு சட்ட விளைவுகள் அடங்கும்."
        ),
        ("What is the legal process for claiming maintenance for a wife?", 
         "A wife can claim maintenance by filing a petition in family court under Section 125 of the Criminal Procedure Code or under personal laws applicable to her religion.",
         "மனைவி, குடும்ப நீதிமன்றத்தில் மனுவை தாக்கல் செய்வதன் மூலம் பராமரிப்பைப் பெறலாம், இது 1973 இன் குற்றவியல் நடைமுறைச் சட்டம் அல்லது அவரின் மதத்திற்கு உட்பட்ட தனிப்பட்ட சட்டத்தின் கீழ் செய்யப்படலாம்.",
         "Section 125, Criminal Procedure Code, 1973", 
         "Section 125 of the Criminal Procedure Code, 1973, provides the legal provision for a wife to claim maintenance if her husband refuses to support her.",
         "1973 இன் குற்றவியல் நடைமுறைச் சட்டம், பிரிவு 125, மனைவிக்கு கணவர் தன்னை பராமரிக்க மறுத்தால் பராமரிப்பு கோருவதற்கான சட்டப்பிரிவை வழங்குகிறது."
        )
    ],
    "Criminal Law": [
        ("What are the legal rights of an arrested person in India?", 
         "An arrested person in India has the right to remain silent, the right to be informed of the grounds of arrest, and the right to consult a lawyer.",
         "இந்தியாவில் கைது செய்யப்பட்டவருக்கு மௌனமாக இருக்க உரிமை, கைது செய்யப்பட்ட காரணங்களைத் தெரிந்து கொள்ள உரிமை, மற்றும் ஒரு வக்கீலுடன் ஆலோசிக்க உரிமை உள்ளது.",
         "Article 22, Indian Constitution", 
         "Article 22 of the Indian Constitution provides protection against arbitrary arrest and detention in certain cases.",
         "இந்திய அரசியலமைப்பின் Article 22, தற்காலிக அல்லது ஏனைய கைது மற்றும் தடுப்பதற்கு எதிரான பாதுகாப்பை வழங்குகிறது."
        ),
        ("How can I file an FIR in India?", 
         "To file an FIR in India, you need to visit the nearest police station, provide details of the incident, and the police will register the complaint.",
         "இந்தியாவில் ஒரு FIR-ஐ தாக்கல் செய்ய, நீங்கள் அருகிலுள்ள போலீஸ் நிலையத்திற்கு சென்று, சம்பவத்தின் விவரங்களை வழங்க வேண்டும், மற்றும் போலீஸ் புகாரை பதிவு செய்யும்.",
         "Section 154, Criminal Procedure Code, 1973", 
         "Section 154 of the CrPC outlines the procedure for filing a First Information Report (FIR).",
         "CrPC இன் பிரிவு 154 FIR தாக்கல் செய்யும் முறையை வரையறுக்கிறது."
        ),
        ("What are the punishments for murder in India?", 
         "Murder is punishable by death or life imprisonment, depending on the severity of the case and the court's discretion.",
         "இந்தியாவில் கொலைக்கு மரண தண்டனை அல்லது ஆயுள் தண்டனை அளிக்கப்படலாம், இது வழக்கின் தீவிரம் மற்றும் நீதிமன்றத்தின் விவகாரத்தைப் பொறுத்தது.",
         "Section 302, Indian Penal Code", 
         "Section 302 of the Indian Penal Code prescribes death or life imprisonment as the punishment for murder.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 302, கொலைக்கான தண்டனையாக மரண தண்டனை அல்லது ஆயுள் தண்டனையை விவரிக்கிறது."
        ),
        ("What is the difference between murder and culpable homicide?", 
         "Murder is the intentional killing of a person with malicious intent, while culpable homicide involves the act of killing without premeditation.",
         "கொலை என்பது தீவிர நோக்கத்துடன் ஒருவரை எறிதலும், தவறான கொலை என்பது முன்முயற்சி இல்லாமல் செய்வது ஆகும்.",
         "Sections 299 & 300, Indian Penal Code", 
         "Sections 299 and 300 of the Indian Penal Code distinguish between culpable homicide and murder, focusing on intent and circumstances.",
         "இந்திய தண்டனைச் சட்டம், பிரிவுகள் 299 மற்றும் 300, கொலை மற்றும் தவறான கொலைக்கு இடையிலான வேறுபாட்டைப் பலன்கள் மற்றும் சூழ்நிலைகளை அடிப்படையாகக் கொண்டு விவரிக்கின்றன."
        ),
        ("What is the punishment for attempt to murder in India?", 
         "The punishment for an attempt to murder is imprisonment up to 10 years and may also include a fine. If harm is caused, the punishment may extend to life imprisonment.",
         "இந்தியாவில் கொலை முயற்சிக்கு 10 ஆண்டுகள் வரை சிறைத்தண்டனை விதிக்கப்படுகிறது மற்றும் அபராதமும் இருக்கலாம். சேதம் ஏற்பட்டால், தண்டனை ஆயுள் தண்டனை வரை நீடிக்கலாம்.",
         "Section 307, Indian Penal Code", 
         "Section 307 of the Indian Penal Code prescribes the punishment for an attempt to murder, including imprisonment up to life in case of injury.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 307, கொலை முயற்சிக்கான தண்டனையை குறிப்படுகிறது, இதில் சேதம் ஏற்பட்டால் ஆயுள் தண்டனை அடங்கும்."
        ),
        ("What constitutes criminal conspiracy under Indian law?", 
         "Criminal conspiracy occurs when two or more people agree to commit an illegal act, or an act by illegal means.",
         "குற்றசெயல் சதி என்பது இரண்டு அல்லது அதற்கு மேற்பட்ட நபர்கள் சட்டவிரோத செயலை செய்ய ஒப்புக்கொள்வதையே குறிக்கிறது.",
         "Section 120B, Indian Penal Code", 
         "Section 120B of the Indian Penal Code defines criminal conspiracy and prescribes punishment for such conspiracies.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 120B, குற்றசெயல் சதியை வரையறுக்கிறது மற்றும் அவற்றுக்கான தண்டனைகளை வழங்குகிறது."
        ),
        ("What is bail and how can it be obtained?", 
         "Bail is the temporary release of an accused person from custody, provided they meet certain legal conditions. It can be applied for in the magistrate's court.",
         "உத்தரவாதம் என்பது குற்றஞ்சாட்டப்பட்ட நபரை கஸ்டடியில் இருந்து தற்காலிகமாக விடுவிப்பது, சில சட்ட நிபந்தனைகளைப் பூர்த்தி செய்தால். இது மாஜிஸ்திரேட் நீதிமன்றத்தில் மனு மூலம் பெற முடியும்.",
         "Section 436-450, Criminal Procedure Code, 1973", 
         "Sections 436 to 450 of the Criminal Procedure Code, 1973, deal with the provisions related to bail and the conditions under which it can be granted.",
         "1973 இன் குற்றவியல் நடைமுறைச் சட்டம், பிரிவுகள் 436 முதல் 450 வரை, ஜாமீனுக்கான விதிகள் மற்றும் அதை வழங்குவதற்கான நிபந்தனைகளை வரையறுக்கின்றன."
        ),
        ("What is anticipatory bail?", 
         "Anticipatory bail is a legal provision that allows a person to seek bail in anticipation of arrest on accusation of having committed a non-bailable offense.",
         "முன்கூட்டிய ஜாமீன் என்பது குற்றச்சாட்டின் அடிப்படையில் கைது செய்யப்படுவதற்கு முன் குற்றஞ்சாட்டப்பட்ட நபர் ஜாமீனுக்கான மனுவை முன்கூட்டியே தாக்கல் செய்வதைக் குறிக்கிறது.",
         "Section 438, Criminal Procedure Code, 1973", 
         "Section 438 of the Criminal Procedure Code, 1973, provides for anticipatory bail, allowing individuals to seek bail before being arrested.",
         "1973 இன் குற்றவியல் நடைமுறைச் சட்டம், பிரிவு 438, முன்கூட்டிய ஜாமீனுக்கு அனுமதிக்கிறது, அதில் கைது செய்யப்படுவதற்கு முன் நபர் ஜாமீனை நாடலாம்."
        ),
        ("What is defamation under Indian law?", 
         "Defamation occurs when a person makes false statements about another person, harming their reputation. Defamation can be civil or criminal under Indian law.",
         "இழிவுபடுத்துதல் என்பது மற்றொரு நபரின் சிந்தனை அல்லது சாசனத்தைத் தவறான செய்திகளை பரப்புவதைக் குறிக்கிறது. இந்திய சட்டத்தில் இழிவுபடுத்துதல் சிவில் அல்லது குற்றவியல் குற்றமாக இருக்கும்.",
         "Section 499, Indian Penal Code", 
         "Section 499 of the Indian Penal Code defines defamation and Section 500 prescribes punishment for criminal defamation.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 499 இழிவுபடுத்துதலை வரையறுக்கிறது, மற்றும் பிரிவு 500 குற்றவியல் இழிவுபடுத்துதலுக்கான தண்டனையை நிர்ணயிக்கிறது."
        ),
        ("What are the provisions for dowry-related offenses?", 
         "Dowry-related offenses include demanding dowry and harassment for dowry. These are punishable under the Dowry Prohibition Act, 1961, and the IPC.",
         "நகைச்சுவை தொடர்பான குற்றங்கள் நகைச்சுவை கேட்பதும், நகைச்சுவைக்கு துன்புறுத்துவதும் அடங்கும். 1961 இல் கொண்டுவரப்பட்ட நகைச்சுவை தடைச் சட்டம் மற்றும் இந்திய தண்டனைச் சட்டத்தின் கீழ் தண்டிக்கப்படும்.",
         "Section 498A, Indian Penal Code & Dowry Prohibition Act, 1961", 
         "Section 498A of the Indian Penal Code and the Dowry Prohibition Act, 1961, provide the legal framework for addressing dowry harassment and related offenses.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 498A மற்றும் நகைச்சுவைத் தடைச் சட்டம், 1961, நகைச்சுவை தொடர்பான குற்றங்களை நிவர்த்தி செய்யும் சட்டப்பிரிவுகளை வழங்குகின்றன."
        )
    ],
    "Property Law": [
        ("What is the legal process for transferring property ownership in India?", 
         "The transfer of property ownership in India requires a sale deed, which must be registered with the Sub-Registrar's office. The deed is signed by both parties and involves stamp duty payment.",
         "இந்தியாவில் சொத்து உரிமை மாற்றம் செய்ய, விற்பனை ஒப்பந்தம் தேவைப்படுகிறது, இது துணை பதிவாளரின் அலுவலகத்தில் பதிவு செய்யப்பட வேண்டும். ஒப்பந்தத்தை இருபுறமும் கையொப்பமிட வேண்டும் மற்றும் முத்திரை கட்டணம் செலுத்தப்பட வேண்டும்.",
         "Section 54, Transfer of Property Act, 1882", 
         "Section 54 of the Transfer of Property Act, 1882, outlines the process of sale and transfer of immovable property, including registration and payment of stamp duty.",
         "இந்திய சொத்து பரிமாற்ற சட்டம், 1882 இன் பிரிவு 54, நிலையான சொத்து விற்பனை மற்றும் பரிமாற்றத்தின் செயல்முறையை, பதிவு மற்றும் முத்திரை கட்டணம் அடங்கிய வழிமுறைகளை விவரிக்கிறது."
        ),
        ("What is the difference between lease and license in property law?", 
         "A lease grants the tenant exclusive possession of the property for a specific period, while a license grants a temporary, non-exclusive right to use the property.",
         "ஒரு குத்தகை சொத்து உரிமையாளருக்கு குறிப்பிட்ட காலத்திற்காக சொத்து உபயோக உரிமையை அளிக்கிறது, ஆனால் உரிமம் சொத்து அடையாளமாக பயன்படுத்தப்படுவதற்கான தற்காலிக, நிர்பந்தமற்ற உரிமையை அளிக்கிறது.",
         "Section 105, Transfer of Property Act, 1882", 
         "Section 105 of the Transfer of Property Act, 1882, defines the terms of lease agreements, including the rights of tenants and landlords.",
         "இந்திய சொத்து பரிமாற்ற சட்டம், 1882 இன் பிரிவு 105 குத்தகை ஒப்பந்தங்களின் விதிகளை வரையறுக்கிறது, இதில் குத்தகையாளர்கள் மற்றும் சொந்தக்காரர்களின் உரிமைகள் அடங்கும்."
        ),
        ("What is adverse possession under Indian property law?", 
         "Adverse possession refers to a situation where someone who is not the original owner of a property gains legal ownership through continuous, open, and hostile possession for a prescribed period.",
         "சொத்து உரிமையாளராக இல்லாத நபர், குறிப்பிட்ட காலத்திற்கு சொத்து நிரந்தரமாக, வெளிப்படையாக, மற்றும் விரோதமாக வைத்திருப்பதன் மூலம் உரிமையைப் பெறுவதை மாறிய சொத்து உரிமை என்று குறிப்பிடுகிறார்கள்.",
         "Article 65, Limitation Act, 1963", 
         "Article 65 of the Limitation Act, 1963, sets the limitation period for claiming ownership through adverse possession to 12 years for private property and 30 years for government property.",
         "வரம்பு சட்டம், 1963 இன் பிரிவு 65, தனியார் சொத்துக்களுக்கு 12 ஆண்டுகள் மற்றும் அரசு சொத்துக்களுக்கு 30 ஆண்டுகளாக மாறிய சொத்து உரிமைக்கான கால வரம்பை நிர்ணயிக்கிறது."
        ),
        ("What are the rules for partition of property among family members?", 
         "Partition of property among family members can be done through mutual consent or by filing a suit for partition in court, where the court divides the property based on the legal shares of the heirs.",
         "குடும்ப உறுப்பினர்களுக்கு இடையில் சொத்து பிரிப்பு பரஸ்பர ஒப்புதல் மூலம் அல்லது நீதிமன்றத்தில் பிரிப்பு வழக்கு தாக்கல் செய்வதன் மூலம் செய்யப்படலாம், இதில் நீதிமன்றம் வாரிசுகளின் சட்ட பங்குகளின் அடிப்படையில் சொத்தைப் பிரிக்கும்.",
         "Section 4, Partition Act, 1893", 
         "Section 4 of the Partition Act, 1893, provides for the division of jointly owned property and outlines the rights of co-owners during partition.",
         "பிரிப்பு சட்டம், 1893 இன் பிரிவு 4, கூட்டாக சொத்து வைத்திருப்பவர்களின் சொத்து பிரிப்பு மற்றும் கூட்டுரிமையாளர்களின் உரிமைகளை விவரிக்கிறது."
        ),
        ("What is the procedure for inheriting property in India?", 
         "Property inheritance in India is governed by personal laws depending on the religion of the deceased. A legal heir must apply for a succession certificate or probate to transfer ownership.",
         "இந்தியாவில் சொத்து வாரிசு இறந்தவரின் மதத்தைப் பொறுத்து தனிப்பட்ட சட்டங்களால் நிர்ணயிக்கப்படுகிறது. சட்ட வாரிசு உரிமை பெற, ஒரு வாரிசு சான்றிதழ் அல்லது ப்ரொபேட் பெற வேண்டும்.",
         "Hindu Succession Act, 1956", 
         "The Hindu Succession Act, 1956, governs the inheritance of property among Hindus, providing for both male and female heirs to inherit ancestral and self-acquired property.",
         "இந்திய வாரிசுரிமை சட்டம், 1956, இந்துக்கள் இடையிலான சொத்து வாரிசுரிமையை நிர்ணயிக்கிறது, இதில் ஆண் மற்றும் பெண் வாரிசுகள் பாரம்பரிய மற்றும் சுயமாகக் கொள்வனவு செய்யப்பட்ட சொத்துக்களைப் பெறுவதற்கான விதிகளைக் குறிப்பிடுகிறது."
        ),
        ("What is the rule of survivorship in joint property ownership?", 
         "In joint property ownership, the rule of survivorship dictates that when one co-owner dies, their share automatically passes to the surviving co-owner(s).",
         "கூட்டு சொத்து உரிமையில், உயிர்தப்பிக்கக்கூடியவரின் விதி ஒரு கூட்டுரிமையாளர் இறந்தால், அவரது பங்கு மற்ற உயிர்ப்பிக்கக்கூடிய கூட்டுரிமையாளருக்கு தானாகவே செல்கிறது.",
         "Hindu Succession Act, 1956", 
         "The Hindu Succession Act, 1956, abolished the rule of survivorship for joint family property and replaced it with the rule of inheritance for both male and female heirs.",
         "இந்திய வாரிசுரிமை சட்டம், 1956, கூட்டுக்குடும்ப சொத்துக்கான உயிர்தப்பிக்கக்கூடியவரின் விதியை நீக்கி, ஆண் மற்றும் பெண் வாரிசுகளுக்கு வாரிசுரிமை விதியை அறிமுகப்படுத்தியது."
        ),
        ("What is the process for challenging property encroachment?", 
         "To challenge property encroachment, the property owner can file a suit in the civil court for eviction and seek a permanent injunction against the trespasser.",
         "சொத்து கவர்ச்சி குற்றச்சாட்டை எதிர்த்து, சொத்து உரிமையாளர் குடியிருப்பாளரை அகற்ற சிவில் நீதிமன்றத்தில் வழக்கு தொடர முடியும் மற்றும் முறையற்றவருக்கு எதிராக நிரந்தர தடையைத் தேடலாம்.",
         "Section 5, Specific Relief Act, 1963", 
         "Section 5 of the Specific Relief Act, 1963, provides for the recovery of possession of immovable property from someone who has encroached or trespassed on it.",
         "விதி நிவாரணச் சட்டம், 1963 இன் பிரிவு 5, ஒருவர் மாறியிருக்கும் நிலையான சொத்து அல்லது முறையற்ற உபயோகத்தை மீட்குவதற்கான உரிமையை வழங்குகிறது."
        ),
        ("What is the meaning of easement rights in property law?", 
         "Easement rights refer to the legal right to use another's property for a specific purpose, such as access to a road or water source.",
         "சொத்து உரிமையில் குறுக்கு உரிமைகள் என்பது பிறர் சொத்தை ஒரு குறிப்பிட்ட நோக்கத்திற்காக (எ.கா. ரோடு அல்லது நீர்க்கரை பயன்பாடு) பயன்படுத்துவதற்கான சட்ட உரிமையை குறிப்பிடுகிறது.",
         "Easements Act, 1882", 
         "The Easements Act, 1882, governs the rights and obligations of property owners regarding easements, including the right of way, air, light, and water.",
         "குறுக்கு உரிமைகள் சட்டம், 1882, குறுக்கு உரிமைகளுக்கான உரிமைகள் மற்றும் கடமைகளை, அதில் வழி, காற்று, ஒளி, மற்றும் நீர் அடங்கிய விதிகளை நிர்ணயிக்கிறது."
        ),
        ("What is the role of a mutation in property transactions?", 
         "Mutation refers to the process of updating the revenue records to reflect the change in ownership after the sale, inheritance, or transfer of property.",
         "சொத்து பரிவர்த்தனைகளில் மியூடேஷன் என்பது விற்பனை, வாரிசுரிமை அல்லது சொத்து மாற்றத்தின் பிறகு சொத்து உரிமையைப் பதிவு செய்யும் செயல்முறையைக் குறிக்கிறது.",
         "Section 128, Land Revenue Act", 
         "Section 128 of the Land Revenue Act provides the legal procedure for mutation in the case of property ownership change due to sale, inheritance, or gift.",
         "நில வரி சட்டம், பிரிவு 128, விற்பனை, வாரிசுரிமை அல்லது பரிசு காரணமாக சொத்து உரிமை மாற்றத்தின் போது மியூடேஷன் செய்யும் சட்ட செயல்முறையை வழங்குகிறது."
        ),
        ("What are the legal requirements for a gift deed in property transfer?", 
         "A gift deed is a legal document used to voluntarily transfer ownership of property without consideration. It must be signed and registered with the Sub-Registrar's office to be legally valid.",
         "சொத்து பரிமாற்றத்தில் பரிசு ஒப்பந்தம் என்பது எதிர்பார்ப்பின்றி சொத்து உரிமையை விருப்பமாக மாற்றுவதற்கான சட்ட ஆவணமாகும். இது கையொப்பம் செய்யப்பட்டு துணை பதிவாளரின் அலுவலகத்தில் பதிவு செய்யப்பட வேண்டும்.",
         "Section 122, Transfer of Property Act, 1882", 
         "Section 122 of the Transfer of Property Act, 1882, provides the legal framework for gifting immovable property and the requirements for the validity of a gift deed.",
         "இந்திய சொத்து பரிமாற்ற சட்டம், 1882 இன் பிரிவு 122, நிலையான சொத்தை பரிசளிக்கக்கான சட்ட அடித்தளத்தை வழங்குகிறது மற்றும் பரிசு ஒப்பந்தத்தின் முற்றுப்புள்ளிக்கான நிபந்தனைகளை அளிக்கிறது."
        )
    ],
    "Robbery": [
        ("What is the legal definition of robbery in India?", 
         "Under Indian law, robbery is defined as the act of taking property from another person by force or threat of force. This is covered under Section 390 of the Indian Penal Code (IPC).",
         "இந்திய சட்டத்தின் கீழ், கொள்ளையடி என்பது மற்றவரின் சொத்தை வலியுடன் அல்லது வலியையின் அச்சுறுத்தலால் எடுப்பது என்று வரையறுக்கப்படுகிறது. இது இந்திய பினியல் சட்டம் (IPC) இன் பிரிவு 390ல் உள்ளடக்கப்பட்டுள்ளது.",
         "Section 390 of the IPC", 
         "Section 390 of the Indian Penal Code defines robbery and includes elements of theft combined with force or intimidation.",
         "IPC இன் பிரிவு 390 கொள்ளையடியை வரையறுக்கிறது மற்றும் கொள்ளையடியில் திருட்டும் வலியோ அல்லது அச்சுறுத்தலும் உள்ளடங்கியுள்ளது."
        ),
        ("What are the penalties for committing robbery in India?", 
         "The punishment for robbery under Indian law can include imprisonment for up to 14 years, along with a fine. The severity of the punishment depends on the circumstances and whether any injury or grievous harm was caused.",
         "இந்தியாவில் கொள்ளையடித்தல் செய்யும் மரியாதை 14 ஆண்டுகளுக்குள் சிறைதண்டனை மற்றும் அபராதம் என்பவற்றை உள்ளடக்கியது. தண்டனையின் கடுமை சூழ்நிலைகளுக்கு மற்றும் எந்தவொரு காயம் அல்லது தீவிர சேதம் ஏற்பட்டதற்கேற்ப மாற்றப்படலாம்.",
         "Section 392 of the IPC", 
         "Section 392 of the Indian Penal Code outlines the punishment for robbery, specifying imprisonment and fines.",
         "IPC இன் பிரிவு 392, கொள்ளையடிக்கு வழங்கப்படும் தண்டனைகளை, சிறை மற்றும் அபராதங்களை குறிப்பிடுகிறது."
        ),
        ("What is the difference between robbery and theft under Indian law?", 
         "Robbery involves the use of force or intimidation to take property, whereas theft does not involve force or intimidation. Robbery is a more serious offense compared to theft.",
         "கொள்ளையடி என்பது சொத்தைப் பெற வலியோ அல்லது அச்சுறுத்தலோ பயன்படுத்தப்படுகிறது, ஆனால் திருட்டில் வலியோ அல்லது அச்சுறுத்தலோ உள்ளதில்லை. கொள்ளையடி திருட்டைவிட மிகவும் கடுமையான குற்றமாகும்.",
         "Section 378 and 390 of the IPC", 
         "Section 378 defines theft, while Section 390 defines robbery, highlighting the use of force or intimidation as a distinguishing factor.",
         "IPC இன் பிரிவு 378 திருட்டைப் பற்றிய விளக்கமாகும், மற்றும் பிரிவு 390 கொள்ளையடியை வரையறுக்கிறது, வலியோ அல்லது அச்சுறுத்தலோ மாறுபாட்டை குறிக்கிறது."
        ),
        ("What are the legal defenses available for someone accused of robbery?", 
         "Defenses against robbery charges may include proving lack of intent to commit robbery, mistaken identity, or claiming that the force used was not sufficient to constitute robbery.",
         "கொள்ளையடிக்கான குற்றச்சாட்டுகளுக்கு எதிரான defesa குற்றத்தைச் செய்யக் கூடிய நோக்கம் இல்லாமையை, தவறான அடையாளம் அல்லது பயன்படுத்திய வலியோ கொள்ளையடி உருவாக்குவதற்கு போதுமானது இல்லையெனக் கூறுதல் ஆகியவை அடங்கும்.",
         "Indian Penal Code", 
         "Legal defenses are addressed within the Indian Penal Code, where specific defenses and exceptions related to the offense of robbery are outlined.",
         "இந்திய பினியல் சட்டத்தில் குற்றங்களைச் செய்யும் நோக்கம் இல்லாமை, தவறான அடையாளம், மற்றும் பயன்படுத்திய வலியோ கொள்ளையடி உருவாக்காதவை போன்ற குறிப்பிட்ட defensa மற்றும் தவிர்க்கப்படுவதற்கான முறைகள் விவரிக்கப்படுகின்றன."
        ),
        ("How is aggravated robbery defined in Indian law?", 
         "Aggravated robbery involves the use of deadly weapons or causing serious harm during the commission of robbery. It is covered under Section 397 of the IPC.",
         "கடுமையான கொள்ளையடி என்பது மரணமான ஆயுதங்களைப் பயன்படுத்துதல் அல்லது கொள்ளையடிக்கும் போது கடுமையான சேதத்தை ஏற்படுத்துதல் என்பவற்றை உள்ளடக்குகிறது. இது IPC இன் பிரிவு 397ல் உள்ளடக்கப்பட்டுள்ளது.",
         "Section 397 of the IPC", 
         "Section 397 of the Indian Penal Code addresses aggravated robbery, specifying enhanced penalties for using deadly weapons or causing serious injury.",
         "IPC இன் பிரிவு 397, கடுமையான கொள்ளையடிக்கான விதிகளை, மரணமான ஆயுதங்களைப் பயன்படுத்துதல் அல்லது கடுமையான காயங்களை ஏற்படுத்துதல் பற்றிய அதிகரிக்கப்பட்ட தண்டனைகளை குறிப்பிடுகிறது."
        ),
        ("What is the role of evidence in proving a robbery case?", 
         "Evidence such as witness testimony, forensic evidence, and material evidence like stolen property are crucial in proving a robbery case. The prosecution must establish that the robbery occurred and that the accused was involved.",
         "சாட்சிகளின் சாட்சி, சோதனைக் குறியீடுகள் மற்றும் திருட்டுப் பொருட்கள் போன்ற பொருள் குறியீடுகள் ஆகியவை கொள்ளையடி வழக்கில் முக்கியமாக உள்ளன. வழக்குப்பூர்வமாக, கொள்ளையடி நிகழ்ந்தது மற்றும் குற்றம் சாட்டப்பட்டவர் ஈடுபட்டுள்ளார் என்பதைக் நிரூபிக்க வேண்டும்.",
         "Indian Evidence Act", 
         "The Indian Evidence Act governs the admissibility and use of evidence in court proceedings, including those related to robbery.",
         "இந்திய சாட்சியச் சட்டம் நீதிமன்றப் பேரவையில் சாட்சியின் அனுமதிப்படுத்தல் மற்றும் பயன்பாட்டை, கொள்ளையடி போன்ற வழக்குகளுடன் தொடர்புடையது உள்ளடக்குகிறது."
        )
    ],
    "Traffic Law": [
        ("What are the main provisions of the Motor Vehicles Act, 1988?", 
         "The Motor Vehicles Act, 1988, provides for the regulation of motor vehicles and drivers, including registration, licensing, penalties for traffic violations, and provisions for road safety.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988, மோட்டார் வாகனங்கள் மற்றும் ஓட்டுநர்களின் ஒழுங்குபடுத்தல், பதிவு, உரிமம், Verkehrsverletzungen தொடர்பான அபராதங்கள் மற்றும் சாலை பாதுகாப்புக்கான நிபந்தனைகளை வழங்குகிறது.",
         "Motor Vehicles Act, 1988", 
         "The Motor Vehicles Act, 1988, establishes the framework for the regulation of motor vehicles and traffic rules, including penalties for violations.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988, மோட்டார் வாகனங்கள் மற்றும் Verkehrsregels ஒழுங்குபடுத்துவதற்கான கட்டமைப்பை நிறுவுகிறது, மற்றும் மீறல்களுக்கு அபராதங்களை அடிப்படையாகக் கொண்டது."
        ),
        ("What are the penalties for driving under the influence of alcohol?", 
         "Driving under the influence of alcohol can result in penalties including fines, imprisonment, suspension of driving license, and mandatory attendance at alcohol education programs.",
         "மதுபானங்களின் ஆளுமையில் ஓட்டுவது அபராதங்கள், அபராதங்கள், சிறை, ஓட்டுநர் உரிமையின் தற்காலிக முக்கடிகாரம் மற்றும் மதுபான கல்வி நிகழ்ச்சிகளுக்கான கட்டாய பங்கேற்பு போன்றவற்றை விளைவிக்க முடியும்.",
         "Section 185 of the Motor Vehicles Act, 1988", 
         "Section 185 of the Motor Vehicles Act, 1988, deals with penalties for driving under the influence of alcohol or drugs.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இன் பிரிவு 185, மதுபானங்கள் அல்லது மருந்துகளின் தாக்கத்தின் கீழ் ஓட்டுவதற்கான அபராதங்களை குறிக்கிறது."
        ),
        ("What are the rules for wearing seat belts in India?", 
         "The law mandates that both drivers and passengers in the front seats must wear seat belts while the vehicle is in motion. Failure to comply can result in fines.",
         "வாகனம் இயக்கப்படுகிற போது முன்னணி சீட்டுகளில் உள்ள ஓட்டுநர்கள் மற்றும் பயணிகள் இருவரும் சீட் பெல்ட் அணிய வேண்டும். அதற்கேற்ப அதிகாரப்பூர்வமாக செயல்படாதது அபராதங்களை விளைவிக்கக்கூடும்.",
         "Section 138 of the Motor Vehicles Act, 1988", 
         "Section 138 of the Motor Vehicles Act, 1988, stipulates the requirement for wearing seat belts and the penalties for non-compliance.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இன் பிரிவு 138, சீட் பெல்டு அணிய தேவையை மற்றும் அதற்கான தவறுகள் தொடர்பான அபராதங்களை குறிக்கிறது."
        ),
        ("What are the regulations for using mobile phones while driving?", 
         "Using a mobile phone while driving without a hands-free device is prohibited. Violators can face fines and other penalties.",
         "ஓட்டும்போது கைமுறை சாதனமின்றி மொபைல் போன் பயன்படுத்துவது தடைசெய்யப்படுகிறது. குற்றவாளிகள் அபராதங்கள் மற்றும் பிற தண்டனைகளை சந்திக்கலாம்.",
         "Section 184 of the Motor Vehicles Act, 1988", 
         "Section 184 of the Motor Vehicles Act, 1988, addresses the prohibition of using mobile phones while driving and specifies penalties for offenders.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இன் பிரிவு 184, ஓட்டும்போது மொபைல் போன்களைப் பயன்படுத்துவதற்கான தடை மற்றும் குற்றவாளிகளுக்கான தண்டனைகளை குறிப்பிடுகிறது."
        ),
        ("What are the rules regarding speed limits in India?", 
         "Speed limits vary based on the type of road and vehicle. The law specifies maximum speed limits for different categories of roads, and exceeding these limits can result in fines and penalties.",
         "வேக எல்லைகள் சாலையின் வகை மற்றும் வாகனத்தைப் பொறுத்தது. சட்டம் வித்தியாசமான வகைகளுக்கான அதிகபட்ச வேக எல்லைகளை குறிப்பிடுகிறது மற்றும் இந்த எல்லைகளை மீறுவது அபராதங்கள் மற்றும் தண்டனைகளை விளைவிக்கலாம்.",
         "Section 112 of the Motor Vehicles Act, 1988", 
         "Section 112 of the Motor Vehicles Act, 1988, sets forth the maximum speed limits for different types of roads and vehicles.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இன் பிரிவு 112, வெவ்வேறு வகை சாலைகளுக்கான மற்றும் வாகனங்களுக்கு அதிகபட்ச வேக எல்லைகளை அமைக்கிறது."
        ),
        ("What are the requirements for vehicle registration in India?", 
         "All motor vehicles in India must be registered with the Regional Transport Office (RTO). The registration process includes submitting necessary documents, paying registration fees, and obtaining a registration certificate.",
         "இந்தியாவில் அனைத்து மோட்டார் வாகனங்களும் பிராந்திய போக்குவரத்து அலுவலகத்தில் (RTO) பதிவு செய்யப்பட வேண்டும். பதிவு செயல்முறை தேவையான ஆவணங்களை சமர்ப்பிக்க, பதிவு கட்டணங்களை செலுத்த மற்றும் பதிவு சான்றிதழைப் பெற வேண்டும்.",
         "Section 39 of the Motor Vehicles Act, 1988", 
         "Section 39 of the Motor Vehicles Act, 1988, mandates the registration of motor vehicles and details the process and requirements for vehicle registration.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இன் பிரிவு 39, மோட்டார் வாகனங்களின் பதிவை கட்டாயமாக்குகிறது மற்றும் வாகன பதிவுக்கான செயல்முறை மற்றும் தேவைகளை விவரிக்கிறது."
        ),
        ("What are the provisions for issuing a driving license?", 
         "To obtain a driving license in India, an individual must pass a driving test and a theoretical exam, and meet the age and health requirements specified by law.",
         "இந்தியாவில் ஓட்டுநர் உரிமை பெற, ஒருவர் ஓட்டுநர் தேர்வு மற்றும் கொள்கை பரீட்சைகளை எடுக்கும் மற்றும் சட்டத்தால் குறிப்பிடப்பட்ட வயது மற்றும் ஆரோக்கிய தேவைகளை பூர்த்தி செய்ய வேண்டும்.",
         "Section 7 of the Motor Vehicles Act, 1988", 
         "Section 7 of the Motor Vehicles Act, 1988, outlines the provisions for the issuance of driving licenses, including testing and documentation requirements.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இன் பிரிவு 7, ஓட்டுநர் உரிமைகளின் வழங்கலுக்கான நிபந்தனைகளை, தேர்வு மற்றும் ஆவண தேவைகளை உள்ளடக்கியது."
        ),
        ("What are the regulations for vehicle insurance in India?", 
         "All motor vehicles in India must have a valid insurance policy. The insurance should cover third-party liability and, optionally, comprehensive coverage.",
         "இந்தியாவில் அனைத்து மோட்டார் வாகனங்களும் செல்லுபடியான காப்பீட்டு கொள்கை கொண்டிருக்க வேண்டும். காப்பீட்டு மூலமாக மூன்றாம் தரப்பு பொறுப்பு மற்றும் விருப்பமாக முழுமையான காப்பீடு உள்ளடங்க வேண்டும்.",
         "Section 145 of the Motor Vehicles Act, 1988", 
         "Section 145 of the Motor Vehicles Act, 1988, requires all motor vehicles to be insured and outlines the types of coverage required.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இன் பிரிவு 145, அனைத்து மோட்டார் வாகனங்களும் காப்பீடு செய்யப்பட வேண்டும் மற்றும் தேவையான காப்பீட்டு வகைகளை விளக்குகிறது."
        ),
        ("What are the procedures for challenging traffic fines?", 
         "Traffic fines can be challenged by filing a complaint or appeal with the relevant traffic police department or the court, within the time frame specified in the fine notice.",
         "தராதிகாரம் சுருக்கமாகவும் சுருக்கமாகவும் காவல் துறையுடன் அல்லது நீதிமன்றத்துடன் குற்றச்சாட்டுகளை அல்லது அங்கீகாரங்களை தாக்கல் செய்வதன் மூலம் சவால் செய்யப்படலாம், அபராதக் குறிப்பில் குறிப்பிட்ட நேரக்கருவி வரம்புக்குள்.",
         "The Motor Vehicles Act, 1988", 
         "Procedures for challenging traffic fines are detailed in the Motor Vehicles Act, 1988, including avenues for appeal and dispute resolution.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இல், சீராக்கும் சலுகைகள் மற்றும் முறைகள் உட்பட அபராதங்களை சவால் செய்யும் நடைமுறைகள் விவரிக்கப்படுகின்றன."
        ),
        ("What are the rules for driving in emergency situations?", 
         "In emergency situations, drivers must ensure that they use their vehicles safely and responsibly, and they are permitted to use emergency lights and sirens if necessary. However, they must follow all other traffic laws.",
         "அவசர நிலைகளில், ஓட்டுநர்கள் தங்கள் வாகனங்களை பாதுகாப்பாக மற்றும் பொறுப்புடன் பயன்படுத்த வேண்டும் என்பதை உறுதி செய்ய வேண்டும், மற்றும் அவசியம் என்றால் அவசர ஒளிகள் மற்றும் சீரன்களைப் பயன்படுத்த அனுமதிக்கப்படுகிறார்கள். எனினும், அவர்கள் மற்ற அனைத்து போக்குவரத்து சட்டங்களை பின்பற்ற வேண்டும்.",
         "Motor Vehicles Act, 1988", 
         "The Motor Vehicles Act, 1988, includes provisions for emergency driving, allowing the use of emergency signals and requiring adherence to other traffic laws.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இல், அவசர ஓட்டுதலுக்கான நிபந்தனைகளை, அவசர சிக்னல்களைப் பயன்படுத்துவதற்கும் மற்ற போக்குவரத்து சட்டங்களைப் பின்பற்றுவதற்கும் அனுமதிக்கின்றது."
        ),
        ("What is the role of the Road Transport Office (RTO)?", 
         "The Road Transport Office (RTO) is responsible for vehicle registration, issuing driving licenses, enforcing traffic regulations, and ensuring road safety.",
         "பாதுகாப்பு மற்றும் சாலை பாதுகாப்பை உறுதி செய்ய, வாகன பதிவு, ஓட்டுநர் உரிமைகளை வழங்குதல், போக்குவரத்து விதிகளைப் கட்டுப்படுத்துதல் மற்றும் சாலை பாதுகாப்பை உறுதி செய்ய RTO பொறுப்பாக உள்ளது.",
         "Motor Vehicles Act, 1988", 
         "The Motor Vehicles Act, 1988, delineates the role of the RTO in vehicle and driver regulation, and enforcement of traffic laws.",
         "மோட்டார் வாகனங்கள் சட்டம், 1988 இல், RTO-வின் வாகன மற்றும் ஓட்டுநர் ஒழுங்குபடுத்தல் மற்றும் போக்குவரத்து சட்டங்களை அமல்படுத்துவதில் பங்காற்றுவது விவரிக்கப்படுகிறது."
        )
    ],
    "Education Law": [
        ("What is the Right to Education Act (RTE)?", 
         "The Right to Education Act (RTE) is a law enacted to provide free and compulsory education to children aged 6 to 14 years in India.",
         "உத்தரவாத கல்வி சட்டம் (RTE) என்பது இந்தியாவில் 6 முதல் 14 வயதினருக்கான இலவச மற்றும் கட்டாயமான கல்வியை வழங்கும் சட்டம் ஆகும்.",
         "Article 21A of the Constitution of India", 
         "Article 21A of the Indian Constitution guarantees the right to education to children aged 6 to 14 years.",
         "இந்திய அரசியலமைப்பின் Article 21A, 6 முதல் 14 வயதினருக்கான கல்வி உரிமையை உத்தரிக்கிறது."
        ),
        ("What are the provisions for reservation of seats in educational institutions?", 
         "Reservations in educational institutions are provided for Scheduled Castes (SC), Scheduled Tribes (ST), and Other Backward Classes (OBC) under various laws and regulations.",
         "கல்வி நிறுவனங்களில் இடங்களுக்கான பாதுகாப்புகள், அடிப்படையில் வட்டார ஒதுக்கீடு (SC), திட்டமிடப்பட்ட பழங்குடிகள் (ST) மற்றும் பிற பிறன்கள் (OBC) போன்ற வரிசைகளை வழங்கப்படுகிறது.",
         "Article 15(4) and Article 16(4) of the Constitution of India", 
         "Articles 15(4) and 16(4) of the Indian Constitution allow the state to make special provisions for the advancement of SCs, STs, and OBCs in educational institutions and employment.",
         "இந்திய அரசியலமைப்பின் 15(4) மற்றும் 16(4) நாட்டு அரசு SCs, STs, மற்றும் OBCs-ன் முன்னேற்றத்திற்கு சிறப்பு ஒதுக்கீடுகளை கல்வி நிறுவனங்களில் மற்றும் வேலைவாய்ப்புகளில் செய்ய அனுமதிக்கின்றன."
        ),
        ("What is the National Education Policy (NEP) 2020?", 
         "The National Education Policy (NEP) 2020 is a comprehensive policy aimed at transforming the education system in India to make it more holistic, flexible, multidisciplinary, aligned to the needs of the 21st century, and to promote regional languages and culture.",
         "தேசிய கல்வி கொள்கை (NEP) 2020, இந்திய கல்வி அமைப்பை முழுமையாக மாற்றுவதற்கும், அதனை மேலும் விரிவான, 유연மான, பல்துறை, 21ஆம் நூற்றாண்டின் தேவைகளுக்கு இணக்கமான, மற்றும் மண்டல மொழிகள் மற்றும் கலையை ஊக்குவிக்கும் வகையில் வடிவமைக்கப்படுகிறது.",
         "NEP 2020 Document", 
         "The NEP 2020 document outlines the new vision for education in India, including reforms in school and higher education, vocational training, and teacher education.",
         "NEP 2020 ஆவணம், இந்தியாவில் கல்விக்கான புதிய காட்சி மற்றும் பள்ளி மற்றும் உயர் கல்வி, தொழில்நுட்ப பயிற்சி மற்றும் ஆசிரியர் கல்வியில் மாற்றங்களை அடிப்படையாகக் கொண்டது."
        ),
        ("What is the role of the National Commission for Protection of Child Rights (NCPCR)?", 
         "The National Commission for Protection of Child Rights (NCPCR) is a statutory body responsible for safeguarding and promoting child rights in India, including the right to education.",
         "சிறுவர் உரிமைகளைக் காக்கும் மற்றும் ஊக்குவிக்கும் பொறுப்பை வைத்துள்ள தேசிய சிறுவர் உரிமைகள் பாதுகாப்பு ஆணையம் (NCPCR), இந்தியாவில் சிறுவர் உரிமைகளைப் பாதுகாக்கும் மற்றும் ஊக்குவிக்கும் சட்டவிரோதமான அமைப்பு ஆகும்.",
         "The Commission for Protection of Child Rights Act, 2005", 
         "The Commission for Protection of Child Rights Act, 2005 establishes the NCPCR and outlines its powers and functions in protecting and promoting child rights.",
         "சிறுவர் உரிமைகள் பாதுகாப்பு சட்டம், 2005, NCPCR-ஐ உருவாக்கி, சிறுவர் உரிமைகளைப் பாதுகாக்கும் மற்றும் ஊக்குவிக்கும் அதன் அதிகாரங்களையும் செயல்பாடுகளையும் விளக்குகிறது."
        ),
        ("What are the regulations for private schools in India?", 
         "Private schools in India are regulated by the respective State Education Acts and guidelines issued by the State Governments, covering aspects like infrastructure, curriculum, teacher qualifications, and fees.",
         "இந்தியாவில் தனியார் பள்ளிகள் மாநில கல்வி சட்டங்கள் மற்றும் மாநில அரசுகளால் வெளியிடப்பட்ட வழிகாட்டுதல்களின் அடிப்படையில் ஒழுங்குபடுத்தப்படுகின்றன, கட்டமைப்பு, பாடத்திட்டம், ஆசிரியர் தகுதிகள் மற்றும் கட்டணங்களைப் போன்ற அம்சங்களை உள்ளடக்கியது.",
         "The Right of Children to Free and Compulsory Education Act, 2009", 
         "The Right of Children to Free and Compulsory Education Act, 2009, mandates regulations for private schools to ensure compliance with the RTE Act, including infrastructure and quality standards.",
         "சிறுவர் உரிமை இலவச மற்றும் கட்டாய கல்வி சட்டம், 2009, தனியார் பள்ளிகள் RTE சட்டத்துடன் இணங்க உரிய கட்டமைப்புகள் மற்றும் தரநிலைகளை உறுதி செய்ய ஒழுங்குபடுத்துகிறது."
        ),
        ("What is the purpose of the Mid-Day Meal Scheme?", 
         "The Mid-Day Meal Scheme is a government program aimed at providing free lunches to children in primary and upper primary schools to improve nutritional levels and promote school attendance.",
         "மிட்-டே மில் திட்டம், முதன்மை மற்றும் மேல்நிலை முதன்மை பள்ளிகளில் குழந்தைகளுக்கு இலவச மதிய உணவுகளை வழங்குவதற்கான அரசு திட்டம் ஆகும், இது ஊட்டச்சத்து நிலைகளை மேம்படுத்த மற்றும் பள்ளி வருகையை ஊக்குவிக்கிறது.",
         "National Food Security Act, 2013", 
         "The National Food Security Act, 2013, provides for the Mid-Day Meal Scheme and other food security measures to improve the nutritional status of children.",
         "நாட்டிய உணவுத்தாக்கல் சட்டம், 2013, மிட்-டே மில் திட்டம் மற்றும் பிற உணவுத்தாக்கல் நடவடிக்கைகள் மூலம் குழந்தைகளின் ஊட்டச்சத்து நிலையை மேம்படுத்துகிறது."
        ),
        ("What are the provisions for higher education under Indian law?", 
         "Higher education in India is governed by various acts and regulations including the University Grants Commission (UGC) Act, 1956, and the All India Council for Technical Education (AICTE) Act, 1987.",
         "இந்தியாவில் உயர் கல்வி பல்வேறு சட்டங்கள் மற்றும் ஒழுங்குபடுத்தப்படுகின்றன, அதில் பல்கலைக்கழக உதவித்தொகை ஆணையம் (UGC) சட்டம், 1956, மற்றும் அனைத்து இந்திய தொழில்நுட்ப கல்வி மன்றம் (AICTE) சட்டம், 1987 அடங்குகிறது.",
         "University Grants Commission Act, 1956", 
         "The University Grants Commission Act, 1956, establishes the UGC and outlines its responsibilities in regulating and promoting higher education in India.",
         "பல்கலைக்கழக உதவித்தொகை ஆணையம் சட்டம், 1956, UGC-ஐ நிறுவுகிறது மற்றும் இந்தியாவில் உயர் கல்வியை ஒழுங்குபடுத்த மற்றும் ஊக்குவிக்க அதன் பொறுப்புகளை விளக்குகிறது."
        ),
        ("How does the National Assessment and Accreditation Council (NAAC) contribute to education?", 
         "The National Assessment and Accreditation Council (NAAC) assesses and accredits higher education institutions in India, ensuring they meet quality standards and improve educational outcomes.",
         "தேசிய மதிப்பீட்டு மற்றும் அங்கீகாரம் ஆணையம் (NAAC) இந்தியாவில் உயர் கல்வி நிறுவனங்களை மதிப்பீட்டு செய்யும் மற்றும் அங்கீகரிக்கும், அவர்கள் தரத்தினை பூர்த்தி செய்கிறார்கள் மற்றும் கல்வி முடிவுகளை மேம்படுத்துகிறார்கள்.",
         "NAAC Act and Guidelines", 
         "The NAAC Act and Guidelines establish the framework for the assessment and accreditation of higher education institutions to ensure quality education.",
         "NAAC சட்டம் மற்றும் வழிகாட்டுதல்களும், தரமான கல்வியை உறுதி செய்ய உயர் கல்வி நிறுவனங்களின் மதிப்பீட்டு மற்றும் அங்கீகரிக்கும் முறைமையை நிறுவுகிறது."
        ),
        ("What are the legal provisions for vocational education in India?", 
         "Vocational education in India is governed by various laws and policies, including the National Skill Development Act, 2009, which aims to enhance skills and employability among the youth.",
         "இந்தியாவில் தொழில்நுட்ப கல்வி பல்வேறு சட்டங்கள் மற்றும் கொள்கைகளால் ஒழுங்குபடுத்தப்படுகிறது, அதில் தேசிய திறன் மேம்பாட்டுச் சட்டம், 2009, இளம் பருவத்தினருக்கான திறன்களை மற்றும் வேலை வாய்ப்புகளை மேம்படுத்தும் நோக்கில் உள்ளது.",
         "National Skill Development Act, 2009", 
         "The National Skill Development Act, 2009, establishes the National Skill Development Mission and provides for the development of vocational skills and training.",
         "தேசிய திறன் மேம்பாட்டுச் சட்டம், 2009, தேசிய திறன் மேம்பாட்டுப் பணியகம் உருவாக்குவதையும் தொழில்நுட்ப திறன்கள் மற்றும் பயிற்சிகளின் மேம்பாட்டை வழங்குவதையும் குறிப்பிடுகிறது."
        ),
        ("What are the rights of students in Indian educational institutions?", 
         "Students in Indian educational institutions have rights to quality education, non-discrimination, protection from harassment, and participation in decision-making processes related to their education.",
         "இந்திய கல்வி நிறுவனங்களில் உள்ள மாணவர்களுக்கு, தரமான கல்வி, பாகுபாடு இல்லாமை, வன்கொடுமை எதிர்க்கும் பாதுகாப்பு மற்றும் தங்கள் கல்வியுடன் தொடர்புடைய முடிவெடுத்தல் செயல்முறைகளில் பங்கேற்கும் உரிமைகள் உள்ளன.",
         "The Right of Children to Free and Compulsory Education Act, 2009", 
         "The Right of Children to Free and Compulsory Education Act, 2009, provides for students' rights to education and mandates protection from discrimination and harassment.",
         "சிறுவர் உரிமை இலவச மற்றும் கட்டாய கல்வி சட்டம், 2009, மாணவர்களின் கல்வி உரிமைகளை வழங்குகிறது மற்றும் பாகுபாடு மற்றும் வன்கொடுமையிலிருந்து பாதுகாப்பை கட்டாயமாக்குகிறது."
        )
    ],
    "Contract Law": [
        ("What is a valid contract under Indian law?", 
         "A valid contract under Indian law requires an offer, acceptance, lawful consideration, free consent, lawful object, and competent parties. The agreement must not be expressly declared void.",
         "இந்திய சட்டத்தின் கீழ் செல்லுபடியாகும் ஒப்பந்தம் என்பது ஒரு முன்மொழிவு, ஏற்றுக்கொள்வது, சட்டப்படி பரிகாரம், சுதந்திரமான ஒப்புதல், சட்டபூர்வமான நோக்கம், மற்றும் தகுதியான தரப்புகளைக் கொண்டிருக்கும். ஒப்பந்தம் வெளிப்படையாக செல்லாதது என்று அறிவிக்கப்படக்கூடாது.",
         "Section 10, Indian Contract Act, 1872", 
         "Section 10 of the Indian Contract Act, 1872, outlines the essential elements that make an agreement legally enforceable as a valid contract.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 10, ஒரு ஒப்பந்தத்தைச் சட்டரீதியாகப் போதுமானதாக மாற்றும் அத்தியாவசிய கூறுகளை விவரிக்கிறது."
        ),
        ("What constitutes a breach of contract under Indian law?", 
         "A breach of contract occurs when one party fails to fulfill its contractual obligations, either by not performing as agreed or by performing improperly.",
         "ஒரு தரப்பினர் ஒப்பந்தத்தின் அடிப்படையில் அவருடைய பொறுப்புகளை நிறைவேற்ற தவறும்போது அல்லது தவறான முறையில் செயல்படும் போது ஒப்பந்த மீறல் ஏற்படுகிறது.",
         "Section 73, Indian Contract Act, 1872", 
         "Section 73 of the Indian Contract Act, 1872, provides for compensation in case of a breach of contract, outlining the consequences and remedies available.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 73, ஒப்பந்த மீறலுக்கான நிவாரணம் மற்றும் இதற்கு கிடைக்கும் சட்டரீதியான தண்டனைகளைக் குறிப்பிடுகிறது."
        ),
        ("What is the difference between void and voidable contracts?", 
         "A void contract is one that is unenforceable from the beginning, while a voidable contract is valid until one party chooses to void it due to certain conditions like coercion or misrepresentation.",
         "செல்லுபடியாகாத ஒப்பந்தம் ஆரம்பத்திலிருந்தே நடைமுறைப்படுத்த முடியாத ஒன்று, ஆனால் செல்லுபடியாகக்கூடிய ஒப்பந்தம் சில நிபந்தனைகளால் (கட்டாயம் அல்லது பொய்மையளிப்பு போன்றவை) ஒரு தரப்பினரால் ரத்து செய்யப்படும் வரை செல்லுபடியாகும்.",
         "Section 2(j) and Section 2(i), Indian Contract Act, 1872", 
         "Section 2(j) of the Indian Contract Act defines void contracts, while Section 2(i) explains voidable contracts.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 2(j) செல்லாத ஒப்பந்தங்களை வரையறுக்கிறது, மற்றும் பிரிவு 2(i) செல்லுபடியாகக்கூடிய ஒப்பந்தங்களை விளக்குகிறது."
        ),
        ("What are the remedies available for breach of contract in India?", 
         "The remedies for breach of contract in India include compensation for loss or damage, specific performance, and rescission of the contract.",
         "இந்தியாவில் ஒப்பந்த மீறலுக்கான நிவாரணங்கள் இழப்பு அல்லது சேதத்திற்கு இழப்பீடு, குறிப்பிட்ட செயல்திறனை பெறுதல், மற்றும் ஒப்பந்தத்தை ரத்து செய்வது ஆகியவை அடங்கும்.",
         "Section 73, 74, and 75, Indian Contract Act, 1872", 
         "Sections 73, 74, and 75 of the Indian Contract Act provide for compensation, liquidated damages, and the right to claim restitution in case of breach of contract.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 73, 74, மற்றும் 75 இழப்பீடு, தீர்வான நிவாரணங்கள், மற்றும் ஒப்பந்த மீறல் ஏற்பட்டால் நிவாரணத்தைப் பெறுவதற்கான உரிமையை வழங்குகிறது."
        ),
        ("What is the principle of free consent in contract law?", 
         "Free consent means that parties entering into a contract must do so voluntarily, without coercion, undue influence, fraud, misrepresentation, or mistake.",
         "சுதந்திரமான ஒப்புதல் என்பது ஒப்பந்தத்தில் தரப்பினர் கட்டாயம், ஒடுக்குதல், மோசடி, தவறான விளக்கம் அல்லது பிழை இன்றி சுதந்திரமாக ஒப்புதல் கொடுக்க வேண்டும் என்பதைக் குறிக்கிறது.",
         "Section 14, Indian Contract Act, 1872", 
         "Section 14 of the Indian Contract Act, 1872, defines free consent and specifies situations where consent is not considered free.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 14 சுதந்திரமான ஒப்புதலை வரையறுக்கிறது மற்றும் ஒப்புதல் சுதந்திரமாகக் கருதப்படாத சூழலைக் குறிப்பிடுகிறது."
        ),
        ("What are contingent contracts under Indian law?", 
         "Contingent contracts are those where the performance depends on the occurrence or non-occurrence of a future uncertain event.",
         "நிகழ்ச்சிகளைச் சார்ந்த ஒப்பந்தம் என்பது எதிர்காலத்தில் நிகழக்கூடிய அல்லது நிகழாத ஒரு நிகழ்வின் அடிப்படையில் செயல்படப்படும் ஒப்பந்தமாகும்.",
         "Section 31, Indian Contract Act, 1872", 
         "Section 31 of the Indian Contract Act, 1872, defines contingent contracts and outlines the conditions under which they are enforceable.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 31 நிகழ்ச்சிகளை சார்ந்த ஒப்பந்தங்களை வரையறுக்கிறது மற்றும் அவற்றின் நடைமுறைப்படுத்தக்கூடிய விதிகளை விளக்குகிறது."
        ),
        ("What are the rules regarding undue influence in contract law?", 
         "Undue influence occurs when one party uses its position of power to obtain an unfair advantage in a contract, making the agreement voidable.",
         "ஒப்பந்தத்தில் ஒரு தரப்பு தனது அதிகாரத்தின் நிலையைப் பயன்படுத்தி, மறுமுனை தரப்பின் மீதான மடிப்பைச் செலுத்தி, மறுசீரமைக்கப்படும் வகையில் நன்மையைப் பெறுவதை ஒடுக்குமுறை இழுத்தல் எனக் குறிப்பிடுகிறார்கள்.",
         "Section 16, Indian Contract Act, 1872", 
         "Section 16 of the Indian Contract Act, 1872, defines undue influence and the circumstances under which a contract can be voidable due to undue influence.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 16 ஒடுக்குமுறை இழுத்தலை வரையறுக்கிறது மற்றும் அது காரணமாக ஒப்பந்தம் செல்லுபடியாகக்கூடியது என்று கூறும் சூழல்களை விளக்குகிறது."
        ),
        ("What is meant by frustration of contract?", 
         "Frustration of contract occurs when a contract becomes impossible to perform due to unforeseen circumstances beyond the control of the parties.",
         "ஒப்பந்தத்தை நிறைவேற்ற முடியாத சூழ்நிலைகள் (இரு தரப்பினராலும் கட்டுப்படுத்த முடியாத) ஏற்பட்டால், ஒப்பந்தம் முற்றுப்பெறும் அல்லது தோல்வியுறும் என்பதை ஒப்பந்த முற்றுப்பாடு எனக் குறிப்பிடுகிறார்கள்.",
         "Section 56, Indian Contract Act, 1872", 
         "Section 56 of the Indian Contract Act, 1872, deals with the doctrine of frustration and states that a contract becomes void when it is impossible to perform due to unforeseen circumstances.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 56 ஒப்பந்த முற்றுப்பாட்டின் கொள்கையை விவரிக்கிறது மற்றும் எதிர்பாராத சூழ்நிலைகளால் செயல்படுத்த முடியாத ஒப்பந்தங்கள் செல்லாததாக மாற்றப்படுவதைக் குறிப்பிடுகிறது."
        ),
        ("What are liquidated damages under Indian contract law?", 
         "Liquidated damages refer to a pre-determined amount of compensation mentioned in the contract, payable in case of a breach by either party.",
         "ஒப்பந்தத்தில் குறிக்கப்படுகின்ற நிலையான இழப்பீடு என்பது ஒப்பந்தத்தை மீறியவரால் தரப்படும் நஷ்டஈடு தொகையாகும்.",
         "Section 74, Indian Contract Act, 1872", 
         "Section 74 of the Indian Contract Act, 1872, deals with liquidated damages and provides for reasonable compensation in the case of a breach of contract.",
         "இந்திய ஒப்பந்த சட்டம், 1872 இன் பிரிவு 74 தீர்வான நஷ்டஈடுகளை வரையறுக்கிறது மற்றும் ஒப்பந்தத்தின் மீறல் ஏற்பட்டால் ஏற்படும் இழப்பீடுகளை நிர்ணயிக்கிறது."
        )],
    "Constitutional Law": [
        ("What are fundamental rights under the Indian Constitution?", 
         "Fundamental rights under the Indian Constitution include the right to equality, right to freedom, right against exploitation, right to freedom of religion, cultural and educational rights, and the right to constitutional remedies.",
         "இந்திய அரசியலமைப்பின் கீழ் அடிப்படை உரிமைகளில் சமத்துவம், சுதந்திரம், 착ுஷ்டம் காக்கப்பட்டிருக்கும் விடுதலை, அடிமை விலக்கு, மதசார்பின்மை, கலாச்சாரம் மற்றும் கல்வி உரிமைகள் ஆகியவை அடங்கும்.",
         "Part III, Articles 12-35, Constitution of India", 
         "Part III of the Indian Constitution guarantees fundamental rights to every citizen and outlines the legal provisions to protect them.",
         "இந்திய அரசியலமைப்பின் III பகுதி ஒவ்வொரு குடிமகனுக்கும் அடிப்படை உரிமைகளை உறுதிசெய்கிறது மற்றும் அவற்றை பாதுகாக்கும் சட்டப்பூர்வப் பிரிவுகளை குறிப்பிடுகிறது."
        ),
        ("What is the 'right to equality' under the Indian Constitution?", 
         "The right to equality ensures that the state shall not deny any person equality before the law or equal protection of the laws within the territory of India.",
         "சமத்துவம் உரிமை இந்தியாவின் எல்லைகளுக்குள் எந்த நபருக்கும் சட்டத்தின் முன் சமத்துவம் அல்லது சமமான பாதுகாப்பை மறுப்பதில்லை என்பதற்கான உத்தரவாதமாகும்.",
         "Article 14, Constitution of India", 
         "Article 14 of the Indian Constitution guarantees equality before the law and equal protection of the law to all persons within the territory of India.",
         "இந்திய அரசியலமைப்பின் Article 14 இந்தியாவின் எல்லைகளுக்குள் உள்ள அனைத்து நபர்களுக்கும் சட்டத்தின் முன் சமத்துவத்தை உறுதிசெய்கிறது."
        ),
        ("What is the 'right to freedom of speech and expression' under the Indian Constitution?", 
         "The right to freedom of speech and expression allows every citizen to express their opinions freely, subject to reasonable restrictions in the interest of sovereignty, security, public order, and decency.",
         "சொற்பொழிவு மற்றும் வெளிப்பாட்டின் சுதந்திரம் உரிமை ஒவ்வொரு குடிமகனுக்கும் தங்கள் கருத்துக்களை சுதந்திரமாக வெளியிட அனுமதிக்கிறது, ஆனால் பாதுகாப்பு, பொதுமக்கள் ஒழுங்கு, மற்றும் மரியாதைக்கு உட்பட்டு நியாயமான கட்டுப்பாடுகள் உள்ளன.",
         "Article 19(1)(a), Constitution of India", 
         "Article 19(1)(a) of the Indian Constitution provides for the freedom of speech and expression, with reasonable restrictions outlined in Article 19(2).",
         "இந்திய அரசியலமைப்பின் Article 19(1)(a) சொற்பொழிவு மற்றும் வெளிப்பாட்டின் சுதந்திரத்தை வழங்குகிறது, மற்றும் Article 19(2) இல் கூறப்பட்ட நியாயமான கட்டுப்பாடுகளுடன்."
        ),
        ("What is the 'right to constitutional remedies'?", 
         "The right to constitutional remedies allows citizens to approach the courts if their fundamental rights are violated, empowering the courts to issue writs such as habeas corpus, mandamus, prohibition, quo warranto, and certiorari.",
         "அடிப்படை உரிமைகள் மீறப்பட்டால் நீதிமன்றங்களை அணுகுவதற்கான உரிமையை அரசியலமைப்பு சீர்திருத்தங்கள் உரிமை அளிக்கிறது, மற்றும் நீதிமன்றம் பரிதானம், தடை, சிறப்பு அலுவல், மற்றும் சான்றிதழ் போன்ற ஆணைகளை வெளியிட அனுமதிக்கிறது.",
         "Article 32, Constitution of India", 
         "Article 32 of the Indian Constitution provides for the right to constitutional remedies, allowing citizens to approach the Supreme Court directly in case of a violation of their fundamental rights.",
         "இந்திய அரசியலமைப்பின் Article 32 அரசியலமைப்பு சீர்திருத்த உரிமையை வழங்குகிறது, மற்றும் அடிப்படை உரிமைகள் மீறப்பட்டால் உச்ச நீதிமன்றத்தை நேரடியாக அணுக உரிமை அளிக்கிறது."
        ),
        ("What is the significance of the 'right to life and personal liberty' under the Indian Constitution?", 
         "The right to life and personal liberty ensures that no person shall be deprived of life or personal liberty except according to the procedure established by law.",
         "ஒரு நபரின் வாழ்க்கை அல்லது தனிப்பட்ட சுதந்திரத்தை சட்டத்தின் அடிப்படையில் வெளிவரும் நடைமுறைகளைத் தவிர எந்த காரணத்தாலும் பறிக்கக்கூடாது என்பதை வாழ்க்கை மற்றும் தனிப்பட்ட சுதந்திரம் உரிமை உறுதிசெய்கிறது.",
         "Article 21, Constitution of India", 
         "Article 21 of the Indian Constitution guarantees the right to life and personal liberty, interpreted to include various rights like the right to privacy, right to health, and right to a clean environment.",
         "இந்திய அரசியலமைப்பின் Article 21 வாழ்க்கை மற்றும் தனிப்பட்ட சுதந்திரத்தின் உரிமையை உறுதிசெய்கிறது, மற்றும் தனியுரிமை, சுகாதார உரிமை, சுத்தமான சூழல் போன்ற பல உரிமைகளை உட்படுத்துகிறது."
        ),
        ("What is the 'directive principles of state policy'?", 
         "Directive Principles are guidelines for the state to ensure social and economic welfare, and to promote justice in governance, although they are not enforceable by the courts.",
         "நடத்தைக் கொள்கைகளின் கோட்பாடுகள் என்பது சமூக மற்றும் பொருளாதார நலத்தை உறுதிசெய்து, நல்லாட்சி அடிப்படையில் நீதியை முன்னேற்றும் நோக்கத்துடன் மாநிலத்திற்கு வழங்கப்படும் வழிகாட்டல்களாகும், ஆனால் நீதிமன்றங்களால் நடைமுறைக்கு வரவைக்க முடியாது.",
         "Part IV, Articles 36-51, Constitution of India", 
         "Part IV of the Indian Constitution outlines the Directive Principles of State Policy, aiming to create a welfare state by guiding legislative and executive decisions.",
         "இந்திய அரசியலமைப்பின் IV பகுதி மாநில கொள்கை ஆவணத்தின் கோட்பாடுகளை விவரிக்கிறது, மற்றும் சட்டத்திட்டங்கள் மற்றும் நிர்வாக முடிவுகளை வழிநடத்துவதன் மூலம் நலமுள்ள ஒரு நாட்டை உருவாக்குவதை நோக்கமாகக் கொண்டுள்ளது."
        ),
        ("What is the basic structure doctrine in Indian Constitutional law?", 
         "The basic structure doctrine holds that certain fundamental features of the Constitution cannot be altered by amendments, even by the Parliament.",
         "அரசியலமைப்பின் சில அடிப்படை அம்சங்களை சீர்திருத்தங்கள் மூலம், கூட நாடாளுமன்றத்தால் மாற்ற முடியாது என்பதற்கான கொள்கையை அடிப்படை அமைப்பு கொள்கை என குறிப்பிடுகிறார்கள்.",
         "Kesavananda Bharati v. State of Kerala, 1973", 
         "In the landmark Kesavananda Bharati case, the Supreme Court held that Parliament's amending power is subject to the Constitution's basic structure, which cannot be altered.",
         "Kesavananda Bharati வழக்கில் உச்ச நீதிமன்றம், அரசியலமைப்பின் அடிப்படை அமைப்பை நாடாளுமன்றத்தின் திருத்த அதிகாரத்திற்கு உட்பட்டதாக கருத முடியாது என்று தீர்ப்பு வழங்கியது."
        ),
        ("What is the 'right to privacy' under Indian Constitutional law?", 
         "The right to privacy is recognized as a fundamental right under the right to life and personal liberty, ensuring protection from state and non-state actors in matters of personal information, bodily autonomy, and intimate decisions.",
         "தனியுரிமை உரிமை என்பது வாழ்க்கை மற்றும் தனிப்பட்ட சுதந்திரத்தின் அடிப்படையில் அடிப்படை உரிமையாக அங்கீகரிக்கப்படுகிறது, மற்றும் தனிப்பட்ட தகவல்கள், உடல் சுயவிவசாயம் மற்றும் நெருங்கிய முடிவுகள் ஆகியவற்றில் மாநிலம் மற்றும் மாநிலம் சாரா இயக்குனர்களிடமிருந்து பாதுகாப்பை உறுதிசெய்கிறது.",
         "Justice K. S. Puttaswamy (Retd.) v. Union of India, 2017", 
         "In the landmark Justice Puttaswamy case, the Supreme Court recognized the right to privacy as a fundamental right under Article 21 of the Constitution.",
         "Justice Puttaswamy வழக்கில் உச்ச நீதிமன்றம், Article 21 இன் கீழ் தனியுரிமை உரிமையை அடிப்படை உரிமையாக அங்கீகரித்தது."
        ),
        ("What are the powers and functions of the President of India?", 
         "The President of India is the ceremonial head of state, with powers such as appointing the Prime Minister, granting pardons, and being the supreme commander of the armed forces, among other executive, legislative, and judicial functions.",
         "இந்தியாவின் குடியரசுத் தலைவர் என்பது அடையாள அமைப்பு ஆளுநராக இருக்கிறார் மற்றும் பிரதமரை நியமிப்பது, மன்னிப்புகளை வழங்குவது மற்றும் ஆயுத படைகளின் தலைமைத் தளபதியாக இருப்பது போன்ற செயற்பாடுகள் மற்றும் சட்டம் மற்றும் நீதிமன்ற செயல்பாடுகளைப் பயன்படுத்துகிறார்.",
         "Articles 52-78, Constitution of India", 
         "Articles 52-78 of the Indian Constitution outline the powers, responsibilities, and functions of the President, detailing their role in the executive branch.",
         "இந்திய அரசியலமைப்பின் Articles 52-78 குடியரசுத் தலைவர் அதிகாரங்கள் மற்றும் அவர்களின் செயல்பாடுகளை விவரிக்கின்றன, மேலும் அவர்கள் நிறைவேற்று பிரிவில் உள்ள அதிகாரங்கள் விவரிக்கின்றன."
        ),
        ("What is the significance of the 42nd Amendment to the Indian Constitution?", 
         "The 42nd Amendment, often referred to as the 'Mini Constitution,' made sweeping changes to the Constitution, including the insertion of the words 'socialist' and 'secular' in the Preamble and increased powers of the Parliament.",
         "42ஆவது திருத்தம், அடிக்கடி 'சின்ன அரசியலமைப்பு' என குறிப்பிடப்படுகிறது, அரசியலமைப்பில் முக்கியமான மாற்றங்களைச் செய்தது, உட்பட முன்னுரையில் 'சோஷலிச' மற்றும் 'மதசார்பின்மை' என்ற வார்த்தைகளை சேர்த்தது மற்றும் நாடாளுமன்றத்தின் அதிகாரங்களை உயர்த்தியது.",
         "42nd Amendment, 1976", 
         "The 42nd Amendment of 1976 significantly altered the Indian Constitution, affecting the relationship between the judiciary and Parliament and expanding the scope of the directive principles.",
         "42ஆவது திருத்தம், 1976, இந்திய அரசியலமைப்பில் குறிப்பிடத்தக்க மாற்றங்களைச் செய்தது, நீதிமன்றம் மற்றும் நாடாளுமன்றத்தின் உறவை பாதித்தது மற்றும் வழிகாட்டல் கொள்கைகளை விரிவுபடுத்தியது."
        )
    ],
   
    "Intellectual Property Law": [
        ("What is a trademark under Indian law?", 
         "A trademark is a symbol, word, or phrase legally registered or established by use as representing a company or product. It helps consumers identify the source of goods or services.",
         "ஒரு வணிக குறியீடு என்பது ஒரு நிறுவனம் அல்லது தயாரிப்பை அடையாளம் காணும் ஒரு சின்னம், வார்த்தை அல்லது பிரசாரம் ஆகும், மற்றும் இது சட்டப்படி பதிவு செய்யப்பட வேண்டும்.",
         "Section 2(1)(zb), Trade Marks Act, 1999", 
         "Section 2(1)(zb) of the Trade Marks Act defines a trademark and provides protection for marks associated with goods or services.",
         "Trade Marks Act 1999 இன் பிரிவு 2(1)(zb) ஒரு வணிக குறியீட்டை வரையறுக்கிறது மற்றும் வணிக அல்லது சேவைகளுடன் தொடர்புடைய குறியீடுகளுக்கு பாதுகாப்பு வழங்குகிறது."
        ),
        ("How to apply for a patent in India?", 
         "To apply for a patent in India, one must file a patent application with the Indian Patent Office, disclosing the invention and its claims. The patent is granted after a thorough examination.",
         "இந்தியாவில் ஒரு காப்புரிமை பெற, நீங்கள் காப்புரிமை அலுவலகத்தில் விண்ணப்பத்தை தாக்கல் செய்ய வேண்டும், மற்றும் காப்புரிமை ஆய்வு செய்யப்பட்ட பின்பே வழங்கப்படும்.",
         "Patents Act, 1970, Sections 6-10", 
         "Sections 6 to 10 of the Patents Act outline the procedure for applying for patents, including the requirements for disclosure of the invention and payment of fees.",
         "Patents Act 1970 இன் பிரிவுகள் 6 முதல் 10 வரை காப்புரிமை விண்ணப்பிக்கப்படும் முறையினை விளக்குகின்றன."
        ),
        ("What is the duration of copyright protection in India?", 
         "In India, copyright protection lasts for the lifetime of the author plus 60 years after their death for literary, dramatic, musical, and artistic works.",
         "இந்தியாவில், காப்புரிமை பாதுகாப்பு எழுத்தாளர் வாழ்நாள் மற்றும் அவர் இறந்த பின் 60 ஆண்டுகள் வரை நின்று நிற்கிறது.",
         "Section 22, Copyright Act, 1957", 
         "Section 22 of the Copyright Act, 1957, provides that the term of copyright for works like books, music, and paintings lasts for 60 years after the author's death.",
         "Copyright Act 1957 இன் பிரிவு 22 இல் காப்புரிமையின் காலத்தை எழுத்தாளர் இறந்த பின் 60 ஆண்டுகள் என குறிப்பிடுகிறது."
        ),
        ("What constitutes infringement of a trademark in India?", 
         "Trademark infringement occurs when a mark similar to a registered trademark is used without authorization, leading to confusion among consumers regarding the source of goods or services.",
         "பதிவுசெய்யப்பட்ட வணிக குறியீட்டை அனுமதியின்றி பயன்படுத்துவது, குறிப்பாக பொருட்களின் மூலத்தைப் பற்றி நுகர்வோரை குழப்பத்திற்குள்ளாக்குவது குறியீடு மீறல் ஆகும்.",
         "Section 29, Trade Marks Act, 1999", 
         "Section 29 of the Trade Marks Act explains trademark infringement, including when a registered trademark is misused by unauthorized parties, causing confusion.",
         "Trade Marks Act 1999 இன் பிரிவு 29 ஒரு வணிக குறியீட்டை அனுமதியின்றி பயன்படுத்தப்படும் சூழல்களை விளக்குகிறது."
        ),
        ("What is the role of the Copyright Board in India?", 
         "The Copyright Board in India is a quasi-judicial body that resolves disputes related to copyright, such as licensing, infringement, and ownership claims.",
         "காப்புரிமை குழு என்பது காப்புரிமை தொடர்பான மோதல்களைத் தீர்க்கும் மற்றும் உரிமையை நிலைநாட்டும் ஒரு நீதிமன்ற முறை அமைப்பு ஆகும்.",
         "Chapter XI, Copyright Act, 1957", 
         "Chapter XI of the Copyright Act, 1957, describes the powers and functions of the Copyright Board, including dispute resolution and determining statutory licensing fees.",
         "Copyright Act 1957 இன் அத்தியாயம் XI காப்புரிமை குழுவின் அதிகாரங்கள் மற்றும் செயல்பாடுகளை விவரிக்கிறது."
        ),
        ("What is compulsory licensing under Indian Patent Law?", 
         "Compulsory licensing allows the government to authorize a third party to produce a patented product without the patent owner's consent, usually in cases of public interest like healthcare.",
         "காப்புரிமை உரிமையாளர் ஒப்புதலின்றி, பொதுநலத்தில் அரசாங்கம் ஒரு மூன்றாம் தரப்பிற்கு தயாரிப்பு உரிமையை வழங்கும் அதிகாரம் கொண்டது.",
         "Section 84, Patents Act, 1970", 
         "Section 84 of the Patents Act provides for compulsory licensing if the patented product is not available at a reasonable price, or in sufficient quantity to the public.",
         "Patents Act 1970 இன் பிரிவு 84, பொதுநலத்திற்கு ஒரு காப்புரிமைப் பொருள் போதுமான அளவிலும் சரியான விலையிலும் கிடைக்கவில்லை என்றால் கட்டாய உரிமையை வழங்குகிறது."
        ),
        ("What is the difference between a copyright and a patent?", 
         "A copyright protects original works of authorship such as literature and music, while a patent protects new inventions or technological advancements for a limited period.",
         "ஒரு காப்புரிமை, இலக்கியம் மற்றும் இசை போன்ற புத்தாக்கங்களைப் பாதுகாக்கிறது, ஆனால் ஒரு காப்புரிமை புதிய கண்டுபிடிப்புகளை அல்லது தொழில்நுட்ப முன்னேற்றங்களை ஒரு குறிப்பிட்ட காலத்திற்கு மட்டுமே பாதுகாக்கும்.",
         "Copyright Act, 1957 & Patents Act, 1970", 
         "The Copyright Act, 1957, governs protection for creative works, while the Patents Act, 1970, provides the legal framework for protecting inventions.",
         "Copyright Act, 1957 மற்றும் Patents Act, 1970 முறையிலான புதுமைகளைப் பாதுகாக்கும் சட்ட அமைப்பை வழங்குகிறது."
        ),
        ("What is 'fair use' in copyright law?", 
         "Fair use allows limited use of copyrighted material without permission from the copyright owner for purposes such as criticism, news reporting, teaching, or research.",
         "காப்புரிமை உரிமையாளர் அனுமதியின்றி சில குறிப்பிட்ட செயல்களில் பயன்படுத்த அனுமதிக்கப்படும் உரிமையை நிலைநாட்டுகிறது.",
         "Section 52, Copyright Act, 1957", 
         "Section 52 of the Copyright Act lists the conditions under which copyrighted materials can be used for fair purposes like education or review without it being considered infringement.",
         "Copyright Act 1957 இன் பிரிவு 52 கல்வி அல்லது விமர்சனம் போன்ற நியாயமான நோக்கங்களுக்கு காப்புரிமை உள்ள பொருட்களை பயன்படுத்த அனுமதிக்கிறது."
        ),
        ("What is the duration of patent protection in India?", 
         "A patent is granted for a maximum period of 20 years from the date of filing the application, subject to renewal fees.",
         "காப்புரிமை 20 ஆண்டுகள் வரை செல்லுபடியாகும், அப்போது வருடாந்திர கட்டணம் செலுத்தி புதுப்பிக்கப்படும்.",
         "Section 53, Patents Act, 1970", 
         "Section 53 of the Patents Act specifies that a patent remains in force for 20 years from the date of filing, provided all renewal fees are paid.",
         "Patents Act 1970 இன் பிரிவு 53 காப்புரிமை விண்ணப்பத்தின் நாளிலிருந்து 20 ஆண்டுகள் வரை செல்லும் என்பதை விளக்குகிறது."
        ),
        ("What are geographical indications under Indian law?", 
         "Geographical indications identify a product as originating from a specific location, where a given quality, reputation, or other characteristic is essentially attributable to its geographic origin.",
         "வணிக குறிப்புகள் ஒரு குறிப்பிட்ட இடத்தில் உருவாகும் ஒரு தயாரிப்பைப் பற்றி அதனுடைய தரத்திற்கும், புகழுக்கும் புவியியல் மூலாதாரத்தை அடிப்படையாகக் கொண்டது என்று அடையாளம் காணும்.",
         "Geographical Indications of Goods (Registration and Protection) Act, 1999", 
         "This Act governs the protection of geographical indications in India, enabling producers to register names of products that have a specific origin and quality linked to a geographical region.",
         "Geographical Indications Act, 1999, குறிப்பிட்ட புவியியல் இடத்தில் உருவாகும் தயாரிப்புகளுக்கு அடையாளம் காணும் உரிமை வழங்குகிறது."
        )
    ],

    "Labor Law": [
        ("What is the minimum wage law in India?", 
         "The Minimum Wages Act, 1948 mandates that employers pay workers at least the minimum wage as determined by the government, based on factors like industry, location, and type of work.",
         "குறைந்தபட்ச ஊதியச் சட்டம், 1948, தொழிலாளர், இடம் மற்றும் தொழிலின் தன்மை போன்ற காரணிகளை அடிப்படையாகக் கொண்டு குறைந்தபட்ச ஊதியத்தை அரசு நிர்ணயிக்கும் விதமாக பணியாளர்களுக்கு கொடுக்க வேண்டும் என்று சொல்கிறது.",
         "Minimum Wages Act, 1948", 
         "The Minimum Wages Act, 1948, ensures that workers in certain sectors receive wages that are at least equal to the minimum wage set by the government.",
         "Minimum Wages Act, 1948, உத்தியோகப்பணியாளர்களுக்கு அரசு நிர்ணயித்த குறைந்தபட்ச ஊதியத்தைப் பெறுவதற்கான பாதுகாப்பை வழங்குகிறது."
        ),
        ("What is the Maternity Benefit Act in India?", 
         "The Maternity Benefit Act, 1961 provides paid leave and other benefits to female employees for pregnancy, childbirth, and post-natal care, ensuring job security during this period.",
         "Maternity Benefit Act, 1961 கர்ப்பம், குழந்தை பிறப்பு மற்றும் பிறப்புக்குப் பிந்தைய பராமரிப்பு ஆகியவற்றிற்கு பெண்கள் ஊழியர்களுக்கு சம்பளத்துடன் விடுமுறை மற்றும் பிற நன்மைகளை வழங்குகிறது.",
         "Maternity Benefit Act, 1961", 
         "The Maternity Benefit Act, 1961, mandates that women are entitled to maternity leave for up to 26 weeks, including provisions for health benefits and job protection.",
         "Maternity Benefit Act, 1961, பெண்களுக்கு 26 வாரங்கள் வரை விடுமுறை மற்றும் உடல் நலத்தின் பாதுகாப்பையும் வேலை பாதுகாப்பையும் வழங்குகிறது."
        ),
        ("What is the Industrial Disputes Act in India?", 
         "The Industrial Disputes Act, 1947 regulates the investigation and settlement of industrial disputes between employers and employees to ensure fair labor practices and maintain industrial peace.",
         "Industrial Disputes Act, 1947, வேலைதாரர்கள் மற்றும் பணியாளர்களுக்கு இடையிலான தொழிற்சங்க சண்டைகளை சீர்செய்யும் மற்றும் முறைப்படுத்துகிறது.",
         "Industrial Disputes Act, 1947", 
         "The Industrial Disputes Act, 1947, establishes mechanisms for the resolution of disputes, such as conciliation and arbitration, and prevents unfair labor practices.",
         "Industrial Disputes Act, 1947, தொழிற்சங்க சண்டைகளை சீராக முடிக்க மற்றும் பணியாளர்களின் உரிமைகளை பாதுகாக்க வாய்ப்பு அளிக்கிறது."
        ),
        ("What is the Payment of Gratuity Act?", 
         "The Payment of Gratuity Act, 1972 requires employers to provide a lump sum payment to employees who have completed at least five years of continuous service, upon retirement, resignation, or death.",
         "Payment of Gratuity Act, 1972, ஐந்தாண்டு பணியில் தொடர்ச்சியாக வேலை செய்து வந்தவர்களுக்கு ஓய்வு, ராஜினாமா அல்லது இறப்பின் போது ஒரு தொகையாக பணம் வழங்க வேண்டும் என்று வேலைதாரர்கள் கண்டிப்பாக வழங்க வேண்டும் என்று சொல்கிறது.",
         "Payment of Gratuity Act, 1972", 
         "The Payment of Gratuity Act, 1972, ensures that workers who have served for five years or more are entitled to gratuity as a form of retirement benefit.",
         "Payment of Gratuity Act, 1972, பணியாளர்கள் குறைந்தது ஐந்தாண்டுகள் தொடர்ந்து பணியாற்றிய பின்னர் ஓய்வுநிதியாக Gratuity பெற தகுதியானவர்களாக இருப்பார்கள்."
        ),
        ("What are the provisions under the Employees' Provident Fund (EPF) Act?", 
         "The EPF Act, 1952 mandates contributions from both employer and employee towards a provident fund, which acts as a retirement savings plan for employees in certain sectors.",
         "EPF Act, 1952, வேலைதாரர்கள் மற்றும் பணியாளர்களுக்கு ஓய்வுக்குப் பிந்தைய நிதி திட்டமாக செயல்படும் கொடுப்பனவுகளை வழங்குகிறது.",
         "Employees' Provident Fund (EPF) Act, 1952", 
         "The EPF Act, 1952, governs the management of provident funds for workers, ensuring long-term financial security for employees by compulsory contributions from both employer and employee.",
         "EPF Act, 1952, வேலைதாரர்கள் மற்றும் பணியாளர்களின் நீண்டகால நிதி பாதுகாப்பை உறுதிப்படுத்தும் விதமாக Provident Fund ஆகும் நிதியை உருவாக்குகிறது."
        ),
        ("What is the Equal Remuneration Act, 1976?", 
         "The Equal Remuneration Act, 1976 ensures that men and women workers receive equal pay for the same work, preventing gender-based wage discrimination in employment.",
         "சமச்சீர் சம்பளச் சட்டம், 1976, ஒரே வேலைக்கு ஆண்களும் பெண்களும் சமமாக சம்பளம் பெற வேண்டும் என்று கூறுகிறது மற்றும் பாலின அடிப்படையிலான ஊதியப் பாகுபாட்டைத் தடுக்கும்.",
         "Equal Remuneration Act, 1976", 
         "The Equal Remuneration Act, 1976, mandates that employers pay equal wages to male and female workers for the same or similar work and prohibits discrimination in recruitment.",
         "Equal Remuneration Act, 1976, ஒரே வேலைக்கு ஆண்களுக்கும் பெண்களுக்கும் சமமான சம்பளத்தை வழங்க வேண்டும் என்று கூறுகிறது மற்றும் ஆட்களை நிரப்புவதில் பாகுபாடு இல்லாமல் இருக்க வேண்டும்."
        ),
        ("What are the provisions under the Workmen’s Compensation Act?", 
         "The Workmen’s Compensation Act, 1923 requires employers to compensate workers who suffer injuries or death while performing their duties, offering financial protection to the employees and their families.",
         "Workmen’s Compensation Act, 1923, பணியாளர்கள் அவர்கள் தங்களது கடமைகளைச் செய்யும் போது ஏற்பட்ட காயம் அல்லது மரணத்திற்கு வேலைதாரர்கள் தகுந்த பரிசீலனை வழங்க வேண்டும் என்று கூறுகிறது.",
         "Workmen’s Compensation Act, 1923", 
         "The Workmen’s Compensation Act, 1923, provides compensation to employees or their dependents in the event of injury, disability, or death caused by workplace accidents.",
         "Workmen’s Compensation Act, 1923, பணியாளர்கள் அல்லது அவர்களது உறவினர்களுக்கு தொழில் விபத்தால் காயம், ஊனமுற்றல் அல்லது மரணத்தின் போது பரிசீலனை வழங்குகிறது."
        ),
        ("What is the Employees' State Insurance (ESI) Act?", 
         "The ESI Act, 1948 provides health insurance and social security benefits to workers in case of sickness, maternity, disability, or death due to employment-related injuries.",
         "ESI Act, 1948, பணியாளர்களுக்கு உடல்நல காப்பீடு மற்றும் சமூகப் பாதுகாப்பு நன்மைகளை வழங்குகிறது, குறிப்பாக நோய்வாய்ப்பு, கர்ப்பம் அல்லது வேலை தொடர்பான காயங்களுக்கு உகந்தது.",
         "Employees' State Insurance (ESI) Act, 1948", 
         "The ESI Act, 1948, mandates that employees contribute towards a fund that provides medical and financial benefits to workers in case of illness, maternity, or injury.",
         "Employees' State Insurance (ESI) Act, 1948, பணியாளர்கள் ஒரு நிதிக்கு பங்களிக்க வேண்டும் என்று கூறுகிறது, நோய், கர்ப்பம் அல்லது காயத்திற்கு மருத்துவ மற்றும் நிதி நன்மைகளை வழங்குகிறது."
        ),
        ("What is the Bonded Labour System (Abolition) Act?", 
         "The Bonded Labour System (Abolition) Act, 1976 abolishes all forms of bonded labor, making it illegal for anyone to force individuals to work to repay a debt or obligation.",
         "Bonded Labour System (Abolition) Act, 1976, அனைத்து விதமான அடிமைப் பணி முறைகளையும் தடைசெய்கிறது, நபர்களை கடனை அல்லது கடமையை அடைக்கக் கட்டாயமாக வேலை செய்ய வைப்பதை சட்டவிரோதமாக்குகிறது.",
         "Bonded Labour System (Abolition) Act, 1976", 
         "The Bonded Labour System (Abolition) Act, 1976, makes it a crime to compel any person to work in a bonded labor situation, thereby freeing people from exploitative labor practices.",
         "Bonded Labour System (Abolition) Act, 1976, மனிதர்களை அடிமைப்பணியில் ஈடுபடுத்துவது சட்டவிரோதம் என்பதை உறுதி செய்கிறது."
        ),
        ("What are the provisions under the Child Labour (Prohibition and Regulation) Act?", 
         "The Child Labour (Prohibition and Regulation) Act, 1986 prohibits the employment of children below 14 years in certain occupations and regulates the working conditions of children in other sectors.",
         "Child Labour (Prohibition and Regulation) Act, 1986, சில தொழில்களில் 14 வயதிற்குக் குறைந்தவயதுள்ள குழந்தைகளை வேலைக்குச் சேர்ப்பதை தடைசெய்கிறது மற்றும் பிற துறைகளில் பணியாளர் நிபந்தனைகளை ஒழுங்குபடுத்துகிறது.",
         "Child Labour (Prohibition and Regulation) Act, 1986", 
         "The Child Labour Act, 1986, prohibits the employment of children under 14 in hazardous industries and regulates their work hours and conditions in non-hazardous sectors.",
         "Child Labour (Prohibition and Regulation) Act, 1986, ஆபத்தான தொழில்களில் 14 வயதிற்குக் குறைவான குழந்தைகளை வேலை செய்வதைத் தடுக்கும் விதமாகச் செயல்படுகிறது."
        )
    ],
    "Environmental Law": [
        ("What is the purpose of the Environment Protection Act, 1986?", 
         "The Environment Protection Act, 1986 provides a framework for the protection and improvement of the environment and aims to prevent environmental pollution.",
         "சுற்றுச்சூழல் பாதுகாப்பு சட்டம், 1986 சுற்றுச்சூழலைப் பாதுகாக்கவும், மேம்படுத்தவும் ஒரு சட்டமூலம் அமைக்கிறது மற்றும் சுற்றுச்சூழல் மாசுக்களைத் தடுப்பதற்கான நடவடிக்கைகளைத் தெரிவிக்கிறது.",
         "Environment Protection Act, 1986", 
         "The Environment Protection Act, 1986 empowers the government to take necessary actions to protect the environment and control pollution.",
         "Environment Protection Act, 1986, அரசுக்கு சுற்றுச்சூழலைக் காக்கவும், மாசுக்களை கட்டுப்படுத்தவும் தேவையான நடவடிக்கைகளை எடுக்க அதிகாரம் அளிக்கிறது."
        ),
        ("What is the Water (Prevention and Control of Pollution) Act?", 
         "The Water (Prevention and Control of Pollution) Act, 1974 aims to prevent and control water pollution by establishing Pollution Control Boards at the state and central levels.",
         "நீர் (மாசுபடுத்தலைத் தடுக்கும் மற்றும் கட்டுப்படுத்தும்) சட்டம், 1974, மாநில மற்றும் மத்திய அளவில் மாசுபாடு கட்டுப்பாட்டு வாரியங்களை நிறுவுவதன் மூலம் நீர் மாசுபாட்டைத் தடுக்கவும், கட்டுப்படுத்தவும் நோக்கமாகக் கொண்டுள்ளது.",
         "Water (Prevention and Control of Pollution) Act, 1974", 
         "The Water (Prevention and Control of Pollution) Act, 1974, regulates and monitors pollution in water bodies to ensure clean and safe water for public consumption.",
         "Water (Prevention and Control of Pollution) Act, 1974, நீர்நிலைகளில் மாசுபாட்டை ஒழுங்குபடுத்துகிறது மற்றும் பொது பயன்பாட்டிற்கு தூய்மையான நீரை உறுதிப்படுத்துகிறது."
        ),
        ("What are the objectives of the Air (Prevention and Control of Pollution) Act, 1981?", 
         "The Air (Prevention and Control of Pollution) Act, 1981 aims to prevent, control, and reduce air pollution in India by regulating emissions from industries and vehicles.",
         "காற்று (மாசுபடுத்தலைத் தடுக்கும் மற்றும் கட்டுப்படுத்தும்) சட்டம், 1981, தொழில்கள் மற்றும் வாகனங்களில் இருந்து வெளிவரும் புகையை ஒழுங்குபடுத்துவதன் மூலம் காற்று மாசுக்களைத் தடுப்பதையும் கட்டுப்படுத்துவதையும் நோக்கமாகக் கொண்டுள்ளது.",
         "Air (Prevention and Control of Pollution) Act, 1981", 
         "The Air (Prevention and Control of Pollution) Act, 1981, provides for the establishment of Pollution Control Boards and empowers them to regulate air pollution sources.",
         "Air (Prevention and Control of Pollution) Act, 1981, மாசுப்பாட்டு வாரியங்களை நிறுவுகிறது மற்றும் காற்று மாசுக்கான மூலம் மதிப்பீடு மற்றும் ஒழுங்குபடுத்துதலை அதிகாரம் அளிக்கிறது."
        ),
        ("What is the role of the National Green Tribunal (NGT)?", 
         "The National Green Tribunal (NGT) was established under the National Green Tribunal Act, 2010, to handle cases related to environmental protection and conservation of forests and natural resources.",
         "தேசிய பசுமை நீதிமன்றம் (NGT) பசுமை நீதிமன்ற சட்டம், 2010 இன் கீழ் அமைக்கப்பட்டது, சுற்றுச்சூழல் பாதுகாப்பு மற்றும் காடுகள் மற்றும் இயற்கை வளங்களைப் பாதுகாப்பதற்கான வழக்குகளை நியாயப்படுத்துகிறது.",
         "National Green Tribunal Act, 2010", 
         "The National Green Tribunal (NGT) provides for the quick disposal of cases related to environmental protection and issues binding decisions on matters of environment and conservation.",
         "National Green Tribunal Act, 2010, சுற்றுச்சூழல் பாதுகாப்பு தொடர்பான வழக்குகளின் விரைவான தீர்மானத்தை வழங்குகிறது மற்றும் சுற்றுச்சூழல் சார்ந்த முடிவுகளை கட்டாயமாக்குகிறது."
        ),
        ("What is the Wildlife Protection Act, 1972?", 
         "The Wildlife Protection Act, 1972 provides for the protection of wild animals, birds, and plants to ensure ecological and environmental security in India.",
         "விலங்கியல் பாதுகாப்பு சட்டம், 1972, காட்டுமிருகங்கள், பறவைகள் மற்றும் தாவரங்களை பாதுகாக்கவும், இந்தியாவின் பசுமை மற்றும் சுற்றுச்சூழல் பாதுகாப்பை உறுதிப்படுத்தவும் ஒரு சட்டமாக உள்ளது.",
         "Wildlife Protection Act, 1972", 
         "The Wildlife Protection Act, 1972, establishes a legal framework for protecting endangered species and regulates hunting, poaching, and trade of wildlife.",
         "Wildlife Protection Act, 1972, ஆபத்துக்குள்ளான விலங்குகளைப் பாதுகாக்கும் சட்டவிழுக்கை உருவாக்குகிறது மற்றும் விலங்குகளை வேட்டையாடுதல், கொன்றல் மற்றும் வணிகம் செய்வதை கட்டுப்படுத்துகிறது."
        ),
        ("What is the Forest Conservation Act?", 
         "The Forest Conservation Act, 1980 aims to preserve forests and restrict the use of forest land for non-forest purposes, ensuring sustainable forest management.",
         "காடு பாதுகாப்பு சட்டம், 1980, காடுகளைப் பாதுகாக்கவும் மற்றும் காடற்ற பணிகளுக்கான காடுகளை உபயோகப்படுத்துவதைத் தடுக்கவும் ஒரு சட்டமாக உள்ளது.",
         "Forest Conservation Act, 1980", 
         "The Forest Conservation Act, 1980, restricts deforestation and ensures that forest land is diverted only for activities beneficial to the environment and sustainable development.",
         "Forest Conservation Act, 1980, காடுகளின் வளர்ச்சியை கட்டுப்படுத்துகிறது மற்றும் சுற்றுச்சூழலுக்கு உகந்த நடவடிக்கைகளுக்கே காடுகளை மாற்ற பயன்படுத்த அனுமதிக்கிறது."
        ),
        ("What is the Public Liability Insurance Act?", 
         "The Public Liability Insurance Act, 1991 mandates that industries dealing with hazardous substances provide compensation to victims of accidents caused by their activities.",
         "பொது பொறுப்பு காப்பீடு சட்டம், 1991, ஆபத்தான பொருட்களுடன் தொடர்புடைய தொழில்களால் ஏற்படும் விபத்துகளில் பாதிக்கப்பட்டவர்களுக்கு ஊதியம் வழங்க வேண்டும் என்று கூறுகிறது.",
         "Public Liability Insurance Act, 1991", 
         "The Public Liability Insurance Act, 1991, ensures that industries handling hazardous materials are required to maintain insurance policies that cover public liabilities in the event of accidents.",
         "Public Liability Insurance Act, 1991, ஆபத்தான பொருட்களை கையாளும் தொழில்களால் ஏற்படும் விபத்து போது பொது பொறுப்பு உடனடி நிவாரணத்தை வழங்குவதற்காக காப்பீட்டை நிர்ணயமாக்குகிறது."
        ),
        ("What is the role of the Biodiversity Act, 2002?", 
         "The Biodiversity Act, 2002 promotes the conservation of biological diversity and the sustainable use of its components, while also addressing fair and equitable sharing of the benefits arising out of the utilization of genetic resources.",
         "உயிர்வேதியியல் சட்டம், 2002, உயிர்வாழும் தாவரங்கள் மற்றும் விலங்குகளின் தத்துலியல் பாதுகாப்பை மேம்படுத்துகிறது மற்றும் ஜீவராசிகள் வளங்களின் நன்மைகளின் சீரான பங்கீட்டை உறுதிப்படுத்துகிறது.",
         "Biodiversity Act, 2002", 
         "The Biodiversity Act, 2002, provides a legal framework to protect and conserve biological resources while promoting the sustainable use of biodiversity and ensuring benefit-sharing.",
         "Biodiversity Act, 2002, உயிர்வாழும் வளங்களைப் பாதுகாக்கும் ஒரு சட்டவிழுக்கை உருவாக்குகிறது மற்றும் தத்துலிய வளங்களை பாதுகாக்கவும், பயன்படுத்தவும், சமமாக பங்கீடு செய்யவும் சட்டமாக்குகிறது."
        ),
        ("What is the Hazardous Waste Management Rules?", 
         "The Hazardous Waste (Management and Handling) Rules, 1989 outline the management, transportation, and disposal of hazardous wastes to minimize risks to health and the environment.",
         "ஆபத்தான கழிவுகளின் (மேலாண்மை மற்றும் கையாளுதல்) விதிகள், 1989, ஆபத்தான கழிவுகளின் மேலாண்மை, போக்குவரத்து மற்றும் அகற்றத்தை கையாளுவதற்கான விதிகளைச் சொல்கிறது.",
         "Hazardous Waste (Management and Handling) Rules, 1989", 
         "The Hazardous Waste (Management and Handling) Rules, 1989, regulate the storage, transportation, and disposal of hazardous wastes to ensure safe handling and minimize environmental risks.",
         "Hazardous Waste (Management and Handling) Rules, 1989, ஆபத்தான கழிவுகளின் பாதுகாப்பான கையாளுதல் மற்றும் சுற்றுச்சூழலுக்கு வரும் ஆபத்துகளைத் தடுப்பதற்கான விதிகளை வெளியிடுகிறது."
        ),
        ("What is the National Water Policy?", 
         "The National Water Policy aims to manage water resources in a sustainable manner, ensuring equitable distribution and conservation of water for various uses including agriculture, drinking water, and industrial use.",
         "தேசிய நீர் கொள்கை நீர்வளங்களை நிலைத்திருக்கும் முறையில் நிர்வகிக்கவும், விவசாயம், குடிநீர் மற்றும் தொழில்துறைகளுக்கான நீரின் சமமான விநியோகத்தை உறுதிப்படுத்தவும் நோக்கமாகக் கொண்டுள்ளது.",
         "National Water Policy, 2012", 
         "The National Water Policy, 2012, emphasizes integrated water resource management, the need for water conservation, and the efficient use of water resources across sectors.",
         "National Water Policy, 2012, நீர்வள மேலாண்மையை ஒருங்கிணைக்கும் முறையை மற்றும் நீரைச் சேமிக்கவும், மற்றும் நீர்வளங்களின் பயன்பாட்டை எல்லா துறைகளிலும் திறமையாக செயல்படுத்துவதற்கான உத்திவாதத்தை வெளிப்படுத்துகிறது."
        )
    ],
    "Cyber Law": [
        ("What is the purpose of the Information Technology Act, 2000?", 
         "The Information Technology Act, 2000 provides a legal framework to address issues related to cybercrime, electronic commerce, and electronic governance.",
         "தகவல் தொழில்நுட்ப சட்டம், 2000, சைபர் குற்றங்கள், மின்னணு வர்த்தகம் மற்றும் மின்னணு ஆட்சி தொடர்பான பிரச்சினைகளைத் தீர்ப்பதற்கான சட்ட அடிப்படையைக் கொடுக்கிறது.",
         "Information Technology Act, 2000", 
         "The Information Technology Act, 2000 establishes rules for electronic transactions and legal recognition of digital signatures, along with penalties for cybercrimes.",
         "Information Technology Act, 2000, மின்னணு பரிவர்த்தனைகளுக்கான விதிகளை உருவாக்குகிறது மற்றும் டிஜிட்டல் கையொப்பங்களுக்கு சட்ட அங்கீகாரம் அளிக்கிறது, மற்றும் சைபர் குற்றங்களுக்கு தண்டனைகளை வழங்குகிறது."
        ),
        ("What constitutes hacking under Indian cyber law?", 
         "Hacking under Indian cyber law refers to unauthorized access to computer systems or networks with the intent to steal, corrupt, or destroy data.",
         "இந்திய சைபர் சட்டத்தின் கீழ் ஹாக்கிங் என்பது கணினி அமைப்புகளில் அல்லது நெட்வொர்க்களில் அனுமதியற்ற அணுகல், அதன் மூலம் தரவைத் திருடுவதற்கும் அழிப்பதற்கும் எடுத்துகொள்ளப்படும் நடவடிக்கை ஆகும்.",
         "Section 66 of the IT Act, 2000", 
         "Section 66 of the IT Act, 2000 defines hacking and prescribes penalties for those who hack into computer systems without authorization.",
         "IT Act, 2000 இன் பிரிவு 66, ஹாக்கிங் குறித்த விவரங்களை வழங்குகிறது மற்றும் கணினி அமைப்புகளில் அனுமதியின்றி நுழையும் நபர்களுக்கான தண்டனைகளை நிர்ணயிக்கிறது."
        ),
        ("What are the penalties for identity theft under Indian cyber law?", 
         "Identity theft under Indian cyber law is punishable with imprisonment up to 3 years and a fine under the IT Act.",
         "இந்திய சைபர் சட்டத்தின் கீழ் அடையாள திருட்டிற்கு 3 ஆண்டுகள் வரை சிறைத் தண்டனையும், அபராதமும் விதிக்கப்படும்.",
         "Section 66C of the IT Act, 2000", 
         "Section 66C of the IT Act, 2000, prescribes penalties for identity theft, which involves the use of someone’s personal information without authorization.",
         "IT Act, 2000 இன் பிரிவு 66C, அடையாளத் திருட்டிற்கு விதிக்கப்பட்ட தண்டனையை விவரிக்கிறது, இது அனுமதியின்றி ஒருவரின் தனிப்பட்ட தகவலை பயன்படுத்துவதைக் குறிக்கிறது."
        ),
        ("What is phishing under Indian law, and how is it punishable?", 
         "Phishing involves deceiving individuals into providing sensitive information like passwords and banking details. It is punishable under Indian law with fines and imprisonment.",
         "Phishing என்பது கடவுச்சொற்கள் மற்றும் வங்கித் தகவல்களைப் பெற நபர்களை ஏமாற்றுவது ஆகும். இது இந்திய சட்டத்தின் கீழ் அபராதங்கள் மற்றும் சிறைத் தண்டனையை உடையதாக உள்ளது.",
         "Section 66D of the IT Act, 2000", 
         "Section 66D of the IT Act, 2000, defines phishing as cheating by impersonation and prescribes penalties for such cyber fraud.",
         "IT Act, 2000 இன் பிரிவு 66D, Phishing (மறைமுகமாக ஏமாற்றுதல்) குறித்து விவரிக்கிறது மற்றும் சைபர் மோசடிகளுக்கு விதிக்கப்படும் தண்டனைகளை நிர்ணயிக்கிறது."
        ),
        ("How does Indian law protect data privacy?", 
         "Indian law protects data privacy through the Information Technology Act and rules that regulate the collection, storage, and sharing of personal data.",
         "இந்திய சட்டம் தகவல் தொழில்நுட்ப சட்டத்தின் கீழ் தனிநபர் தரவுகளைப் பாதுகாக்கும் விதிகளின் மூலம் தரவுகள் சேகரிப்பு, சேமிப்பு மற்றும் பகிர்வு செயல்களை ஒழுங்குபடுத்துகிறது.",
         "Section 43A of the IT Act, 2000", 
         "Section 43A of the IT Act, 2000 requires companies handling sensitive personal data to implement reasonable security practices and provides for compensation in case of data breaches.",
         "IT Act, 2000 இன் பிரிவு 43A, நுகர்வோர் தனிப்பட்ட தகவல்களை கையாளும் நிறுவனங்களுக்கு தரவுகளை பாதுகாக்குமாறு கட்டாயமாக்குகிறது மற்றும் தரவுகள் கசியும் போது இழப்பீடு வழங்க வேண்டும் என உத்தரவிடுகிறது."
        ),
        ("What are the legal provisions for cyberstalking in India?", 
         "Cyberstalking in India involves harassing someone using the internet, social media, or electronic communication. It is a punishable offense under Indian cyber law.",
         "இந்தியாவில் சைபர் ஸ்டாக்கிங் என்பது இணையம், சமூக ஊடகம் அல்லது மின்னணு தொடர்புகொள்வதன் மூலம் ஒருவரைத் துன்புறுத்துவது ஆகும். இது தண்டனையை உடைய குற்றமாக உள்ளது.",
         "Section 354D of the Indian Penal Code", 
         "Section 354D of the Indian Penal Code deals with cyberstalking and prescribes penalties for the harassment of individuals through online mediums.",
         "இந்திய தண்டனைச் சட்டம், பிரிவு 354D, சைபர் ஸ்டாக்கிங்குடன் தொடர்புடையதாக உள்ளது மற்றும் ஆன்லைன் வழியாக ஒருவரை துன்புறுத்துவதற்கான தண்டனைகளை வழங்குகிறது."
        ),
        ("What is the legal validity of digital signatures in India?", 
         "Digital signatures in India are legally valid under the Information Technology Act, 2000, and can be used to authenticate electronic documents.",
         "இந்தியாவில் டிஜிட்டல் கையொப்பங்கள் தகவல் தொழில்நுட்ப சட்டம், 2000 இன் கீழ் சட்டப்படி செல்லுபடியாகும் மற்றும் மின்னணு ஆவணங்களை சரிபார்க்க பயன்படுத்தலாம்.",
         "Section 5 of the IT Act, 2000", 
         "Section 5 of the IT Act, 2000 grants legal recognition to digital signatures for authenticating electronic records and contracts.",
         "IT Act, 2000 இன் பிரிவு 5, மின்னணு பதிவுகள் மற்றும் ஒப்பந்தங்களை சரிபார்ப்பதற்காக டிஜிட்டல் கையொப்பங்களுக்கு சட்ட அங்கீகாரம் வழங்குகிறது."
        ),
        ("What is Section 69 of the IT Act, 2000, and how does it regulate surveillance?", 
         "Section 69 of the IT Act allows the government to monitor and intercept communications in the interest of national security, public order, or to prevent crimes.",
         "IT Act, 2000 இன் பிரிவு 69, தேசிய பாதுகாப்பு, பொது ஒழுங்கு அல்லது குற்றங்களைத் தடுப்பதற்காக அரசாங்கத்திற்கு தொடர்புகளை கண்காணிக்கும் மற்றும் தடுத்து நிறுத்துவதற்கான அதிகாரத்தை வழங்குகிறது.",
         "Section 69 of the IT Act, 2000", 
         "Section 69 of the IT Act, 2000, empowers authorities to issue directions for interception or monitoring of information for reasons of sovereignty, integrity, or defense of India.",
         "IT Act, 2000 இன் பிரிவு 69, இந்தியாவின் இறையாண்மை, अखண்டता அல்லது பாதுகாப்பை நிமித்தம் தகவல்களை தடுத்தல் மற்றும் கண்காணிப்பதற்கான உத்தரவுகளை அதிகாரிகளுக்கு வழங்குகிறது."
        ),
        ("How does Indian law address online defamation?", 
         "Online defamation in India refers to the act of publishing defamatory content over the internet. It is punishable under both the IT Act and the Indian Penal Code.",
         "இந்தியாவில் ஆன்லைன் அவதூறு என்பது இணையத்தின் மூலம் அவதூறான உள்ளடக்கத்தை வெளியிடுதல் ஆகும். இது தகவல் தொழில்நுட்ப சட்டத்தின் கீழ் மற்றும் இந்திய தண்டனைச் சட்டத்தின் கீழ் தண்டனையை உடையதாக உள்ளது.",
         "Section 66A of the IT Act, 2000", 
         "Section 66A of the IT Act, 2000 deals with online defamation, prescribing penalties for the circulation of defamatory messages and content via electronic communication.",
         "IT Act, 2000 இன் பிரிவு 66A, மின்னணு தொடர்புகளின் வழியாக அவதூறான செய்திகளையும் உள்ளடக்கத்தையும் பரப்பியதற்கான தண்டனைகளை வழங்குகிறது."
        )
    ],
    "Taxation Law": [
        ("What are the types of taxes in India?", 
         "The taxes in India are broadly classified into two categories: Direct Taxes (like Income Tax) and Indirect Taxes (like GST).",
         "இந்தியாவில் வரிகள் பொதுவாக இரண்டு பிரிவுகளாக வகைப்படுத்தப்படுகின்றன: நேரடி வரிகள் (உதாரணமாக வருமான வரி) மற்றும் மறைமுக வரிகள் (உதாரணமாக GST).",
         "Article 265 of the Indian Constitution", 
         "Article 265 of the Indian Constitution states that no tax shall be levied or collected except by the authority of law.",
         "Article 265 இந்திய அரசியலமைப்பின் படி, சட்டத்தின் ஆணையின்றி எவ்வித வரிகளும் விதிக்கப்படக்கூடாது அல்லது வசூலிக்கப்படக்கூடாது என்று கூறுகிறது."
        ),
        ("What is the procedure for filing Income Tax returns in India?", 
         "In India, income tax returns can be filed online using the Income Tax Department’s e-filing portal by providing the necessary financial details and documents.",
         "இந்தியாவில், வருமான வரி அறிக்கைகள், வருமான வரித்துறையின் இ-பதிவு தளத்தின் மூலம் இணையத்தில் தாக்கல் செய்ய முடியும், தேவையான நிதி விவரங்கள் மற்றும் ஆவணங்களை வழங்கி.",
         "Income Tax Act, 1961", 
         "The Income Tax Act, 1961, provides the framework for the filing of income tax returns and lays down the process and timelines for filing.",
         "Income Tax Act, 1961, வருமான வரி அறிக்கைகளை தாக்கல் செய்வதற்கான கட்டமைப்பை வழங்குகிறது மற்றும் தாக்கல் செய்வதற்கான நடைமுறைகள் மற்றும் காலக்கெடுகளை நிர்ணயிக்கிறது."
        ),
        ("What is the Goods and Services Tax (GST) in India?", 
         "The Goods and Services Tax (GST) is a comprehensive indirect tax levied on the supply of goods and services across India, replacing multiple indirect taxes like VAT, excise duty, and service tax.",
         "விளைபொருட்கள் மற்றும் சேவைகளுக்கான வரி (GST) என்பது இந்தியாவிலுள்ள சரக்கு மற்றும் சேவைகளின் வழங்குதலுக்கு விதிக்கப்படும் ஒரு முழுமையான மறைமுக வரியாகும், இது பல மறைமுக வரிகளை மாற்றுகிறது.",
         "GST Act, 2017", 
         "The GST Act, 2017, consolidates various indirect taxes into a single tax system, simplifying the taxation process in India.",
         "GST Act, 2017, பல மறைமுக வரிகளை ஒரே வரி அமைப்பாக மாற்றுகிறது, இந்தியாவில் வரி விதிப்பு செயல்முறையை எளிதாக்குகிறது."
        ),
        ("What are the penalties for tax evasion in India?", 
         "Tax evasion in India can lead to penalties including fines, interest on unpaid tax, and imprisonment depending on the severity of the offense.",
         "இந்தியாவில் வரி ஏய்ப்பு செய்தால், அபராதங்கள், செலுத்தப்படாத வரிக்கு வட்டி மற்றும் குற்றத்தின் தீவிரத்தைப் பொறுத்து சிறைத் தண்டனை ஆகியவை விதிக்கப்படலாம்.",
         "Section 276C of the Income Tax Act, 1961", 
         "Section 276C of the Income Tax Act, 1961, prescribes penalties and imprisonment for willful tax evasion.",
         "Income Tax Act, 1961 இன் பிரிவு 276C, ஜாக்கிரதையாக வரி ஏய்ப்பு செய்வதற்கான தண்டனைகள் மற்றும் சிறைத் தண்டனையை வழங்குகிறது."
        ),
        ("How is capital gains tax calculated in India?", 
         "Capital gains tax in India is calculated on the profit earned from the sale of a capital asset, and the tax rate depends on whether the asset is long-term or short-term.",
         "இந்தியாவில் மூலதன ஆதாய வரி என்பது ஒரு மூலதன சொத்தை விற்பனையிலிருந்து பெறப்படும் இலாபத்தின் அடிப்படையில் கணக்கிடப்படுகிறது, மற்றும் வரி விகிதம் சொத்து நீண்ட காலமாக அல்லது குறுகிய காலமாக இருக்கிறதா என்பதில் அடிப்படையாகும்.",
         "Sections 45-55 of the Income Tax Act, 1961", 
         "Sections 45-55 of the Income Tax Act, 1961, provide the rules for calculating capital gains tax on the sale of capital assets.",
         "Income Tax Act, 1961 இன் பிரிவு 45-55, மூலதன சொத்துகளை விற்பனை செய்வதற்கான மூலதன ஆதாய வரியை கணக்கிடுவதற்கான விதிகளை வழங்குகிறது."
        ),
        ("What is the difference between TDS and TCS?", 
         "TDS (Tax Deducted at Source) is deducted by the payer before making payments, while TCS (Tax Collected at Source) is collected by the seller from the buyer.",
         "TDS (மூலத்தில் குறைக்கப்படும் வரி) என்பது பணம் செலுத்துவதற்கு முன்பு பணம் செலுத்துநர் பிடித்துக் கொள்வது, மற்றும் TCS (மூலத்தில் வசூலிக்கப்படும் வரி) என்பது விற்பனையாளர் வாங்கியவரிடமிருந்து வரியைச் சேகரிப்பது.",
         "Sections 192-206 of the Income Tax Act, 1961", 
         "Sections 192-206 of the Income Tax Act, 1961, outline the provisions for TDS and TCS and their applicability to different types of income.",
         "Income Tax Act, 1961 இன் பிரிவு 192-206, TDS மற்றும் TCS க்கான விதிகளை மற்றும் அவற்றின் பல்வேறு வகையான வருமானங்களுக்கு விதிக்கப்படுதலை விளக்குகிறது."
        ),
        ("What is the purpose of tax audits in India?", 
         "A tax audit in India ensures that the taxpayer has accurately reported income and deductions. It is mandatory for businesses and professionals whose turnover exceeds prescribed limits.",
         "இந்தியாவில் ஒரு வரி ஆடிட்டின் நோக்கம், வரியாளர்கள் வருமானம் மற்றும் கழிவுகளை சரியாக அறிவித்துள்ளனரா என்பதைக் கண்டு பிடிக்கிறது. இது குறிப்பிடப்பட்ட வரம்புகளை மிஞ்சும் வருவாய் கொண்ட தொழில்களுக்கும், நிபுணர்களுக்கும் கட்டாயமாகும்.",
         "Section 44AB of the Income Tax Act, 1961", 
         "Section 44AB of the Income Tax Act, 1961, mandates tax audits for certain categories of taxpayers based on their income and turnover thresholds.",
         "Income Tax Act, 1961 இன் பிரிவு 44AB, வருமானம் மற்றும் வருவாய் வரம்புகளின் அடிப்படையில் குறிப்பிட்ட வரியாளர்களுக்கான வரி ஆடிட்களை கட்டாயமாக்குகிறது."
        ),
        ("What is the legal provision for GST registration?", 
         "GST registration is mandatory for businesses with annual turnover exceeding Rs. 40 lakhs in most states, and Rs. 20 lakhs for service providers.",
         "GST பதிவு, ஆண்டுக்கு ரூ. 40 லட்சத்தை மிஞ்சும் வருவாய் கொண்ட தொழில்களுக்கு, மற்றும் சேவை வழங்குநர்களுக்கு ரூ. 20 லட்சத்தை மிஞ்சும் வருவாய் கொண்டவர்களுக்கு கட்டாயமாகும்.",
         "Section 22 of the CGST Act, 2017", 
         "Section 22 of the CGST Act, 2017, outlines the eligibility criteria for GST registration based on the annual turnover of businesses and service providers.",
         "CGST Act, 2017 இன் பிரிவு 22, தொழில்கள் மற்றும் சேவை வழங்குநர்களின் ஆண்டு வருவாயின் அடிப்படையில் GST பதிவுக்கான தகுதிகளை விளக்குகிறது."
        ),
        ("What is the Anti-Profiteering Rule under GST law?", 
         "The Anti-Profiteering Rule under GST ensures that businesses pass on the benefit of tax reduction to consumers by reducing prices.",
         "GST சட்டத்தின் கீழ் லாபத்தைக் குறைக்கும் விதி, வரி குறைக்கப்பட்டால் விலைகளை குறைத்து வாடிக்கையாளர்களுக்கு அந்த நன்மையை வழங்கும் வழியை உறுதிப்படுத்துகிறது.",
         "Section 171 of the CGST Act, 2017", 
         "Section 171 of the CGST Act, 2017, empowers authorities to monitor whether the reduction in tax rates has been passed on to consumers.",
         "CGST Act, 2017 இன் பிரிவு 171, வரி விகிதங்களை குறைத்தால் அந்த நன்மையை வாடிக்கையாளர்களுக்கு அளித்துள்ளதா என கண்காணிக்க அதிகாரிகளுக்கு அதிகாரங்களை வழங்குகிறது."
        )
    ],
    "Consumer Protection Law": [
        ("What are the rights of consumers under the Consumer Protection Act?", 
         "Under the Consumer Protection Act, consumers have the right to be protected against unfair trade practices, the right to information, the right to choose, and the right to be heard, among others.",
         "நுகர்வோர் பாதுகாப்பு சட்டத்தின் கீழ், நுகர்வோருக்கு அநியாயமான வணிக நடைமுறைகளுக்கு எதிராக பாதுகாப்பு பெறும் உரிமை, தகவல்களை அறிந்து கொள்வது, தேர்வு செய்யும் உரிமை மற்றும் கருத்து கேட்கப்படுவது ஆகியவற்றின் உரிமைகள் உள்ளன.",
         "Section 2(9) of the Consumer Protection Act, 2019", 
         "Section 2(9) of the Consumer Protection Act, 2019, defines consumer rights, including protection against unfair trade practices and access to justice.",
         "Consumer Protection Act, 2019 இன் பிரிவு 2(9), அநியாயமான வணிக நடைமுறைகளுக்கு எதிரான பாதுகாப்பு உள்ளிட்ட நுகர்வோர் உரிமைகளை வரையறுக்கிறது."
        ),
        ("How can a consumer file a complaint under the Consumer Protection Act?", 
         "A consumer can file a complaint under the Consumer Protection Act by submitting a written complaint to the Consumer Disputes Redressal Commission, either online or in person.",
         "நுகர்வோர் பாதுகாப்பு சட்டத்தின் கீழ், ஒரு நுகர்வோர் எழுதப்பட்ட புகாரை நுகர்வோர் தகராறு தீர்வு ஆணையத்தில் ஆன்லைன் அல்லது நேரில் சமர்ப்பிக்க முடியும்.",
         "Section 35 of the Consumer Protection Act, 2019", 
         "Section 35 of the Consumer Protection Act, 2019, outlines the procedure for filing complaints regarding defective goods, deficient services, or unfair practices.",
         "Consumer Protection Act, 2019 இன் பிரிவு 35, குறைபாடுள்ள பொருட்கள், குறைபாடான சேவைகள் அல்லது அநியாயமான நடைமுறைகள் குறித்து புகார்களை தாக்கல் செய்யும் முறையை விளக்குகிறது."
        ),
        ("What is the concept of product liability under the Consumer Protection Act?", 
         "Product liability refers to the responsibility of manufacturers, sellers, and service providers for any harm caused by defective products or services.",
         "பொருள் பொறுப்பு என்பது குறைபாடுள்ள பொருட்கள் அல்லது சேவைகள் மூலம் ஏற்படும் சேதத்திற்கு உற்பத்தியாளர்கள், விற்பனையாளர்கள் மற்றும் சேவை வழங்குநர்கள் பொறுப்பை குறிக்கிறது.",
         "Chapter VI of the Consumer Protection Act, 2019", 
         "Chapter VI of the Consumer Protection Act, 2019, deals with product liability, holding manufacturers and sellers accountable for defective products.",
         "Consumer Protection Act, 2019 இன் VIஆம் அத்தியாயம் பொருள் பொறுப்பை பற்றியதாகும், குறைபாடுள்ள பொருட்களுக்கு உற்பத்தியாளர்கள் மற்றும் விற்பனையாளர்களை பொறுப்பாக வைத்திருக்கும்."
        ),
        ("What are misleading advertisements under Consumer Protection Law?", 
         "Misleading advertisements are those that falsely represent products or services, leading consumers to make uninformed decisions.",
         "தவறான விளம்பரங்கள் என்பது பொருட்கள் அல்லது சேவைகளை தவறாக பிரதிபலிக்கின்றன, இதனால் நுகர்வோர் தவறான முடிவுகளை எடுக்கின்றனர்.",
         "Section 2(28) of the Consumer Protection Act, 2019", 
         "Section 2(28) of the Consumer Protection Act, 2019, defines misleading advertisements and outlines the penalties for companies that engage in such practices.",
         "Consumer Protection Act, 2019 இன் பிரிவு 2(28), தவறான விளம்பரங்களை வரையறுக்கிறது மற்றும் அத்தகைய நடைமுறைகளை மேற்கொள்ளும் நிறுவனங்களுக்கு தண்டனைகளை விளக்குகிறது."
        ),
        ("What is the Consumer Disputes Redressal Commission?", 
         "The Consumer Disputes Redressal Commission is a three-tier quasi-judicial system that provides consumers with a mechanism to resolve disputes through District, State, and National Commissions.",
         "நுகர்வோர் தகராறு தீர்வு ஆணையம் என்பது மூன்று நிலை شبه நீதிமன்ற அமைப்பு ஆகும், இது மாவட்டம், மாநிலம் மற்றும் தேசிய ஆணையங்களின் மூலம் நுகர்வோர் தகராறுகளைத் தீர்க்க ஒரு முறைமை வழங்குகிறது.",
         "Chapter IV of the Consumer Protection Act, 2019", 
         "Chapter IV of the Consumer Protection Act, 2019, establishes the Consumer Disputes Redressal Commissions at the District, State, and National levels.",
         "Consumer Protection Act, 2019 இன் IVஆம் அத்தியாயம் மாவட்ட, மாநில, மற்றும் தேசிய அளவுகளில் நுகர்வோர் தகராறு தீர்வு ஆணையங்களை நிறுவுகிறது."
        ),
        ("What are the penalties for engaging in unfair trade practices?", 
         "Engaging in unfair trade practices can result in penalties including fines and imprisonment, depending on the nature and severity of the violation.",
         "அநியாயமான வணிக நடைமுறைகளில் ஈடுபடுதல் அபராதங்கள் மற்றும் சிறைத் தண்டனைகளை விளைவிக்கக்கூடும், மீறல் எந்த விதத்தில் இருக்கிறது என்பதைப் பொறுத்து.",
         "Section 89 of the Consumer Protection Act, 2019", 
         "Section 89 of the Consumer Protection Act, 2019, prescribes penalties for engaging in unfair trade practices, including fines and imprisonment.",
         "Consumer Protection Act, 2019 இன் பிரிவு 89, அநியாயமான வணிக நடைமுறைகளில் ஈடுபடுவதற்கான அபராதங்கள் மற்றும் சிறைத் தண்டனைகளை அளிக்கிறது."
        ),
        ("What is the definition of 'consumer' under Consumer Protection Law?", 
         "A consumer is any person who buys goods or services for personal use and not for resale or commercial purposes.",
         "ஒரு நுகர்வோர் என்பது தனிப்பட்ட பயன்பாட்டிற்காக பொருட்கள் அல்லது சேவைகளை வாங்கும் எந்தவொரு நபராகவும் வரையறுக்கப்படுகிறது, மறுவிற்பனை அல்லது வர்த்தக நோக்கத்திற்காக அல்ல.",
         "Section 2(7) of the Consumer Protection Act, 2019", 
         "Section 2(7) of the Consumer Protection Act, 2019, defines 'consumer' and specifies the rights and protections they are entitled to.",
         "Consumer Protection Act, 2019 இன் பிரிவு 2(7), 'நுகர்வோர்' என்பதைக் குறிக்கும் மற்றும் அவர்கள் பெறக்கூடிய உரிமைகள் மற்றும் பாதுகாப்புகளை வரையறுக்கிறது."
        ),
        ("What is the time limit for filing a consumer complaint?", 
         "A consumer complaint must be filed within two years from the date on which the cause of action arises.",
         "ஒரு நுகர்வோர் புகார், நடவடிக்கை எடுக்கும் காரணம் உருவாகிய தேதியிலிருந்து இரண்டு ஆண்டுகளுக்குள் தாக்கல் செய்யப்பட வேண்டும்.",
         "Section 69 of the Consumer Protection Act, 2019", 
         "Section 69 of the Consumer Protection Act, 2019, sets a two-year limitation period for filing consumer complaints from the date of the cause of action.",
         "Consumer Protection Act, 2019 இன் பிரிவு 69, நடவடிக்கையின் காரணமான தேதியிலிருந்து நுகர்வோர் புகார்களை தாக்கல் செய்யும் இரண்டு ஆண்டுகளுக்கான வரம்பை நிர்ணயிக்கிறது."
        ),
        ("What remedies are available to consumers for defective goods?", 
         "Consumers can seek remedies like repair, replacement, refund, or compensation for defective goods under the Consumer Protection Act.",
         "குறைபாடுள்ள பொருட்களுக்கு நுகர்வோர் பழுது செய்வது, மாற்றுவது, பணத்தைத் திருப்பி அளிப்பது அல்லது இழப்பீடு பெறுவது போன்ற தீர்வுகளை விரும்பலாம்.",
         "Section 38 of the Consumer Protection Act, 2019", 
         "Section 38 of the Consumer Protection Act, 2019, outlines the remedies available to consumers for defective goods or deficient services.",
         "Consumer Protection Act, 2019 இன் பிரிவு 38, குறைபாடுள்ள பொருட்கள் அல்லது குறைபாடான சேவைகளுக்கான நுகர்வோருக்கு கிடைக்கும் தீர்வுகளை விளக்குகிறது."
        ),
        ("What is the concept of 'deficiency in service' under Consumer Protection Law?", 
         "Deficiency in service refers to any shortfall or inadequacy in the quality, nature, or manner of performance of a service that a consumer has paid for.",
         "சேவையின் குறைபாடு என்பது நுகர்வோர் பணம் கொடுத்து பெற்ற சேவையின் தரம், இயல்பு அல்லது செயல்பாட்டின் விதத்தில் ஏதேனும் குறைபாடு அல்லது போதாமை ஆகியவற்றைக் குறிக்கிறது.",
         "Section 2(11) of the Consumer Protection Act, 2019", 
         "Section 2(11) of the Consumer Protection Act, 2019, defines 'deficiency' in service and the grounds for claiming compensation.",
         "Consumer Protection Act, 2019 இன் பிரிவு 2(11), சேவையின் 'குறைபாடு' என்ற பதத்தைக் குறிப்பிட்டு, இழப்பீடு கோரும் காரணங்களை வரையறுக்கிறது."
        )
    ],

    "Indian Election Law": [
        ("What is the role of the Election Commission of India?", 
         "The Election Commission of India is responsible for conducting free and fair elections to the Parliament, State Legislatures, and the offices of the President and Vice-President of India.",
         "இந்திய தேர்தல் ஆணையம் பாராளுமன்றம், மாநில சட்டமன்றங்கள், மற்றும் இந்தியாவின் குடியரசுத் தலைவர் மற்றும் துணைத் தலைவர் பதவிகளுக்கான சுதந்திரமான மற்றும் நியாயமான தேர்தல்களை நடத்துவதற்குப் பொறுப்பாக உள்ளது.",
         "Article 324 of the Constitution of India", 
         "Article 324 of the Indian Constitution empowers the Election Commission to supervise, direct, and control elections to various public offices.",
         "இந்திய அரசியலமைப்பின் Article 324, பொதுப் பதவிகளுக்கான தேர்தல்களை மேற்பார்வையிட, இயக்கி, மற்றும் கட்டுப்படுத்த தேர்தல் ஆணையத்திற்கு அதிகாரம் அளிக்கிறது."
        ),
        ("What are the eligibility criteria to contest in Lok Sabha elections?", 
         "To contest in Lok Sabha elections, a candidate must be at least 25 years old, a citizen of India, and should not hold any office of profit under the government.",
         "லோக் சபா தேர்தலில் போட்டியிட, ஒரு வேட்பாளர் குறைந்தபட்சம் 25 வயதானவராக, இந்தியாவின் குடிமகனாகவும், அரசு பதவியை வகிக்காதவராகவும் இருக்க வேண்டும்.",
         "Article 84 of the Constitution of India", 
         "Article 84 of the Indian Constitution outlines the qualifications for membership in Parliament, including age and citizenship requirements.",
         "இந்திய அரசியலமைப்பின் Article 84, வயது மற்றும் குடிமகன் தேவைகள் உள்ளிட்ட பாராளுமன்றத்தில் உறுப்பினராவதற்கான தகுதிகளை வரையறுக்கிறது."
        ),
        ("What is the process of voter registration in India?", 
         "To register as a voter in India, an individual must be 18 years of age or above and apply through the Election Commission's official website or by submitting Form 6 at the nearest electoral office.",
         "இந்தியாவில் ஓட்டுச்சாவடி பதிவுக்கு, ஒரு நபர் 18 வயதுக்கு மேற்பட்டவராக இருக்க வேண்டும், மற்றும் தேர்தல் ஆணையத்தின் அதிகாரப்பூர்வ இணையதளம் மூலம் அல்லது அருகிலுள்ள தேர்தல் அலுவலகத்தில் படிவம் 6 சமர்ப்பித்து விண்ணப்பிக்க வேண்டும்.",
         "Section 19 of the Representation of the People Act, 1950", 
         "Section 19 of the Representation of the People Act, 1950, outlines the eligibility criteria for voter registration based on age and residency.",
         "Representation of the People Act, 1950 இன் பிரிவு 19, வயதும் வசிப்பிடமும் அடிப்படையாகக் கொண்டு ஓட்டுச்சாவடி பதிவுக்கான தகுதிகளை வரையறுக்கிறது."
        ),
        ("What are the grounds for disqualification of a Member of Parliament?", 
         "A Member of Parliament can be disqualified if they hold an office of profit, are declared bankrupt, or have been convicted of certain crimes.",
         "பாராளுமன்ற உறுப்பினர் ஒரு லாப பதவியை வகித்தால், கடன் செலுத்த முடியாதவராக அறிவிக்கப்படுபவர், அல்லது குறிப்பிட்ட குற்றங்களில் குற்றவாளியாக அடையாளம் காணப்பட்டால் பதவியிலிருந்து தகுதி நீக்கம் செய்யப்படலாம்.",
         "Article 102 of the Constitution of India", 
         "Article 102 of the Indian Constitution lays down the conditions for disqualification of MPs on grounds like holding an office of profit, insolvency, and criminal conviction.",
         "இந்திய அரசியலமைப்பின் Article 102, லாப பதவியை வகித்தல், கடன் செலுத்த முடியாத நிலை மற்றும் குற்றவியல் தீர்ப்பு போன்ற அடிப்படைகளில் எம்.பிக்களின் தகுதி நீக்க நிபந்தனைகளை குறிப்பிடுகிறது."
        ),
        ("How is the President of India elected?", 
         "The President of India is elected by an electoral college consisting of the elected members of both Houses of Parliament and the Legislative Assemblies of States and Union Territories.",
         "இந்தியாவின் குடியரசுத் தலைவர், இரு அவைகளின் தெரிவு செய்யப்பட்ட உறுப்பினர்களும், மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் சட்டப்பேரவைகளின் உறுப்பினர்களும் உள்ள தேர்தல் கல்லூரியால் தேர்வு செய்யப்படுகிறார்கள்.",
         "Article 54 of the Constitution of India", 
         "Article 54 of the Indian Constitution specifies that the President shall be elected by an electoral college comprising elected MPs and MLAs.",
         "இந்திய அரசியலமைப்பின் Article 54, குடியரசுத் தலைவர் தேர்தல் கல்லூரி எனப்படுவது, தேர்ந்தெடுக்கப்பட்ட எம்.பிக்கள் மற்றும் எம்.எல்.ஏக்களை உள்ளடக்கியதாக இருக்க வேண்டும் என குறிப்பிடுகிறது."
        ),
        ("What is the procedure for challenging election results in India?", 
         "Election results in India can be challenged by filing an election petition in the High Court within 45 days of the election results being declared.",
         "இந்தியாவில் தேர்தல் முடிவுகளை 45 நாட்களுக்குள் உயர்நீதிமன்றத்தில் தேர்தல் மனுவை தாக்கல் செய்வதன் மூலம் எதிர்க்கலாம்.",
         "Section 80 of the Representation of the People Act, 1951", 
         "Section 80 of the Representation of the People Act, 1951, provides for the filing of election petitions to challenge the validity of election results.",
         "Representation of the People Act, 1951 இன் பிரிவு 80, தேர்தல் முடிவுகளின் சரியான நிலையை எதிர்க்க தேர்தல் மனுக்களை தாக்கல் செய்யும் முறைகளை வழங்குகிறது."
        ),
        ("What are the restrictions on election campaign spending in India?", 
         "There are specific limits on the amount candidates can spend during election campaigns, depending on the type of election and the constituency size.",
         "தேர்தல் பிரசாரங்களில் செலவழிக்ககூடிய தொகையில் வேட்பாளர்களுக்கு குறிப்பிட்ட வரம்புகள் உள்ளன, இது தேர்தல் வகை மற்றும் தொகுதியின் அளவைப் பொறுத்தது.",
         "Section 77 of the Representation of the People Act, 1951", 
         "Section 77 of the Representation of the People Act, 1951, mandates limits on election campaign expenses, including expenditures on publicity and travel.",
         "Representation of the People Act, 1951 இன் பிரிவு 77, தேர்தல் பிரசார செலவுகளை, விளம்பரம் மற்றும் பயணம் போன்ற செலவுகளை உள்ளடக்கிய செலவுகளை வரம்பு செய்கிறது."
        ),
        ("What are the penalties for engaging in corrupt practices during elections?", 
         "Engaging in corrupt practices during elections, such as bribery, intimidation, or undue influence, can result in fines, imprisonment, or disqualification from future elections.",
         "தேர்தலின்போது ஊழல் நடைமுறைகளில் ஈடுபடுதல், உதாரணமாக லஞ்சம், மிரட்டல் அல்லது அநியாயமான செல்வாக்கு ஏற்படுத்தல், அபராதங்கள், சிறை தண்டனை அல்லது எதிர்கால தேர்தல்களில் தகுதிநீக்கம் ஆகியவற்றை விளைவிக்கலாம்.",
         "Section 123 of the Representation of the People Act, 1951", 
         "Section 123 of the Representation of the People Act, 1951, lists corrupt practices like bribery, impersonation, and undue influence, with penalties for offenders.",
         "Representation of the People Act, 1951 இன் பிரிவு 123, லஞ்சம், வேட்பாளரைத் தவறாகப் பெயரிடுதல் மற்றும் அநியாயமான செல்வாக்கு போன்ற ஊழல் நடைமுறைகளை வரையறுக்கிறது மற்றும் குற்றவாளிகளுக்கு தண்டனைகளை வழங்குகிறது."
        ),
        ("Who is eligible to vote in Indian elections?", 
         "Any citizen of India who is 18 years of age or above and registered as a voter in the electoral rolls is eligible to vote in Indian elections.",
         "இந்தியாவின் தேர்தல்களில் வாக்களிக்க, இந்தியாவின் எந்த குடிமகனும் 18 வயதிற்கு மேற்பட்டவராகவும், தேர்தல் பட்டியலில் ஓட்டாளராக பதிவு செய்யப்பட்டவராகவும் இருக்கலாம்.",
         "Section 19 of the Representation of the People Act, 1950", 
         "Section 19 of the Representation of the People Act, 1950, specifies the qualifications for voters, including age and residency requirements.",
         "Representation of the People Act, 1950 இன் பிரிவு 19, ஓட்டாளர்களுக்கான தகுதிகளை குறிப்பிட்டு, வயது மற்றும் குடியிருப்பு தேவைகளை விளக்குகிறது."
        ),
        ("How are Rajya Sabha members elected?", 
         "Rajya Sabha members are elected by the elected members of the State Legislative Assemblies through proportional representation by means of a single transferable vote.",
         "ராஜ்ய சபா உறுப்பினர்கள் மாநில சட்டமன்றங்களின் தெரிவு செய்யப்பட்ட உறுப்பினர்களால், ஒற்றை மாற்றக்கூடிய வாக்கு மூலம் விகிதாசார பிரதிநிதித்துவத்தின் மூலம் தேர்வு செய்யப்படுகிறார்கள்.",
         "Article 80 of the Constitution of India", 
         "Article 80 of the Indian Constitution provides for the composition and election of Rajya Sabha members by the elected representatives of State Legislative Assemblies.",
         "இந்திய அரசியலமைப்பின் Article 80, மாநில சட்டமன்றங்களின் தெரிவு செய்யப்பட்ட பிரதிநிதிகள் மூலம் ராஜ்ய சபா உறுப்பினர்களின் அமைப்பையும் தேர்தலையும் வழங்குகிறது."
        ),
        ("What should a voter do if someone has already voted in their name during elections?", 
         "If a voter finds that someone else has already voted in their name, they can invoke Section 49P of the Conduct of Election Rules, 1961. This allows the voter to cast a ‘tendered vote’. The voter will be required to provide identification, and their vote will be recorded on a separate ballot paper and kept aside for verification.",
         "ஒரு வாக்காளர், தனது பெயரில் யாரோ ஒருவர் ஏற்கனவே வாக்களித்துவிட்டார் என்று கண்டால், அவர் 1961 தேர்தல் நடத்தை விதிகள், பிரிவு 49Pஐப் பயன்படுத்தலாம். இது வாக்காளருக்கு ‘தண்டர் வோட்’ (tendered vote) பதிவு செய்ய அனுமதிக்கிறது. வாக்காளர் அடையாளத்தை வழங்க வேண்டும், மற்றும் அவரின் வாக்கு தனி வாக்குச் சீட்டில் பதிவு செய்யப்பட்டு மறுபரிசீலனைக்காக வைக்கப்படும்.",
         "Section 49P of the Conduct of Election Rules, 1961", 
         "Section 49P of the Conduct of Election Rules, 1961, allows voters to cast a tendered vote if someone else has voted in their name, ensuring the right to vote is protected.",
         "1961 தேர்தல் நடத்தை விதிகள், பிரிவு 49P, வேறு ஒருவர் பெயரில் வாக்களித்திருந்தாலும், அந்த வாக்காளரின் வாக்குரிமையை பாதுகாக்க தண்டர் வோட் பதிவு செய்ய அனுமதிக்கிறது."
        ),(
    "What should a voter do if their name is missing from the electoral roll on the day of the election?", 
    "If a voter's name is missing from the electoral roll on the day of the election, they can file a complaint with the presiding officer at the polling station. According to Section 49O of the Conduct of Election Rules, 1961, the presiding officer will verify the complaint and, if satisfied, allow the voter to cast a vote using a ‘tendered ballot paper’. This ensures that the voter's right to vote is not denied.",
    "தேர்தல் நாள் போது ஓட்டாளரின் பெயர் தேர்தல் பட்டியலில் இல்லை என்றால், அவர்கள் polling stationல் தலைமை அலுவலருக்கு புகார் செய்யலாம். 1961 தேர்தல் நடத்தை விதிகள், பிரிவு 49Oன் படி, தலைமை அலுவலர் புகாரை சரிபார்க்க முடிவு செய்வார்கள், மற்றும் அவர்களின் உரிமையை மறுக்காமல் ‘தண்டர் வாக்குச் சீட்டில்’ வாக்களிக்க அனுமதிக்கிறார்கள்.",
    "Section 49O of the Conduct of Election Rules, 1961", 
    "Section 49O of the Conduct of Election Rules, 1961, allows voters whose names are missing from the electoral roll to file a complaint and cast a tendered vote, ensuring their right to vote is protected.",
    "1961 தேர்தல் நடத்தை விதிகள், பிரிவு 49O, தேர்தல் பட்டியலில் பெயர் காணப்படாத ஓட்டாளர்களுக்கு புகார் செய்யும் மற்றும் தண்டர் வாக்குச் சீட்டில் வாக்களிக்க அனுமதிக்கிறது, இது அவர்களின் வாக்குரிமையை பாதுகாக்கிறது."
)

    ],
    "Indian Penal Code (IPC), 1860": [
        ("What is the punishment for murder under Indian law?", 
         "Section 302 of the IPC prescribes two forms of punishment for murder: death penalty or life imprisonment, depending on the severity of the case. In addition, the accused may also be liable to pay a fine. The court considers the motive, the method used, and the circumstances surrounding the crime when determining the appropriate punishment.",
         "இந்திய தண்டனைச் சட்டத்தின் பிரிவு 302 இன் கீழ், கொலைக்கான தண்டனையாக மரண தண்டனை அல்லது ஆயுள் சிறைத் தண்டனை வழங்கப்படுகிறது. மேலும், குற்றவாளிக்கு அபராதமும் விதிக்கப்படலாம். குற்றத்தின் சிக்கல், குற்றம் செய்வதற்கான நோக்கம் மற்றும் சூழ்நிலைகள் ஆகியவற்றின் அடிப்படையில் நீதிமன்றம் தண்டனையை நிர்ணயிக்கிறது.",
         "Section 302 of the IPC", 
         "Section 302 defines the punishment for murder, allowing the courts to impose either the death penalty or life imprisonment depending on the gravity of the offense. It is often used in conjunction with other sections, such as those that define abetment or conspiracy to murder.",
         "பிரிவு 302 கொலைக்கான தண்டனையை வரையறுக்கிறது, இது மரண தண்டனை அல்லது ஆயுள் சிறைத் தண்டனையை விதிக்க நீதிமன்றத்துக்கு உரிமையளிக்கிறது. இந்த பிரிவானது உடந்தை அல்லது சதி குற்றங்களுடன் சேர்த்து பயன்படுத்தப்படுகிறது."
        ),
        
        ("What is the penalty for attempting to commit murder in India?", 
         "Under Section 307 of the IPC, the punishment for attempting to commit murder is imprisonment for up to 10 years, and in cases where serious injury is caused, the punishment may extend to life imprisonment. If the victim is a public servant on duty, the punishment is more severe. The court takes into account the intent, weapon used, and severity of the injury caused.",
         "இந்திய தண்டனைச் சட்டத்தின் பிரிவு 307 இன் கீழ், கொலை செய்ய முயற்சித்ததற்கான தண்டனையாக 10 ஆண்டுகள் வரை சிறைத் தண்டனை வழங்கப்படுகிறது. கூடுதலாக, கடுமையான காயங்கள் ஏற்பட்டால், தண்டனை ஆயுள் சிறைத் தண்டனையாக நீட்டிக்கப்படலாம். அரசுப் பணியாளர் மீது இக்குற்றம் மேற்கொள்ளப்பட்டால், தண்டனை மேலும் கடுமையாகும்.",
         "Section 307 of the IPC", 
         "Section 307 outlines the punishment for attempts to commit murder, considering the use of force, the intention of the accused, and the outcome of the act (whether injury or harm was caused). It is often applied in cases where the attempt was thwarted before completion.",
         "பிரிவு 307 கொலை முயற்சிக்கான தண்டனையை விளக்குகிறது, இது வலிமையின் அளவையும், குற்றவாளியின் நோக்கத்தையும், அச்செயலால் ஏற்பட்ட விளைவுகளையும் (காயம் அல்லது சேதம்) கருத்தில் கொண்டு செயல்படுகிறது."
        ),
        
        ("What is the punishment for rape under Indian law?", 
         "Section 376 of the IPC prescribes rigorous imprisonment of no less than 10 years, which can extend to life imprisonment or even death in extreme cases. The section also allows for fines. The severity of punishment depends on the circumstances, including whether the victim was a minor or if the act was committed by a person in a position of authority.",
         "இந்திய தண்டனைச் சட்டத்தின் பிரிவு 376 இன் கீழ், குறைந்தது 10 ஆண்டுகள் கடுமையான சிறைத் தண்டனை அல்லது ஆயுள் சிறைத் தண்டனை, மேலும் மிகக் கடுமையான சிக்கல்களில் மரண தண்டனையும் வழங்கப்படலாம். இது குறிப்பாக பாதிக்கப்பட்டவர் சிறுவராக இருப்பது அல்லது அதிகாரமுள்ளவரால் குற்றம் நடைபெறுவது போன்ற சூழ்நிலைகளில் மிகவும் கடுமையாகும்.",
         "Section 376 of the IPC", 
         "Section 376 is applied in rape cases, with increased punishment in instances of gang rape or repeated offenses. It also covers custodial rape, marital rape (under certain conditions), and child rape, all with varying degrees of punishment depending on the gravity of the offense.",
         "பிரிவு 376 பாலியல் வன்கொடுமை தொடர்பான வழக்குகளில் பயன்படுத்தப்படுகிறது, குறிப்பாக கூட்டுக் குற்றங்கள் அல்லது மீண்டும் குற்றம் செய்வதற்கான தண்டனைகள் அதிகரிக்கின்றன. இது காவல் நிலையத்தில் பாலியல் வன்கொடுமை, திருமண உறவுகளில் ஏற்படும் வன்கொடுமை மற்றும் சிறார் பாலியல் வன்கொடுமையைப் பற்றிய தண்டனைகளையும் உள்ளடக்கியது."
        ),
        
        ("What is Section 498A of the IPC about?", 
         "Section 498A addresses cruelty by a husband or his relatives toward a married woman. Cruelty includes any conduct that is likely to drive the woman to suicide or cause grave injury to her mental or physical health. The punishment under this section is imprisonment for up to 3 years and a fine. This section aims to protect women from domestic violence and dowry-related harassment.",
         "இந்திய தண்டனைச் சட்டத்தின் பிரிவு 498A, கணவர் அல்லது அவரது உறவினர்களால் திருமணமான பெண்ணுக்கு கொடுமை கொடுப்பது தொடர்பானது. இது பெண்ணை தற்கொலை செய்ய அல்லது தனது உடல் அல்லது மனநிலைக்கு கடுமையான சேதத்தை ஏற்படுத்தும் செயல்பாடுகளை உள்ளடக்கியுள்ளது. தண்டனையாக 3 ஆண்டுகள் சிறைத் தண்டனையும் அபராதமும் வழங்கப்படுகிறது.",
         "Section 498A of the IPC", 
         "Section 498A is frequently used in cases involving domestic violence and dowry harassment. It includes both mental and physical cruelty, and the law provides specific provisions to protect women and ensure justice is served. However, false allegations under this section have also led to criticism.",
         "பிரிவு 498A, உடல் மற்றும் மனநல கொடுமையை உள்ளடக்கிய வழக்குகளில் பயன்படுத்தப்படுகிறது, குறிப்பாக திருமணத் தொகை மற்றும் குடும்பத்தில் பெண்கள் வன்கொடுமைக்கு எதிராக சட்ட பாதுகாப்பை வழங்குகிறது. ஆனால், இவ்விதமான வழக்குகளில் தவறான குற்றச்சாட்டுகள் அளிக்கப்படுவதால் விமர்சனங்களையும் சந்தித்துள்ளது."
        ),
        
        ("What is the definition of murder under Section 300 of the IPC?", 
         "Section 300 defines murder as a culpable homicide with intent to cause death, or bodily injury that is likely to cause death, or if the act is done with the knowledge that it is so imminently dangerous that it must result in death or injury likely to cause death. There are exceptions in cases of self-defense or lack of intent.",
         "இந்திய தண்டனைச் சட்டத்தின் பிரிவு 300 இன் கீழ், கொலை என்பது மரணத்தை ஏற்படுத்தும் நோக்கத்துடன் குணப்படுத்த முடியாத மனநிலையைப் பற்றிய குற்றமாகும். மேலும், அந்தக் குற்றம் மரணத்தை ஏற்படுத்தும் என்று அறிந்திருக்கும்போது அவ்வாறு பயங்கரமான செயல்களில் ஈடுபடுவதால் மரணத்தை அல்லது கடுமையான காயங்களை உண்டாக்கும் என்று சட்டம் வரையறுக்கிறது.",
         "Section 300 of the IPC", 
         "Section 300 is the primary legal definition of murder under Indian law, focusing on the intent and the knowledge that the act was likely to result in death. The section distinguishes between different degrees of culpable homicide based on the intent and circumstances surrounding the crime.",
         "பிரிவு 300, கொலைக்கான முக்கிய சட்ட வரையறையை வழங்குகிறது, இதில் குற்றத்தின் நோக்கம் மற்றும் மரணத்தை ஏற்படுத்தக்கூடிய செயல்கள் பற்றிய அறிவு அடிப்படையாக எடுக்கப்படுகிறது. இந்த பிரிவானது, குற்றத்தின் நோக்கம் மற்றும் சூழ்நிலைகளின் அடிப்படையில் மற்ற குற்றங்களிலிருந்து வேறுபடுகிறது."
        ),
        
        ("What is dowry death under Indian law?", 
         "Section 304B of the IPC defines dowry death as the death of a woman within 7 years of marriage caused by burns or bodily injury or under suspicious circumstances, where it is proven that she was subjected to cruelty or harassment in relation to demands for dowry. The punishment for dowry death is imprisonment for not less than 7 years, which can extend to life imprisonment.",
         "பிரிவு 304B இன் கீழ், திருமணமாகி 7 ஆண்டுகளுக்குள் எரிவி அல்லது உடல் காயத்தால் அல்லது சந்தேகத்துக்குரிய சூழ்நிலைகளில் மரணம் அடைந்த பெண் திருமணத் தொகை தொடர்பான கொடுமைகள் அல்லது அச்சுறுத்தல்களுக்கு உட்பட்டிருந்தால், அது திருமணத் தொகைக் கொலை என்று வரையறுக்கப்படுகிறது. குறைந்தது 7 ஆண்டுகள் சிறைத் தண்டனையும், அதிகபட்சமாக ஆயுள் சிறைத் தண்டனையும் வழங்கப்படும்.",
         "Section 304B of the IPC", 
         "Section 304B addresses dowry deaths, a major issue in India. This section holds the accused responsible for the woman's death if it can be proven that her death was linked to dowry demands and harassment. The section is crucial in cases involving suspicious deaths of women shortly after marriage.",
         "பிரிவு 304B, இந்தியாவில் மிகுந்த பிரச்சனையாக உள்ள திருமணத் தொகைக் கொலைகளை சட்டத்திற்கு உட்படுத்துகிறது. திருமணத் தொகைக்கான கொடுமைகள் மற்றும் அச்சுறுத்தல்களுக்கு உட்பட்டு ஏற்பட்ட மரணங்கள் தொடர்பான வழக்குகளில் குற்றவாளிகளை இந்த பிரிவு பொறுப்பாகப் பார்க்கிறது."
        ),
        
        ("What is the punishment for cheating under Section 420 of the IPC?", 
         "Section 420 of the IPC prescribes imprisonment of up to 7 years and a fine for anyone who cheats and dishonestly induces the delivery of property, or deceives a person into making, altering, or destroying any valuable security or contract. The intent to deceive is a key element in prosecuting under this section.",
         "பிரிவு 420 இன் கீழ், ஏமாற்றி சொத்து பெற முயன்றவர்களுக்கு 7 ஆண்டுகள் வரை சிறைத்தண்டனை மற்றும் அபராதம் விதிக்கப்படுகிறது. மேலும், ஏமாற்றல் மூலம் சொத்து அல்லது மதிப்புள்ள ஆவணங்கள் அல்லது ஒப்பந்தங்களை மாற்றச் செய்பவர்கள் இந்த பிரிவின் கீழ் குற்றவாளிகள் ஆவார்கள். ஏமாற்றல் நோக்கம் இந்த வழக்குகளில் முக்கியதாக கருதப்படுகிறது.",
         "Section 420 of the IPC", 
         "Section 420 covers cheating, focusing on cases where individuals deceive others into parting with property or altering agreements under false pretenses. It is often applied in cases involving fraud in contracts, business dealings, or financial transactions.",
         "பிரிவு 420 ஏமாற்றல் குற்றங்களை வரையறுக்கிறது, இது முக்கியமாக ஒப்பந்தங்களில், வணிக செயல்பாடுகளில் அல்லது நிதி பரிவர்த்தனைகளில் ஏமாற்றத்தை உள்ளடக்கிய வழக்குகளில் பயன்படுத்தப்படுகிறது."
        ),
        
        ("What is the punishment for insulting the modesty of a woman?", 
         "Section 509 of the IPC deals with words, gestures, or acts intended to insult the modesty of a woman. It provides for imprisonment of up to 1 year, or a fine, or both. The intent behind the act and whether the woman felt insulted are crucial in determining guilt under this section.",
         "பிரிவு 509 பெண்களின் கண்ணியத்தை இழிவாகச் செய்ய முயற்சிக்கும் வார்த்தைகள், சைகைகள் அல்லது செயல்களை உள்ளடக்கியது. தண்டனையாக 1 ஆண்டுவரை சிறைத் தண்டனையும் அபராதமும் அல்லது இரண்டுமே வழங்கப்படலாம். குற்றவாளியின் நோக்கம் மற்றும் பெண் அவமானப்பட்டதா என்பதை ஆதாரங்களின் அடிப்படையில் நிர்ணயிக்கப்படும்.",
         "Section 509 of the IPC", 
         "Section 509 focuses on actions that insult the modesty of women, with an emphasis on verbal and non-verbal forms of harassment. This section is used in cases of street harassment, lewd gestures, and derogatory language directed at women.",
         "பிரிவு 509, பெண்களின் கண்ணியத்தை இழிவாகச் செய்யும் செயல்களை முன்வைத்து குற்றவாளிகளை தண்டிக்கிறது. இது வார்த்தை மற்றும் செயல்களால் ஏற்படும் அவமானங்களை உள்ளடக்கியது."
        )
    ],
    "Code of Criminal Procedure (CrPC), 1973": [
        ("What is the procedure for arrest by police without a warrant in India?", 
         "Section 41 of the CrPC allows a police officer to arrest a person without a warrant under certain circumstances. These include when a person commits a cognizable offense in the presence of the officer, or if the officer has credible information or reasonable suspicion that the person has committed a cognizable offense. The officer must inform the arrested person of the grounds for arrest and their rights.",
         "CrPC இன் பிரிவு 41 இன் கீழ், குறிப்பிட்ட சூழ்நிலைகளில் போலீசார் பிணையமின்றி ஒருவரை கைது செய்யலாம். இதுவே ஒரு குற்றம் நேரில் நடந்தால், அல்லது பொய்யற்ற தகவல் அல்லது சந்தேகம் இருந்தால் போலீசார் நடவடிக்கை எடுக்கலாம். கைது செய்யப்பட்டவருக்கு தங்கள் கைது காரணம் மற்றும் உரிமைகள் பற்றி அறிவிக்கப்பட வேண்டும்.",
         "Section 41 of the CrPC", 
         "This section is applied when police need to take immediate action in cognizable offenses, such as theft or assault, without waiting for a warrant from a magistrate. It is crucial for maintaining law and order but has been criticized for potential misuse by law enforcement.",
         "இந்த பிரிவு திருட்டு அல்லது தாக்குதல் போன்ற குற்றங்களில் உடனடி நடவடிக்கை எடுக்கும்போது போலீசாரால் பயன்படுத்தப்படுகிறது. இது சட்ட ஒழுங்கை பேணுவதற்கும் முக்கியமாக இருப்பினும், இதன் தவறான பயன்பாடு பற்றிய விமர்சனங்கள் உண்டு."
        ),
        
        ("What is the process for filing an FIR in cognizable cases in India?", 
         "Under Section 154 of the CrPC, any person can file an FIR in a cognizable case by providing information about the offense to the police officer in charge of a station. The FIR must be written down, read to the informant, and signed by them. If the officer refuses to file the FIR, the person can send the complaint to a senior police officer or a magistrate.",
         "CrPC இன் பிரிவு 154 இன் கீழ், குற்றம் நடந்ததற்கான தகவலை போலீசாரிடம் வழங்கி ஒருவர் FIR தாக்கல் செய்யலாம். FIR எழுதப்பட்டு, தகவல் அளித்தவருக்கு வாசிக்கப்பட வேண்டும் மற்றும் அவர்கள் கையொப்பமிட வேண்டும். FIR பதிவு செய்ய மறுத்தால், ஒருவர் மேலதிக அதிகாரி அல்லது நீதிமன்றத்திற்கு புகார் அளிக்கலாம்.",
         "Section 154 of the CrPC", 
         "This section ensures that any individual has the right to file an FIR for cognizable offenses, such as murder, theft, or rape. It is a critical part of the justice system, ensuring that complaints are registered and investigated properly.",
         "இந்த பிரிவு எவரும் சாட்சியங்களுடன் குற்றச்சாட்டுகளை FIR ஆக்க உரிமையளிக்கிறது. இது கொலை, திருட்டு, பாலியல் வன்கொடுமை போன்ற குற்றங்களை பரிசீலிக்க மற்றும் விசாரிக்க மிக முக்கியமானது."
        ),
        
        ("What is the procedure for examining witnesses by police?", 
         "Under Section 161 of the CrPC, police officers have the power to examine any person who is acquainted with the facts of the case. The statement of the witness is recorded in writing by the police officer. The witness is under no obligation to sign the statement, and the accused is not entitled to a copy of the statement during the investigation.",
         "CrPC இன் பிரிவு 161 இன் கீழ், ஒரு வழக்கின் உண்மைகளை அறிந்த எவரும் போலீசால் விசாரணைக்கு அழைக்கப்படலாம். சாட்சியின் வாக்குமூலம் எழுதப்படும், ஆனால் சாட்சி தனது வாக்குமூலத்தில் கையொப்பமிட வேண்டும் என்பதற்கான கட்டாயம் இல்லை. விசாரணைக்காக குற்றவாளி வாக்குமூலத்தைப் பெறுவதற்கு உரிமை இல்லை.",
         "Section 161 of the CrPC", 
         "This section is crucial during the investigation process, as it allows the police to gather witness statements that can be used during the trial. However, these statements cannot be used as direct evidence unless corroborated in court.",
         "இந்த பிரிவு விசாரணையின் போது சாட்சியங்களின் வாக்குமூலங்களை போலீசாரால் சேகரிக்க உதவுகிறது. ஆனால், இவை நேரடி ஆதாரமாக பயன்படுத்தப்படமுடியாது என்றாலும் நீதிமன்றத்தில் சான்றுகள் மூலம் உறுதிசெய்யப்படலாம்."
        ),
        
        ("What happens if the investigation cannot be completed in 24 hours?", 
         "Section 167 of the CrPC allows the police to seek judicial custody of the accused if the investigation cannot be completed within 24 hours. The police must produce the accused before a magistrate, who can grant further detention of up to 15 days in police custody or 60-90 days in judicial custody, depending on the severity of the offense.",
         "CrPC இன் பிரிவு 167 இன் கீழ், 24 மணி நேரத்திற்குள் விசாரணை முடிக்க முடியாவிட்டால் போலீசார் குற்றவாளியை நீதிபதியிடம் சமர்ப்பிக்க வேண்டும். குற்றத்தின் கடுமையின் அடிப்படையில் நீதிபதி 15 நாட்கள் வரை போலீஸ் காவல் அல்லது 60-90 நாட்கள் நீதிமன்ற காவலை வழங்கலாம்.",
         "Section 167 of the CrPC", 
         "This section is often invoked in complex cases that require more time for investigation, such as financial fraud or terrorism. It ensures that the rights of the accused are balanced with the need for a thorough investigation.",
         "பிரிவு 167, பெரும்பாலும் நிதி மோசடி அல்லது பயங்கரவாதம் போன்ற சிக்கலான வழக்குகளில் பயன்படுத்தப்படுகிறது, இது குற்றவாளியின் உரிமைகள் மற்றும் முழுமையான விசாரணை தேவைகள் இடையில் சமநிலையைக் கொண்டிருக்கிறது."
        ),
        
        ("What is Section 313 of the CrPC?", 
         "Section 313 gives the court the power to question the accused on the evidence presented during the trial. The accused is allowed to explain any circumstances appearing against them in the prosecution's case. This examination is conducted without the presence of the prosecution or defense counsel, and the answers cannot be given under oath.",
         "CrPC இன் பிரிவு 313, வழக்கு நடந்து கொண்டிருக்கும் போது குற்றவாளியை ஆதாரங்களின் அடிப்படையில் விசாரணை செய்வதற்கான அதிகாரத்தை நீதிமன்றத்திற்கு அளிக்கிறது. குற்றவாளிக்கு தன்னை எதிர்த்த ஆதாரங்களை விளக்க வாய்ப்பு தரப்படுகிறது. இந்த விசாரணை, வழக்கறிஞர்கள் இல்லாமல் நடத்தப்படுகிறது மற்றும் பதில்கள் சத்தியம் எடுத்துக்கொண்டு அளிக்கப்படமாட்டாது.",
         "Section 313 of the CrPC", 
         "This section is important because it allows the accused to present their version of events, which can help clarify their defense. It is a crucial part of ensuring a fair trial and is often used to resolve ambiguities in the case.",
         "இந்த பிரிவு குற்றவாளிக்கு வழக்கு பற்றிய தன்னுடைய கோணத்தை விளக்க வாய்ப்பளிக்கிறது, இது தற்காப்புக்கு உதவக்கூடியது. இது ஒரு நியாயமான விசாரணையை உறுதிப்படுத்த முக்கியமானது."
        ),
        
        ("What is meant by the compounding of offenses?", 
         "Section 320 of the CrPC provides for the compounding of certain offenses, meaning the victim and the accused can come to a compromise, and the case can be dismissed without further prosecution. The offenses that can be compounded are usually minor in nature, such as defamation, adultery, or causing simple hurt.",
         "CrPC இன் பிரிவு 320 இன் கீழ், சில குற்றங்களை சமரசப்படுத்தலாம், அதாவது பாதிக்கப்பட்டவர் மற்றும் குற்றவாளி இருவரும் உடன்படிக்கையில் சேர்ந்தால் வழக்கு நிறுத்தப்பட்டு, மேலதிக வழக்கு நடத்தப்பட மாட்டாது. பொதுவாக குறைவான குற்றங்களான அவதூறு, திருமணத்திலிருந்து புறம் செல்வது, அல்லது சாதாரண காயம் ஏற்படுத்துதல் போன்றவற்றை சமரசப்படுத்தலாம்.",
         "Section 320 of the CrPC", 
         "This section is used primarily in minor cases where both parties are willing to compromise. It helps reduce the burden on the judicial system and allows for speedy resolution of cases. However, serious crimes cannot be compounded under this section.",
         "இந்த பிரிவு சிறிய குற்றங்களில் பயன்படுத்தப்படுகிறது, இதில் இரண்டு தரப்பினரும் சமரசத்தில் இணங்கும்போது வழக்குகள் முடிவடைகின்றன. இது நீதித்துறையின் சுமையை குறைக்க உதவுகிறது, ஆனால் பெரிய குற்றங்களை இதனால் சமரசம் செய்ய முடியாது."
        ),
        
        ("What are the inherent powers of the High Court under CrPC?", 
         "Section 482 of the CrPC gives inherent powers to the High Court to make orders that are necessary to prevent abuse of the legal process or to secure the ends of justice. This includes quashing FIRs, revising court orders, or intervening in cases where there has been a miscarriage of justice.",
         "CrPC இன் பிரிவு 482, நீதிமன்ற வழிகளின் தவறான பயன்பாட்டைக் கட்டுப்படுத்தவும் அல்லது நீதியை நிலைநிறுத்தவும் நீதிமன்றத்திற்கு உரிய உத்தரவுகளை வழங்க உயர்நீதிமன்றத்திற்கு உள்ள சக்திகளை அளிக்கிறது. இது FIR-களை ரத்து செய்வது, நீதிமன்ற உத்தரவுகளை திருத்துவது அல்லது நீதி தவறான வழக்குகளில் தலையீடு செய்வதை உள்ளடக்கியது.",
         "Section 482 of the CrPC", 
         "This section is critical in cases where there has been a misuse of legal procedures, such as frivolous FIRs or unjust court orders. It empowers the High Court to intervene in the interest of justice.",
         "இந்த பிரிவு நீதிமன்ற நடைமுறைகள் தவறாக பயன்படுத்தப்பட்ட வழக்குகளில், FIR ரத்து மற்றும் நீதிமன்ற உத்தரவுகளை திருத்துவதற்கான அதிகாரத்தை உயர்நீதிமன்றத்திற்கு வழங்குகிறது."
        )
    ],
    "Indian Evidence Act, 1872": [
        ("What is the definition of evidence under the Indian Evidence Act?", 
         "Section 3 of the Indian Evidence Act defines 'evidence' as all statements which the court permits or requires to be made before it by witnesses regarding matters of fact under inquiry, and such documents as are produced for the inspection of the court. Evidence can be either oral or documentary.",
         "இந்திய ஆதாரச்சட்டத்தின் பிரிவு 3, 'ஆதாரம்' என்பது நீதிமன்றத்தில் விசாரணைநிலை உள்ள உண்மைகளை சாட்சி அளிக்கும் போது சாட்சிகள் வழங்கும் அனைத்து அறிக்கைகளும், மற்றும் நீதிமன்றத்தால் பரிசோதிக்கப்பட உள்ள ஆவணங்களும் ஆகும். ஆதாரம் வாய்மொழி அல்லது ஆவணமாக இருக்கலாம்.",
         "Section 3 of the Indian Evidence Act", 
         "This section is fundamental to the law of evidence as it clearly defines what constitutes valid evidence in legal proceedings. It provides the foundation for determining the admissibility of evidence in both civil and criminal cases.",
         "இந்த பிரிவு வழக்குகளின் போது ஆதாரம் என்ன என்பதை விளக்குகிறது. இது நியாயப்படுத்தப்படும் ஆதாரங்களின் அடிப்படையை ஏற்படுத்துகிறது, இது சிவில் மற்றும் குற்றவழக்குகளில் முக்கியமானது."
        ),
        
        ("What is a confession caused by inducement, threat, or promise under Indian law?", 
         "Section 24 of the Indian Evidence Act states that a confession made by an accused is inadmissible if it appears to have been caused by inducement, threat, or promise from a person in authority, and the inducement was such that it gave the accused a reasonable ground to believe that they would gain an advantage or avoid some evil by making the confession.",
         "இந்திய ஆதாரச்சட்டத்தின் பிரிவு 24, ஒரு அதிகாரத்தால் தூண்டப்பட்ட, மிரட்டப்பட்ட அல்லது வாக்குறுதிப்படுத்தப்பட்ட வாக்குமூலம் குற்றவாளியால் அளிக்கப்பட்டால், அந்த வாக்குமூலம் ஏற்றுக்கொள்ளப்படாது என்று கூறுகிறது. இந்த தூண்டுதல் குற்றவாளிக்கு நன்மை கிடைக்கும் அல்லது தீய விளைவுகளைத் தவிர்க்க முடியும் என்ற நம்பிக்கையை அளித்தால், அந்த வாக்குமூலம் பொருந்தாது.",
         "Section 24 of the Indian Evidence Act", 
         "This section ensures that confessions made under pressure or coercion cannot be used as evidence in court. It protects the rights of individuals and ensures that only voluntary confessions are considered in the legal process.",
         "இந்த பிரிவு அழுத்தம் அல்லது வலுக்கட்டாயமாக அளிக்கப்பட்ட வாக்குமூலங்கள் நீதிமன்றத்தில் ஆதாரமாக இருக்க முடியாது என்பதைக் குறிப்பிடுகிறது. இது குற்றவாளிகளின் உரிமைகளைப் பாதுகாக்கிறது."
        ),
        
        ("What is the significance of expert opinion in Indian law?", 
         "Section 45 of the Indian Evidence Act allows the court to consider the opinion of experts on matters that require specialized knowledge in fields such as science, art, or handwriting. The expert opinion is considered relevant when the court needs to form an opinion on a point that requires technical or specialized knowledge.",
         "இந்திய ஆதாரச்சட்டத்தின் பிரிவு 45, விஞ்ஞானம், கலை, அல்லது கையெழுத்து போன்ற தனியறிவு தேவைப்படும் விஷயங்களில் நீதிமன்றம் நிபுணர்களின் கருத்துக்களை கணக்கில் கொள்ள அனுமதிக்கிறது. நிபுணரின் கருத்து, தொழில்நுட்பம் அல்லது சிறப்பு அறிவு தேவைப்படும் நிலைகளில் முக்கியத்துவம் பெறுகிறது.",
         "Section 45 of the Indian Evidence Act", 
         "This section allows the court to rely on expert opinions in specialized areas. For instance, in cases of medical negligence or forensic evidence, expert testimony becomes crucial in forming judgments.",
         "இந்த பிரிவு, தொழில்நுட்ப திறமைகள் தேவைப்படும் வழக்குகளில் நிபுணர் கருத்துகளை எதிர்நோக்கி, மருத்துவ திருப்தி அல்லது நிபுணத்துவ ஆதாரங்கள் வழக்கின் தீர்மானத்திற்கு உதவுகின்றன."
        ),
        
        ("What is the presumption as to dowry death under Indian law?", 
         "Section 113B of the Indian Evidence Act creates a presumption of dowry death if a woman dies under suspicious circumstances within seven years of marriage, and it is shown that she was subjected to cruelty or harassment for dowry soon before her death. The court may presume that the husband or his relatives are responsible for her death.",
         "இந்திய ஆதாரச்சட்டத்தின் பிரிவு 113B, திருமணத்திற்கு பின்னர் ஏழு ஆண்டுகளுக்குள் சந்தேகத்திற்கிடமான சூழ்நிலையில் ஒரு பெண் இறந்தால், இறப்புக்கு முன் தங்கள் மீது கொடுமை அல்லது மிரட்டல் தக்கப்பட்டிருக்கிறார்கள் என்பதால், மரணம் மாப்பிள்ளையோ அல்லது அவரது உறவினராலோ ஏற்பட்டிருக்கலாம் என்று நீதிமன்றம் நினைக்கலாம்.",
         "Section 113B of the Indian Evidence Act", 
         "This section is crucial in cases involving dowry deaths, as it shifts the burden of proof onto the accused (the husband or his family), who must then provide evidence to disprove the presumption of guilt.",
         "இந்த பிரிவு வரதட்சணை மரண வழக்குகளில் முக்கியமானது, இது குற்றச்சாட்டில் குற்றம்சாட்டப்பட்டவர்களுக்கு குற்றத்தை நிரூபிக்க அடிப்படையை மாற்றுகிறது."
        ),
        
        ("What is the court's presumption about certain facts under Indian law?", 
         "Section 114 of the Indian Evidence Act allows the court to presume the existence of certain facts based on the evidence presented, the natural course of events, and common sense. This presumption is discretionary and can be drawn from logical inferences.",
         "இந்திய ஆதாரச்சட்டத்தின் பிரிவு 114, சாட்சியங்களின் அடிப்படையில், சம்பவங்களின் இயல்பான போக்கு, மற்றும் பொதுவான அறிவின் அடிப்படையில் சில உண்மைகளை நீதிமன்றம் எதிர்பார்க்கலாம். இந்த எதிர்பார்ப்பு விருப்பத்திற்குரியது மற்றும் தர்க்கமான முடிவுகளின் அடிப்படையில் இருக்கலாம்.",
         "Section 114 of the Indian Evidence Act", 
         "This section gives the court the power to draw logical inferences from the facts presented, helping in situations where direct evidence may not be available. It enables a flexible approach to the law of evidence.",
         "இந்த பிரிவு நேரடி ஆதாரங்கள் இல்லாத நிலைகளில் நீதிமன்றம் தர்க்கமான முடிவுகளை எடுக்க அனுமதிக்கிறது. இது ஆதாரச்சட்டத்தில் நெகிழ்வுத்தன்மையை வழங்குகிறது."
        ),
        
        ("What does Section 123 of the Indian Evidence Act state about the affairs of the State?", 
         "Section 123 of the Indian Evidence Act provides that no one can be permitted to give evidence derived from unpublished official records relating to any affairs of the State, unless permission is granted by the head of the concerned department. This protects sensitive information from being disclosed in public interest.",
         "இந்திய ஆதாரச்சட்டத்தின் பிரிவு 123, மாநிலத்தின் விவகாரங்களைப் பற்றிய எந்தவொரு அதிகாரப்பூர்வ ஆவணங்களிலிருந்தும் பெறப்பட்ட ஆதாரங்களை எந்த ஒருவரும் வழங்க அனுமதிக்கப்பட மாட்டார்கள், தவிர அந்தப் பிரிவின் தலைமை அதிகாரி அனுமதி வழங்கினால் மட்டுமே. இது பொதுநலனில் முக்கியமான தகவல்களை வெளிப்படுத்துவதைத் தடுக்கிறது.",
         "Section 123 of the Indian Evidence Act", 
         "This section safeguards sensitive government information and ensures that issues of national security or state affairs are not compromised in legal proceedings unless necessary permissions are obtained.",
         "இந்த பிரிவு முக்கியமான அரசியல் தகவல்களை பாதுகாக்க உதவுகிறது, குறிப்பாக தேசிய பாதுகாப்பு தொடர்பான விவகாரங்களில் இதன் முக்கியத்துவம் இருக்கிறது."
        )
    ],
    "Constitution of India, 1950": [
        ("What is the right to equality under the Indian Constitution?", 
         "Article 14 of the Constitution of India provides that the State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India. It ensures that every individual is treated equally without discrimination.",
         "இந்திய அரசியலமைப்பின் Article 14, சட்டத்தின் முன்னிலையில் சமத்துவத்தை அல்லது சம உரிமைகளை இந்தியாவில் உள்ள யாருக்கும் மறுக்கக்கூடாது என மாநிலத்திற்கு உத்தரவிடுகிறது. இது ஒவ்வொரு நபரும் எந்தவித வேறுபாடுமின்றி சமமாக நடத்தப்படுவதை உறுதிசெய்கிறது.",
         "Article 14 of the Constitution of India", 
         "Article 14 is crucial in ensuring equal protection and treatment under the law, preventing discrimination based on religion, race, caste, sex, or place of birth.",
         "Article 14 சம உரிமையை உறுதி செய்கிறது மற்றும் சட்டத்தின் கீழ் சம உரிமையை வழங்குகிறது. இது மதம், இனம், சாதி, பால், பிறப்பிடம் போன்ற அடிப்படைகளில் விலக்குகளைத் தடுக்கிறது."
        ),
        
        ("What are the protections regarding freedom of speech under Article 19?", 
         "Article 19 of the Indian Constitution guarantees certain freedoms to Indian citizens, including the right to freedom of speech and expression, the right to assemble peacefully, and the right to form associations. However, these rights are subject to reasonable restrictions in the interest of the sovereignty and integrity of India, public order, and morality.",
         "இந்திய அரசியலமைப்பின் Article 19, இந்திய குடிமக்களுக்கு சில உரிமைகளை உத்தரவிடுகிறது, இதில் கருத்துரிமை மற்றும் வெளிப்பாட்டுரிமை, அமைதியாக கூடுவது, மற்றும் சங்கங்களை உருவாக்குவது போன்றவையும் அடங்கும். எனினும், இந்த உரிமைகள் இந்தியாவின் ஒருமைப்பாடு, பொது ஒழுக்கம் மற்றும் சட்டமும் ஒழுங்கும் ஆகியவற்றின் நலனில் நியாயமான கட்டுப்பாடுகளுக்குள் வரும்படி உள்ளது.",
         "Article 19 of the Constitution of India", 
         "Article 19 provides the foundation for democratic freedoms, ensuring citizens can express themselves freely while allowing the State to impose reasonable restrictions for security, public order, and decency.",
         "Article 19 நியாயமான கட்டுப்பாடுகளுடன் குடிமக்களுக்கு கருத்துரிமை மற்றும் வெளிப்பாட்டுரிமையை வழங்குகிறது. இது பாதுகாப்பு மற்றும் பொது ஒழுக்கம் போன்ற காரணங்களுக்காக கட்டுப்பாடுகளை விதிக்க மாநிலத்திற்கு அதிகாரம் வழங்குகிறது."
        ),
        
        ("What is the significance of the Right to Life and Personal Liberty under Article 21?", 
         "Article 21 of the Constitution of India states that no person shall be deprived of his life or personal liberty except according to the procedure established by law. This article is fundamental and guarantees that life and personal liberty can only be taken away by following due legal process.",
         "இந்திய அரசியலமைப்பின் Article 21, எந்த நபரின் வாழ்க்கையோ அல்லது தனிப்பட்ட சுதந்திரமோ சட்டத்தால் நிறுவப்பட்ட முறையைத் தவிர வேறு எந்தவிதத்திலும் மறுக்கப்படமாட்டாது எனக் கூறுகிறது. இந்த பாகம் அடிப்படையானது மற்றும் வாழ்க்கையும் தனிப்பட்ட சுதந்திரமும் சட்டத்தைப் பின்பற்றியே கையாளப்பட வேண்டும் என்பதை உறுதிசெய்கிறது.",
         "Article 21 of the Constitution of India", 
         "This article serves as a cornerstone for human rights in India, encompassing everything from the right to privacy, health, education, and a fair trial. It ensures that any deprivation of life or liberty must be just, fair, and reasonable.",
         "இந்த பிரிவு இந்தியாவில் மனித உரிமைகளின் அடிப்படையாக செயல்படுகிறது. இது தனியுரிமை, சுகாதாரம், கல்வி மற்றும் நியாயமான விசாரணை போன்றவற்றைக் கொண்டுள்ளது, மற்றும் வாழ்க்கை அல்லது சுதந்திரம் இழக்கப்படுமாயின் அது நீதி, நியாயம் மற்றும் சட்டத்திற்கு உட்பட்டதாக இருக்க வேண்டும்."
        ),
        
        ("What are the remedies available under Article 32 for enforcement of rights?", 
         "Article 32 of the Indian Constitution provides the right to individuals to approach the Supreme Court for enforcement of the rights conferred under Part III (Fundamental Rights). It gives the Court the power to issue directions or writs, such as habeas corpus, mandamus, prohibition, quo warranto, and certiorari, to enforce these rights.",
         "இந்திய அரசியலமைப்பின் Article 32, Part III (அடிப்படையுரிமைகள்) கீழ் வழங்கப்பட்ட உரிமைகளைக் காக்க மற்றும் நடைமுறைப்படுத்த உச்சநீதிமன்றத்தை அணுகுவதற்கான உரிமையை நபர்களுக்கு வழங்குகிறது. இந்த உரிமைகளை நடைமுறைப்படுத்த உச்சநீதிமன்றம் உத்தரவுகள் அல்லது வழிகாட்டுதல்கள், writs (குறிப்பாக habeas corpus, mandamus, prohibition, quo warranto, மற்றும் certiorari போன்ற writs) பிறப்பிக்கலாம்.",
         "Article 32 of the Constitution of India", 
         "This article is considered the 'heart and soul' of the Constitution because it empowers individuals to seek constitutional remedies for the violation of their Fundamental Rights, ensuring justice and rule of law.",
         "இந்த பிரிவு அரசியலமைப்பின் 'இதயம் மற்றும் ஆன்மா' என்று அழைக்கப்படுகிறது, ஏனெனில் இது அடிப்படையுரிமைகளின் மீறல் காரணமாக நபர்களுக்கு நீதிமன்றத்தை அணுக சுதந்திரம் வழங்குகிறது."
        ),
        
        ("What are the Fundamental Duties listed under Article 51A?", 
         "Article 51A of the Indian Constitution enumerates the Fundamental Duties of every citizen of India. These duties include respecting the Constitution, cherishing its ideals, protecting the sovereignty, integrity, and unity of India, and promoting harmony and the spirit of common brotherhood among all citizens.",
         "இந்திய அரசியலமைப்பின் Article 51A, ஒவ்வொரு இந்திய குடிமகனின் அடிப்படைக் கடமைகளையும் பட்டியலிடுகிறது. இதில் அரசியலமைப்பை மதிக்கிறோம், அதன் சித்தாந்தங்களைப் போற்றுகிறோம், இந்தியாவின் இறையாண்மை, ஒருமைப்பாடு மற்றும் ஒருமைப்பாட்டைப் பாதுகாப்பது, மற்றும் சகோதரத்துவத்தை மேம்படுத்துவது போன்றவையும் அடங்கும்.",
         "Article 51A of the Constitution of India", 
         "This article highlights the responsibilities of every citizen to contribute to the nation’s welfare. It emphasizes civic duties and national unity as part of responsible citizenship.",
         "இந்த பிரிவு ஒவ்வொரு குடிமகனுக்கும் இந்தியாவின் நலனில் பங்களிக்கச் செய்யும் கடமைகளை வலியுறுத்துகிறது. இது குடிமகனின் பொறுப்புகள் மற்றும் தேசிய ஒருமைப்பாட்டை முக்கியமாகக் குறிப்பிடுகிறது."
        ),
        
        ("How can Parliament amend the Constitution under Article 368?", 
         "Article 368 of the Indian Constitution gives Parliament the power to amend the Constitution. The amendment can be initiated in either house of Parliament and must be passed by a majority of the total membership and by a two-thirds majority of members present and voting. Some amendments also require ratification by at least half of the state legislatures.",
         "இந்திய அரசியலமைப்பின் Article 368, பாராளுமன்றத்திற்கு அரசியலமைப்பை திருத்துவதற்கான அதிகாரத்தை வழங்குகிறது. திருத்தம் பாராளுமன்றத்தின் எந்தவொரு அவையிலும் தொடங்கப்படலாம் மற்றும் மென்பொருள் மூலமாகவும் இரண்டு-மூன்றாயிரம் உறுப்பினர்களின் ஒப்புதல் மூலம் நிறைவேற்றப்பட வேண்டும். சில திருத்தங்கள் மாநில சட்டமன்றங்களின் அரைபாகம் அல்லது அதற்கு மேற்பட்டவை வழியாக உத்தரவிடப்பட வேண்டும்.",
         "Article 368 of the Constitution of India", 
         "This article ensures that the Constitution is dynamic and adaptable to changing circumstances. While amendments are allowed, there are checks and balances in place to prevent arbitrary changes.",
         "இந்த பிரிவு அரசியலமைப்பை உட்சேர்த்து மாற்றங்களை செய்யும் ஆற்றலைக் கொடுக்கும் போது, இவை தற்காலிகமாக அல்லது சட்டரீதியாக சரியானதாக இருக்கும் என்பதில் சோதனைகள் உள்ளன."
        )
    ],
    "Code of Civil Procedure (CPC), 1908": [
        ("What is the jurisdiction of civil courts under Section 9 of CPC?", 
         "Section 9 of the Code of Civil Procedure provides that courts shall have the jurisdiction to try all civil suits unless explicitly barred by a statute. This means any civil dispute, unless specifically excluded, can be brought before a civil court.",
         "நாகரிக வழக்கு நடைமுறைக் கோவையின் Section 9, ஒரு சட்டத்தால் குறிப்பிடப்பட்டவாறு முற்றிலும் தவிர்க்கப்பட்டதைத் தவிர, அனைத்து குடியியல் வழக்குகளையும் நீதிமன்றங்கள் விசாரிக்க உரிமை பெற்றதாக கூறுகிறது. இது எந்தவொரு குடியியல் தகராறும் குறிப்பாகத் தவிர்க்கப்படாதவரை, குடியியல் நீதிமன்றத்தில் கொண்டு வரப்படலாம் என்பதைக் குறிக்கிறது.",
         "Section 9 of CPC", 
         "Section 9 ensures that civil courts have the authority to hear and decide civil disputes unless specifically excluded by a law. It sets the foundation for the civil court’s jurisdiction.",
         "Section 9 குடியியல் வழக்குகளுக்கு சட்டப்படி முற்றிலும் தடைக்கப்பட்டதைத் தவிர, நீதிமன்றத்திற்கு அவற்றை விசாரிக்கும் அதிகாரத்தை உறுதிசெய்கிறது."
        ),
        
        ("What does the doctrine of Res Judicata under Section 11 of CPC state?", 
         "Section 11 of the CPC deals with the doctrine of Res Judicata, which means a matter that has already been adjudicated by a competent court cannot be tried again between the same parties. It prevents litigation on the same issues more than once.",
         "CPC இன் Section 11, Res Judicata என்ற கோட்பாட்டை விவரிக்கிறது, இது ஏற்கனவே ஒரு நிபுணத்துவமான நீதிமன்றத்தால் தீர்ப்பளிக்கப்பட்ட ஒரு விவகாரம் அதே தரப்பினரிடையே மீண்டும் விசாரிக்கப்பட முடியாது என்பதைக் குறிக்கிறது. இது ஒரே பிரச்சினையில் மீண்டும் வழக்கைத் தொடங்குவதைத் தடுக்கிறது.",
         "Section 11 of CPC", 
         "Res Judicata is a critical principle in law, ensuring that once a dispute is resolved, it cannot be re-litigated by the same parties, thus preventing unnecessary and repetitive lawsuits.",
         "Res Judicata என்பது ஒரு முக்கிய சட்டக் கோட்பாடாகும், ஒரே விவகாரம் தீர்க்கப்பட்டதும் அதே தரப்பினரால் மீண்டும் வழக்காட முடியாது என்பதைக் கொண்டுள்ளது."
        ),
        
        ("What is the requirement of notice to the government under Section 80 of CPC?", 
         "Section 80 of the CPC mandates that a two-month notice must be given to the government or public officer before suing them. This allows the government or officer to settle the dispute amicably without litigation.",
         "CPC இன் Section 80, அரசு அல்லது பொது அதிகாரியை வழக்காடுவதற்கு முன்பு, இரண்டு மாதங்கள் முன்கூட்டியே அறிவிப்பை அளிக்க வேண்டும் என்று உத்தரவிடுகிறது. இது வழக்காடுதல் இல்லாமல் நண்பகமாய் தீர்வு காண அரசு அல்லது அதிகாரியை அனுமதிக்கிறது.",
         "Section 80 of CPC", 
         "This section ensures that the government has the opportunity to resolve disputes before they reach court, thus avoiding unnecessary litigation and promoting amicable settlements.",
         "இந்த பிரிவு நீதிமன்றத்திற்கு வரும் முன் அரசு தகராறு தீர்க்க ஒரு வாய்ப்பை வழங்குகிறது, இது தேவையற்ற வழக்குகளைக் குறைக்க உதவுகிறது."
        ),
        
        ("What are the rules for issuing summons under Order V of CPC?", 
         "Order V of the CPC lays down the detailed procedure for the issue and service of summons in civil cases. It ensures that a defendant is properly notified of the lawsuit and given an opportunity to respond.",
         "CPC இன் Order V, குடியியல் வழக்குகளில் உத்தரவு மற்றும் சம்மன்ஸ் அளிக்கும் முறையை விரிவாக விளக்குகிறது. இது முறையாகக் குற்றம் சாட்டப்பட்டவருக்கு வழக்கின் தகவலை வழங்கி, பதிலளிக்க ஒரு வாய்ப்பைக் கொடுக்கிறது.",
         "Order V of CPC", 
         "The issue and service of summons is critical in ensuring that all parties in a lawsuit are aware of the proceedings and can participate, maintaining fairness and justice in civil cases.",
         "சம்மன்ஸ் வழங்குவது வழக்கு விசாரணைகளின் நேர்மையையும் நீதி நிலைபேறையும் உறுதிப்படுத்துகிறது, மேலும் குற்றம் சாட்டப்பட்டவருக்கு வழக்கில் பங்கேற்க ஒரு வாய்ப்பை வழங்குகிறது."
        ),
        
        ("What is the significance of Order XX regarding judgments and decrees in CPC?", 
         "Order XX of the CPC deals with the pronouncement of judgments and decrees. It provides the rules regarding how judgments should be delivered in court and how decrees are drawn up based on these judgments.",
         "CPC இன் Order XX, தீர்ப்புகள் மற்றும் உத்தரவுகள் வழங்குவது தொடர்பான விதிகளை வழங்குகிறது. இது நீதிமன்றத்தில் தீர்ப்புகள் எவ்வாறு வழங்கப்பட வேண்டும் மற்றும் இவற்றின் அடிப்படையில் உத்தரவுகள் எவ்வாறு வரையறுக்கப்பட வேண்டும் என்பதைக் கூறுகிறது.",
         "Order XX of CPC", 
         "This order is essential as it outlines the process for delivering judgments and ensuring they are recorded accurately in the form of decrees. This is a crucial step in concluding civil cases.",
         "இந்த உத்தரவு தீர்ப்புகள் வழங்கப்படும் முறையை விரிவாக விளக்குகிறது மற்றும் அவற்றைச் சரியாகப் பதிவுசெய்வதற்கான நடவடிக்கைகளை சீர்திருத்துகிறது."
        )
    ],
    "Transfer of Property Act, 1882": [
        ("What is the definition of property transfer under Section 5 of the Transfer of Property Act?", 
         "Section 5 of the Transfer of Property Act defines the transfer of property as an act by which a living person conveys property, in present or future, to one or more living persons or to himself and one or more other living persons.",
         "பொருள் இடமாற்றம் சட்டத்தின் Section 5, ஒரு வாழும் நபர், தற்போதைய அல்லது எதிர்காலத்தில், ஒரு அல்லது அதற்கு மேற்பட்ட நபர்களுக்கு அல்லது தன்னையும் மற்ற நபர்களுடன் சேர்ந்து சொத்தை மாற்றும் செயலை இடமாற்றம் என விளக்குகிறது.",
         "Section 5 of Transfer of Property Act", 
         "Section 5 defines the legal act of transferring ownership rights over a property from one person to another, whether in present or future, and is essential for understanding property transactions.",
         "Section 5 சொத்து உரிமைகளை ஒருவரிடமிருந்து மற்றவருக்கு மாற்றும் சட்ட நடவடிக்கையை விளக்குகிறது, இது தற்போதைய அல்லது எதிர்கால உரிமைகளை அடிப்படையாகக் கொண்டுள்ளது."
        ),
        
        ("What is the legal definition of sale under Section 54 of the Transfer of Property Act?", 
         "Section 54 of the Act defines sale as the transfer of ownership in exchange for a price, paid or promised. Sale of tangible immovable property of more than Rs. 100 can only be done by a registered instrument.",
         "Section 54, விலை கொடுத்தல் அல்லது உறுதியளித்தல் மூலம் உரிமையை மாற்றும் செயலை விற்பனை என வரையறுக்கிறது. 100 ரூபாயை மிஞ்சிய நிலையான அசையா சொத்துக்களை பதிவு செய்யப்பட்ட ஆவணத்தின் மூலம் மட்டுமே விற்க முடியும்.",
         "Section 54 of Transfer of Property Act", 
         "This section establishes the requirement for proper documentation, especially for large property transactions, ensuring legal protection for both the buyer and the seller.",
         "இது பெரிய சொத்து பரிவர்த்தனைகளுக்கு சரியான ஆவணங்களை உள்ளடக்குவதற்கான தேவையை நிறுவுகிறது, வாங்குபவர் மற்றும் விற்பவருக்கு சட்ட பாதுகாப்பை உறுதிசெய்கிறது."
        ),
        
        ("How is mortgage defined under Section 58 of the Transfer of Property Act?", 
         "Section 58 defines a mortgage as the transfer of an interest in specific immovable property for securing a loan or the performance of an obligation. The transferor is called a mortgagor and the transferee is called a mortgagee.",
         "Section 58, குறிப்பிட்ட நிலையான அசையா சொத்திலுள்ள ஒரு பங்கினை கடன் அல்லது கடன் வழங்கிய நபருக்கு உரிமையளிக்க உதவுவதை அடிப்படையாகக் கொண்டு இடமாற்றம் செய்வதைக் குறிப்பிடுகிறது. உரிமையளிக்கின்றவர் கடனாளராகவும், பெறுபவர் கடன் வழங்குபவராகவும் அழைக்கப்படுவர்.",
         "Section 58 of Transfer of Property Act", 
         "Mortgages play a vital role in securing loans by offering property as collateral, protecting both the lender and the borrower under the law.",
         "மோர்ட்கேஜ் கடன்களை உறுதிசெய்ய இடமாக நிலையான சொத்துக்களை முன்வைக்கின்றது, இது கடன் வழங்குநர் மற்றும் பெறுநருக்கு சட்டத்தில் பாதுகாப்பு வழங்குகிறது."
        ),
        
        ("What is a lease according to Section 105 of the Transfer of Property Act?", 
         "Section 105 defines a lease as the transfer of a right to enjoy immovable property for a certain period in consideration of a price paid or promised.",
         "Section 105, விலை கொடுத்தல் அல்லது உறுதியளித்தல் மூலம் ஒரு குறிப்பிட்ட காலத்திற்கு நிலையான அசையா சொத்தை அனுபவிக்க உரிமையை வழங்குவதை லீஸ் என வரையறுக்கிறது.",
         "Section 105 of Transfer of Property Act", 
         "Leases are critical for property rental transactions, giving legal rights to both the landlord and the tenant for a fixed term and under agreed conditions.",
         "லீசுகள் சொத்து வாடகை பரிவர்த்தனைகளுக்கு முக்கியமானவை, ஒரு குறிப்பிட்ட காலத்திற்கு நிலையான சொத்துக்களை உடையவருக்கும் வாடகையாளருக்கும் சட்ட உரிமைகளை வழங்குகின்றன."
        ),
        
        ("How is the transfer of property effected according to Section 123 of the Transfer of Property Act?", 
         "Section 123 states that a transfer of immovable property must be done through a registered instrument for the purpose of gift, while the delivery of possession is sufficient for movable property.",
         "Section 123, பரிசாக நிலையான அசையா சொத்தை இடமாற்றம் செய்வதற்கு பதிவு செய்யப்பட்ட ஆவணம் அவசியம் என்பதைக் கூறுகிறது, ஆனால் அசையும் சொத்துகளுக்கு கையாள்வது போதுமானது.",
         "Section 123 of Transfer of Property Act", 
         "The legal requirement of registration ensures that immovable property gifts are properly documented and legally recognized, while movable property transfers are more flexible.",
         "பரிசாக நிலையான சொத்துக்களை வழங்குவதற்கான பதிவு அவசியம், இது சட்டப்படி அங்கீகரிக்கப்பட்ட ஆவணங்களாகும், அசையா சொத்து பரிமாற்றங்களில் அதிக சுருக்கம் உள்ளது."
        )
    ],
    "Indian Contract Act, 1872": [
        ("What agreements are considered contracts under Section 10 of the Indian Contract Act?", 
         "Section 10 of the Indian Contract Act states that all agreements are contracts if they are made by free consent of parties competent to contract, for a lawful consideration, with a lawful object, and are not expressly declared void.",
         "இந்திய ஒப்பந்த சட்டத்தின் பிரிவு 10 இல், சட்டபூர்வமான பொருள் மற்றும் சட்டபூர்வமான நோக்கத்துடன், ஒப்பந்தக்காரர்களின் சுதந்திரமான சம்மதத்தால் உருவாக்கப்பட்ட அனைத்து ஒப்பந்தங்களும் ஒப்பந்தங்களாகக் கருதப்படும் என்று கூறுகிறது.",
         "Section 10 of Indian Contract Act", 
         "Section 10 defines the fundamental requirements for a valid contract, including lawful consideration and free consent, ensuring the contract’s legal enforceability.",
         "Section 10, ஒப்பந்தம் சரியானதாக இருப்பதற்கான அடிப்படைத் தேவைகளை விளக்குகிறது, அதில் சட்டபூர்வமான பரிசீலனை மற்றும் சுதந்திர சம்மதம் அடங்கும், இது சட்டரீதியாக ஒப்பந்தத்தை அமல்படுத்த உதவுகிறது."
        ),
        
        ("Who is competent to contract under Section 11 of the Indian Contract Act?", 
         "Section 11 of the Act specifies that every person is competent to contract who is of the age of majority, is of sound mind, and is not disqualified from contracting by any law.",
         "இந்திய ஒப்பந்த சட்டத்தின் பிரிவு 11 இல், பெரும்பான்மைக் காலத்துக்கு வந்தவர்கள், நலமான மனநிலையுடையவர்கள், மற்றும் எந்த சட்டத்தால் ஒப்பந்தம் செய்வதற்காக தடைசெய்யப்படாதவர்கள் ஒப்பந்தம் செய்வதற்குத் தகுதியானவர்களாகக் கருதப்படுவார்கள் என்று கூறுகிறது.",
         "Section 11 of Indian Contract Act", 
         "This section is crucial for determining who has the legal capacity to enter into a contract, protecting minors and individuals with unsound minds from unfair agreements.",
         "இந்த பிரிவு, குறைந்தவயதினர் மற்றும் நலமான மனநிலையற்ற நபர்களுக்கு அநியாயமான ஒப்பந்தங்களிலிருந்து பாதுகாப்பு அளிக்கிறது."
        ),
        
        ("What is the compensation for loss or damage caused by breach of contract under Section 73 of the Indian Contract Act?", 
         "Section 73 of the Act provides for compensation to the aggrieved party for any loss or damage caused by the breach of contract. Compensation is for actual loss, not for any indirect or remote loss.",
         "ஒப்பந்தத்தை மீறுவதால் ஏற்படும் இழப்பு அல்லது சேதத்திற்கு பிரிவு 73 இல் பாதிக்கப்பட்ட நபருக்கு இழப்பீடு வழங்கப்படுகிறது. இந்த இழப்பீடு நேரடி இழப்புக்காக மட்டுமே வழங்கப்படுகிறது, தவிர்க்க முடியாத அல்லது மறைமுக இழப்புக்கு அல்ல.",
         "Section 73 of Indian Contract Act", 
         "Section 73 safeguards the interests of the injured party by ensuring that they are compensated for actual losses caused by breach of contract, thereby reinforcing the accountability of contracting parties.",
         "இந்த பிரிவு, ஒப்பந்தத்தை மீறியவர்களுக்கு சட்டப்படி பொறுப்பை உறுதிசெய்யும் வகையில் பாதிக்கப்பட்டவர்களுக்கு நேரடி இழப்பிற்கான இழப்பீடுகளை உறுதி செய்கிறது."
        ),
        
        ("What compensation is provided for breach of contract where a penalty is stipulated under Section 74?", 
         "Section 74 states that if a contract has a penalty clause for breach, the party in breach is liable to pay reasonable compensation, even if no actual damage or loss is proven.",
         "ஒரு ஒப்பந்தத்தில் தண்டனை விதி குறிப்பிடப்பட்டிருந்தால், பிரிவு 74 இல் ஒப்பந்தம் மீறியவர் நடுநிலை இழப்பீட்டை செலுத்தத் தவிர்க்க முடியாதது என்று கூறுகிறது, இழப்பு அல்லது சேதம் ஆதாரமாகக் காட்டப்படவில்லை என்றாலும்.",
         "Section 74 of Indian Contract Act", 
         "Section 74 protects against the imposition of excessive penalties and ensures that compensation is limited to a reasonable amount, maintaining fairness in contract enforcement.",
         "இந்த பிரிவு, மிகவும் கடுமையான தண்டனைகளிலிருந்து பாதுகாக்கிறது மற்றும் சட்டசபையில் ஒரு தரமான அளவிற்கு இழப்பீடு வழங்கப்பட்டுள்ளதைக் காட்டுகிறது."
        ),
        
        ("What happens in the case of an agreement to do an impossible act under Section 56?", 
         "Section 56 renders any agreement to perform an act impossible of execution as void. If the act becomes impossible after the contract is made, it is also considered void.",
         "ஒரு செயலை செய்ய முடியாதது என்று கூறினால், அந்த ஒப்பந்தம் பிரிவு 56 இல் செல்லாது எனக் கூறப்படுகிறது. ஒப்பந்தம் செய்யப்பட்ட பிறகு ஒரு செயலைச் செய்ய இயலாதபோது, அது மேலும் செல்லாது எனக் கருதப்படுகிறது.",
         "Section 56 of Indian Contract Act", 
         "This section protects contracting parties by nullifying agreements to perform impossible acts, preventing legal obligations in situations of unforeseen impossibilities.",
         "இந்த பிரிவு, எதிர்பாராத சாத்தியமற்ற சூழ்நிலைகளில் சட்டபூர்வமான பொறுப்புகளை தவிர்க்கும் வகையில், இயலாத செயல்களை செய்யும் ஒப்பந்தங்களை செல்லாது என அறிவிக்கிறது."
        )
    ],
    "Specific Relief Act, 1963": [
        ("When is specific performance of a contract granted under Section 10 of the Specific Relief Act?", 
         "Under Section 10 of the Specific Relief Act, specific performance of a contract may be granted when monetary compensation is not an adequate remedy for breach of the contract, and the terms of the contract are certain and enforceable.",
         "குறிப்பிட்ட நிவாரணச் சட்டத்தின் பிரிவு 10 இல், ஒரு ஒப்பந்தத்தை மீறுவதற்கான பண இழப்பீடு போதுமானதாக இல்லாதபோது, மற்றும் ஒப்பந்தத்தின் விதிமுறைகள் உறுதி செய்யப்பட்டு நடைமுறையில் செயல்படுத்தக்கூடியதாக இருந்தால், குறிப்பிட்ட செயலாக்கம் வழங்கப்படும்.",
         "Section 10 of Specific Relief Act", 
         "This section provides specific performance as a remedy in cases where the contract terms are clear and monetary compensation is insufficient, ensuring that the aggrieved party receives what was originally agreed upon.",
         "இந்த பிரிவு, பண இழப்பீடு போதுமானதாக இல்லாத சூழ்நிலைகளில் குறிப்பிட்ட செயலாக்கத்தை நிவாரணமாக வழங்குகிறது, பாதிக்கப்பட்ட நபர் ஒப்பந்தத்தில் முதல்நிலை உடன்படிக்கையைப் பெறுவதை உறுதிப்படுத்துகிறது."
        ),
        
        ("What types of contracts cannot be specifically enforced under Section 14 of the Specific Relief Act?", 
         "Section 14 of the Specific Relief Act specifies contracts that cannot be specifically enforced, such as contracts involving personal skills, determinable contracts, or those dependent on the personal qualifications of a party.",
         "குறிப்பிட்ட நிவாரணச் சட்டத்தின் பிரிவு 14 இல், குறிப்பிட்ட செயலாக்கத்தை வழங்க முடியாத ஒப்பந்தங்கள், நிபுணத்துவ திறன் அடிப்படையிலானவை அல்லது ஒரு நபரின் தனிப்பட்ட தகுதிகளைப் பொறுத்தவை உள்ளிட்டவை குறிப்பிடப்பட்டுள்ளன.",
         "Section 14 of Specific Relief Act", 
         "This section prevents the enforcement of contracts where personal abilities, discretion, or qualifications are central, thus avoiding issues of personal liberty and fairness in contract performance.",
         "இந்த பிரிவு, தனிப்பட்ட திறன்கள் அல்லது தனிப்பட்ட தகுதிகள் முக்கியமான இடத்தில் உள்ள ஒப்பந்தங்களை அமல்படுத்துவதை தடுக்கிறது, இதன் மூலம் ஒப்பந்த செயலாக்கத்தில் தனிநபர் சுதந்திரம் மற்றும் நீதி உறுதி செய்யப்படுகிறது."
        ),
        
        ("What is a declaratory decree under Section 34 of the Specific Relief Act?", 
         "Section 34 of the Specific Relief Act allows courts to declare the rights of the parties without requiring any consequential relief. A declaratory decree is often sought to affirm legal rights or status in a dispute.",
         "குறிப்பிட்ட நிவாரணச் சட்டத்தின் பிரிவு 34 இல், சிக்கலான நிவாரணம் கோராமலேயே நீதிமன்றங்கள் தரப்பினரின் உரிமைகளை அறிவிக்க அனுமதிக்கின்றன. ஒரு அறிவிப்பு உத்தரவு அடிக்கடி ஒரு சர்ச்சையில் சட்ட உரிமைகள் அல்லது நிலையை உறுதிப்படுத்துவதற்காக நாடப்படுகிறது.",
         "Section 34 of Specific Relief Act", 
         "This section allows parties to obtain a legal declaration of their rights, ensuring clarity and resolution of legal questions without additional relief, often used in property or contractual disputes.",
         "இந்த பிரிவு, தரப்பினரின் உரிமைகளை சட்டப்படி அறிவிக்க இயல்புடன் பயன்படுத்தப்படுகிறது, மேலும் தண்டனை இன்றி சட்ட கேள்விகள் தெளிவுபடுத்தப்படுகின்றன."
        )
    ],
    "Muslim Personal Law (Shariat) Application Act, 1937": [
        ("What personal matters are governed under the Muslim Personal Law (Shariat) Application Act, 1937?", 
         "The Muslim Personal Law (Shariat) Application Act, 1937 governs matters related to marriage, divorce, inheritance, succession, gifts, and religious endowments for Muslims in India. These matters are to be decided according to Islamic law (Shariat).",
         "1937 இல் இயற்றப்பட்ட முஸ்லிம் தனி சட்டம் (ஷரீஅத்) நடைமுறைகள் திருமணம், விவாகரத்து, பரம்பரை, வாரிசுகள், பரிசுகள், மற்றும் மத நிதியங்களைப் பற்றிய விவகாரங்களை நிர்வகிக்கின்றது. இந்த விவகாரங்கள் இஸ்லாமிய சட்டத்தின்படி தீர்மானிக்கப்படுகின்றன.",
         "Muslim Personal Law (Shariat) Application Act, 1937", 
         "This act ensures that Muslims in India follow Islamic law in personal matters, offering legal guidance based on their religious beliefs for family and inheritance issues.",
         "இந்த சட்டம், இந்தியாவில் முஸ்லிம்கள் தங்கள் தனிப்பட்ட விவகாரங்களில் இஸ்லாமிய சட்டத்தைப் பின்பற்றுவதற்கான சட்ட வழிகாட்டுதலை வழங்குகிறது, குறிப்பாக குடும்ப மற்றும் பரம்பரைச் சட்டங்களில்."
        ),
        
        ("What are the provisions regarding marriage under the Muslim Personal Law (Shariat) Application Act?", 
         "The Muslim Personal Law (Shariat) Application Act states that marriages among Muslims are governed by Islamic law. A valid Muslim marriage requires consent, the presence of witnesses, and a specified amount of dowry (mahr) agreed upon by both parties.",
         "முஸ்லிம் தனி சட்டம் (ஷரீஅத்) நடைமுறைகள் திருமணங்களை இஸ்லாமிய சட்டத்தின் கீழ் நிர்வகிக்கின்றது. ஒரு செல்லத்தக்க முஸ்லிம் திருமணத்திற்கு இருவரது ஒப்புதல், சாட்சி நபர்கள் மற்றும் மஹர் எனப்படும் குறிக்கப்பட்ட வழங்கல் தொகை அடங்கும்.",
         "Muslim Personal Law (Shariat) Application Act, 1937", 
         "This provision ensures that Muslim marriages in India are based on the principles of Islamic law, safeguarding the consent and legal agreements between the parties.",
         "இந்த விதிமுறை, இந்தியாவில் முஸ்லிம் திருமணங்கள் இஸ்லாமிய சட்டத்தின் அடிப்படையில் நடைபெறுவதை உறுதிப்படுத்துகிறது மற்றும் தரப்பினரின் ஒப்புதல்களை சட்ட ரீதியாக உறுதிப்படுத்துகிறது."
        ),
        
        ("What are the rules for inheritance under the Muslim Personal Law (Shariat) Application Act?", 
         "The Muslim Personal Law (Shariat) Application Act ensures that inheritance among Muslims is governed by Islamic law. Sons generally inherit double the share of daughters, and specific shares are also provided for parents, spouses, and other relatives based on the Quran and Hadith.",
         "முஸ்லிம் தனி சட்டம் (ஷரீஅத்) நடைமுறைகள் பரம்பரை உரிமைகளை இஸ்லாமிய சட்டத்தின் கீழ் நிர்வகிக்கின்றது. மகன்கள் பொதுவாக மகள்களுக்கு இரட்டிப்பு பங்குகளைப் பெறுகிறார்கள், மேலும் பெற்றோர்கள், துணைவர்கள் மற்றும் பிற உறவினர்களுக்கும் குரான் மற்றும் ஹதீசின் அடிப்படையில் குறிப்பிட்ட பங்குகள் வழங்கப்படுகின்றன.",
         "Muslim Personal Law (Shariat) Application Act, 1937", 
         "This section ensures fair division of inheritance among Muslim family members as per Islamic law, respecting the religious guidelines outlined in the Quran and Hadith.",
         "இந்த பிரிவு, முஸ்லிம் குடும்ப உறுப்பினர்களுக்கு பரம்பரை உரிமைகளை இஸ்லாமிய சட்டத்தின் அடிப்படையில் நியாயமாகப் பிரிக்கிறது, குறிப்பாக குரான் மற்றும் ஹதீசில் குறிப்பிடப்பட்டுள்ள வழிகாட்டுதல்களை மதிப்பில் கொண்டு."
        ),
        
        ("What provisions are made for divorce under the Muslim Personal Law (Shariat) Application Act?", 
         "Divorce under the Muslim Personal Law (Shariat) Application Act follows Islamic principles, allowing for various forms of divorce such as Talaq (divorce initiated by the husband), Khula (divorce initiated by the wife), and Mubarat (mutual divorce). Each type has specific requirements under Islamic law.",
         "முஸ்லிம் தனி சட்டம் (ஷரீஅத்) நடைமுறைகளின் கீழ், தலாக் (கணவன் தொடங்கும் விவாகரத்து), குலா (மனைவி தொடங்கும் விவாகரத்து) மற்றும் முபாராத் (ஒப்புதல் விவாகரத்து) போன்ற விவாகரத்து வகைகள் அனுமதிக்கப்படுகின்றன. ஒவ்வொரு விதத்திற்கும் இஸ்லாமிய சட்டத்தின் கீழ் குறிப்பிட்ட நிபந்தனைகள் உள்ளன.",
         "Muslim Personal Law (Shariat) Application Act, 1937", 
         "This provision upholds the rights of both spouses in seeking a divorce under Islamic law, ensuring a fair process based on religious principles.",
         "இந்த விதிமுறை, இரு துணைகளுக்கும் இஸ்லாமிய சட்டத்தின் கீழ் விவாகரத்தை நாடுவதற்கான உரிமையை உறுதிப்படுத்துகிறது, குறிப்பாக மதச் சட்டத்தின் அடிப்படையில் நியாயமான செயல்பாட்டை வழங்குகிறது."
        )
    ],
    "Companies Act, 2013": [
        ("What is the definition of a company under the Companies Act, 2013?", 
         "Under Section 2(20) of the Companies Act, 2013, a company is defined as a legal entity that is incorporated and registered under this Act or any previous company law. It has a separate legal personality from its shareholders and directors.",
         "2013 ஆம் ஆண்டின் நிறுவனச் சட்டத்தின் பிரிவு 2(20) படி, ஒரு நிறுவனம் சட்டப் பண்பாட்டு அமைப்பு ஆகும், இது இச்சட்டம் அல்லது முந்தைய நிறுவனச் சட்டத்தின் கீழ் பதிவு செய்யப்பட்டு துவங்குகிறது. இது அதன் பங்குதாரர்கள் மற்றும் இயக்குநர்களிலிருந்து தனித்துவமான சட்ட உரிமை கொண்டது.",
         "Section 2(20)", 
         "Section 2(20) legally defines what constitutes a company under the Companies Act, setting the foundation for legal identity, registration, and rights of corporations.",
         "Section 2(20) நிறுவனத்தை சட்ட ரீதியாக வரையறுக்கிறது, சட்ட அடையாளம், பதிவு மற்றும் நிறுவனங்களின் உரிமைகளுக்கு அடிப்படையை அமைக்கிறது."
        ),
        
        ("What is the composition of the Board of Directors under the Companies Act, 2013?", 
         "As per Section 149 of the Companies Act, 2013, every company must have a Board of Directors with at least 3 directors for a public company, 2 for a private company, and 1 for a one-person company. There must be at least one woman director in certain classes of companies.",
         "2013 ஆம் ஆண்டின் நிறுவனச் சட்டத்தின் பிரிவு 149 படி, ஒவ்வொரு நிறுவனத்திற்கும் குறைந்தது 3 இயக்குநர்கள் (பொது நிறுவனம்), 2 இயக்குநர்கள் (தனியார் நிறுவனம்), மற்றும் ஒரு இயக்குநர் (ஒரு நபர் நிறுவனம்) இருக்க வேண்டும். குறிப்பிட்ட வகைகளில், ஒரு பெண் இயக்குநர் கண்டிப்பாக இருக்க வேண்டும்.",
         "Section 149", 
         "This section ensures the proper governance of companies through a well-defined Board of Directors, including provisions for female representation in larger companies.",
         "இந்த பிரிவு, நிறுவனங்களின் ஆட்சிப்பண்புகளை சிறப்பாக நிர்வகிக்கும் விதமாக ஒரு நல்ல திட்டமிடப்பட்ட இயக்குநர் குழுவை உறுதிப்படுத்துகிறது, குறிப்பாக பெரிய நிறுவனங்களில் பெண் பிரதிநிதித்துவத்தை வழங்குகிறது."
        ),
        
        ("What are the rules regarding loans to directors under the Companies Act, 2013?", 
         "Section 185 of the Companies Act, 2013 restricts companies from providing loans, guarantees, or securities to its directors or persons connected to them. Certain exceptions apply, including when loans are made to managing or whole-time directors as part of terms of service.",
         "2013 ஆம் ஆண்டின் நிறுவனச் சட்டத்தின் பிரிவு 185 நிறுவனங்கள் தங்கள் இயக்குநர்களுக்கு அல்லது இயக்குநர்களுடன் தொடர்புடையவர்களுக்கு கடன்கள், உத்தரவாதங்கள் அல்லது பாதுகாப்புகள் வழங்குவதைத் தடை செய்கிறது. சில விலக்குகள், நிர்வாக இயக்குநர்கள் அல்லது முழுநேர இயக்குநர்களுக்கு சேவைக்கால நிபந்தனைகளின் ஒரு பகுதியாக கடன் வழங்கப்படும் போது பொருந்தும்.",
         "Section 185", 
         "This section ensures that company resources are not misused by directors for personal benefits, thus promoting transparency and accountability.",
         "இந்த பிரிவு நிறுவனத்தின் ஆதாரங்கள் இயக்குநர்களால் தனிப்பட்ட நலன்களுக்காக தவறாக பயன்படுத்தப்படாதவாறு உறுதிப்படுத்துகிறது, இது வெளிப்படைத்தன்மை மற்றும் பொறுப்பாற்றலை ஊக்குவிக்கிறது."
        ),
        
        ("What are related party transactions under the Companies Act, 2013?", 
         "Section 188 of the Companies Act, 2013 deals with related party transactions, where a company enters into contracts or arrangements with related parties such as directors, key managerial personnel, or relatives. The approval of the Board or shareholders may be required for such transactions.",
         "2013 ஆம் ஆண்டின் நிறுவனச் சட்டத்தின் பிரிவு 188 தொடர்புடைய தரப்புகளின் உடன்படிக்கைகள் தொடர்பானவை, இதில் ஒரு நிறுவனம் தனது இயக்குநர்கள், முக்கிய மேலாண்மை பணியாளர்கள் அல்லது உறவினர்கள் போன்ற தொடர்புடைய தரப்புகளுடன் ஒப்பந்தங்களில் நுழைகிறது. இத்தகைய உடன்படிக்கைகளுக்கு இயக்குநர் குழு அல்லது பங்குதாரர்களின் ஒப்புதல் தேவைப்படலாம்.",
         "Section 188", 
         "This section ensures that companies disclose and seek approval for transactions involving related parties to avoid conflicts of interest and ensure fairness in dealings.",
         "இந்த பிரிவு, நிறுவனங்கள் தொடர்புடைய தரப்புகளின் உடன்படிக்கைகளுக்கு ஒப்புதல் பெறுவதற்கான திட்டத்தை வழங்குகிறது, இது நலவாய்ப்பைத் தவிர்த்து துல்லியமான ஒப்பந்தங்களை உறுதிப்படுத்துகிறது."
        )
    ],
    "Information Technology (IT) Law": [
        ("What is the definition of 'computer network' under the Information Technology Act, 2000?", 
         "Under Section 2(1)(j) of the Information Technology Act, 2000, a 'computer network' means the interconnection of one or more computers through satellite, microwave, terrestrial line, or other communication media.",
         "அ தகவல் தொழில்நுட்பச் சட்டத்தின் 2000-ஆம் ஆண்டின் பிரிவு 2(1)(j) படி, 'கணினி நெட்வொர்க்' என்பது ஒன்றையோ அல்லது அதற்கும் அதிகமான கணினிகளை செயற்கைக்கோள், மைக்ரோவேவ், நிலத்தடி கம்பி அல்லது பிற தொடர்பு ஊடகங்களின் மூலம் தொடர்புகொள்வதை குறிக்கிறது.",
         "Section 2(1)(j)", 
         "This section provides a comprehensive definition of computer networks, crucial for understanding the scope and application of IT laws related to networking.",
         "இந்த பிரிவு கணினி நெட்வொர்க்களுக்கான முழுமையான வரையறையை வழங்குகிறது, இது நெட்வொர்கிங் தொடர்பான தகவல் தொழில்நுட்பச் சட்டங்களைப் புரிந்துகொள்வதற்குப் பயனுள்ளதாக இருக்கிறது."
        ),
        
        ("What are the legal requirements for digital signatures under the Information Technology Act, 2000?", 
         "Section 3 of the Information Technology Act, 2000, provides that a digital signature must be affixed using a private key that is securely held by the signatory. It must comply with the standards prescribed by the Controller of Certifying Authorities.",
         "தகவல் தொழில்நுட்பச் சட்டத்தின் 2000-ஆம் ஆண்டின் பிரிவு 3, ஒரு டிஜிட்டல் கையொப்பம், கையொப்பக்காரரால் பாதுகாப்பாகக் கையாளப்படும் தனிப்பட்ட விசையைப் பயன்படுத்தி முத்திரையிடப்பட வேண்டும் எனத் தெரிவிக்கிறது. இது சான்றிதழ் அதிகாரிகளின் கட்டுப்பாட்டாளரால் நியமிக்கப்பட்ட தரங்களுடன் ஒத்துப்போக வேண்டும்.",
         "Section 3", 
         "This section ensures that digital signatures are secure and compliant with standards set by the Controller of Certifying Authorities, promoting the authenticity of electronic documents.",
         "இந்த பிரிவு, டிஜிட்டல் கையொப்பங்கள் பாதுகாப்பானவையாய் மற்றும் சான்றிதழ் அதிகாரிகளின் கட்டுப்பாட்டாளரால் நிர்ணயிக்கப்பட்ட தரங்களுடன் ஒத்துப்போகும் என்பதை உறுதிப்படுத்துகிறது, மின்னணு ஆவணங்களின் அடையாளத்தை மேம்படுத்துகிறது."
        ),
        
        ("What constitutes cybercrime under the Information Technology Act, 2000?", 
         "The Information Technology Act, 2000, covers various cybercrimes including hacking (Section 66), identity theft (Section 66C), cyber terrorism (Section 66F), and sending offensive messages through communication service, etc. (Section 66A).",
         "தகவல் தொழில்நுட்பச் சட்டத்தின் 2000-ஆம் ஆண்டின் கீழ், பரிதாபம், அடையாளத் திருட்டு, மின்னணு பயங்கரவாதம் மற்றும் தொடர்பு சேவையின் மூலம் குற்றவியல் செய்திகள் அனுப்புதல் போன்ற பல்வேறு மின் குற்றங்கள் உள்ளன.",
         "Section 66, 66A, 66C, 66F", 
         "These sections outline various forms of cybercrimes, including hacking, identity theft, and cyber terrorism, providing a framework for prosecuting and punishing offenders.",
         "இந்தப் பிரிவுகள் மின்குற்றங்களின் பல்வேறு வடிவங்களை, அதாவது ஹாக்கிங், அடையாளத் திருட்டு மற்றும் மின்னணு பயங்கரவாதம் ஆகியவற்றைக் குறிக்கின்றன, குற்றவாளிகளை சட்டப்படி எதிர்பார்க்கும் மற்றும் தண்டிக்கும் வழிகாட்டியைக் வழங்குகின்றன."
        ),
        
        ("What is the significance of data protection under the Information Technology Act, 2000?", 
         "Section 43A of the Information Technology Act, 2000, mandates that companies holding sensitive personal data or information must implement reasonable security practices and procedures to protect this data from unauthorized access, damage, or destruction.",
         "தகவல் தொழில்நுட்பச் சட்டத்தின் 2000-ஆம் ஆண்டின் பிரிவு 43A, சென்சிடிவ் தனிப்பட்ட தரவுகள் அல்லது தகவல்களை வைத்திருக்கும் நிறுவனங்கள், இந்த தரவை அங்கீகாரமற்ற அணுகல், சேதம் அல்லது அழிவிலிருந்து பாதுகாப்பதற்கான அறிவார்ந்த பாதுகாப்பு நடைமுறைகளை செயல்படுத்த வேண்டும் எனக் கட்டளையிடுகிறது.",
         "Section 43A", 
         "This section ensures that organizations handling sensitive personal data adopt proper security measures to safeguard the information from breaches and misuse.",
         "இந்தப் பிரிவு, சென்சிடிவ் தனிப்பட்ட தரவுகளை கையாளும் அமைப்புகள் தகவல்களை முறையான பாதுகாப்பு நடவடிக்கைகள் மூலம் பாதுகாக்க வேண்டும் என்பதைக் உறுதிப்படுத்துகிறது."
        ),
        
        ("What are the penalties for unauthorized access to computer systems under the Information Technology Act, 2000?", 
         "Section 66 of the Information Technology Act, 2000, prescribes penalties for hacking, which include imprisonment for up to three years and/or a fine up to Rs. 5 lakh for unauthorized access to computer systems.",
         "தகவல் தொழில்நுட்பச் சட்டத்தின் 2000-ஆம் ஆண்டின் பிரிவு 66, ஹாக்கிங்கிற்கு தண்டனைகள் வழங்குகிறது, இதில் கணினி அமைப்புகளுக்கு அங்கீகாரமற்ற அணுகல் செய்வதற்காக மூன்று ஆண்டுகள் வரை சிறைத்தண்டனை மற்றும்/அல்லது ரூ. 5 லட்சம் வரை அபராதம் விதிக்கப்படுகிறது.",
         "Section 66", 
         "This section outlines the penalties for unauthorized access to computer systems, aiming to deter and address cyber offenses related to hacking.",
         "இந்தப் பிரிவு, கணினி அமைப்புகளுக்கு அங்கீகாரமற்ற அணுகல் செய்வதற்கான தண்டனைகளை வகுக்கிறது, ஹாக்கிங்கிற்கான மின்குற்றங்களைத் தடுக்கும் மற்றும் கையாளும் நோக்குடன்."
        )
    ],
    "Goods and Services Tax (GST) Act, 2017": [
        ("What is the levy and collection process under the Goods and Services Tax (GST) Act, 2017?", 
         "Section 9 of the GST Act outlines the levy and collection of GST on the supply of goods and services. It specifies that GST is to be paid by the supplier of goods or services and includes provisions for collecting tax at the point of supply.",
         "Goods and Services Tax (GST) Act, 2017 இல் பிரிவு 9 சரக்கு மற்றும் சேவைகள் வழங்கலின் மீது GST வரி விதிப்பு மற்றும் சேகரிப்பு முறையை விவரிக்கிறது. இது GST வழங்குநரால் செலுத்தப்பட வேண்டும் என்று குறிப்பிடுகிறது மற்றும் வழங்கல் இடத்தில் வரி சேகரிக்கும் விதிகளை உள்ளடக்குகிறது.",
         "Section 9", 
         "This section details the mechanism for levying and collecting GST, ensuring that the tax is applied at each stage of the supply chain.",
         "இந்த பிரிவு GST விதிப்பது மற்றும் சேகரிப்பதற்கான முறையை விவரிக்கிறது, வரி வழங்கல் சங்கிலியின் ஒவ்வொரு கட்டத்திலும் பயன்படுத்தப்படுகிறது என்பதை உறுதிப்படுத்துகிறது."
        ),
        
        ("What are the eligibility criteria for input tax credit under the GST Act, 2017?", 
         "Section 16 of the GST Act specifies the conditions under which a taxpayer is eligible to claim input tax credit. This includes having a valid tax invoice, receiving goods or services, and the supplier having filed their returns.",
         "GST சட்டத்தின் பிரிவு 16 ஒரு பயனருக்கு உள்ளீட்டு வரி நஷ்டத்தைக் கோருவதற்கான நிபந்தனைகளை குறிப்பிடுகிறது. இது செல்லுபடியாகும் வரி பில், பொருட்கள் அல்லது சேவைகளைப் பெறுதல், மற்றும் வழங்குநர் அவர்களின் திருப்பிகளை தாக்கல் செய்திருக்க வேண்டும் என்பவற்றை உள்ளடக்கியது.",
         "Section 16", 
         "This section ensures that businesses can recover the GST paid on inputs used in their operations, thereby avoiding cascading taxes.",
         "இந்த பிரிவு, தொழில்கள் தங்கள் செயல்பாட்டில் பயன்படுத்திய உள்ளீடுகளுக்கு செலுத்தப்பட்ட GST ஐ மீட்டு பெற முடியும் என்பதைக் உறுதிப்படுத்துகிறது, இதன் மூலம் வரிசையாக்கப்பட்ட வரிகளைத் தவிர்க்க உதவுகிறது."
        ),
        
        ("What are the requirements for furnishing details of outward supplies under the GST Act, 2017?", 
         "Section 37 of the GST Act requires taxpayers to furnish details of outward supplies of goods or services in the prescribed form and manner. This includes the supply of goods and services made during the tax period.",
         "GST சட்டத்தின் பிரிவு 37 பங்குதாரர்களை சரக்கு அல்லது சேவைகள் வழங்கலின் விவரங்களை ஒப்புக்கொள்ளக்கூடிய வடிவத்தில் மற்றும் முறையில் வழங்க வேண்டும் என்று கட்டாயமாக்குகிறது. இது வரி காலத்தில் செய்யப்படும் சரக்கு மற்றும் சேவைகள் வழங்கலைப் 포함ிக்கிறது.",
         "Section 37", 
         "This section mandates timely and accurate reporting of outward supplies to ensure compliance and transparency in the tax system.",
         "இந்த பிரிவு சரியான மற்றும் நேரத்தில் வெளியீட்டு வழங்கல்களைப் புகாரளிக்குமாறு கட்டாயமாக்குகிறது, இது வரி முறைமையின் பின்பற்றல் மற்றும் வெளிப்படைத்தன்மையை உறுதிப்படுத்துகிறது."
        )
    ],
    
    "Arbitration and Conciliation Act, 1996": [
        ("What is the definition of an arbitration agreement under the Arbitration and Conciliation Act, 1996?", 
         "Section 7 of the Arbitration and Conciliation Act defines an arbitration agreement as an agreement by the parties to submit to arbitration all or certain disputes which have arisen or which may arise between them in respect of a defined legal relationship.",
         "மத்தியதிகாரம் மற்றும் சமரசம் சட்டத்தின் பிரிவு 7 ஒரு மத்தியதிகார ஒப்பந்தத்தை, அல்லது அவற்றிற்கிடையில் உருவாகும் அல்லது உருவாகக்கூடிய அனைத்துப் பிணவுகளை, அல்லது சில பிணவுகளை சமரசத்திற்கு சமர்ப்பிக்க ஒப்பந்தமாக வரையறுக்கிறது.",
         "Section 7", 
         "This section establishes the formal definition and requirements for an arbitration agreement, ensuring that disputes can be resolved through arbitration.",
         "இந்த பிரிவு மத்தியதிகார ஒப்பந்தத்தின் அதிகாரபூர்வ வரையறை மற்றும் நிபந்தனைகளை நிறுவுகிறது, இது மத்தியதிகாரம் மூலம் பிணவுகளை தீர்க்க முடியும் என்பதை உறுதிப்படுத்துகிறது."
        ),
        
        ("How can a party apply for setting aside an arbitral award under the Arbitration and Conciliation Act, 1996?", 
         "Section 34 of the Arbitration and Conciliation Act allows a party to apply to the court to set aside an arbitral award on specific grounds such as invalidity of the arbitration agreement, the award being in conflict with the public policy, or improper conduct by the arbitrator.",
         "மத்தியதிகாரம் மற்றும் சமரசம் சட்டத்தின் பிரிவு 34 ஒரு தரப்புக்கு, மத்தியதிகார ஒப்பந்தத்தின் தகராறு, பொதுவான கொள்கைக்கு மாறுபாடு, அல்லது மத்தியதிகாரியின் தவறான நடத்தை போன்ற குறிப்பிட்ட காரணங்களின் அடிப்படையில் மத்தியதிகார கிட்டையைச் செருகும் வகையில் நீதிமன்றத்திற்கு விண்ணப்பிக்க அனுமதிக்கிறது.",
         "Section 34", 
         "This section provides the legal framework for challenging and setting aside an arbitral award if certain conditions are met.",
         "இந்த பிரிவு சில நிபந்தனைகள் நிறைவேற்றப்பட்டால், மத்தியதிகார கிட்டையை சவாலிட்டும் செருகும் சட்ட ரீதியான கட்டமைப்பைப் வழங்குகிறது."
        ),
        
        ("What is the process for the enforcement of an arbitral award under the Arbitration and Conciliation Act, 1996?", 
         "Section 36 of the Arbitration and Conciliation Act outlines the process for the enforcement of an arbitral award. Once an award is made, it can be enforced in the same manner as a decree of a court.",
         "மத்தியதிகாரம் மற்றும் சமரசம் சட்டத்தின் பிரிவு 36 மத்தியதிகார கிட்டையின் படி அமலாக்கத்தின் முறையை விவரிக்கிறது. ஒரு கிட்டை வழங்கிய பிறகு, அது நீதிமன்றத்தின் தீர்ப்பாகவே செயல்படுத்தப்படலாம்.",
         "Section 36", 
         "This section ensures that arbitral awards are enforceable as if they were court decrees, providing a mechanism for the execution of arbitral decisions.",
         "இந்த பிரிவு மத்தியதிகார கிட்டைகள் நீதிமன்ற தீர்ப்புகளாகவே செயல்படுத்தப்படும் என்பதை உறுதிப்படுத்துகிறது, இது மத்தியதிகார முடிவுகளை செயல்படுத்துவதற்கான முறைமையை வழங்குகிறது."
        )
    ],
    "Right to Information Act, 2005": [
        ("What is the right to information under the Right to Information Act, 2005?", 
         "Section 3 of the Right to Information Act, 2005 provides that all citizens shall have the right to information. This section ensures that every citizen can request information from a public authority, which is obliged to respond within a specified time frame.",
         "Right to Information Act, 2005 இன் பிரிவு 3 ஒவ்வொரு குடிமகனும் தகவலுக்கு உரிமை பெற வேண்டும் என்று வழங்குகிறது. இந்த பிரிவு அனைத்து குடிமகனும் ஒரு பொதுச் சபையிடமிருந்து தகவல்களை கோர முடியும் என்பதைக் உறுதிப்படுத்துகிறது, இது குறிப்பிட்ட காலக்கெடு உள்ளே பதிலளிக்கக் கட்டாயமாகிறது.",
         "Section 3", 
         "This section empowers citizens to access information from public authorities, ensuring transparency and accountability in the functioning of public institutions.",
         "இந்த பிரிவு பொதுச் சபைகளிடமிருந்து தகவல்களைப் பெறும் உரிமையை குடிமகன்களுக்கு வழங்குகிறது, இது பொது அமைப்புகளின் செயல்பாடுகளில் வெளிப்படைத்தன்மையும், பொறுப்பும் உறுதிப்படுத்துகிறது."
        ),
        
        ("What are the exemptions from disclosure of information under the Right to Information Act, 2005?", 
         "Section 8 of the Right to Information Act, 2005 lists the exemptions from disclosure of information. It includes information that could affect national security, sovereignty, and relations with foreign states, as well as personal information that has no public interest.",
         "Right to Information Act, 2005 இல் பிரிவு 8 தகவல்களை வெளிப்படுத்துவதைத் தவிர்க்கும் நிபந்தனைகளை பட்டியலிடுகிறது. இது தேசிய பாதுகாப்பு, மக்களின் சுதந்தரம், வெளிநாட்டு மாநிலங்களுடன் உள்ள உறவுகளை பாதிக்கக்கூடிய தகவல்களை மற்றும் பொது உலாமை இல்லாத தனிப்பட்ட தகவல்களை உள்ளடக்குகிறது.",
         "Section 8", 
         "This section sets out the limitations on the right to information to protect sensitive and confidential information, while balancing transparency with security concerns.",
         "இந்த பிரிவு உணர்தலுக்கு எதிராக பாதுகாப்பு மற்றும் நம்பகமான தகவல்களைப் பாதுகாக்கவும், வெளிப்படைத்தன்மையுடன் பாதுகாப்பு கவலைகளை சமநிலைப்படுத்தவும் உரிமையின் வரையறைகளை அமைக்கிறது."
        )
    ],
    
    "Protection of Women from Domestic Violence Act, 2005": [
        ("What constitutes domestic violence under the Protection of Women from Domestic Violence Act, 2005?", 
         "Section 3 of the Protection of Women from Domestic Violence Act, 2005 defines domestic violence as any act of physical, emotional, verbal, sexual abuse or economic exploitation against a woman. It includes harm, injury, or threat to the health, safety, or well-being of the woman.",
         "Protection of Women from Domestic Violence Act, 2005 இன் பிரிவு 3 குடும்ப வன்முறை என்பதைக் கணிக்கிறது என்று கூறுகிறது, இது ஒரு பெண்மைக்கு எதிராக உடல், உணர்ச்சி, சொற்களால் அல்லது பாலியல் தொழிலாளர் பலவீனம் அல்லது பொருளாதார ஆளுமை செய்யும் எந்தச் செயல். இது பெண்ணின் ஆரோக்கியம், பாதுகாப்பு அல்லது நலத்திற்கு நஷ்டம், காயம், அல்லது அச்சுறுத்தலை அடைகிறது.",
         "Section 3", 
         "This section ensures comprehensive protection for women against various forms of domestic violence, recognizing the multifaceted nature of abuse.",
         "இந்த பிரிவு பலவகை உள்பட மருத்துவ வன்முறை எதிராக பெண்களுக்கு முழுமையான பாதுகாப்பு வழங்குகிறது, வன்முறை பல்துறையைக் அங்கீகரிக்கிறது."
        ),
        
        ("How can a woman apply for protection under the Protection of Women from Domestic Violence Act, 2005?", 
         "Section 12 of the Protection of Women from Domestic Violence Act, 2005 provides that a woman can apply to the Magistrate for protection against domestic violence. The application must be made in the prescribed manner and form.",
         "Protection of Women from Domestic Violence Act, 2005 இல் பிரிவு 12 ஒரு பெண் குடும்ப வன்முறை எதிராக பாதுகாப்பு பெற நீதிபதியிடம் விண்ணப்பிக்க முடியும் என்று வழங்குகிறது. விண்ணப்பம் ஒவ்வொரு முறையிலும் மற்றும் வடிவத்தில் செய்யப்பட வேண்டும்.",
         "Section 12", 
         "This section outlines the legal process for women seeking protection, ensuring that they have access to judicial remedies for addressing domestic violence.",
         "இந்த பிரிவு பெண்கள் பாதுகாப்பு பெறும் சட்ட செயல்முறையை விளக்குகிறது, குடும்ப வன்முறையை சமாளிக்க நீதிமன்ற வழிகாட்டுதலுக்கு அணுகலை உறுதிப்படுத்துகிறது."
        ),
        
        ("What are protection orders under the Protection of Women from Domestic Violence Act, 2005?", 
         "Section 18 of the Protection of Women from Domestic Violence Act, 2005 empowers the Magistrate to issue protection orders to prevent further violence. These orders can include prohibiting the perpetrator from entering the woman's residence, contacting her, or causing harm.",
         "Protection of Women from Domestic Violence Act, 2005 இல் பிரிவு 18 நீதிபதிக்கு மேலதிக வன்முறையைத் தடுக்கும் பாதுகாப்பு உத்திகளை வெளியிட அதிகாரம் வழங்குகிறது. இந்த உத்திகள் குற்றவாளியை பெண்ணின் வாழிடத்திற்கு வராமல், தொடர்புகொள்ளாமல், அல்லது நஷ்டம் ஏற்படுத்தாமல் தடுப்பதற்கானவை ஆக இருக்கலாம்.",
         "Section 18", 
         "This section provides mechanisms for immediate relief and protection for women experiencing domestic violence, facilitating legal safeguards against further abuse.",
         "இந்த பிரிவு குடும்ப வன்முறையை அனுபவிக்கும் பெண்களுக்கு உடனடி நிவாரணம் மற்றும் பாதுகாப்பு வழங்கும் முறைமைகளை வழங்குகிறது, மேலதிகக் கொடுமைகளைத் தடுக்கும் சட்ட பாதுகாப்புகளை எளிதாக்குகிறது."
        )
    ],


}




dataset = []
for category, questions in categories.items():
    for question, response_en, response_ta, article_num, usage_en, usage_ta in questions:
        dataset.extend(generate_variations(question, response_en, response_ta, article_num, usage_en, usage_ta))


while len(dataset) < 10000:
    for category, questions in categories.items():
        for question, response_en, response_ta, article_num, usage_en, usage_ta in questions:
            dataset.extend(generate_variations(question, response_en, response_ta, article_num, usage_en, usage_ta))
            if len(dataset) >= 10000:
                break
        if len(dataset) >= 10000:
            break

dataset = dataset[:10000]

with open('legal_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["query", "response", "article_number", "usage", "language"])
    writer.writerows(dataset)

print(f"Dataset generated with {len(dataset)} entries. File saved as 'legal_data.csv'.")