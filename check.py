import accel
import math

def reference(g):
   # raw = round(g*16384)
    raw=round_halfaway(g*16384)
    raw = max(-32768, min(32767, raw))
    return raw

def round_halfaway(raw):
    if raw>0:
        return math.floor(raw+0.5)
    else:
        return math.ceil(raw-0.5)

LSB = 1/16384
tests = [0.0,                 
    1.0, 0.5,          
    -1.0,                
    2.0, -2.0,          
    3.0, -3.0,         
    LSB, -LSB,          
    0.5 * LSB,          
    2.5 * LSB, ]

errors = 0
for g in tests:
    dut=accel.read_accel(g)
    ref=reference(g)
    if dut == ref:
        print ("pass")
    else:
        errors+=1
        print(f"Status:Fail {g:+8f} ref:{ref:+6d} dut:{dut:+6d}")

print("Test compeleted")