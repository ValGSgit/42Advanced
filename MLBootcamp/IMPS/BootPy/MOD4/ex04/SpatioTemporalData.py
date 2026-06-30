class SpatioTemporalData:

    def __init__(self, df):
        self.df = df

    def when(self, location):
        """Returns a list of years in which the Olympics were held at location."""
        years = self.df[self.df['City'] == location]['Year'].unique().tolist()
        return sorted(years, reverse=True)

    def where(self, year):
        """Returns a list of cities that hosted the Olympics in the given year."""
        cities = self.df[self.df['Year'] == year]['City'].unique().tolist()
        return cities
