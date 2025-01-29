import configparser
import os


class MakeUrl:

    @staticmethod
    def get_url_address(additional_url: str) -> str:
        """
        this methode get dynamic url and return full url
        :param additional_url:
        :return:
        """
        config_path = os.path.join(os.path.dirname(__file__), "..", 'config', 'multiav.ini')
        # Read configuration from server.ini
        config = configparser.ConfigParser()
        config.read(config_path)
        host = config['server']['host']
        port = int(config['server']['port'])
        scheme = 'http://'  # Change to 'https://' if needed
        return_url = f"{scheme}{host}:{port}{additional_url}"

        return return_url
