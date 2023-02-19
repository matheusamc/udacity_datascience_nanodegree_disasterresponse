
<h1 align="center">Disaster Response</h1>

<p>A data based approach to classify messages related to disasters.</p>

<h2>Project Intro</h2>

<p>The purpose of this project is to find some clean and format a group of messages related to disaster an store then in a SQL Database. After that the messages are tokanized and a model is trained.</p>

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
      <li>run.py</li>
  </ul>
  <li>data</li>
  <li>models</li>
  - app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 
</ul>

<h2>Project Description</h2>
  <p>This project is part of the requirements of the Udacity Data Science Nanodegree. In this project we want to explorer the avaible data from <a href="http://insideairbnb.com/rio-de-janeiro/">Inside Airbnb</a> for the listings in Rio de Janeiro for the year of 2022. Taking a closer look at this data we expect to answer the following questions:</p>

  <ul>
    <li><i>In what neighbourhood to stay in Rio?</i></li>
    <li><i>What price weexpected to pay in these places during the main events in the city?</i></li>
    <li><i>What time of the year to come paying better prices?</i></li>
  </ul>

  <p>We will make use of some Python libraries in a Jupyter notebook and the knowledge achieved in the course to answer these questions.</p>

<h2>Summary of Results</h2>
  <p>After analisyng the avaiable data we answered the three questions above:</p>
  <ul>
    <li>The locations with most listing in Airbnb which include Copacabana, Ipanema, Barra da Tijuca, Leblon, Botafogo, Santa Teresa, Centro, Flamengo, Leme and Laranjeiras.</li>
    <li>During New Years' Eve and Carnival, someone would expect to pay from US$90/day to US$350/day.</li>
    <li>The period from the end of July to the beggining of November is the one with best prices.</li>
  </ul>
  <p>The results are detailed presented in <a href="https://medium.com/@matheusamc/cidade-maravilhosa-when-to-visit-1a35d1ba7e1f">this post</a>.</p>
    
<h2>Creator</h2>
<h3>Matheus Campos</h3>
  <ul>
    <li><a href="https://br.linkedin.com/in/matheus-de-abreu-monteiro-campos-90506aa2">LinkedIn</a></li>
    <li><a href="https://github.com/matheusamc">Github Repository</a></li>
  </ul>
  
<h2>Acknowledgements</h2>
    <p>I would like to acknowledge Inside Airbnb for the avaible data.</p>
