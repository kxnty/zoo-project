import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price_5(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    def test_child_ticket_price_0(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_child_ticket_price_12(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    
    def test_child_ticket_price_13(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_child_ticket_price_20(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_child_ticket_price_21(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_child_ticket_price_60(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    
    def test_child_ticket_price_70(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

if __name__ == '__main__':
    unittest.main()