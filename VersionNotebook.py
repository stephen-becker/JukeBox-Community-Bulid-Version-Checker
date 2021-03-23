LastestStableBuild = 17.025
NotebookRange = 2.0

def versionProcess(rVersion):
  versionActual = float(rVersion)
  versionChecker = LastestStableBuild
  forceUpdate = versionChecker - versionActual
    
  if versionActual == versionChecker:
      print("You are running the latest version - Build", versionChecker)
  elif forceUpdate >= NotebookRange:
      ErrorCode = "File Exited, Error 114x0001 - File Too Outdated, Update Notebook"
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
