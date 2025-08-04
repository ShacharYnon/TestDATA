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

    def the_three_longest_tweets(self):
        df_zero = self.data[self.data["Biased"] == 0]
        df_one = self.data[self.data["Biased"] == 1]

        dict_0 = {}
        for tweet in df_zero["Text"]:
            # dict_0[tweet] = len(tweet)
            dict_0[len(tweet)] = tweet
            # print(dict_0.keys())
            # print(dict_0.values())
            # print(dict_0)
        sor_11 = sorted(dict_0.keys(), key=lambda x: x, reverse=True)

        s = [sor_11.[i] for i in range(3)]
        print(s.)

        dict_1 = {}
        for tweet in df_one["Text"]:
            dict_1[tweet] = len(tweet)
        # print(dict_1.values())

        # sor_1 = sorted(dict_1.keys(), key=lambda x: dict_1.get(x, 0), reverse=True)
        sor_11 = sorted(dict_1.keys() ,key=lambda x:x ,reverse=True)
        list_1 = [dict_1[sor_11[i]] for i in range(3)]

        # print(list_1)


    def the_ten_most_common_words(self):
        pass




if __name__=="__main__":
    analyze = Analyzes()
    # print(analyze.sum_values_in_column_to_dict("Biased"))
    # print(analyze.get_sum_tweet_by_category("Biased"))
    # print(analyze.get_avg_word_in_text("Text"))
    print(analyze.the_three_longest_tweets())