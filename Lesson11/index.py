import json
import yaml
import pandas as pd


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

    yaml: yaml
    json: json
    pd_dataframe: pd.DataFrame


    def save_to_yaml(self, file):
        with open(file, "w") as f:
            yaml.dump(self.peoples, f)

    def get_from_yaml(self, file):
        with open(file, "r") as f:
            self.yaml = yaml.load(f, Loader=yaml.FullLoader)
            self.peoples = list(self.yaml)

    def print_yaml(self):
        print(self.yaml)

    def save_to_json(self, file):
        with open(file, "w") as f:
            json.dump(self.peoples, f)

    def get_from_json(self, file):
        with open(file, "r") as f:
            self.json = json.load(f)
            self.peoples = list(self.json)

    def print_json(self):
        print(self.json)

    def save_to_csv(self, file):
        df = pd.DataFrame(self.peoples)
        df.to_csv(file, index=False)

    def get_from_csv(self, file):
        self.pd_dataframe = pd.read_csv(file)

    def print_dataframe(self):
        print(self.pd_dataframe)


peoples = Structure()

peoples.get_from_json("peoples.json")
peoples.print_json()
peoples.save_to_yaml("peoples.yaml")

# peoples.save_to_yaml("peoples.yaml")
# peoples.get_from_yaml("peoples.yaml")
# peoples.print_yaml()
#
# peoples.save_to_json("peoples.json")
# peoples.get_from_json("peoples.json")
# peoples.print_json()
#
# peoples.save_to_csv("peoples.csv")
# peoples.get_from_csv("peoples.csv")
# peoples.print_dataframe()
