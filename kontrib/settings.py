import os
import argparse
import configparser
from exceptions import ConfigFileDamagedError


class SettingsDict():
    REPO_CONFIG_FILE_NAME = '.kontrib'
    REPO_CONFIG_MAIN_SECTION = 'repo'
    kontrib_config = '~/.config/kontrib'
    KONTRIB_CONFIG_MAIN_SECTION = 'user'

    def __init__(self):
        self.repo_path = None
        self.config_parser = None
        self.repo = None

    def read_configs(self):
        self.config_parser = configparser.ConfigParser()
        self.read_kontrib_config()
        self.read_repo_config()

    def read_kontrib_config(self):
        self.config_parser.read(os.path.expanduser(self.kontrib_config))
        if self.KONTRIB_CONFIG_MAIN_SECTION in self.config_parser:
            for key in self.config_parser[self.KONTRIB_CONFIG_MAIN_SECTION]:
                if not getattr(self, key):
                    setattr(self, key, self.config_parser[self.KONTRIB_CONFIG_MAIN_SECTION][key])

    def read_repo_config(self):
        self.config_parser.read(
            os.path.expanduser(
                os.path.join(self.repo_path, self.REPO_CONFIG_FILE_NAME)
            )
        )
        if self.REPO_CONFIG_MAIN_SECTION in self.config_parser:
            self.repo = self.config_parser[self.REPO_CONFIG_MAIN_SECTION]
        else:
            raise ConfigFileDamagedError

    def save_kontrib_config(self):
        pass

class Settings():
    settings = SettingsDict()

    @classmethod
    def set_settings(cls, argv):
        parser = argparse.ArgumentParser()
        parser.add_argument('repo_path', default='.')
        parser.add_argument('--kontrib-config', dest='kontrib_config')
        parser.add_argument('--hosting')
        parser.add_argument('--username')
        parser.add_argument('--password')
        parser.add_argument('--token')
        parser.add_argument('--check', action='store_true', default=False)
        parser.add_argument('--new-pr', nargs='*', default=None)
        parser.parse_args(args=argv[1:], namespace=cls.settings)
        cls.settings.read_configs()
        return cls.settings
