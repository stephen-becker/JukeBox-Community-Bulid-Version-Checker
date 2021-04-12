import sys
from termcolor import colored, cprint

def initalStageCommit(void):
  gpuText = colored('Assigned GPU:', 'red')
  driveText = colored('\nGoogle Drive Connector:', 'red')
  updateText = colored('\nChecking For Updates:', 'red')
  
def versionChecker(vv):
  recentBuild = 9.09
  currentUse = vv
  needsUpdate = false
  goodVersion = colored('Build '+recentBuild, 'green')
  
  if currentUse == recentBuild:
    print("You're running the latest version of this build. ", goodVersion)
