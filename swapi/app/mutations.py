import graphene
from graphql_relay import from_global_id

from .models import People, Planet
from .types import PlanetType
from .types import PeopleType
from .utils import generic_model_mutation_process


class AddUpdatePlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)
        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return AddUpdatePlanetMutation(planet=planet)


class AddUpdatePeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(require=True)
        height = graphene.String(require=False)
        mass = graphene.String(require=False)
        hair_color = graphene.String(require=False)
        skin_color = graphene.String(requiere=False)
        eye_color = graphene.String(require=False)
        birth_year = graphene.String(require=False)
        gender = graphene.String(require=True)
        home_world = graphene.String(require=True)

    people = graphene.Field(PeopleType)
    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)
        raw_home_world = input.get('home_world', None)

        if raw_home_world:
            planet_id = from_global_id(raw_home_world)[1]
            ojb = Planet.objects.get(id=planet_id)
            input.pop('home_world')
            input['home_world'] = ojb

        data = {'model': People, 'data': input}

        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        people = generic_model_mutation_process(**data)
        return AddUpdatePeopleMutation(people=people)
