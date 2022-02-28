import numpy as np
import pandas as pd

data = pd.read_csv('Chase5093_Activity20220225.CSV')
data = data.drop(columns='Memo')
data['Description'] = data['Description'].str.upper()
# strip "'" ssss
data['Description'] = data['Description'].str.replace("'", "")
data['Bucket'] = np.NaN
data['Vendor'] = np.NaN
data.loc[data['Category'] == 'Gas', 'Bucket'] = 'FUEL'


def define_bucket(bucket, comps):
    for i in comps:
        data.loc[data['Description'].str.contains(i), 'Bucket'] = bucket
        data.loc[data['Description'].str.contains(i), 'Vendor'] = i


car = ['CARWASH',
       'DISCOUNT TIRE'
       ]

childcare = ['ADVENTURE KIDS']

coffee = ['STARBUCKS',
          'GOLDEN HOUR',
          'SUMMER MOON',
          'NESPRESSO',
          'MINUTI COFFEE'
          ]

doctor = ['TX CHILDRENS HOSPITAL',
          'DAVAM URGENT CARE',
          'PSYCHIATRIC CONSULTING',
          'TEXAS CHILDRENS PEDI',
          'TX ORTHO SPORTS MED',
          'ADAM TURNER'
          ]

entertainment = ['DISNEYPLUS',
                 'WOODLANDS TENNIS'
                 ]

giving = ['CHRIST COMMUNITY CHURC',
          'MOSAICS OF MERCY',
          'CALVERT HOSPICE'
          ]

grocery = ['H-E-B #',
           'HEB ONLINE',
           'BOISSON',
           'KROGER',
           'TRADER JOES'
           ]

home_improvement = ['THE HOME DEPOT',
                    'LOWES'
                    ]

personal = ['MALIBU NAILS SPA',
            'SNOW WHITE CLEANERS',
            'MOBILITY CHIRO',
            'BELLA VIDA SALON'
            ]

pharmacy = ['WALGREENS',
            'CVS/PHARMACY'
            ]

restaurant = ['SHIPLEY DO-NUTS',
              'FLOWERCHILD',
              'BRUSTER ICE CREAM',
              'MEZCAL CANTINA',
              'RUDY S COUNTRY S',
              'CHICK-FIL-A',
              'THAI GOURMET',
              'KOLACHE FACTORY',
              'MOD PIZZA',
              'SANS BAR',
              'SMOOTHIE KING'
              ]

retail = ['AMAZON',
          'TARGET',
          'THE UPS STORE',
          '2ND AND CHARLES',
          'AMZN',
          'PARTY CITY',
          'OFFICEMAX'
          ]

subscription = ['JETBRAINS',
                'SPOTIFY',
                'GIRL SCOUTS',
                'ADT SECURITY',
                'AUDIBLE',
                'TIME',
                'APPLE.COM',
                'YMCA HOUSTON'
                ]

travel = ['UNITED',
          'AIRBNB',
          'TRAVEL RESERVATION'
          ]

utilities = ['ENTERGY',
             'CONSOLIDATED'
             ]

define_bucket('CAR', car)
define_bucket('CHILDCARE', childcare)
define_bucket('COFFEE', coffee)
define_bucket('DOCTOR', doctor)
define_bucket('ENTERTAINMENT', entertainment)
define_bucket('GIVING', giving)
define_bucket('GROCERY', grocery)
define_bucket('HOME IMPROVEMENT', home_improvement)
define_bucket('PERSONAL', personal)
define_bucket('PHARMACY', pharmacy)
define_bucket('RESTAURANT', restaurant)
define_bucket('RETAIL', retail)
define_bucket('SUBSCRIPTION', subscription)
define_bucket('TRAVEL', travel)
define_bucket('UTILITIES', utilities)

blanks = data.loc[data['Bucket'] == np.nan]
data.to_csv('test.csv')
blanks.to_csv('test1.csv')

print(data.head())
