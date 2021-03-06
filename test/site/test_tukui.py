import unittest

from updater.site import tukui


class TestTukui(unittest.TestCase):
    def setUp(self):
        self.url = 'https://git.tukui.org/elvui/elvui'
        self.tukui = tukui.Tukui(self.url)

    def test_integration_tukui_find_zip_url(self):
        zip_url = self.tukui.find_zip_url()
        self.assertRegex(zip_url, rf"{self.url}/-/archive/v[0-9]+\.[0-9]+/elvui-v[0-9]+\.[0-9]+\.zip")

    def test_integration_tukui_get_addon_name(self):
        addon_name = self.tukui.get_addon_name()
        self.assertEqual(addon_name, 'elvui')

    def test_integration_tukui_get_latest_version(self):
        latest_version = self.tukui.get_latest_version()
        self.assertRegex(latest_version, r"(v[0-9]+\.[0-9]+)")  # something like v12.34

    def test_tukui_get_supported_urls(self):
        supported_urls = self.tukui.get_supported_urls()
        self.assertIsNotNone(supported_urls)
        self.assertTrue(len(supported_urls) != 0)


if __name__ == '__main__':
    unittest.main()
