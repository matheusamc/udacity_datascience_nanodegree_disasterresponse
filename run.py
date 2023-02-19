import json
import plotly
import pandas as pd

import re

import nltk
nltk.download(['punkt', 'wordnet','stopwords'])
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    
    words = word_tokenize(text)
    words = [w for w in words if w not in stopwords.words("english")]

    lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]    
    tokens = [WordNetLemmatizer().lemmatize(w, pos='v') for w in lemmed]
    
    return tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('Messages', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    #Graph 1
    genre_counts = df.groupby('genre').count()['message']
    genre_names = [ x.capitalize() for x in list(genre_counts.index)]
    
    #Graph 2
    categories_counts = 100*df[df.columns[4:]].sum(axis=0)/df.shape[0]
    categories_names = [x.replace('_', ' ').capitalize() for x in df.columns[4:]]
    
    #Graph 3
    weather_counts = 100*df[df['weather_related'] == 1][['floods', 'storm', 'fire', 'earthquake', 'cold']].sum(axis=0)/df[df['weather_related'] == 1].shape[0]
    weather_names = ['Floods', 'Storm', 'Fire', 'Earthquake', 'Cold']
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    #Graph 1
    graphs = [
        
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        # Graph 2
        {
            'data': [
                Bar(
                    x=categories_names,
                    y=categories_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Categories',
                'yaxis': {                          
                    'title': "Count [%]"
                },
                'xaxis': {              
                    'title': "Category",
                    'ticksuffix' : "  ",
                    'tickangle' : 45
                },
                'margin' : {'b' : 150
                }
            }
        },
        
        # Graph 3
        {
            'data': [
                Bar(
                    x=weather_names,
                    y=weather_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Weather Related Messages',
                'yaxis': {                          
                    'title': "Count [%]"
                },
                'xaxis': {              
                    'title': "Category",
                    'ticksuffix' : "  ",
                    'tickangle' : 45
                },
                'margin' : {'b' : 150
                }
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3000, debug=True)


if __name__ == '__main__':
    main()