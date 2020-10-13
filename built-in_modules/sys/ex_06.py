import sys

status = sys.stdout

file = open("log.txt", "w")
sys.stdout = file

print('Logging...')
print('Connecting...')
print('Closing...')

file.close()

sys.stdout = status

print('Completed successfully')
