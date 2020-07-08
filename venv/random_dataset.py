"""
The output of the program is a set of Dictionaries to work with, when needed
It can be depicted in 2 ways :
                                    {
                                        "name":"Myles",
                                        "surname":"Parker",
                                        "Nationality":"Austrian",
                                        "date_of_birth":"1979-06-29",
                                        "sex":"M",
                                        "age":42,
                                        "workplace":"Hall University College London",
                                        "Country":"Virgin Islands, U.S.",
                                        "Country_Code":"VI",
                                        "ZipCode":987678,
                                        "Email":"Myles_Parker@Email.com",
                                        "Phone":"+(296)58893885"
                                    }
OR

{"name":"Jayden","surname":"Kayden","Nationality":"Costa Rican","date_of_birth":"1994-11-13","sex":"F","age":26,"workplace":"City of Poznan","Country":"Thailand","Country_Code":"TH","ZipCode":922744,"Email":"Jayden_Kayden@Email.com","Phone":"+(138)48973128"}

"""
import random
import datetime
from datetime import date
import json

list_name = ['Jack', 'Oliver', 'James', 'Charlie', 'Harris', 'Lewis', 'Leo', 'Noah', 'Alfie', 'Rory', 'Alexander',
             'MaxLogan', 'Lucas', 'Harry', 'Theo', 'Thomas', 'Brodie', 'Archie', 'Jacob', 'Finlay', 'Finn', 'Daniel',
             'Joshua', 'Oscar', 'Arthur', 'Hunter', 'Ethan', 'Mason', 'Harrison', 'Freddie', 'Ollie', 'Adam', 'William',
             'Jaxon', 'Aaron', 'Cameron', 'Liam', 'George', 'Jamie', 'Callum', 'Matthew', 'Muhammad', 'Caleb', 'Nathan',
             'Tommy', 'Carter', 'Blake', 'Andrew', 'Luke', 'Jude', 'Angus', 'Riley', 'Luca', 'Samuel', 'Joseph',
             'David', 'Isaac', 'Ryan', 'Hamish', 'Sonny', 'Arlo', 'Arran', 'Cooper', 'Louis', 'Theodore', 'Fraser',
             'Owen', 'Reuben', 'John', 'Carson', 'Innes', 'Elijah', 'Murray', 'Grayson', 'Aiden', 'Aidan', 'Cody',
             'Elliot', 'Ben', 'Henry', 'Sam', 'Alex', 'Ellis', 'Gabriel', 'Jax', 'Callan', 'Ruairidh', 'Frankie',
             'Lachlan', 'Roman', 'Brody', 'Josh', 'Sebastian', 'Struan', 'Evan', 'Kyle', 'Myles', 'Calum', 'Lochlan',
             'Jayden', 'Lyle', 'Robbie', 'Calvin', 'Corey', 'Jaxson', 'Christopher', 'Teddy', 'Eli', 'Marcus', 'Parker',
             'Tyler', 'Euan', 'Hudson', 'Joey', 'Austin', 'Zac', 'Dominic', 'Kayden', 'Zack', 'Harvey', 'Rowan', 'Hugo',
             'Edward', 'Fergus', 'Finley', 'Patrick', 'Cillian', 'Conor', 'Ruben', 'Flynn', 'Jake', 'Albie', 'Levi',
             'Mohammad', 'Cole', 'Robert', 'Blair', 'Dylan', 'Louie', 'Ruaridh', 'Connor', 'Benjamin', 'Kai', 'Michael',
             'Jackson', 'Leon', 'Cooper', 'Louis', 'Theodore', 'Fraser', 'Owen', 'Reuben', 'John', 'Carson', 'Innes',
             'Elijah', 'Murray', 'Grayson', 'Aiden', 'Aidan', 'Cody', 'Elliot', 'Ben', 'Henry', 'Sam', 'Alex', 'Ellis',
             'Gabriel', 'Jax', 'Callan', 'Ruairidh', 'Frankie', 'Lachlan', 'Roman', 'Brody', 'Josh', 'Sebastian',
             'Struan', 'Evan', 'Kyle', 'Myles', 'Calum', 'Lochlan', 'Jayden', 'Lyle', 'Robbie', 'Calvin', 'Corey',
             'Jaxson', 'Christopher', 'Teddy', 'Eli', 'Marcus', 'Parker', 'Tyler', 'Euan', 'Hudson', 'Joey', 'Austin',
             'Zac', 'Dominic', 'Kayden', 'Zack', 'Harvey', 'Rowan', 'Hugo', 'Edward', 'Fergus', 'Finley', 'Patrick',
             'Cillian', 'Conor', 'Ruben', 'Flynn', 'Jake', 'Albie', 'Levi', 'Mohammad', 'Isabel', 'André',

             'Thierry', 'Baert', 'Alessandro', 'Balducci', 'Catalin', 'Berescu', 'Fiona', 'Bult', 'Antonio', 'Calafati',
             'Pierre', 'Calame', 'Jennifer', 'Cassingena Malta', 'Patrick', 'Crehan', 'Philippe', 'Destatte',
             'Jean-Loup', 'Drubigny', 'Dominique', 'Dujols', 'Martin', 'Eyres', 'Elie', 'Faroult', 'Sonia', 'Fayman',
             'Birgit', 'Georgi', 'Grzegorz', 'Gorzelak', 'Sir', 'Peter', 'Tomasz', 'Kayser', 'Krisztina', 'Clemens',
             'Klikar', 'Vanda', 'Knowles' 'Moritz', 'Lennert', 'Bernhard', 'Leubolt']

