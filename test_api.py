import unittest
import requests


class TestAPI(unittest.TestCase):
  
  get_actor_details_Expected_result={
    "count": 1,
    "next": None,
    "previous": None,
    "results": [
        {
            "birth_year": "19BBY",
            "created": "2014-12-09T13:50:51.644000Z",
            "edited": "2014-12-20T21:17:56.891000Z",
            "eye_color": "blue",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "gender": "male",
            "hair_color": "blond",
            "height": "172",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "mass": "77",
            "name": "Luke Skywalker",
            "skin_color": "fair",
            "species": [],
            "starships": [
                "https://swapi.dev/api/starships/12/",
                "https://swapi.dev/api/starships/22/"
            ],
            "url": "https://swapi.dev/api/people/1/",
            "vehicles": [
                "https://swapi.dev/api/vehicles/14/",
                "https://swapi.dev/api/vehicles/30/"
            ]
        }
    ]
  }

  def get_all_people(self):
    resp= requests.get('http://127.0.0.1:5000/people')
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(len(resp.json()), 10)
    print("get_all_people test completed")
  
  def get_all_movies(self):
    resp= requests.get('http://127.0.0.1:5000/movies')
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(len(resp.json()), 6)
    print("get_all_movies test completed")
  
  def get_movie_details(self):
    resp= requests.get('http://127.0.0.1:5000/movies/1')
    self.assertEqual(resp.status_code, 200)
    print("get_movie_details and include actor names test completed")
  
  def get_actor_details(self):
    resp= requests.get('http://127.0.0.1:5000/people/Luke Skywalker')
    self.assertEqual(resp.status_code, 200)
    self.assertDictEqual(resp.json(), self.get_actor_details_Expected_result)
    print("get_actor_details search by name test completed")





if __name__ =='__main__':
  tester=TestAPI()

  tester.get_all_people()
  tester.get_all_movies()
  tester.get_movie_details()
  tester.get_actor_details()