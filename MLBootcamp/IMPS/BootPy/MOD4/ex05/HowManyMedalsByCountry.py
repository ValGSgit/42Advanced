import pandas as pd

TEAM_SPORTS = [
    'Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing',
    'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
    'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
    'Rugby', 'Lacrosse', 'Polo',
]


def how_many_medals_by_country(df, country):
    """
    Returns {year: {'G': count, 'S': count, 'B': count}} for a given country.
    Team sports are deduplicated so the same medal is not counted multiple times.
    """
    country_df = df[df['Team'] == country]

    # For team sports, one Event entry per medal — keep one row per (Year, Sport, Event, Medal)
    # For individual sports, keep one row per (Year, Name, Event, Medal)
    individual = country_df[~country_df['Sport'].isin(TEAM_SPORTS)]
    team       = country_df[ country_df['Sport'].isin(TEAM_SPORTS)]

    # Deduplicate team medals: same event/year/medal = one team medal
    team = team.drop_duplicates(subset=['Year', 'Sport', 'Event', 'Medal'])

    combined = pd.concat([individual, team])
    medal_rows = combined[combined['Medal'].notna()]

    result = {}
    for year, group in medal_rows.groupby('Year'):
        result[year] = {
            'G': int((group['Medal'] == 'Gold').sum()),
            'S': int((group['Medal'] == 'Silver').sum()),
            'B': int((group['Medal'] == 'Bronze').sum()),
        }
    return result
