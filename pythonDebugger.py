# pythonDebugger.py
# Sunny Vinay

import sys
import inspect

def sample(a, b):
    z = 2
    x = a + b
    y = x * 2
    z = 3
    print('Sample: ' + str(y))

def trace_calls(frame, event, arg):
    if frame.f_code.co_name == "sample":
        print(frame.f_code)
        return trace_lines

def trace_lines(frame, event, arg):
    varDict = frame.f_locals
    for var in varDict:
        print("Line " + str(frame.f_lineno) + ": " + "\'" + var + "\'" +
              " changed to " + str(varDict[var]))
    print()

sys.settrace(trace_calls)
sample(3,2)


'''
Output:

<code object sample at 0x1032ab4b0, file "/Users/sunnyvinay/GCI2019/pythonDebugger.py", line 6>
Line 7: 'a' changed to 3
Line 7: 'b' changed to 2

Line 8: 'a' changed to 3
Line 8: 'b' changed to 2
Line 8: 'z' changed to 2

Line 9: 'a' changed to 3
Line 9: 'b' changed to 2
Line 9: 'z' changed to 2
Line 9: 'x' changed to 5

Line 10: 'a' changed to 3
Line 10: 'b' changed to 2
Line 10: 'z' changed to 2
Line 10: 'x' changed to 5
Line 10: 'y' changed to 10

Line 11: 'a' changed to 3
Line 11: 'b' changed to 2
Line 11: 'z' changed to 3
Line 11: 'x' changed to 5
Line 11: 'y' changed to 10

Sample: 10
Line 11: 'a' changed to 3
Line 11: 'b' changed to 2
Line 11: 'z' changed to 3
Line 11: 'x' changed to 5
Line 11: 'y' changed to 10
'''
