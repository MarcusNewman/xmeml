import unittest
import xmeml

class xmemlTests(unittest.TestCase):

    xmlString="<xmeml><bin><name>Day_00</name></bin></xmeml>"    
    data = xmeml(xmlString)
    
    def test_get_day_should_return_Day_00(self):
        day = data.get_day()
        self.assertEqual(day,"Day_00")
       
if __name__ == '__main__':
    unittest.main()
