"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting
from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting
pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
 the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels
connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
"""

import unittest


def flood_fill(image, sr, sc, new_color):
    row, column = len(image), len(image[0])
    color = image[sr][sc]
    if color == new_color:
        return image

    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = new_color
            if r >= 1:
                dfs(r-1, c)
            if r + 1 < row:
                dfs(r+1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < column:
                dfs(r, c + 1)
    dfs(sr, sc)
    return image


class Tests(unittest.TestCase):
    def test_the_first(self):
        ex1 = flood_fill(image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, new_color=2)
        self.assertEqual(ex1, [[2,2,2],[2,2,0],[2,0,1]])

    def test_the_second(self):
        ex2 = flood_fill(image=[[0,0,0],[0,0,0]], sr=0, sc=0, new_color=2)
        self.assertEqual(ex2, [[2,2,2],[2,2,2]])