Workplace_name = ['University of Vienna', 'Universite Libre de Bruxelles', 'EUROCITIES', 'Stadt Menschen Berlin',
                  'Keresztely', 'ACT Consultants', 'City of Poznan', 'Hall University College London',
                  'Warsaw University', 'European Environment Agency', 'ACT Consultants', 'Independent consultant',
                  'City of Liverpool', 'CECODHAS Housing Europe' 'URBACT Secretariat',
                  'The Destree Institute' 'CKA Brussels', 'Council for Science and Technology',
                  "Fondation Charles Leopold Mayer pour le progres de l’Homme",'Universita Politecnica delle Marche',
                  'Bilbao Metropoli-30', 'University of Architecture and Urbanism, Bucharest', 'Ioan Mincu',
                  'University of Milan', "Agence d'urbanisme de Lille metropole", 'University of Lisbon',
                  'ex-Director Deutsches Institut fur Urbanistik', 'Energy Cities', 'Czech Technical University Prague',
                  'City of Stockholm', 'University of Salford', 'Katholieke Universiteit Leuven', 'City of Lille',
                  'University of Vienna', 'Katholieke Universiteit Leuven', 'University of Salford',
                  'Member of Brussels Parliament', "Council of European Municipalities and Region's", 'URBAN-NET',
                  'Porto Vivo Sociedade de Reabilitacao Urbana', 'Ratcliffe The Futures Academy',
                  'University of Manchester', 'KARO, Leipzig', 'Deltares',
                  'Federal Institute for Research on Building,Urban Affairs and Spatial Development, Germany ',
                  'Rodriguez Universidad Politecnica de Valencia',
                  'Bundesministerium fur Verkehr, Bau und Stadte ntwicklung', 'Stockholm University',
                  'University of Leicester', 'Charles University in Prague', 'Clusella EUROCITIES',
                  'French ministry of ecology, energy, sustainable development and regional planning',
                  'Metropolitan Research Institute, Budapest', 'European Environment Agency',
                  'Cutsem The Destree Institute', 'University of Antwerp', 'City of Sofia', 'City of Brno']

nations = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean',
           'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian',
           'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian',
           'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian',
           'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran', 'Congolese',
           'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'East Timorese',
           'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino',
           'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan',
           'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati',
           'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian',
           'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti',
           'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian',
           'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese',
           'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian',
           'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'New Zealander',
           'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani',
           'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari',
           'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi',
           'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian',
           'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer',
           'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan',
           'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan',
           'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']

Countries = ['Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'AndorrA', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda',
'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize',
'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory',
'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic',
'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'The Democratic Republic of the Congo',
'Cook Islands', 'Costa Rica', "Cote D'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland',
'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece',
'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and Mcdonald Islands',
'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Islamic Republic Of Iran', 'Iraq', 'Ireland',
'Isle of Man', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Democratic People'S Republic of Korea", 'Korea, Republic of',
'Kuwait', 'Kyrgyzstan', "Lao People'S Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania',
'Luxembourg', 'Macao', 'The Former Yugoslav Republic of Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique',
'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Federated States of Micronesia', 'Republic of Moldova', 'Monaco', 'Mongolia', 'Montserrat', 'Morocco', 'Mozambique',
'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island',
'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russian Federation', 'RWANDA', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia',
'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro',
'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain',
'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China',
'Tajikistan', 'United Republic of Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay',
'Uzbekistan', 'Vanuatu', 'Venezuela', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

Code_Countries = ['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB',
'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD',
'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ',
'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT',
'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ',
'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT',
'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE',
'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW',
'SH', 'KN', 'LC', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'CS', 'SC', 'SL', 'SG', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'ES', 'LK', 'SD',
'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE',
'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW']

# Join countrie with ther country_code
cntry_code = list(zip(Countries, Code_Countries))


# Generate each time a new dictionnary while i < 18000, you can change i as the number of dicts needed;

number_of_dict_wanted = 0
while number_of_dict_wanted < 4000:
    # __Generate random name, surname, ... from our predefined list;

    name = random.choice(list_name)
    surname = random.choice(list_name)
    Nationality = random.choice(nations)
    random_country = random.choice(cntry_code)
    Country = random_country[0]
    Country_Code = random_country[1]

    # _Random ZipCode

    Zipcode = random.randint(000000,999999)

    # _Email

    concat_email = [name,'_', surname,'@Email.com']
    Email = ''.join(concat_email)

    #_Random Phone Number

    Phone_num = random.randint(44444444,99999999)
    Phone_cod = random.randint(000, 999)
    phone_concat = ['+(', str(Phone_cod), ')',str(Phone_num)]
    Phone_Number = ''.join(phone_concat)

    # __Generate random sex

    sex = random.choice("F M None Null".split())

    # __Generate a random date_of_birth;

    start_date = datetime.date(1976, 1, 1)
    end_date = datetime.date(2004, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    date_of_birth = start_date + datetime.timedelta(days=random_number_of_days)
    birth_date = str(date_of_birth)


    # CALCULATE AGE;
    def calculateAge(birthDate):
        today = date.today()
        age_c = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age_c + 1


    age = calculateAge(date_of_birth)

    # GENERATE RANDOM WORKPLACE;
    workplace = random.choice(Workplace_name)

    info = ['name', 'surname', 'Nationality', 'date_of_birth', 'sex', 'age', 'workplace', 'Country', 'Country_Code', 'ZipCode', 'Email', 'Phone']

    label = [name, surname, Nationality, birth_date, sex, age, workplace, Country, Country_Code,Zipcode, Email, Phone_Number]

    info_per = dict(zip(info, label))

    # SAVE RESULTS TO JSON FILE;
    with  open('person_info_dataset.json', 'a') as dataset:
        json.dump(info_per, dataset,indent=4, sort_keys=False, separators=(',', ':'))
        dataset.write(',\n')
    number_of_dict_wanted += 1

    dataset.close()
