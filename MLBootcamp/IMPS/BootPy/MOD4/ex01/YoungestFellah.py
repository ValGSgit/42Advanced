def youngest_fellah(df, year):
    """
    Returns a dict with the age of the youngest woman and man
    who participated in the Olympics for the given year.
    """
    year_df = df[df['Year'] == year]
    youngest_f = year_df[year_df['Sex'] == 'F']['Age'].min() #smallest value in list of female ages in given data frame of year 
    youngest_m = year_df[year_df['Sex'] == 'M']['Age'].min()
    return {'f': youngest_f, 'm': youngest_m} # dictionary returning f with youngest female and m as youngest male
