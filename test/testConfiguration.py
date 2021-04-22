import unittest
import pytz
import pandas as pd
import yaml
from os.path import exists, isdir

from gctools.configuration import Configuration, PathConfiguration
from definitions import CONFIG_FILE_PATH

class TestConfiguration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg_data = cls.prepare_data() # Configuration read from file
        cls.cfg = Configuration()

    @classmethod
    def setUp(cls):
        pass

    @classmethod
    def tearDown(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def prepare_data(cls):
        '''Parse the configuration file and populate fields'''
        try:
            with open(CONFIG_FILE_PATH, 'r') as f:
                data = yaml.safe_load(f)
        except:
            raise
        finally:
            return data

    def testConfigurationHasAllAttributes(self):
        self.assertIsInstance(self.cfg.get_config_file_path(), str)
        self.assertIsInstance(self.cfg.get_athlete(), str)
        self.assertIsInstance(self.cfg.get_timezone(), pytz.BaseTzInfo)
        self.assertIsInstance(self.cfg.get_data(), pd.DataFrame)
        self.assertIsInstance(self.cfg.get_cfg_paths(), PathConfiguration)

    def testPathConfigurationHasAllAttributes(self):
        cfg_paths = self.cfg.get_cfg_paths()
        self.assertIsInstance(cfg_paths._get_root(), str)

    def testConfigurationHasCorrectValues(self):
        self.assertEqual(self.cfg.get_config_file_path(), CONFIG_FILE_PATH)
        self.assertEqual(self.cfg.get_athlete(), self.cfg_data['app']['athlete'])
        self.assertEqual(self.cfg.get_timezone(), pytz.timezone(self.cfg_data['app']['timezone']))

    # def testAllPathsExist(self):
        # cfg_paths = self.cfg.get_cfg_paths()

        # # self.assertTrue(cfg_paths.get_athlete_path()) # TODO Remove
        # self.assertTrue(exists(cfg_paths.get_athlete_path()))

    def testInternalPathsAreCorrect(self):
        # self.assertEqual(self.cfg._get_root(),
                         # self.cfg_data['app']['gc_database_path'])
        self.assertTrue(exists(self.cfg._get_root()))
        self.assertTrue(exists(self.cfg._get_athlete_path()))
        self.assertTrue(exists(self.cfg._get_activities_path()))


if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)
