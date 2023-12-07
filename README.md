## Usage
I used SWAPI For the data source.

In order to run this project, you can run it locally or through docker.

### Run the server

#### Localy:
<ol>
<li> First make sure to have python and pip installed </li>
<li> cd into the TASK_PROJ folder </li>
</ol>

#### Then commands to run:
<ol>
<li> pip install -r requirements.txt</li>
<li> python app.py</li>
<li> python test_api.py // to run the unit testing</li>
</ol>

#### Docker:
<ol>
<li> First make sure to have docker</li>
<li> cd into the TASK_PROJ folder</li>
<li> make sure port 5000 on your local machine is empty</li>
</ol>

#### Then commands to run:
<ol>
<li> docker image build -t docker-flask-app .</li>
<li> docker run -p 5000:5000 -d docker-flask-app</li>
<li> docker exec -it conatinerID</li>
<li> python test_api.py // to run the unit testing</li>
</ol>

#### Using
The app will run on port 5000. You can access the server on localhost on
port 5000, so http://localhost:5000.
It will give you nothing but a greeting message "Hello world".

##### people routes
- Index: [get] http://localhost:5000/people will list all the people.
- Show: [get] http://localhost:3000/people/:name will list the information for that person with the `name` ex.`http://127.0.0.1:5000/people/Luke Skywalker`.


##### movies routes
- Index: [get] http://localhost:5000/movies will list all the movies.
- Show: [get] http://localhost:3000/movies/:id will list the information for that movie and the actors names with the `id` ex.`http://127.0.0.1:5000/movies/1`.


