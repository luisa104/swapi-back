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
