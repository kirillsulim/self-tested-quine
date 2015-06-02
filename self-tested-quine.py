code = r'''code = r{1}{1}{1}{0}{1}{1}{1}
import subprocess
import sys

if len(sys.argv) == 1:
  print(code.format(code, chr(39)))
elif len(sys.argv) == 2 and sys.argv[1] == 'test':
  with open(__file__, 'r') as file:
    text = file.read().replace('\r\n', '\n')
  out = subprocess.check_output(['python', __file__]).decode('raw-unicode-escape').replace('\r\n', '\n')
  
  if text == out:
    print('Test passed')
  else:
    for i in range(0, len(out)):
      print(i, out[i], text[i], out[i] == text[i])
else:
  print('Call this file with no arguments for quine or with "test" for self-test.')
'''
import subprocess
import sys

if len(sys.argv) == 1:
  print(code.format(code, chr(39)))
elif len(sys.argv) == 2 and sys.argv[1] == 'test':
  with open(__file__, 'r') as file:
    text = file.read().replace('\r\n', '\n')
  out = subprocess.check_output(['python', __file__]).decode('raw-unicode-escape').replace('\r\n', '\n')
  
  if text == out:
    print('Test passed')
  else:
    for i in range(0, len(out)):
      print(i, out[i], text[i], out[i] == text[i])
else:
  print('Call this file with no arguments for quine or with "test" for self-test.')

