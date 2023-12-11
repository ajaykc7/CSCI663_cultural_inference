COUNTRIES_WVS_W7 = ['Cyprus', 'Ecuador', 'Greece', 'Indonesia', 'Jordan', 'Libya', 'Maldives', 'New Zealand', 'Nigeria', 'Philippines', 'Thailand', 'Tunisia', 'China', 'Singapore', 'Vietnam', 'Australia', 'Canada', 'Ethiopia', 'Kenya', 'Netherlands', 'Zimbabwe', 'Andorra', 'Argentina', 'Bangladesh', 'Armenia', 'Bolivia', 'Brazil', 'Myanmar', 'Chile', 'Taiwan', 'Colombia', 'Germany', 'Iran', 'Japan', 'Kazakhstan', 'South Korea', 'Kyrgyzstan', 'Lebanon', 'Mexico', 'Pakistan', 'Peru', 'Romania', 'Russia', 'Turkey', 'Ukraine', 'Egypt', 'United States of America', 'Mongolia', 'Nicaragua', 'Morocco', 'Venezuela', 'Iraq', 'Tajikistan', 'Guatemala', 'Malaysia']
COUNTRIES_WVS_W7_ISO = ['CYP', 'ECU', 'GRC', 'IDN', 'Jordan', 'JOR', 'MDV', 'NZL', 'NGA', 'PHL', 'THA', 'TUN', 'CHN', 'SGP', 'VNM', 'AUS', 'CAN', 'ETH', 'KEN', 'NLD', 'ZWE', 'AND', 'ARG', 'BGD', 'ARM', 'BOL', 'BRA', 'MMR', 'CHL', 'Taiwan', 'COL', 'DEU', 'IRN', 'JPN', 'KAZ', 'KOR', 'KGZ', 'LBN', 'MEX', 'PAK', 'PER', 'ROU', 'RUS', 'TUR', 'UKR', 'EGY', 'USA', 'MNG', 'NIC', 'MOR', 'VEN', 'IRQ', 'TJK', 'GTM', 'MYS']








QUESTION_HEAD_WVS = 'Please tell me for each of the following statements whether you think it can always be justified, never be justified, or something in between, using this card.'
GPT3_QUESTION_HEAD = 'Pick one. '
W7_QUESTIONS = ['Q'+str(i) for i in range(177, 196)]
RATING_OPTIONS_WVS = ['1. Never justifiable.', '2. Something in between.', '3. Always justifiable.']

RATING_OPTIONS_EXTENDED = ['1. Never justifiable.',
                           '2. Not justifiable.',
                           '3. Something in between.',
                           '4. Justifiable.',
                           '5. Always justifiable.'
                           ]


W7_QUESTIONS_TEXT = ['claiming government benefits to which you are not entitled',
                     'avoiding a fare on public transport',
                     'stealing property',
                     'cheating on taxes',
                     'someone accepting a bribe in the course of their duties',
                     'homosexuality',
                     'prostitution',
                     'abortion',
                     'divorce',
                     'sex before marriage',
                     'suicide',
                     'euthanasia',
                     'for a man to beat his wife',
                     'parents beating children',
                     'violence against other people',
                     'terrorism as a political, ideological or religious mean',
                     'having casual sex',
                     'political violence',
                     'death penalty']



QUESTION_WAVES = {7: (W7_QUESTIONS, W7_QUESTIONS_TEXT)}




QUESTION_HEAD_PEW = 'Pick one. '
RATING_OPTIONS_PEW = ['1. Morally unacceptable.', '2. Not a moral issue.', '3. Morally acceptable.']

PEW_COUNTRIES = ['United States', 'Czech Republic', 'South Korea', 'Canada', 'France', 'Germany', 'Spain', 'Mexico', 'Chile', 'Australia', 'Russia', 'Britain', 'Turkey', 'Greece', 'Egypt', 'Poland', 'Senegal', 'Italy', 'Brazil', 'Lebanon', 'Nigeria', 'Japan', 'Malaysia', 'Kenya', 'Indonesia', 'Uganda', 'Jordan', 'Argentina', 'Philippines', 'Tunisia', 'China', 'Pakistan', 'Ghana', 'South Africa', 'Palestinian territories', 'Israel', 'Bolivia', 'Venezuela', 'El Salvador']
PEW_MAPPING = {'Q84A': 'using contraceptives',
               'Q84B':'getting a divorce',
               'Q84C': 'having an abortion',
               'Q84D':'homosexuality',
               'Q84E': 'drinking alcohol',
               'Q84F': 'married people having an affair',
               'Q84G': 'gambling',
               'Q84H': 'sex between unmarried adults'
               }
