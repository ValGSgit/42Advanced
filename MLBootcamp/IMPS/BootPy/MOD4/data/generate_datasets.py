"""
Generate synthetic datasets for MOD4 Pandas exercises.
Run: python generate_datasets.py
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

# ── adult_data.csv (32 561 x 15) ─────────────────────────────────────────────
N = 32561
workclasses   = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',
                 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
educations    = ['Bachelors','Some-college','11th','HS-grad','Prof-school',
                 'Assoc-acdm','Assoc-voc','9th','7th-8th','12th','Masters',
                 '1st-4th','10th','Doctorate','5th-6th','Preschool']
marital       = ['Married-civ-spouse','Divorced','Never-married','Separated',
                 'Widowed','Married-spouse-absent','Married-AF-spouse']
occupations   = ['Tech-support','Craft-repair','Other-service','Sales',
                 'Exec-managerial','Prof-specialty','Handlers-cleaners',
                 'Machine-op-inspct','Adm-clerical','Farming-fishing',
                 'Transport-moving','Priv-house-serv','Protective-serv','Armed-Forces']
relationships = ['Wife','Own-child','Husband','Not-in-family','Other-relative','Unmarried']
races         = ['White','Asian-Pac-Islander','Amer-Indian-Eskimo','Other','Black']
sexes         = ['Male','Female']
countries     = ['United-States','Cuba','Jamaica','India','Mexico','South','Japan',
                 'Philippines','Germany','Puerto-Rico','Canada','El-Salvador',
                 'Dominican-Republic','Laos','Columbia','Thailand','Hungary',
                 'Honduras','Haiti','Vietnam','Portugal']
salaries      = ['<=50K', '>50K']

adult = pd.DataFrame({
    'age':              rng.integers(17, 91, N),
    'workclass':        rng.choice(workclasses, N),
    'fnlwgt':           rng.integers(12285, 1490400, N),
    'education':        rng.choice(educations, N),
    'education-num':    rng.integers(1, 17, N),
    'marital-status':   rng.choice(marital, N),
    'occupation':       rng.choice(occupations, N),
    'relationship':     rng.choice(relationships, N),
    'race':             rng.choice(races, N),
    'sex':              rng.choice(sexes, N),
    'capital-gain':     rng.integers(0, 99999, N),
    'capital-loss':     rng.integers(0, 4356, N),
    'hours-per-week':   rng.integers(1, 100, N),
    'native-country':   rng.choice(countries, N),
    'salary':           rng.choice(salaries, N, p=[0.75, 0.25]),
})
adult.to_csv('adult_data.csv', index=False)
print(f"adult_data.csv:       {adult.shape[0]} x {adult.shape[1]}")

# ── athlete_events.csv (271 116 x 15) ────────────────────────────────────────
sports = ['Athletics','Swimming','Gymnastics','Cycling','Shooting','Rowing',
          'Football','Basketball','Tennis','Volleyball','Hockey','Sailing',
          'Weightlifting','Wrestling','Boxing','Diving','Fencing','Canoeing',
          'Judo','Equestrian','Handball','Water Polo','Badminton','Archery',
          'Alpine Skiing','Cross Country Skiing','Bobsleigh','Figure Skating',
          'Speed Skating','Ice Hockey','Softball','Baseball','Rugby Sevens',
          'Synchronized Swimming','Rowing','Triathlon','Modern Pentathlon']

team_sports = ['Basketball','Football','Handball','Water Polo','Hockey','Rowing',
               'Bobsleigh','Softball','Volleyball','Synchronized Swimming',
               'Baseball','Rugby Sevens','Badminton','Sailing']

countries_noc = {
    'USA': 'United States', 'GBR': 'Great Britain', 'GER': 'Germany',
    'FRA': 'France',        'AUS': 'Australia',     'RUS': 'Russia',
    'CHN': 'China',         'ITA': 'Italy',          'CAN': 'Canada',
    'JPN': 'Japan',         'NED': 'Netherlands',    'SWE': 'Sweden',
    'NOR': 'Norway',        'FIN': 'Finland',        'HUN': 'Hungary',
    'KOR': 'South Korea',   'BRA': 'Brazil',         'CUB': 'Cuba',
    'POL': 'Poland',        'ROU': 'Romania',
}
nocs   = list(countries_noc.keys())
teams  = list(countries_noc.values())

summer_years = [1896,1900,1904,1906,1908,1912,1920,1924,1928,1932,1936,
                1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,
                1992,1996,2000,2004,2008,2012,2016]
winter_years = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,
                1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]

summer_cities = {
    1896:'Athina',1900:'Paris',1904:'St. Louis',1906:'Athina',1908:'London',
    1912:'Stockholm',1920:'Antwerpen',1924:'Paris',1928:'Amsterdam',
    1932:'Los Angeles',1936:'Berlin',1948:'London',1952:'Helsinki',
    1956:'Melbourne',1960:'Roma',1964:'Tokyo',1968:'Mexico City',
    1972:'Munich',1976:'Montreal',1980:'Moskva',1984:'Los Angeles',
    1988:'Seoul',1992:'Barcelona',1996:'Atlanta',2000:'Sydney',
    2004:'Athina',2008:'Beijing',2012:'London',2016:'Rio de Janeiro',
}
winter_cities = {
    1924:'Chamonix',1928:'Sankt Moritz',1932:'Lake Placid',1936:'Garmisch-Partenkirchen',
    1948:'Sankt Moritz',1952:'Oslo',1956:'Cortina d\'Ampezzo',1960:'Squaw Valley',
    1964:'Innsbruck',1968:'Grenoble',1972:'Sapporo',1976:'Innsbruck',
    1980:'Lake Placid',1984:'Sarajevo',1988:'Calgary',1992:'Albertville',
    1994:'Lillehammer',1998:'Nagano',2002:'Salt Lake City',2006:'Turin',
    2010:'Vancouver',2014:'Sochi',
}

rows = []
athlete_id = 1
# Generate ~270k rows across summer + a few winter games
for year in summer_years:
    city = summer_cities[year]
    n_athletes = rng.integers(3000, 12000)
    for _ in range(n_athletes):
        sex    = rng.choice(['M', 'F'], p=[0.7, 0.3])
        age    = rng.integers(14, 45) if year > 1920 else rng.integers(16, 50)
        noc_i  = rng.integers(len(nocs))
        noc    = nocs[noc_i]
        team   = teams[noc_i]
        sport  = rng.choice(sports)
        event  = f"{sport} Men's Event" if sex == 'M' else f"{sport} Women's Event"
        medal  = rng.choice(['Gold','Silver','Bronze', np.nan, np.nan, np.nan,
                             np.nan, np.nan, np.nan, np.nan], p=[.05,.05,.05,
                             .85/7,.85/7,.85/7,.85/7,.85/7,.85/7,.85/7])
        rows.append({
            'ID': athlete_id, 'Name': f'Athlete_{athlete_id}',
            'Sex': sex, 'Age': float(age),
            'Height': float(rng.integers(150, 210)),
            'Weight': float(rng.integers(50, 110)),
            'Team': team, 'NOC': noc,
            'Games': f'{year} Summer', 'Year': year,
            'Season': 'Summer', 'City': city,
            'Sport': sport, 'Event': event,
            'Medal': medal,
        })
        athlete_id += 1

# Add a few winter games rows to reach ~271k
for year in winter_years[-8:]:
    city = winter_cities[year]
    for _ in range(rng.integers(500, 2000)):
        sex    = rng.choice(['M', 'F'], p=[0.6, 0.4])
        noc_i  = rng.integers(len(nocs))
        sport  = rng.choice(['Alpine Skiing','Cross Country Skiing','Bobsleigh',
                             'Figure Skating','Speed Skating','Ice Hockey'])
        medal  = rng.choice(['Gold','Silver','Bronze', np.nan], p=[.05,.05,.05,.85])
        rows.append({
            'ID': athlete_id, 'Name': f'Athlete_{athlete_id}',
            'Sex': sex, 'Age': float(rng.integers(16, 40)),
            'Height': float(rng.integers(155, 205)),
            'Weight': float(rng.integers(55, 105)),
            'Team': teams[noc_i], 'NOC': nocs[noc_i],
            'Games': f'{year} Winter', 'Year': year,
            'Season': 'Winter', 'City': city,
            'Sport': sport, 'Event': f'{sport} Event',
            'Medal': medal,
        })
        athlete_id += 1

# Add a named athlete with known medals for ex03 testing
named_athlete = 'Kjetil Andr Aamodt'
known_medals = [
    (1992,'Gold'),(1992,'Bronze'),
    (1994,'Silver'),(1994,'Silver'),(1994,'Bronze'),
    (1998, np.nan),
    (2002,'Gold'),(2002,'Gold'),
    (2006,'Gold'),
]
for year, medal in known_medals:
    city = summer_cities.get(year, winter_cities.get(year, 'Unknown'))
    rows.append({
        'ID': athlete_id, 'Name': named_athlete,
        'Sex': 'M', 'Age': float(20 + (year - 1992)),
        'Height': 180.0, 'Weight': 80.0,
        'Team': 'Norway', 'NOC': 'NOR',
        'Games': f'{year} Winter', 'Year': year,
        'Season': 'Winter', 'City': winter_cities.get(year, 'Unknown'),
        'Sport': 'Alpine Skiing', 'Event': "Alpine Skiing Men's Super G",
        'Medal': medal,
    })
    athlete_id += 1

df = pd.DataFrame(rows)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv('athlete_events.csv', index=False)
print(f"athlete_events.csv:   {df.shape[0]} x {df.shape[1]}")
print("Done.")
