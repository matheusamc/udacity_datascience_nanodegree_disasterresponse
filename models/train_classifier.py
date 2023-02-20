import sys

import pandas as pd
import numpy as np
import pickle

from sqlalchemy import create_engine

import re

import nltk
nltk.download(['punkt', 'wordnet','stopwords'])

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline 
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


def load_data(database_filepath):
    '''
    Load data from the  sql database, format it to a DataFrame, and assign the inputs X and outpts Y for the model.
    
    input: path to the sql database containing a a table called "Messages".
    
    output: formatted inputs X and outputs Y for the model.
    '''
    
    # load data from database
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table("Messages",engine)
    
    X = df['message']
    
    # drop column with only one class in the results
    Y = df[df[df.columns[df.columns!='child_alone']].columns[4:]]
        
    return X,Y,Y.columns

def tokenize(text):    
    '''
    Tokenize and lemmatize the messages.
    
    input: Message text.
    
    output: Tokenized message.    
    '''
    
    # lowering cases and removing marks
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    
    # tokenizing words
    words = word_tokenize(text)
    words = [w for w in words if w not in stopwords.words("english")]

    # lemmatizing words
    lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]    
    tokens = [WordNetLemmatizer().lemmatize(w, pos='v') for w in lemmed]
    
    return tokens


def build_model():
    '''
    Build a model with the best found parameters following the pipeline.
    
    input: None
    
    output: Built pipeline model.
    '''
    
    # model pipeline
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(LogisticRegression()))
    ])
    
    # Gride search model
    parameters = {'clf__estimator__solver':['lbfgs', 'liblinear', 'newton-cg'],
             'clf__estimator__C':[1.,.5,.25]}

    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    '''
    Evalate the model creating a report it.
    
    input: model -> built model; X_test -> model test inputs in an array; Y_test -> model test outputs in an array; 
    category_names -> list with the names of the categories to be classified.
    
    output: None. The report is printed.
    '''
    
    # result prediction
    Y_pred = model.predict(X_test)
    
    # classification reports
    for i in range(Y_pred.shape[1]):
        print("Category: {}".format(category_names[i]))
        print(classification_report(np.array(Y_test)[:,i], np.array(Y_pred)[:,i]))

    return

def save_model(model, model_filepath):
    '''
    Save the built model to a pickle file.
    
    input: model -> built model; model_filepath -> path to where the model pickle file will be stored.
    
    outpt: None. The file will be saved in a pickle file.
    '''
    #saving model in pickle
    file = open(model_filepath, 'wb')
    
    pickle.dump(model, file)
    
    file.close()

    return

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        model = model.best_estimator_
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
