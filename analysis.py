import pandas as pd
class MovieAnalyzer:
    
    def __init__(self):
        self.movie = None

    def open_movie_data(self):
        self.movie = pd.read_csv("data/movies.csv")
        return self.movie