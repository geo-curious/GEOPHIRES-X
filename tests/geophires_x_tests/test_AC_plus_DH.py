from pathlib import Path

from base_test_case import BaseTestCase
from geophires_x_client import GeophiresInputParameters
from geophires_x_client import GeophiresXClient


class ACplusDHTestCase(BaseTestCase):
    def test_ac_plus_dh(self):
        client = GeophiresXClient()

        result = client.get_geophires_result(
            GeophiresInputParameters(from_file_path=self._get_test_file_path(Path('geo-curious_AC_plus_DH.txt')))
        )
        del result.result['metadata']

        self.assertIsNotNone(result)
        # TODO assert that calculated properties of result are correct (@geo-curious)
