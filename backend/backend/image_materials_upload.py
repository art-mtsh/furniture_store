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

            f = open(local_path, 'rb')
            the_file = File(f)

            # the_item = Items.objects.get(id=int(item))
            ItemMaterials.objects.create(
                material_type=material_type,
                manufacturer=manufacturer,
                title=title,
                colour=colour,
                photo=the_file
            )
            f.close()

        # last_char = root[-1]
        # if not root.endswith('db4') and last_char.isdigit():  # and root == 'D:\\IT\\Pycharm Projects\\MyStore CREDENTIALS\\db4\\5.14. Ліжка\\8':
        #     root_split = root.split('\\')
        #     item = root_split[-1]
        #     root_split = root_split[-2]
        #     root_split = root_split.split('.')
            # room = root_split[0]
            # category = root_split[1]
            # print(f'Room: {room}, category: {category}, item: {item}')
            # print(f'Files: {files}')
            # for file in files:
            #     local_path = os.path.join(root, file)
                # remote_path = f"items/{room}/{category}/{item}/{file}"
                # print(f'The ITEM id from script: {int(item)}')
                # print(f'Local path: {local_path}')
                # print(f'Remote path {remote_path}')
                # print('___________________')




process_directory("D:\IT\Pycharm Projects\MyStore CREDENTIALS\МАТЕРІАЛИ\ДСП")
