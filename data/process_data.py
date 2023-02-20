import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath): 
    '''
    Load data from csv files ans store in dataframe.
    
    input: messages_filepath -> path to the csv message file; categories_filepath -> path to the csv category file.
    
    output: df -> dataframe with processed data.
    '''
    
    #load data sets
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    # merge datasets
    df = messages.merge(categories)

    # expand categories datas
    categories = df.categories.str.split(";",expand=True)
    
    # find categories names
    row = categories.iloc[0]
    
    category_colnames = [str(x).split("-")[0] for x in row]
    
    categories.columns = category_colnames
    
    # keep only the values of categories
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = [ int(str(x).split("-")[1]) for x in categories[column]]
    
    # drop categories column
    df.drop(['categories'], axis=1, inplace = True)
    
    #concat categories to dataframe
    df = pd.concat([df,categories], axis=1)

    return df

def clean_data(df):
    '''
    Remove duplicate data.
    
    input: df -> dataframe with stored messages.
    
    output: df -> dataframe after cleaning.
    '''
    
    # remove duplicates
    df = df.drop_duplicates(subset=['id'], keep='first')
    
    return df

def save_data(df, database_filename):
    '''
    Save the dataframe into a sql database.
    
    input: df -> dataframe with the messages; database_filename -> file where the database will be saved.
    
    output: None. Database saved into the asigned path.
    '''
    
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('Messages', engine, index=False, if_exists='replace')
    return  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
