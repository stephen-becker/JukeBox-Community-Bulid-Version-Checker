import sys
InputValuesFalse = "Program's Basic Check Was Not Ran, Proceed With Caution - "
InputValuesTrue = "Program's Basic Check Has Determined That It Is Safe To Proceed - "
def checkInput(ab, a, b, c, d, e):
  if ab == ' ' or ab == '':
    ErrorCode = "File Exited, Error 115x0001 - Check Mode Value, Not Set?"
    sys.exit(ErrorCode)
  if not a > 0:
    ErrorCode = "File Exited, Error 115x0002 - Check SampleCount Value"
    sys.exit(ErrorCode)
    
  if not b >= 30:
    ErrorCode = "File Exited, Error 116x1001 - Check SampleLength Value?"
    sys.exit(ErrorCode)

  if c < .50:
    ErrorCode = "File Exited, Error 117x0001 - Check SampleHops Values (1)"
    sys.exit(ErrorCode)

  if d < .50:
    ErrorCode = "File Exited, Error 117x0002 - Check SampleHops Values (2)"
    sys.exit(ErrorCode)

  if e < 0.0625:
    ErrorCode = "File Exited, Error 117x0003 - Check SampleHops Values (3)"
    sys.exit(ErrorCode)

def setToFalse():
  print(InputValuesFalse + "Code 118x0002")

def setToTrue():
  print(InputValuesTrue + "Code 118x0001")
