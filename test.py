import unittest
import arduino_interface

class NeoPixelServerTests(unittest.TestCase):



    def test_pixel_display_conversion(self):
        inputData = {
            "mode": "cycle",
            "data": [
                0x20, 0x10, 0x53,
                0x01, 0x02, 0x03,
                0x04, 0x05, 0x06,
                0x07, 0x08, 0x07
            ]
        }

        expectedResult = "\x63\x20\x10\x53\x01\x02\x03\x04\x05\x06\x07\x08\x07\n"
        self.assertEqual(
            arduino_interface.dictToPixelPacket(inputData),
            expectedResult)

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

