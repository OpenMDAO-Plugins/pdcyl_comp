# pylint: disable-msg=C0111,C0103

import unittest
import os
import sys
import shutil

# Append the path above us, so that we can run the test even if we don't
# have the package installed.
from pdcyl_comp.pdcyl_comp import PdcylComp

from openmdao.main.container import dump


class PdcylCompTestCase(unittest.TestCase):

    def setUp(self):
        """this setup function will be called before each test in this class"""
        pass
    
    def tearDown(self):
        """this teardown function will be called after each test"""
        
        for filename in ['PDCYL.in', 'PDCYL.out', 'PDCYL.err', 'pdcyl.dump']:
            if os.path.exists(filename):
                os.remove(filename)
                
    def test_PDCYL_case(self):
        
        comp = PdcylComp()

        dirname = os.path.abspath(os.path.dirname(__file__))

        basename = os.getcwd()
        os.chdir(dirname)

        try:
            # Check input file generation
            
            comp.load_model('transport.in')
            comp.generate_input()
    
            file1 = open('transport.in', 'r')
            result1 = file1.read()
            file1.close()
            file2 = open('PDCYL.in', 'r')
            result2 = file2.read()
            file2.close()
            
            self.assertEqual(result1, result2)
            
            # Check output file parsing
                
            shutil.copyfile('transport.out', 'PDCYL.out')
            comp.parse_output()
            
            file1 = open('pdcyl.dump', 'w')
            dump(comp, stream=file1, recurse=True)
            file1.close()
            
            file1 = open('transport.dump', 'r')
            result1 = file1.readlines()
            file1.close()
            file2 = open('pdcyl.dump', 'r')
            result2 = file2.readlines()
            file2.close()
            
            for line1, line2 in zip(result1, result2):
                # Omit lines with objects, because memory location differs
                if 'object at' not in line1:
                    self.assertEqual(line1, line2)

        finally:
            os.chdir(basename)



if __name__ == "__main__":
    unittest.main()
