import pandas as pd
from pyspark.sql import SparkSession
import pyspark.sql.functions as FUN
#PYSPARK_DRIVER_PYTHON = 3.85
#PYSPARK_PYTHON = 3.85
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Same code as shown in SimpleApp.py


class MovieAnalyzer:
    
    def __init__(self):
        pass

    def open_movie_data(self, movie_data):
        #self.movie = pd.read_csv("data/movies.csv")
        #return self.movie
        print(movie_data.head(5))
        return self