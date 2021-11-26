from .models import MyModel


def get_objects():
    objects = MyModel.objects.all()
    return objects
