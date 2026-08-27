# test_primetorch.py
"""
Tests for PrimeTorch module.
"""

import unittest
from primetorch import PrimeTorch

class TestPrimeTorch(unittest.TestCase):
    """Test cases for PrimeTorch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeTorch()
        self.assertIsInstance(instance, PrimeTorch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeTorch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
