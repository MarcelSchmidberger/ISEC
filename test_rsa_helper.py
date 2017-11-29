import unittest
import rsa_helper


class TestRSAHelper(unittest.TestCase):

    def test_is_prim(self):
        self.assertEqual(rsa_helper.is_prim(0), False)
        self.assertEqual(rsa_helper.is_prim(1), False)
        self.assertEqual(rsa_helper.is_prim(2), True)
        self.assertEqual(rsa_helper.is_prim(17), True)
        self.assertEqual(rsa_helper.is_prim(3242), False)
        self.assertEqual(rsa_helper.is_prim(997), True)

    #def test_getPrime(self):
        #self.assertEqual(rsa_helper.get_prim_in_range(1, 1), 1)
        #self.assertEqual(rsa_helper.get_prim_in_range(0, 0), 0)
        #  self.assertTrue(rsa_helper.get_prim_in_range(10, 100) >= 10 and )

    def test_phi(self):
        self.assertEqual(rsa_helper.phi(2, 2), 1)

    def test_gcd(self):
        self.assertEqual(rsa_helper.gcd(1, 1), 1)
        self.assertEqual(rsa_helper.gcd(0, 0), 0)
        self.assertEqual(rsa_helper.gcd(1, 0), 1)
        self.assertEqual(rsa_helper.gcd(0, 1), 1)
        self.assertEqual(rsa_helper.gcd(112, 2), 2)
        self.assertEqual(rsa_helper.gcd(100, 1110), 10)


if __name__ == '__main__':
    unittest.main()