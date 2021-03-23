import sys
InputValuesFalse = "Program's Basic Check Was Not Ran, Proceed With Caution - "
InputValuesTrue = "Program's Basic Check Has Determined That It Is Safe To Proceed - "
def checkInput():
  if not SampleCount > 0:
    ErrorCode = "File Exited, Error 115x0001 - Check SampleCount Value"
    sys.exit(ErrorCode)
    
  if not SampleLength >= 30:
    ErrorCode = "File Exited, Error 116x1001 - Check SampleLength Value?"
    sys.exit(ErrorCode)

  if SampleHops[0] <= .45:
    ErrorCode = "File Exited, Error 117x0001 - Check SampleHops Values"
    sys.exit(ErrorCode)

  if SampleHops[1] <= .90:
    ErrorCode = "File Exited, Error 117x0002 - Check SampleHops Values"
    sys.exit(ErrorCode)

   if SampleHops[2] <= 0.1:
    ErrorCode = "File Exited, Error 117x0003 - Check SampleHops Values"
    sys.exit(ErrorCode)
      
#checkInput()
#print(InputValuesTrue + "Code 118x0001")

#else:
#  print(InputValuesFalse + "Code 118x0002")
