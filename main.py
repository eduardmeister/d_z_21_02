from data.cls_request import Request
from data.cls_shop import Shop
from data.cls_store import Store

items_1 = {
        "лист": 20,
        "одежда": 15,
        "продукты": 20
}
items_2 = {
        "вещи": 4,
        "одежда": 5,
        "продукты": 6
}
store = Store(items=items_1, capacity=100)
shop = Shop(items=items_2, capacity=20)
list_of_store = {"магазин": shop, "склад": store}


def main():



    while True:

        print("Hello")
        print("_" * 20)
        print("На складе хранится:")
        for items, value in store.get_items.items():
            print(f"{items} - {value}")
        print("В магазине хранится:")
        for items, value in shop.get_items.items():
            print(f"{items} - {value}")
        print("_" * 20)


        order = input('Введите запрос формата '
              '"Доставить 3 вещи из склад в магазин"\n'
                      'Или введите "стоп" для выхода:\n')
        if order == "стоп":
            break


        request = Request(list_of_store, order)

        delivery_from = list_of_store[request.from_]
        delivery_to = list_of_store[request.to]

        delivery_from.remove(request.product, request.amount)
        print(f"Нужное количество есть на {request.from_}")

        print("_" * 20)
        print(f"Курьер забрал {request.amount} {request.product} со {request.from_}\n"
              f"Курьер везет  {request.amount} {request.product} со {request.from_} в {request.to}")
        delivery_to.add(request.product, request.amount)
        print(f"Курьер доставил {request.amount} {request.product} в {request.to}")

        print("_"*20)
        print(f"request.from_={request.from_}" )
        print(f"request.to={request.to}")
        print("_" * 20)

        print("На складе хранится:")
        for product, value in store.get_items.items():
            print(f"{product} - {value}")
        print("В магазине хранится:")
        for product, value in shop.get_items.items():
            print(f"{product} - {value}")

        print("_" * 20)









if __name__ == "__main__":
    main()


