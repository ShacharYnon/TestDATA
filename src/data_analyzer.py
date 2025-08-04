import pandas as pd
from data_loader import LoadingData

class Analyzes:

    def __init__(self):
        self.data = None



    def sum_values_in_column_to_dict(self ,column:str):
        """
        Receives nothing
        but runs data loading functions
        :return: Summary of how many are in each column within a dictionary.
        """
        data = LoadingData(r"C:\Users\Work\OneDrive\Desktop\NaiveBayesProject\TestDATA\data\tweets_dataset.csv")
        data = data.read_data()

        return data[column].value_counts().to_dict()




if __name__=="__main__":
    analyze = Analyzes()
    print(analyze.sum_values_in_column_to_dict("Biased"))
