import sys
LastestStableBuild = 15.35
NotebookRange = 2.0

def preVersionProcess(rVersion):
  versionActual = float(rVersion)
  versionChecker = LastestStableBuild
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
      print("Running behind", forceUpdate, "version(s). Update soon!")
  else:
      ErrorCode = "File Exited, Failed To Check For Update"
      sys.exit(ErrorCode)

def versionProcess(rVersion):
  versionActual = float(rVersion)
  versionChecker = LastestStableBuild
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
