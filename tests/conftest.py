import pytest

from src.goods import Category, Product


@pytest.fixture
def prodact1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category1() -> Category:
    Category.category_count = 0
    Category.product_count = 0

    prodact1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    prodact2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    name = "Смартфоны"
    description = (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    prodacts = [prodact1, prodact2]
    return Category(name, description, prodacts)
