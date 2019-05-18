from pyowm import OWM
from pyowm.tiles.enums import MapLayerEnum


owm = OWM('160058a98508149e10affb7930083705')
layer_name = MapLayerEnum.PRESSURE
tm = owm.tile_manager(layer_name)
tile = tm.get_tile(345, 9, 1)
tile.persist('layer.png')