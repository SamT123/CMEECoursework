__name__ = '__main__'
__name__ = 'demo'

import sys
def main(args):
    print('yo')
print(__name__)

def sqr(x):
    return x*x

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)