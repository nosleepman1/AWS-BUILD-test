import unittest
from myApp import sayGoodbye, sayHello



class TestApp(unittest.TestCase):
    def test_sayHello(self):
        self.assertEqual(sayHello("AWS"), "Hello AWS")
    
    def test_sayGoodbye(self):
        self.assertEqual(sayGoodbye("AWS"), "Goodbye AWS")



if __name__ == "__main__":
    unittest.main()
