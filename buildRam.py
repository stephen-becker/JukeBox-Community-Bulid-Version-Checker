import sys
from termcolor import colored, cprint

def initalStageCommit(textCaller):
  
  if textCaller == gpuTxt:
    gpuText = colored('Assigned GPU:', 'red')
    print(gpuText)
  elif textCaller == driveTxt:
    driveText = colored('\nGoogle Drive Connector:', 'red')
    print(driveText)
  elif textCaller == updateTxt:
    updateText = colored('\nChecking For Updates:', 'red')
    print(updateText)
  
def versionChecker(vv):
  recentBuild = 9.09
  currentUse = vv
  needsUpdate = false
  goodVersion = colored('Build '+recentBuild, 'green')
  
  if currentUse == recentBuild:
    print("You're running the latest version of this build. ", goodVersion)
