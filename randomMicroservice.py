# Name: Lam Phung
# Assignment: Microservice to return random movie from open source movie db
# https://developer.themoviedb.org/reference/intro/getting-started

from dotenv import load_dotenv
import os
import requests
import random

def randomMovie():
    load_dotenv()
    api_token = os.getenv('apiReadToken')

    # Get the id of the latest movie added 
    # https://developer.themoviedb.org/reference/movie-latest-id
    latest_url = "https://api.themoviedb.org/3/movie/latest"

    headers = {
        "accept": "application/json",
        "Authorization": api_token
    }

    response = requests.get(latest_url, headers=headers)
    response_text = response.json()

    id_limit = response_text['id']

    # Roll a random id from 1 -> that latest added id 
    # https://stackoverflow.com/questions/47833878/themoviedb-find-random-movie
    while True:
    # Try to recall data --> if 404, then reoll the number
    #https://developer.themoviedb.org/reference/movie-details
        random_id = random.randrange(1, id_limit)

        spec_url = f"https://api.themoviedb.org/3/movie/{random_id}?language=en-US"

        spec_response = requests.get(spec_url, headers=headers)
    # Return the random data that does work
        if spec_response.status_code == 200:
            movie_data = spec_response.json()
            if movie_data['adult'] == True:
                continue
            return movie_data
       
        
if __name__ == "__main__":
    print(randomMovie())