class Request:

    def __init__(self, dict_of_store, order):
        self.dict_of_store = dict_of_store
        self._order = order
        self._order_arg()

    def _order_arg(self):
        list_order = self._order.split()

        if not len(list_order) == 7:
            raise "Неправильный запрос"

        self.from_ = list_order[4]
        self.to = list_order[6]
        self.amount = int(list_order[1])
        self.product = list_order[2]

        if self.from_ not in self.dict_of_store and self.to not in self.dict_of_store:
            raise "Ошибка в пункте отправления/получения"

