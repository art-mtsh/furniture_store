import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

import os
from items.models import ItemPhoto, Items, ItemMaterials
from django.core.files import File


def process_directory(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            local_path = os.path.join(root, file)
            print(local_path)
            parts = file.split('.')

            material_type = parts[0]
            manufacturer = parts[1]
            title = parts[2]
            colour = parts[3]

            # print(f'-| {material_type}')
            # print(f'-|-| {manufacturer}')
            # print(f'-|-|-| {title}')
            # print(f'-|-|-|-| {colour}')
            #
            f = open(local_path, 'rb')
            the_file = File(f)

            ItemMaterials.objects.create(
                material_type=material_type,
                manufacturer=manufacturer,
                title=title,
                colour=colour,
                photo=the_file
            )
            f.close()


process_directory("D:\IT\Pycharm Projects\MyStore CREDENTIALS\МАТЕРІАЛИ\ДСП")
