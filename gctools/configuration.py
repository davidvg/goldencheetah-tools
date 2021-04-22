import pytz
import pandas as pd
import yaml
import datetime as dt
# import re

from gctools import logger
from definitions import CONFIG_FILE_PATH

logger = logger.getChild(__name__)
logger.debug(CONFIG_FILE_PATH)

# TODO Leave as public only the methods that are needed to run it

class PathConfiguration(object):
    def __init__(self):
        self._gc_path = ''  # TODO: validate string
        self._athlete_path = ''

    def _set_root(self, root):
        self._gc_path = root

    def _get_root(self):
        return self._gc_path

    def _set_athlete_path(self, path):
        self._athlete_path = path

    def _get_athlete_path(self):
        return self._athlete_path


class Configuration(object):
    def __init__(self, config_file=CONFIG_FILE_PATH):
        self.set_config_file_path(config_file)
        self._cfg_paths = PathConfiguration()
        # self._tz = pytz.timezone('UTC')  # TODO: Modify this!
        self._dataframe = pd.DataFrame()

        self.parse_configuration_file()
        self._make_paths()

    def parse_configuration_file(self):
        with open(CONFIG_FILE_PATH, 'r') as f:
            self._cfg_dict = yaml.safe_load(f)

        self.set_athlete()
        self.set_timezone()
        self._set_root()

    def set_config_file_path(self, cfg_path):
        self._cfg_file_path = cfg_path

    # TODO: Remove if not needed when using wrapper to PathConfiguration
    def get_config_file_path(self):
        return self._cfg_file_path

    def set_athlete(self):
        athlete = self._cfg_dict['app']['athlete']
        logger.debug('Reading configuration: {} = {}'.format('athlete', athlete))
        self._athlete = athlete  # TODO: Validate string

    def get_athlete(self):
        return self._athlete

    def set_timezone(self):
        tz = self._cfg_dict['app']['timezone']
        logger.debug('Reading configuration: {} = {}'.format('timezone', tz))
        self._tz = pytz.timezone(tz) # TODO: Validate string

    def get_timezone(self):
        return self._tz




    def get_data(self):
        return self._dataframe

    def get_cfg_paths(self):
        """Returns a PathConfiguration object
        """
        return self._cfg_paths

    def _string_ends_with_slash(self, path):
        res = path.endswith('/')
        logger.debug('Path string ends with "/": {}'.format(res))
        return res

    def _validate_path_string(self, path):
        if not self._string_ends_with_slash(path):
            path += '/'
        return path

    def _append_to_path(self, path, append):
        path = self._validate_path_string(path)
        res = path + append
        # logger.debug('Joined path: {}'.format(res))
        return res

    def _make_athlete_path(self):
        root = self._get_root()
        athlete = self.get_athlete()
        athlete_path = self._append_to_path(root, athlete)
        logger.debug('Athlete path: {}'.format(athlete_path))
        self._cfg_paths._set_athlete_path(athlete_path)

    def _make_paths(self):
        """Generate all the internal paths needed by the app
        """
        # TODO: Make activities path
        # TODO: Make cache path
        self._make_athlete_path()


    # Wrappers for PathConfiguration
    def _set_root(self):
        root = self._cfg_dict['app']['gc_database_path']
        logger.debug('Reading configuration: {} = {}'.format('root', root))
        self._cfg_paths._set_root(root)

    def _get_root(self):
        cfg_paths = self.get_cfg_paths()
        return cfg_paths._get_root()

    def _get_athlete_path(self):
        cfg_paths = self.get_cfg_paths()
        return cfg_paths._get_athlete_path()
