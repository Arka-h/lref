from html import unescape as code #Find out more about encodings and parser s and thir meanings
string='utf-8 &#39;'# &#39; is used in html strings called ASCII code to represent ' to prevent entering executable code
strng=code(string)
print(strng)