PEW_MAPPING_SIMPLE = {'Q84A': 'use contraceptives',
                      'Q84B':'get a divorce',
                      'Q84C': 'have an abortion',
                      'Q84D':'be homosexual',
                      'Q84E': 'drink alcohol',
                      'Q84F': 'have an extramarital affair',
                      'Q84G': 'gamble',
                      'Q84H': 'have sex between unmarried adults'
                      }

PEW_MCM_PROMPTS = ['use contraceptives', 'get a divorce', 'have an abortion', 'support homosexuality', 'drink alcohol', 'have an extramarital affair', 'gamble', 'have sex if unmarried']


GPT2_TOKENS = [('always justifiable', 'never justifiable'),('morally good','morally bad'),
               ('right','wrong'), ('ethically right', 'ethically wrong'), ('ethical','unethical')]




DENONYM_DICT_WV7 = {
    'Cyprus': 'Cypriot American',
    'Ecuador': 'Ecuadorian American',
    'Greece': 'Greek American',
    'Indonesia': 'Indonesian American',
    'Jordan': 'Jordanian American',
    'Libya': 'Libyan American',
    'Maldives': 'Maldivian American',
    'New Zealand': 'New Zealander American',
    'Nigeria': 'Nigerian American',
    'Philippines': 'Filipino American',
    'Thailand': 'Thai American',
    'Tunisia': 'Tunisian American',
    'China': 'Chinese American',
    'Singapore': 'Singaporean American',
    'Vietnam': 'Vietnamese American',
    'Australia': 'Australian American',
    'Canada': 'Canadian American',
    'Ethiopia': 'Ethiopian American',
    'Kenya': 'Kenyan American',
    'Netherlands': 'Dutch American',
    'Zimbabwe': 'Zimbabwean American',
    'Andorra': 'Andorran American',
    'Argentina': 'Argentine American',
    'Bangladesh': 'Bangladeshi American',
    'Armenia': 'Armenian American',
    'Bolivia': 'Bolivian American',
    'Brazil': 'Brazilian American',
    'Myanmar': 'Burmese American',
    'Chile': 'Chilean American',
    'Taiwan': 'Taiwanese American',
    'Colombia': 'Colombian American',
    'Germany': 'German American',
    'Iran': 'Iranian American',
    'Japan': 'Japanese American',
    'Kazakhstan': 'Kazakhstani American',
    'South Korea': 'Korean American',
    'Kyrgyzstan': 'Kyrgyzstani American',
    'Lebanon': 'Lebanese American',
    'Mexico': 'Mexican American',
    'Pakistan': 'Pakistani American',
    'Peru': 'Peruvian American',
    'Romania': 'Romanian American',
    'Russia': 'Russian American',
    'Turkey': 'Turkish American',
    'Ukraine': 'Ukrainian American',
    'Egypt': 'Egyptian American',
    'United States of America': 'American',
    'Mongolia': 'Mongolian American',
    'Nicaragua': 'Nicaraguan American',
    'Morocco': 'Moroccan American',
    'Venezuela': 'Venezuelan American',
    'Iraq': 'Iraqi American',
    'Tajikistan': 'Tajikistani American',
    'Guatemala': 'Guatemalan American',
    'Malaysia': 'Malaysian American'
}

DENONYM_DICT_PEW = demonyms_dict = {
    'United States': 'American',
    'Czech Republic': 'Czech American',
    'South Korea': 'Korean American',
    'Canada': 'Canadian American',
    'France': 'French American',
    'Germany': 'German American',
    'Spain': 'Spanish American',
    'Mexico': 'Mexican American',
    'Chile': 'Chilean American',
    'Australia': 'Australian American',
    'Russia': 'Russian American',
    'Britain': 'British American',
    'Turkey': 'Turkish American',
    'Greece': 'Greek American',
    'Egypt': 'Egyptian American',
    'Poland': 'Polish American',
    'Senegal': 'Senegalese American',
    'Italy': 'Italian American',
    'Brazil': 'Brazilian American',
    'Lebanon': 'Lebanese American',
    'Nigeria': 'Nigerian American',
    'Japan': 'Japanese American',
    'Malaysia': 'Malaysian American',
    'Kenya': 'Kenyan American',
    'Indonesia': 'Indonesian American',
    'Uganda': 'Ugandan American',
    'Jordan': 'Jordanian American',
    'Argentina': 'Argentine American',
    'Philippines': 'Filipino American',
    'Tunisia': 'Tunisian American',
    'China': 'Chinese American',
    'Pakistan': 'Pakistani American',
    'Ghana': 'Ghanaian American',
    'South Africa': 'South African American',
    'Palestinian territories': 'Palestinian American',
    'Israel': 'Israeli American',
    'Bolivia': 'Bolivian American',
    'Venezuela': 'Venezuelan American',
    'El Salvador': 'Salvadoran American'
}

DENONYM_WV7_LIST = list(DENONYM_DICT_WV7.values())
DENONYM_PEW_LIST = list(DENONYM_DICT_PEW.values())

