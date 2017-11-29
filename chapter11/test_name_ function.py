import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    #test name_function.py
    def test_firt_last_name(self):
        #能够正确处理Janis Joplin这样的姓名吗
        formatted_name = get_formatted_name('janis','Joplin');
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_firt_last_name2(self):
        #能够正确处理Janis Joplin这样的姓名吗
        formatted_name = get_formatted_name('周秋明','Joplin');
        self.assertEqual(formatted_name.strip(),'Joplin')
unittest.main()

