from sys import argv
from app import CAV


if __name__ == '__main__':
  voice = True

  if '--voiceoff' in argv:
    voice = False

  cav = CAV(voice=voice)
  while cav.on:
    cav.run()
