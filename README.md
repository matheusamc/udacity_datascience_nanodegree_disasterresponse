
<h1 align="center">Disaster Response</h1>

<p>A data based approach to classify messages related to disasters.</p>

<h2>Project Intro</h2>

<p>Following a disaster there is the need to make an efficient response as soon as possible in order to provide assitance to maintain life, improve help and support affected people. There may be different needs for the affected people and usually there are different organizations responsable for each problem. In times like these multiple messages asking for help will be received and it is important to assign a the responsability to answer the call for a organization capable of solving that. The aim of this project is to provide a classifier that after a received message, will indicate to what category the message belongs and, thus, help to get a faster and correct response to the needs of affected people. To achieve the purpose of this project we will need to clean and format a group of messages related to disaster and store then in a SQL Database. After that the messages will be tokanized and a classification model will be trained. An app to visualize data and classify a message with our trained model will be provided.</p>

<h3>Libraries</h3>
<ul>
  <li>Pandas</li>
  <li>Numpy</li>
  <li>Sqlalchemy</li>
  <li>Pickle</li>
  <li>Re</li>
  <li>Nltk</li>
  <li>Sklearn</li>
</ul>

<h3>Files Structure</h3>
<ul>
  <li><a><a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/tree/main/app">app</a></li>
    <ul>
      <li><a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/tree/main/app/templates">template</a></li>
      <ul>
        <li><a href = "https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/app/templates/master.html">master.html</a> - master template</li>
        <li><a href = "https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/app/templates/go.html">go.html</a> - go template</li>
      </ul>
      <li><a href = "https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/app/run.py">run.py</a> - app run</li>
  </ul>
  <li><a href = "https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/tree/main/data">data</a></li>
  <ul>
    <li><a href = "https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/data/disaster_categories.csv">disaster_categories.csv</a> - data to process</li>
    <li><a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/data/disaster_messages.csv">disaster_messages.csv</a> - data to process</li>
    <li><a href = "https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/data/process_data.py">process_data.py</a> - data processing file</li>
    <li><a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/data/DisasterResponse.db">DisasterResponse.db</a> - database to save clean data to</li>
  </ul>
  <li><a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/tree/main/models">models</a></li>
  <ul>
    <li><a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/models/train_classifier.py">train_classifier.py</a> - model training file</li>
    <li><a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/models/classifier.pkl">classifier.pkl</a> - saved model</li>
  </ul>
</ul>

<h2>Project Description</h2>
  <p>This project is part of the requirements of the Udacity Data Science Nanodegree. In this project we want to explorer the avaible data from Disaster Response messages and create a model to classify messages. An app is created to visualize some data and classify new messages.</p>

<h3>Run instruction:</h3>
<ul>
  <li>Run the <a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/data/process_data.py">process_data.py</a> file to treat the data from the csv files and load then in a database with the correct format. (see the <a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/ETL%20Pipeline%20Preparation.ipynb">ETL notebook</a> to have a better look at the processing done to the data and test any changes).</li>
  <li>Run the <a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/models/train_classifier.py">train classifier file</a> to train the model (see the <a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/ML%20Pipeline%20Preparation.ipynb">ML notebook</a> to look at the different models evaluated and find a better model if there is any change in the data).</li>
  <li>Run the <a href="https://github.com/matheusamc/udacity_datascience_nanodegree_disasterresponse/blob/main/app/run.py">run file</a> in the app folder to load the app.</li>
</ul>

<h2>Creator</h2>
<h3>Matheus Campos</h3>
  <ul>
    <li><a href="https://br.linkedin.com/in/matheus-de-abreu-monteiro-campos-90506aa2">LinkedIn</a></li>
    <li><a href="https://github.com/matheusamc">Github Repository</a></li>
  </ul>
