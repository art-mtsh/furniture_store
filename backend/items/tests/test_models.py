import pytest
from django.core.exceptions import ValidationError
from backend.items.models import *


@pytest.mark.django_db
def test_item_room_type():
    # Create an instance of ItemRoomType
    item_room_type = ItemRoomType.objects.create(title="Test Room Type")
    assert str(item_room_type) == "Test Room Type"


@pytest.mark.django_db
def test_item_category():
    # Create an instance of ItemRoomType
    item_room_type = ItemRoomType.objects.create(title="Test Room Type")
    # Create an instance of ItemCategory with the created ItemRoomType
    item_category = ItemCategory.objects.create(title="Test Category", room=item_room_type)
    assert str(item_category) == "Test Category"


@pytest.mark.django_db
def test_item_manufacturer():
    # Create an instance of ItemManufacturer
    item_manufacturer = ItemManufacturer.objects.create(title="Test Manufacturer")
    assert str(item_manufacturer) == "Test Manufacturer"


@pytest.mark.django_db
def test_item_collection():
    # Create an instance of ItemManufacturer
    item_manufacturer = ItemManufacturer.objects.create(title="Test Manufacturer")
    # Create an instance of ItemCollection with the created ItemManufacturer
    item_collection = ItemCollection.objects.create(title="Test Collection", manufacturer=item_manufacturer)
    assert str(item_collection) == "Test Collection"


@pytest.mark.django_db
def test_items():
    # Create an instance of ItemCategory
    item_room_type = ItemRoomType.objects.create(title="Test Room Type")
    item_category = ItemCategory.objects.create(title="Test Category", room=item_room_type)
    # Create an instance of ItemCollection
    item_manufacturer = ItemManufacturer.objects.create(title="Test Manufacturer")
    item_collection = ItemCollection.objects.create(title="Test Collection", manufacturer=item_manufacturer)
    # Create an instance of Items with the created ItemCategory and ItemCollection
    item = Items.objects.create(title="Test Item", price=100.0, article_code=12345, item_category=item_category, collection=item_collection, length=10, width=10, height=10, form="Test Form")
    assert str(item) == "Test Item"


@pytest.mark.django_db
def test_item_materials():
    # Create an instance of ItemMaterials
    item_materials = ItemMaterials.objects.create(material_type="Test Material Type", manufacturer="Test Manufacturer", title="Test Material", colour="Test Colour")
    assert str(item_materials) == "Test Material"


@pytest.mark.django_db
def test_item_hard_body():
    # Create an instance of Items
    item = Items.objects.create(title="Test Item", price=100.0, article_code=12345, length=10, width=10, height=10, form="Test Form")
    # Create an instance of ItemMaterials
    item_materials = ItemMaterials.objects.create(material_type="Test Material Type", manufacturer="Test Manufacturer", title="Test Material", colour="Test Colour")
    # Create an instance of ItemHardBody with the created Items and ItemMaterials
    item_hard_body = ItemHardBody.objects.create(related_item=item, body_material=item_materials)
    assert item_hard_body.related_item == item


@pytest.mark.django_db
def test_item_soft_body():
    # Create an instance of Items
    item = Items.objects.create(title="Test Item", price=100.0, article_code=12345, length=10, width=10, height=10, form="Test Form")
    # Create an instance of ItemMaterials
    item_materials = ItemMaterials.objects.create(material_type="Test Material Type", manufacturer="Test Manufacturer", title="Test Material", colour="Test Colour")
    # Create an instance of ItemSoftBody with the created Items and ItemMaterials
    item_soft_body = ItemSoftBody.objects.create(related_item=item, sleep_place="Test Sleep Place", sleep_size="Test Sleep Size", springs_type="Test Springs Type", linen_niche=True, mechanism="Test Mechanism", filler="Test Filler", counter_claw=True, armrests="Test Armrests", max_weight=100, upholstery_material=item_materials, other="Test Other")
    assert item_soft_body.related_item == item


@pytest.mark.django_db
def test_item_photo():
    # Create an instance of Items
    item = Items.objects.create(title="Test Item", price=100.0, article_code=12345, length=10, width=10, height=10, form="Test Form")
    # Create an instance of ItemPhoto with the created Items
    item_photo = ItemPhoto.objects.create(related_item=item)
    assert item_photo.related_item == item


@pytest.mark.django_db
def test_item_review():
    # Create an instance of Items
    item = Items.objects.create(title="Test Item", price=100.0, article_code=12345, length=10, width=10, height=10, form="Test Form")
    # Create an instance of ItemReview with the created Items
    item_review = ItemReview.objects.create(related_item=item, first_name="Test First Name", second_name="Test Second Name", rating=4)
    assert item_review.related_item == item
