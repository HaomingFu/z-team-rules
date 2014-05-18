import argparse
import sys
import datetime

print('"""')
print('From: ' + sys.argv[1])
print('Author: Jing Zhou')
print('Date: '+ datetime.date.today().strftime('%b %d, %Y'))
print('Thought: ' + sys.argv[2])
print('"""')
print('\n'*3)
