import basic
from sys import argv
import sys

text = argv[1]
if text.strip() == "": sys.exit()
text = f'RUN("{text}")'
result, error = basic.run('<stdin>', text)

if error:
    print(error.as_string())
elif result:
	if len(result.elements) == 1:
		print(repr(result.elements[0]))
	else:
		print(repr(result))