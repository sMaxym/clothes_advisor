from weather.clothing import Clothing
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
        best_error = 100000
        diff = 100000
        spread = 100000
        best_index = None
        for index in indexes:
            try:
                vals = list()
                for i, key in enumerate(keys):
                    cloth_item = self._data[key][index[i]]
                    vals.append(cloth_item)
                    if not (cloth_item.temperature_range[0] <= temperature <= cloth_item.temperature_range[1]):
                        raise ValueError
                cur_spread = max(val.warmness for val in vals) - \
                             min(val.warmness for val in vals)
                cur_diff = abs(warm_coef - sum(val.warmness for val in vals))
                cur_error = Wardrobe._estimation(cur_diff, cur_spread ** 2)
                if cur_error < best_error:
                    best_index = index
                    best_error = cur_error
            except:
                pass
        clothing = [self._data[key][best_index[i]] for i, key in enumerate(keys)]
        return clothing
