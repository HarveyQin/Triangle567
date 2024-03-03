# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle as classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_invalid_input_greater_than_200(self):
        self.assertEqual(classifyTriangle(201, 150, 100), 'InvalidInput')

    def test_invalid_input_less_than_or_equal_to_zero(self):
        self.assertEqual(classifyTriangle(-1, 150, 100), 'InvalidInput')

    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 2, 4), 'NotATriangle')

    def test_equilateral_triangle(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral')

    def test_right_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def test_scalene_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene')

    def test_isosceles_triangle(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isosceles')

    def test_invalid_input_float(self):
        self.assertEqual(classifyTriangle(3.5, 4, 6), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

