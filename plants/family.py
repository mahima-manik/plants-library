class PlantFamily:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"{self.name} family with {len(self.members)} members"


class IndoorPlant(PlantFamily):
    def __init__(self, name, is_indoor=True):
        super().__init__(name)
        self.is_indoor = is_indoor

    def __str__(self):
        return f"{self.name} family with {len(self.members)} members and is indoor: {self.is_indoor}"


class OutdoorPlant(PlantFamily):
    def __init__(self, name, is_indoor=False):
        super().__init__(name)
        self.is_indoor = is_indoor

    def __str__(self):
        return f"{self.name} family with {len(self.members)} members and is indoor: {self.is_indoor}"


INDOOR_PLANTS = ['Monstera', 'Fiddle Leaf Fig', 'Snake Plant', 'Pothos']


def find_plant_type(plant_name):
    if plant_name in INDOOR_PLANTS:
        return 'IndoorPlant'
    else:
        return 'OutdoorPlant'
