import nltk
from geotext import GeoText

sf = "San Francisco, CA"
ma = "Mantua, UT"
og = "Ogden to San Fran"


places = GeoText(sf)
#print places.states
print places.cities

places = GeoText(ma)
#print places.states
print places.cities

places = GeoText(og)
#print places.states
print places.cities

stateDictionary =  {'AL' : 'Alabama',
                    'AK' : 'Alaska',
                    'AZ' : 'Arizona',
                    'AR' : 'Arkansas',
                    'CA' : 'California',
                    'CO' : 'Colorado',
                    'CN' : 'Connecticut',
                    'DE' : 'Delaware',
                    'FL' : 'Florida',
                    'GA' : 'Georgia',
                    'HI' : 'Hawaii',
                    'ID' : 'Idaho', 
                    'IL' : 'Illinois',
                    'IN' : 'Indiana',
                    'IA' : 'Iowa',
                    'KS' : 'Kansas',
                    'KY' : 'Kentucky',
                    'LA' : 'Louisiana',
                    'ME' : 'Maine',
                    'MD' : 'Maryland',
                    'MA' : 'Massachusetts',
                    'MI' : 'Michigan',
                    'MN' : 'Minnesota',
                    'MS' : 'Mississippi',
                    'MO' : 'Missouri',
                    'MT' : 'Montana',
                    'NE' : 'Nebraska',
                    'NV' : 'Nevada',
                    'NH' : 'New Hampshire',
                    'NJ' : 'New Jersey',
                    'NM' : 'New Mexico',
                    'NY' : 'New York',
                    'NC' : 'North Carolina',
                    'ND' : 'North Dakota',
                    'OH' : 'Ohio',    
                    'OK' : 'Oklahoma',
                    'OR' : 'Oregon',
                    'PA' : 'Pennsylvania',
                    'RI' : 'Rhode Island',
                    'SC' : 'South  Carolina',
                    'SD' : 'South Dakota',
                    'TN' : 'Tennessee',
                    'TX' : 'Texas',
                    'UT' : 'Utah',
                    'VT' : 'Vermont',
                    'VA' : 'Virginia',
                    'WA' : 'Washington',
                    'WV' : 'West Virginia',
                    'WI' : 'Wisconsin',
                    'WY' : 'Wyoming' }
