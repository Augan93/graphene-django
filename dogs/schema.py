import graphene
from graphene_django.types import DjangoObjectType
from . models import Dog


class DogType(DjangoObjectType):
    class Meta:
        model = Dog


class Query(object):
    dogs = graphene.List(DogType)
    dog = graphene.Field(
        DogType,
        breed=graphene.String(),
    )

    def resolve_dogs(self, info, **kwargs):
        return Dog.objects.all()

    def resolve_dog(self, info, **kwargs):
        breed = kwargs.get('breed')

        if breed is not None:
            return Dog.objects.get(breed=breed)

        return None
