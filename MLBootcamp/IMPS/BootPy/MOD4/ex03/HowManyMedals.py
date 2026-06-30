def how_many_medals(df, name):
    """
    Returns a dict of dicts: {year: {'G': count, 'S': count, 'B': count}}
    Only includes years in which the athlete won at least one medal.
    """
    athlete = df[df['Name'] == name]

    result = {}
    for year, group in athlete.groupby('Year'):
        result[year] = {
            'G': int((group['Medal'] == 'Gold').sum()),
            'S': int((group['Medal'] == 'Silver').sum()),
            'B': int((group['Medal'] == 'Bronze').sum()),
        }
    return result
