from json import loads, dumps

class ServerConfig:
    def __init__(self):
        self.data = {}
        self.update_data()

        self.main_data_direction = self.data["main_data_direction"]
        self.data_directions = self.data["data_directions"]
        self.data_directions_backup = self.data["data_directions_backup"]

        self.default_coloborators_space_volume = self.data["default_coloborators_space_volume"]
        self.default_user_space_volume = self.data["default_user_space_volume"]

    def update_data(self):
        with open("data/server_config.json", "r", encoding="utf-8") as file:
            self.data = loads(file.read())

    def local_save(self, key, value):
        try:
            self.data[key] = value
        except Exception as e:
            print(f"Error saving key {key}: {e}")

        with open("data/server_config.json", "w") as file:
            file.write(dumps(self.data, indent=4, ensure_ascii=False))

    def save(self, data: dict = None):
        if data is None:
            self.data["main_data_direction"] = self.main_data_direction
            self.data["data_directions"] = self.data_directions
            self.data["data_directions_backup"] = self.data_directions_backup
            self.data["default_coloborators_space_volume"] = self.default_coloborators_space_volume
            self.data["default_user_space_volume"] = self.default_user_space_volume
            data = self.data
            self.update_data()

        with open("data/server_config.json", "w") as file:
            file.write(dumps(data, indent=4, ensure_ascii=False))

class ClientSetting:
    def __init__(self):
        self.data = {}
        self.update_data()
        self.required_email = self.data["required_email"]
        self.required_telephone = self.data["required_telephone"]

    def update_data(self):
        with open("data/client_settings.json", "r", encoding="utf-8") as file:
            self.data = loads(file.read())

    def local_save(self, key, value):
        try:
            self.data[key] = value
        except Exception as e:
            print(f"Error saving key {key}: {e}")

        with open("data/client_settings.json", "w") as file:
            file.write(dumps(self.data, indent=4, ensure_ascii=False))

    def save(self, data: dict = None):
        if data is None:
            self.data["required_email"] = self.required_email
            self.data["required_telephone"] = self.required_telephone
            data = self.data
            self.update_data()

        with open("data/client_settings.json", "w") as file:
            file.write(dumps(data, indent=4, ensure_ascii=False))


client_setting = ClientSetting()
server_config = ServerConfig()