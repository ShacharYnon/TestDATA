import pandas as pd



class LoadingData:

    def __init__(self ,path:str):
        self.path = path
        self.df = None

    def read_data(self ):
        """
        Gets a path to a file
        :return: The file is convenient to work with. or error
        """
        try:
            self.df = pd.read_csv(self.path)
            return self.df

        except Exception as e:
            print(f"ERROR from LoadingData.read_data: {e}")

    def print_head(self):
        """
        Receiving the file
        :return: Prints the first 5 lines of the file or error that there is no file
        """
        try:
            print(self.df.head(5))

        except Exception as e:
            print(f"ERROR from LoadingData.print_head: {e}")


    def print_info(self):
        try:
            print(self.df.info(5))

        except Exception as e:
            print(f"ERROR from LoadingData.print_head: {e}")



if __name__ =="__main__":

    data = LoadingData(r"C:\Users\Work\OneDrive\Desktop\NaiveBayesProject\TestDATA\data\tweets_dataset.csv")
    data.read_data()
    data.print_head()
    data.print_info()


