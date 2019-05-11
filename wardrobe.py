from clothing import Clothing
from math import ceil
from itertools import combinations_with_replacement as cwr


class Wardrobe:
    def __init__(self, *clothing):
        self._data = dict()
        for item in list(clothing):
            if self._data.get(item.body_part) is None:
                self._data[item.body_part] = list()
            self._data[item.body_part].append(item)

    @staticmethod
    def _warmness_coefficient(temperature):
        return ceil(-13 / 40 * temperature + 18)

    @staticmethod
    def _estimation(val_a, val_b):
        return (val_a ** 2 + val_b ** 2) ** 0.5

    def get_clothing(self, temperature):
        warm_coef =  Wardrobe._warmness_coefficient(temperature)
        keys = self._data.keys()
        lengths = [len(item) for item in self._data]
        elms = list(range(max(lengths)))
        indexes = list(cwr(elms, len(keys)))
        best_error = 1000
        diff = 1000
        spread = 1000
        best_index = None
        for index in indexes:
            try:
                vals = list()
                for i, key in enumerate(keys):
                    vals.append(self._data[key][index[i]])
                cur_spread = max(vals) - min(vals)
                cur_diff = abs(warm_coef - sum(vals))
                if Wardrobe._estimation(cur_diff ** 1.5, cur_spread) < best_error:
                    best_index = indexes[i]
            except:
                pass
        clothing = [self._data[key][best_index[i]] for i, key in enumerate(keys)]
        return clothing



# [-40; 40] length = b - a = 80, temp = 40 warm = 5, temp = -40 warm = 31