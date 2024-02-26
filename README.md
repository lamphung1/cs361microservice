# Microservice for randomly generated movie
The microservice uses "themoviedb" API to return a randomly selected movie in JSON format. 

## Request Data
User must import the randomMicroservice.py to their local workspace. An authentication token must be generated from themoviedb.com after account creation. <br/>
To use the microservice, the user should <br/>
  1) pip install the packages at the top of the randomMicroservice.py file , including dotenv (for python use) </br>
  2) create a local .env file and store the personal authentication token as a variable (the microservice will pull that token once called) </br>
  3) once valid token is accepted, import the randomMovie() method into your mainApp.py (your main CLI app) </br>
  4) perform your logic to ensure that the user wants a randomly generated movie (i.e if user_input == random...)  
  5) call the randomMovie() method (no parameters), to begin the request for a randomly generated movie </br>

## Recieve Data
  1) Once randomMovie() is called, the movie_ID of the newest database entry from 'themoviedb' will be obtained </br>
  2) A random movie_id will be generated in range(1, newest db entry movie_id) </br>
  3) That random movie_id will be used to extract a movie and it's details, and that will be returned to user in a dictionary </br> 
  4) The returned data can be stored in a variable, and the user can the parse through the data as they need to. </br>

![UML](https://github.com/lamphung1/cs361microservice/assets/114099999/b8529bf4-54ed-43bb-a3e4-ce7789e51893)

