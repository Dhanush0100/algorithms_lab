# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1deOoRStrkC4c8EXpvgpWUeVPaAgprR9m
"""

def search(pat, txt):
    M = len(pat)
    N = len(txt)

    # Loop through the text to find the pattern
    for i in range(N - M + 1):
        # Compare the substring with the pattern
        j = 0
        while j < M and txt[i + j] == pat[j]:
            j += 1

        # If we found the complete pattern
        if j == M:
            print("Pattern found at index", i)

# Test the function
txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(pat, txt)
