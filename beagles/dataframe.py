from beagles import Series

class DataFrame:
    def __init__(self, data: dict):
        self.data = {}

        for key, value in data.items():
            self.data[key] = Series(value, key)

    def shape(self):
        length = len(self.table)