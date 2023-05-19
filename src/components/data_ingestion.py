import os
# For sys we are importing bcoz we will be using our custom exception
import sys
# For exception we need to import it from source folder in our project folder & we really need to call this customexception
from src.exception import CustomException
# Along this also we also require logger
# So then we will be able to log in the data ingestion part  
from src.logger import logging

# Along this we'll also be using pandas bcox we need to work with dataframe
import pandas as pd
# We will be using sklearn.model_selection to import train test split
from sklearn.model_selection import train_test_split
# So here we will use one more very import class i.e dataclass
# This basically used to create class variables in short
from dataclasses import dataclass



# The reason why we are making this data ingestion config , bocz in my data ingestion component any input that is required 
# anything that i specificaly require i'll probably give through this particular data ingestion config.
# So probably you data transformation also , you will probably go ahead and write Data Transformation Config bcoz there
# also you'll be requiring some kinds of inputs 

# We will use this decorator dataclass - as it is very helpful bcoz inside a class to define a class variable you basically -,
# use init , but if you write this dataclass you will be able to directly define your class variable  
@dataclass
class DataIngestionConfig:
    # so here i define my class variable train_data_path , which will of string or str type and here we will give some path
    train_data_path : str = os.path.join("artifacts","train.csv")
    # So initially this will be this path which we are giving to our data ingestion component and data ingestion output will save,
    # all the file in this path , like the train data it will be saved in this path , 
    # So all the outputs will basically be showed inside this artifacts folder and have this file name train.csv  
    # So basically this is the input we are giving later on my data ingestion will save the train.csv file in this particular path.
    test_data_path :str = os.path.join("artifacts","test.csv")
    # Similary we will do it for test data
    raw_data_path :str = os.path.join('artifacts',"data.csv")
    # & one more path & for that we also require the initial path that is raw data path , initially how my raw data is
    # That we will save in the form of data.csv



# Lets start 
class DataIngestion:
    def __init__(self):
        # So we create this variable called ingestion_config and this ingestion_config will consist of these paths,
        # That we wrote in DataIngestionConfig , bcoz that is the input that we really need to initialize DataIngestionConfig()
        # So as soon as this gets executed when we call this particular class DataIngestion , these three paths will get saved
        # inside this particular class Variable.
        self.ingestion_config=DataIngestionConfig() # And inside this variable you have a subobject itself

    # Now we try to create our own function
    # So what this initiate_data_ingestion will do is , if your data is stored in some databases , i'll write my code 
    # here to read from that database 
    def initiate_data_ingestion(self):
        # Initially lets read the dataset in a very easy way.
        logging.info("Enter the data ingestion method or component")
        # Now lets write try method , bcoz any time my error will come i'll probably write in this way 
        try:
            # Right now we are reading it from the csv file 
            df=pd.read_csv('notebook\data\stud.csv')
            # Now we can log another log inside it
            logging.info("Read the dataset as dataframe")

            # Now inside this we will write self.ingestion config and inside ingestion config have the parameter which is 
            # Train data path.
            # Now inside this makedirectory i have to combine the directory path 
            # which is os.path.dirname , so what it does is it basically getting the directory name ,with respect to this 
            # Specific path , and here we also give another parameter which is exist_ok=True
            # So if it is already there we will keep that particular folder , we don't have to delete and create it again
            # So this is what we will  be doing with respect to the os.makesdirectory 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)


            # So what'll do here 
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test Split initiated")
            train_set , test_set = train_test_split(df,test_size=0.2,random_state=42)
            # Once we get our train and test set
            # Now we will save this in same atrifact folder by just changing form raw data path to train_data_path
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            # Similarly for the test also we can do the same thing 
            # So now we have done the splitting and now saving it inside the artifacts folder 
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")
            # So usually in ingestion these all things basically happen 

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        
        except Exception as e:
            # Now once we do this automatically our exception will be raised 
            raise CustomException(e,sys)



# Now lets try to run this using scripting as __name__ == __main__
if __name__ == "__main__":
    # So we will initiate it , and take data ingestion object 
    obj = DataIngestion()
    obj.initiate_data_ingestion()

    # Once we execute all this my artifacts folder will be created , and my logs 4th file will also get create as you 
    # can currently see there are only 4 files there 

