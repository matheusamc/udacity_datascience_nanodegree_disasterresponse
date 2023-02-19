
<h1 align="center">Disaster Response</h1>

<p>A data based approach to classify messages related to disasters.</p>

<h2>Project Intro</h2>

<p>The purpose of this project is to find some clean and format a group of messages related to disaster an store then in a SQL Database. After that the messages are tokanized and a model is trained. An app to visualize data and classify a message with our trained model is provided.</p>

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
  <li>app</li>
    <ul>
      <li>template</li>
      <ul>
        <li>master.html</li>
        <li>go.html</li>
      </ul>
      <li>run.py - app run</li>
  </ul>
  <li>data</li>
  <ul>
    <li>disaster_categories.csv - data to process</li>
    <li>disaster_messages.csv - data to process</li>
    <li>process_data.py</li>
    <li>DisasterResponse.db - database to save clean data to</li>
  </ul>
  <li>models</li>
  <ul>
    <li>train_classifier.py - model training file</li>
    <li>classifier.pkl - saved model </li>
  </ul>
</ul>

<h2>Project Description</h2>
  <p>This project is part of the requirements of the Udacity Data Science Nanodegree. In this project we want to explorer the avaible data from Disaster Response messages and create a model to classify messages. An app is created to visualize some data and classify new messages.</p>

<h3>Run instruction:</h3>
<ul>
  <li>Run the proccess_data.py file to treat the data from the csv files and load then in a database with the correct format.</li>
  <li>Run the train classifier file to train the model.</li>
  <li>Run the rn file in the app folder to load the app.</li>
</ul>

<h2>Creator</h2>
<h3>Matheus Campos</h3>
  <ul>
    <li><a href="https://br.linkedin.com/in/matheus-de-abreu-monteiro-campos-90506aa2">LinkedIn</a></li>
    <li><a href="https://github.com/matheusamc">Github Repository</a></li>
  </ul>
