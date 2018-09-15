import os
import argparse
import configparser
from exceptions import ConfigFileDamagedError


class SettingsDict():
    CONFIG_FILE_NAME = '.kontrib'
    CONFIG_FILE_MAIN_SECTION = 'repo'

    def __init__(self):
        self.config_path = None
        self.config_parser = None
        self.repo = None

    def read_config(self):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(os.path.join(self.config_path, self.CONFIG_FILE_NAME))
        if self.CONFIG_FILE_MAIN_SECTION in self.config_parser:
            self.repo = self.config_parser[self.CONFIG_FILE_MAIN_SECTION]
        else:
            raise ConfigFileDamagedError


class Settings():
    settings = SettingsDict()

    @classmethod
    def set_settings(cls, argv):
        parser = argparse.ArgumentParser()
        parser.add_argument('config_path')
        parser.add_argument('--username')
        parser.add_argument('--password')
        parser.add_argument('--token')
        parser.parse_args(args=argv[1:], namespace=cls.settings)
        cls.settings.read_config()
