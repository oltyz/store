from datetime import datetime

# Класс Store для управления магазином и его ассортиментом
class Store:
    def __init__(self, name, address):
        """Конструктор класса, инициализирует название, адрес и пустой словарь для товаров."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Метод для добавления товара в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в магазин {self.name} по цене {price}.")

    def remove_item(self, item_name):
        """Метод для удаления товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён из магазина {self.name}.")
        else:
            print(f"Товар '{item_name}' не найден в магазине {self.name}.")

    def get_price(self, item_name):
        """Метод для получения цены товара по его названию."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Метод для обновления цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' в магазине {self.name} обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в магазине {self.name}.")

    def __str__(self):
        """Метод для удобного вывода информации о магазине."""
        return f"Магазин {self.name}, Адрес: {self.address}, Товары: {self.items}"


# Создание трёх магазинов с разными названиями и адресами
store1 = Store("Магазин №1", "ул. Пушкина, д. 1")
store2 = Store("Магазин №2", "ул. Ленина, д. 2")
store3 = Store("Магазин №3", "ул. Гагарина, д. 3")

# Добавление товаров в каждый магазин
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("milk", 1.2)
store2.add_item("bread", 0.9)

store3.add_item("cheese", 2.5)
store3.add_item("yogurt", 1.1)

# Печать информации о магазинах
print(store1)
print(store2)
print(store3)

# Тестирование методов на магазине store1
print("\nТестирование магазина store1")

# Добавляем новый товар
store1.add_item("oranges", 1.0)

# Обновляем цену на существующий товар
store1.update_price("apples", 0.6)

# Получаем цену на товар
price_apples = store1.get_price("apples")
print(f"Цена на яблоки: {price_apples}")

# Получаем цену на товар, которого нет в магазине
price_grapes = store1.get_price("grapes")
print(f"Цена на виноград: {price_grapes}")  # Должен вернуть None

# Удаляем товар
store1.remove_item("bananas")

# Печатаем обновлённый ассортимент магазина
print(store1)
