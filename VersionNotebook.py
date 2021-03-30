import sys
LatestStableBuild = 15.42
LatestVBuild = 127.02
NotebookRange = 2.0

class colors:
  GREEN = '\033(32m'
  ENDC = '\033[m' # reset to the defaults

def vBuildVersion(rVersion):
  vMath = (rVersion - 1.0) * 1000
  versionActual = round(vMath, 3)
  versionChecker = LatestVBuild
  forceUpdate = versionChecker - versionActual
  forceUpdate = float("{:.5f}".format(forceUpdate))
  
  if versionActual == 1.337:
      print("You are running a developer build, good luck with the coding.")
  elif versionActual == versionChecker:
      print("You are running the latest experimental version - Build", versionChecker)
  elif forceUpdate >= NotebookRange:
      print("File Will Exit, Error 114x0001 - File Too Outdated, Update Notebook\n**In order to bypass update checker, if you choose, set BypassVersionUpdateChecker to True in the Mainframe section.**")
  elif versionActual > versionChecker:
      ErrorCode = "File Exited, Error 114x0002 - Version Newer?"
      sys.exit(ErrorCode)
  elif versionActual < versionChecker:
      print("You are running an outdated version of this notebook!")
      print("Running behind", forceUpdate, "version(s). Update soon!")
  else:
      ErrorCode = "File Exited, Failed To Check For Update"
      sys.exit(ErrorCode)
  

def preVersionProcess(rVersion):
  versionActual = float(rVersion)
  versionChecker = LatestStableBuild
  forceUpdate = versionChecker - versionActual
  forceUpdate = float("{:.2f}".format(forceUpdate))
  
  if versionActual == 1.337:
      print("You are running a developer build, good luck with the coding.")
  elif versionActual == versionChecker:
      print("You are running the latest version - Build", versionChecker)
  elif forceUpdate >= NotebookRange:
      print("File Will Exit, Error 114x0001 - File Too Outdated, Update Notebook\n**In order to bypass update checker, if you choose, set BypassVersionUpdateChecker to True in the Mainframe section.**")
  elif versionActual > versionChecker:
      ErrorCode = "File Exited, Error 114x0002 - Version Newer?"
      sys.exit(ErrorCode)
  elif versionActual < versionChecker:
      print("You are running an outdated version of this notebook!")
      print(TGREEN + "Running behind", forceUpdate, "version(s). Update soon!", ENDC)
  else:
      ErrorCode = "File Exited, Failed To Check For Update"
      sys.exit(ErrorCode)

def versionProcess(rVersion):
  versionActual = float(rVersion)
  versionChecker = LatestStableBuild
  forceUpdate = versionChecker - versionActual
  forceUpdate = float("{:.2f}".format(forceUpdate))
  
  if versionActual == 1.337:
      print("You are running a developer build, good luck with the coding.")
  elif versionActual == versionChecker:
      print("You are running the latest version - Build", versionChecker)
  elif forceUpdate >= NotebookRange:
      ErrorCode = "File Exited, Error 114x0001 - File Too Outdated, Update Notebook\n**In order to bypass update checker, if you choose, set BypassVersionUpdateChecker to True in the Mainframe section.**"
      sys.exit(ErrorCode)
  elif versionActual > versionChecker:
      ErrorCode = "File Exited, Error 114x0002 - Version Newer?"
      sys.exit(ErrorCode)
  elif versionActual < versionChecker:
      print("You are running an outdated version of this notebook!")
      print("Running behind", forceUpdate, "version(s). Update soon!")
  else:
      ErrorCode = "File Exited, Failed To Check For Update"
      sys.exit(ErrorCode)
