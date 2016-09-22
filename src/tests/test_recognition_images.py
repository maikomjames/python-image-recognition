
import unittest
from src.recognition.recognition import Recognition


class TestRecognitionImagesCase(unittest.TestCase):

    def test_recognition_positions_on_prints(self):
        """
            Test for to find image part in prints
        """

        print_full = "assets/print-full.png"
        part_of_print = "assets/an.png"

        recog = Recognition(image=print_full)
        point = recog.find(part_of_print)

        point_found = point[0]

        w, h = recog.dimensions

        self.assertEqual(recog.get_top_left(), point_found)
        self.assertEqual(recog.get_top_center(), (point_found[0] + w/2, point_found[1]))
        self.assertEqual(recog.get_top_right(), (point_found[0] + w, point_found[1]))
        self.assertEqual(recog.get_center_left(), (point_found[0], point_found[1] + h/2))
        self.assertEqual(recog.get_center(), (point_found[0] + w/2, point_found[1] + h/2))
        self.assertEqual(recog.get_center_right(), (point_found[0] + w, point_found[1] + h/2))
        self.assertEqual(recog.get_bottom_left(), (point_found[0], point_found[1] + h))
        self.assertEqual(recog.get_bottom_center(), (point_found[0] + w/2, point_found[1] + h))
        self.assertEqual(recog.get_bottom_right(), (point_found[0] + w, point_found[1] + h))

if __name__ == '__main__':
    unittest.main()
