import unittest
import arduino_interface
import server
import json

class NeoPixelServerTests(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()

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
            arduino_interface.pack_pixel_data(inputData),
            expectedResult)
        print("TODO: add data unpacking test")

    def test_mode_conversion(self):
        modes = [
            ("cycle",  "\x63"),
            ("both",  "\x62"),
            ("all-on",  "\x61")
        ]
        for inVal, expectedResult in modes:
            self.assertEqual(
                arduino_interface.mode_to_header(inVal),
                expectedResult)
        
    def test_api_get_pixels(self):
        rv = self.app.get("/pixels/")
        self.assertEqual(rv.status_code, 200)

    def test_api_put_pixel_data(self):
        inputData = {
            "mode": "cycle",
            "data": [
                0x20, 0x10, 0x53,
                0x01, 0x02, 0x15,
                0x04, 0x15, 0x06,
                0x07, 0x08, 0x07
            ]
        }
        rv = self.app.put(path="/pixels/",
            headers=[("Content-Type", "application/json")],
            data = json.dumps(inputData))
        self.assertEqual(rv.status_code, 200)

    def test_api_html_endpoint(self):
        pass

    def test_api_get_current_display_data(self):
        pass


if __name__ == '__main__':
    unittest.main(failfast=True)

