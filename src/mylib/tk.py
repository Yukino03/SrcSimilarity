from tokenize import tokenize,untokenize
from io import BytesIO

def tknize(string):
  result = []
  g = tokenize(BytesIO(string).readline)  # tokenize the string
  for toknum, tokval, _, _, _ in g:
    result.append((toknum, tokval))
    print(toknum,tokval)
  return untokenize(result).decode('utf-8')

f = open(__file__)
for x in f:
  txt = tknize(x.encode())
f.close()