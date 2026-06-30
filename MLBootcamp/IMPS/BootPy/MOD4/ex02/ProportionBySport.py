def proportion_by_sport(df, year, sport, gender):
    """
    Returns the proportion (float in [0,1]) of participants in `sport`
    among all participants of `gender` in the given Olympic `year`.
    Duplicates are dropped on (Name, Sport) so team-sport athletes count once.
    """
    year_gender = df[(df['Year'] == year) & (df['Sex'] == gender)]
    # Drop duplicates: count each unique athlete once per sport
    year_gender = year_gender.drop_duplicates(subset=['Name', 'Sport'])

    total = len(year_gender)
    if total == 0:
        return 0.0

    in_sport = len(year_gender[year_gender['Sport'] == sport])
    return in_sport / total
