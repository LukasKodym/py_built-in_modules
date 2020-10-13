import sys

if len(sys.argv) > 1:
    arg = 0
    for i in range(1, len(sys.argv)):
        arg += int(sys.argv[i])
    print(f'Average: {(arg / i):.4f}')
else:
    print('No value were given.')
