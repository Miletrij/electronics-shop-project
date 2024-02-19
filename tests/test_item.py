"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from config import ITEMS
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone():
    return Phone("Смартфон", 10000, 20, 2)


def test_name(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.pay_rate == 0.8
    item.apply_discount()
    item.price == 8000


def test_instantiate_from_csv():
    Item.instantiate_from_csv(ITEMS)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('1.5') == 1


def test_repr_and_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add(phone, item):
    assert item + phone == 40


def test_add_error(phone, item):
    with pytest.raises(ValueError):
        item + 2


def test_instantiate_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/items.csv")


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("")
