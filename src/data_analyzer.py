from data_loader import LoadingData

class Analyzes:

    def __init__(self):
        data = LoadingData(r"C:\Users\Work\OneDrive\Desktop\NaiveBayesProject\TestDATA\data\tweets_dataset.csv")
        self.data = data.read_data()





    def sum_values_in_column_to_dict(self ,column:str):
        """
        Receives nothing
        but runs data loading functions
        :return: Summary of how many are in each column within a dictionary.
        """
        return self.data[column].value_counts().to_dict()


    def get_sum_tweet_by_category(self ,column:str):
        """
        It is possible to get an array or a result
        :param column: Gets a column name
        :return: and returns how many values it has and returns how many are in each category
        """
        df_column = self.data[column]
        mask_all = self.data[column].count()
        mask_1 = df_column[self.data[column] == 1].count()
        mask_0 = df_column[self.data[column] == 0].count()
        return (f"sum all tweets in column {column}: {mask_all} "
                f"\nsum tweets if is 1: {mask_1} "
                f"\nsum tweets if is 0: {mask_0}")
        # return {"get_sum_tweet_by_category:" :[{"sum all tweets in column" + column : mask_all} , {"sum tweets if is 1:" : mask_1 } , {"sum tweets if is 0:" : mask_0}]}

    def get_avg_word_in_text(self ,column:str):
        df_zero = self.data[self.data["Biased"] == 0]
        df_one = self.data[self.data["Biased"] == 1]

        total0 = 0
        dict0 = {}
        for  idx ,tweet in enumerate(df_zero["Text"]):

            dict0[idx] = len([word for word in tweet])
            total0 += dict0[idx]
            last_idx = idx
        avg_zero = total0 / last_idx + 1

        total1 = 0
        dict1 = {}
        for  idx ,tweet in enumerate(df_one["Text"]):

            dict1[idx] = len([word for word in tweet])
            total1 += dict1[idx]
            last_idx = idx
        avg_one = total1 / last_idx + 1

        total_all = (avg_one + avg_zero) / 2
        return f"avg one:{avg_one} ,avg zero:{avg_zero} ,total all:{total_all}"





if __name__=="__main__":
    analyze = Analyzes()
    # print(analyze.sum_values_in_column_to_dict("Biased"))
    # print(analyze.get_sum_tweet_by_category("Biased"))
    print(analyze.get_avg_word_in_text("Text"))