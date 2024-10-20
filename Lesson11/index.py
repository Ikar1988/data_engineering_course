import json

import yaml

class Structure:
    peoples = [
        {
            "name": "Вася Пупкин",
            "age": 21,
            "gender": "m"
        },
        {
            "name": "Настя Иванова",
            "age": 33,
            "gender": "f"
        },
    ]

    def save_to_yaml(self, file):
        with open(file, "w") as f:
            yaml.dump(self.peoples, f)

    def get_from_yaml(self, file):
        with open(file, "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def save_to_json(self, file):
        with open(file, "w") as f:
            json.dump(self.peoples, f)

    def get_from_json(self, file):
        with open(file, "r") as f:
            return json.load(f)


peoples = Structure()
# peoples.save_to_yaml("peoples.yaml")
# peoples.peoples = peoples.get_from_yaml("peoples.yaml")
peoples.save_to_json("peoples.json")
peoples.peoples = peoples.get_from_json("peoples.json")

print(peoples.peoples)