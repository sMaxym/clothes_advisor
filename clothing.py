class Clothing:
    def __init__(self,
                 name,
                 body_part,
                 temperature_range,
                 rain_suitable,
                 amount_at_once,
                 warmness):
        """
        Initializing main class parameters, variables and properties.
        :param name: name of the clothing.
        :param body_part: part of the body where it can be weared:
            - head
            - chest
            - hands
            - legs
            - foots
        :param temperature_range: tuple of min and max clothing temperature.
        :param rain_suitable: is it suitable for rain.
        :param amount_at_once: amount of units can be weared at once.
        :param warmness: warmness criteria from 1 to 10.
        """
        self.name = name
        self.body_part = body_part
        self.temperature_range = temperature_range
        self.rain_suitable = rain_suitable
        self.amount_at_once = amount_at_once
        self.warmness = warmness

    def __str__(self):
        return str(self.warmness)