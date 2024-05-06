import pytest
from items.models import *


@pytest.mark.django_db
def test_room_type_creation():
    room_type = RoomType.objects.create(title="Test Room Type")
    assert room_type.title == "Test Room Type"


@pytest.mark.django_db
def test_room_type_str_method():
    room_type = RoomType.objects.create(title="Test Room Type")
    assert str(room_type) == "Test Room Type"


@pytest.mark.django_db
def test_manufacturer_creation():
    manufacturer = Manufacturer.objects.create(title="Test Manufacturer")
    assert manufacturer.title == "Test Manufacturer"


@pytest.mark.django_db
def test_manufacturer_str_method():
    manufacturer = Manufacturer.objects.create(title="Test Manufacturer")
    assert str(manufacturer) == "Test Manufacturer"


@pytest.mark.django_db
def test_item_category_creation():
    room_type = RoomType.objects.create(title="Test Room Type")
    item_category = ItemCategory.objects.create(title="Test Item Category", room=room_type)
    assert item_category.title == "Test Item Category"
    assert item_category.room == room_type


@pytest.mark.django_db
def test_item_category_str_method():
    room_type = RoomType.objects.create(title="Test Room Type")
    item_category = ItemCategory.objects.create(title="Test Item Category", room=room_type)
    assert str(item_category) == "Test Item Category"


@pytest.mark.django_db
def test_item_collection_creation():
    manufacturer = Manufacturer.objects.create(title="Test Manufacturer")
    item_collection = ItemCollection.objects.create(title="Test Item Collection", manufacturer=manufacturer)
    assert item_collection.title == "Test Item Collection"
    assert item_collection.manufacturer == manufacturer


@pytest.mark.django_db
def test_item_collection_str_method():
    manufacturer = Manufacturer.objects.create(title="Test Manufacturer")
    item_collection = ItemCollection.objects.create(title="Test Item Collection", manufacturer=manufacturer)
    assert str(item_collection) == "Test Item Collection"


@pytest.mark.django_db
def test_colours_creation():
    colour = ItemColour.objects.create(title="Test Colour")
    assert colour.title == "Test Colour"


@pytest.mark.django_db
def test_colours_str_method():
    colour = ItemColour.objects.create(title="Test Colour")
    assert str(colour) == "Test Colour"


@pytest.mark.django_db
def test_wood_creation():
    material = ItemMaterial.objects.create(title="Test Wood")
    assert material.title == "Test Wood"


@pytest.mark.django_db
def test_wood_str_method():
    material = ItemMaterial.objects.create(title="Test Wood")
    assert str(material) == "Test Wood"


@pytest.mark.django_db
def test_items_creation():
    room_type = RoomType.objects.create(title="Test Room Type")
    item_category = ItemCategory.objects.create(title="Test Item Category", room=room_type)
    manufacturer = Manufacturer.objects.create(title="Test Manufacturer")
    item_collection = ItemCollection.objects.create(title="Test Item Collection", manufacturer=manufacturer)
    item = Items.objects.create(
        title="Test Item",
        article_code=12345,
        price=100.0,
        upholstery_material="Test Upholstery Material",
        upholstery_capacity=100,  # Provide a value for upholstery_capacity
        d_length=10,
        d_width=5,
        d_height=2,
        dimension_in_use_length=8,
        dimension_in_use_width=4,
        dimension_in_use_height=1,
        counter_claw=False,
        manufacturer=manufacturer,
        collection=item_collection,
        item_category=item_category,
        room_type=room_type,
    )
    assert item.title == "Test Item"
    assert item.article_code == 12345



@pytest.mark.django_db
def test_items_str_method():
    room_type = RoomType.objects.create(title="Test Room Type")
    item_category = ItemCategory.objects.create(title="Test Item Category", room=room_type)
    manufacturer = Manufacturer.objects.create(title="Test Manufacturer")
    item_collection = ItemCollection.objects.create(title="Test Item Collection", manufacturer=manufacturer)
    item = Items.objects.create(
        title="Test Item",
        article_code=12345,
        price=100.0,
        upholstery_material="Test Upholstery Material",
        upholstery_capacity=50,
        d_length=10,
        d_width=5,
        d_height=2,
        dimension_in_use_length=8,
        dimension_in_use_width=4,
        dimension_in_use_height=1,
        counter_claw=False,
        manufacturer=manufacturer,
        collection=item_collection,
        item_category=item_category,
        room_type=room_type,
    )
    assert str(item) == "Test Item"


# @pytest.mark.django_db
# def test_photos_creation():
#     item = Items.objects.create(title="Test Item", article_code=12345, price=100.0, upholstery_material='test', upholstery_capacity=100)
#     photo = ItemPhoto.objects.create(photo="test.jpg", item=item)
#     assert photo.photo == "test.jpg"
#     assert photo.item == item
#
#
# @pytest.mark.django_db
# def test_reviews_creation():
#     item = Items.objects.create(title="Test Item", article_code=12345, price=100.0, upholstery_material='test', upholstery_capacity=100)
#     review = Reviews.objects.create(item=item, first_name="John", second_name="Doe", rating=4)
#     assert review.first_name == "John"
#     assert review.rating == 4
#
#
# @pytest.mark.django_db
# def test_reviews_str_method():
#     item = Items.objects.create(title="Test Item", article_code=12345, price=100.0, upholstery_material='test', upholstery_capacity=100)
#     review = Reviews.objects.create(item=item, first_name="John", second_name="Doe", rating=4)
#     assert str(review) == str(item)
