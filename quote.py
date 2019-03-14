
string = 'Some text'
string2 = "어떤 텍스트"
string3 = '{} 도 {} 도 지금 이것도 문자열'.format(string, string2)

print(string, string2, string3)

quote = '문법검사기 및 "직접인용은 큰따옴표다"'
emphassize = "'문법검사기'를 인용하다니"
# error = "엄마친구아들이 "파이썬 좋아" 라고 했데"

long_string = ''' 첫재쭐
둘째줄 '''

print(long_string)

quote1 = "가끔은 '와 " + '"를 모두 쓰기도 해'
quote2 = """가끔은 '와 "를 모두 쓰기도 해"""

print(quote1)
print(quote2)