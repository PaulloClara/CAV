from app import CAV
from sys import argv

if __name__ == '__main__':
  cav = CAV(argv[1:])
  cav.run()
