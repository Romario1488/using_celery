import random
import string

from celery import shared_task

import os

from .models import MyModel


@shared_task
# Creating an object with random parameters
def create_new_object():
    random_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    dirname = 'media/'
    files = os.listdir(dirname)
    random_picture = random.randint(0, len(files))
    new_object = MyModel.objects.create(name=random_name, image=files[random_picture-1])
    return new_object.name


@shared_task
# A function that removes the oldest objects
def cleaning_up():
    obj = MyModel.objects.all()
    while True:
        if len(obj) > 5:
            MyModel.objects.filter(name=obj[0]).delete()
        else:
            break
