from testing_config import BaseTestConfig
import pytest


# @pytest.mark.skip(reason="Using Prod Cert")
class TestGuestySDK(BaseTestConfig):

    '''
    Test sdk
    '''

    @pytest.mark.skip(reason="Using Prod Cert")
    def test_guesty_get_listing(self):
        property = self.client.get_property('327154')
        self.assertNotEqual(property.to_any_object(), {})
        self.assertEqual(property.id, '327154')

    @pytest.mark.skip(reason="Using Prod Cert")
    def test_guesty_listings(self):
        properties = self.client.properties
        self.assertNotEqual(len(properties), 0)
