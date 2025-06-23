from src.goods import Product, Category


def test_init_prodact(prodact1: Product) -> None:
    """Функция проверят корректность инициализации объектов класса Product"""
    assert prodact1.name == "Samsung Galaxy S23 Ultra"
    assert prodact1.description == "256GB, Серый цвет, 200MP камера"
    assert prodact1.price == 180000.0
    assert prodact1.quantity == 5


def test_init_category(category1: Category) -> None:
    """Функция проверят корректность инициализации объектов класса Category"""
    assert category1.category_count == 1
    assert category1.product_count == 2
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
