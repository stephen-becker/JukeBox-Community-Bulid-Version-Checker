import sys
def checkInput(a, b, c, d, e):
  if not a > 0:
    ErrorCode = "File Exited, Error 115x0001 - Check SampleCount Value"
    sys.exit(ErrorCode)
    
  if not b >= 30:
    ErrorCode = "File Exited, Error 116x1001 - Check SampleLength Value?"
    sys.exit(ErrorCode)

  if c <= .45:
    ErrorCode = "File Exited, Error 117x0001 - Check SampleHops Values"
    sys.exit(ErrorCode)

  if d <= .90:
    ErrorCode = "File Exited, Error 117x0002 - Check SampleHops Values"
    sys.exit(ErrorCode)

  if e <= 0.1:
    ErrorCode = "File Exited, Error 117x0003 - Check SampleHops Values"
    sys.exit(ErrorCode)
