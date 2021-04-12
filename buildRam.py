import sys
from termcolor import colored, cprint

def initalStageCommit(typePrint):
  
  if typePrint == 'gpuTxt':
    gpuText = colored('Assigned GPU:', 'red')
    print(gpuText)
  elif typePrint == 'driveTxt':
    driveText = colored('\nGoogle Drive Connector:', 'red')
    print(driveText)
  elif typePrint == 'updateTxt':
    updateText = colored('\nChecking For Updates:', 'red')
    print(updateText)
  
def versionChecker(vv):
  recentBuild = 9.09
  currentUse = vv
  convertedNum = str(recentBuild)
  needsUpdate = False
  goodVersion = colored('Build '+convertedNum, 'green')
  
  if currentUse == recentBuild:
    print("You're running the latest version of this build. ", goodVersion)
