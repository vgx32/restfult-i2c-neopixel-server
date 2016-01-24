import unittest
import arduino_interface

class NeoPixelServerTests(unittest.TestCase):



    def test_pixel_display_conversion(self):
        pass
        # inputData = {
        #     "mode": ""
        # }
        # self.assertEqual(1,2)

    def test_mode_conversion(self):
        modes = [
            ("cycle",  "\x63"),
            ("both",  "\x62"),
            ("all-on",  "\x61")
        ]
        for inVal, expectedResult in modes:
            self.assertEqual(
                arduino_interface.modeToModeChar(inVal),
                expectedResult)
        

    def test_api_post_pixel_data(self):
        pass

    def test_api_html_endpoint(self):
        pass

    def test_api_get_current_display_data(self):
        pass


if __name__ == '__main__':
    unittest.main(failfast=True)

