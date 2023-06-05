import unittest
from rutpy import clean, validate, get_check_digit, format, generate

class RutpyTestCase(unittest.TestCase):
    def test_clean(self):
        ruts = ['14.961.581-4', '15.001.650-9', '3.148.184-8']
        expected_results = ['149615814', '150016509', '31481848']
        cleaned_ruts = [clean(rut) for rut in ruts]
        self.assertEqual(cleaned_ruts, expected_results)

    def test_validate(self):
        ruts = ['5.250.755-3', '14.461.448-8', '20.351.114-0']
        expected_results = [True, True, True]
        for rut, expected_result in zip(ruts, expected_results):
            self.assertEqual(validate(rut), expected_result)

    def test_get_check_digit(self):
        ruts = ['8.421.600', '8.991.701', '10.452.296']
        expected_results = ['3', '8', '3']
        check_digits = [get_check_digit(rut) for rut in ruts]
        self.assertEqual(check_digits, expected_results)

    def test_format(self):
        ruts = ['17.335.995-0', '20.709.073-5']
        expected_results = ['17.335.995-0', '20.709.073-5']
        formatted_ruts = [format(rut) for rut in ruts]
        self.assertEqual(formatted_ruts, expected_results)

    def test_generate(self):
        generated_rut = generate()
        self.assertTrue(validate(generated_rut))

if __name__ == '__main__':
    unittest.main()
