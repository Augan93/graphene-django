import graphene
import graphql_jwt
import ingredients.schema
import movies.schema
import user.schema


class Query(ingredients.schema.Query, movies.schema.Query, user.schema.Query, graphene.ObjectType):
    pass


class Mutation(movies.schema.Mutation, user.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query,
                         mutation=Mutation)

