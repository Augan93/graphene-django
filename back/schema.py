import graphene
import ingredients.schema
import movies.schema


class Query(ingredients.schema.Query, movies.schema.Query, graphene.ObjectType):
    pass


class Mutation(movies.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,
                         mutation=Mutation)

