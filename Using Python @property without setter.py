if __name__ == "__main__":

    class Celsius:
        def __init__(self, temperature=0):
            self.temperature = temperature

        def temperature(self):
            print("Getting value...")
            return self._temperature

        # @temperature.setter
        def temperature(self, value):
            print("Setting value...")
            self._temperature = value

    human = Celsius(37)
    print(human.temperature)
    # human.temperature = 40
