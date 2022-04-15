import json

from graphene_django.utils.testing import GraphQLTestCase

from swapi.schema import schema


class FirstTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_planet_query(self):
        response = self.query(
            '''
                query{
                  allPlanets {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPlanets']['edges']), 61)

    def test_people_query(self):
        response = self.query(
            '''
              query {
                  allPeople{
                      edges{
                          node{
                              id
                              name
                          }
                      }
                  }
              }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPeople']['edges']), 84)

    def test_people_mutation(self):
        add_response = self.query(
            '''
                mutation addNewPeople{
                    addUpdatePeopleMutation(input:{name: "Kylo Ren", gender: "male", height: "189", mass: "89", hairColor: "black", eyeColor: "brown", skinColor: "light", birthYear: "5ABY", homeWorld: "UGxhbmV0VHlwZToz"}){
                        people{
                            id,
                            name,
                            gender,
                            height,
                            mass,
                            hairColor,
                            eyeColor,
                            skinColor,
                            birthYear
                            homeWorld{
                                name,
                            }
                        }
                    }
                }
            ''',
        )
        self.assertResponseNoErrors(add_response)

        add_content = json.loads(add_response.content)
        add_expected_result = {'id': 'UGVvcGxlVHlwZTo4OQ==', 'name': 'Kylo Ren', 'gender': 'male', 'height': '189',
                               'mass': '89', 'hairColor': 'black', 'eyeColor': 'brown', 'skinColor': 'light',
                               'birthYear': '5ABY', 'homeWorld': {'name': 'Yavin IV'}}
        self.assertEqual(add_content['data']['addUpdatePeopleMutation']['people'], add_expected_result)

        udpdate_response = self.query(
            '''
                mutation UpdatePeople{
                    addUpdatePeopleMutation(input:{id: "UGVvcGxlVHlwZTo4OQ==", name: "Kylo Ren (Ben Solo)", homeWorld: "UGxhbmV0VHlwZToz"}){
                        people{
                            name,
                            gender,
                            height,
                            mass,
                            hairColor,
                            eyeColor,
                            skinColor,
                            birthYear
                            homeWorld{
                                name,
                            }
                        }
                    }
                }
            ''',
        )
        self.assertResponseNoErrors(udpdate_response)

        update_content = json.loads(udpdate_response.content)
        update_expected_result = {'name': 'Kylo Ren (Ben Solo)', 'gender': 'male',
                                  'height': '189', 'mass': '89', 'hairColor': 'black', 'eyeColor': 'brown',
                                  'skinColor': 'light', 'birthYear': '5ABY', 'homeWorld': {'name': 'Yavin IV'}}
        self.assertEqual(update_content['data']['addUpdatePeopleMutation']['people'], update_expected_result)

    def test_planet_mutation(self):
        add_response = self.query(
            '''
                mutation addNewPlanet{
                    addUpdatePlanetMutation(input:{name: "Tatooine", rotationPeriod: "23", orbitalPeriod: "304", diameter: "10465", climate: "arid", gravity: "1 standard", terrain: "desert", surfaceWater: "1", population: "200000"}){
                        planet{
                            id,
                            name,
                            rotationPeriod,
                            orbitalPeriod,
                            diameter,
                            climate,
                            gravity,
                            terrain,
                            surfaceWater,
                            population
                        }
                    }
                }
            ''',
        )
        self.assertResponseNoErrors(add_response)

        add_content = json.loads(add_response.content)
        add_expected_result = {'id': 'UGxhbmV0VHlwZTo2Mw==', 'name': 'Tatooine', 'rotationPeriod': '23', 'orbitalPeriod': '304',
                               'diameter': '10465', 'climate': 'arid', 'gravity': '1 standard', 'terrain': 'desert',
                               'surfaceWater': '1', 'population': '200000'}
        self.assertEqual(add_content['data']['addUpdatePlanetMutation']['planet'], add_expected_result)

        udpdate_response = self.query(
            '''
                mutation UpdatePlanet{
                    addUpdatePlanetMutation(input:{id: "UGxhbmV0VHlwZTo2Mw==", name: "Tatooine", rotationPeriod: "23", orbitalPeriod: "304", diameter: "10465", climate: "arid", gravity: "1 standard", terrain: "desert", surfaceWater: "1", population: "200000"}){
                        planet{
                            id,
                            name,
                            rotationPeriod,
                            orbitalPeriod,
                            diameter,
                            climate,
                            gravity,
                            terrain,
                            surfaceWater,
                            population
                        }
                    }
                }
            ''',
        )

        self.assertResponseNoErrors(udpdate_response)
        
        update_content = json.loads(udpdate_response.content)
        update_expected_result = {'id': 'UGxhbmV0VHlwZTo2Mw==', 'name': 'Tatooine', 'rotationPeriod': '23', 'orbitalPeriod': '304',
                               'diameter': '10465', 'climate': 'arid', 'gravity': '1 standard', 'terrain': 'desert',
                               'surfaceWater': '1', 'population': '200000'}
        self.assertEqual(update_content['data']['addUpdatePlanetMutation']['planet'], update_expected_result)