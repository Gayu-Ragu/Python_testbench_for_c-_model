import math
import random
import accel

# Refrence Model
def round_halfaway(x):
    if x>0:
        return math.floor(x+0.5)
    else:
        return math.ceil(x-0.5)

def reference(g):
    raw = round_halfaway(g*16384)
    #raw = round(g*16384)
    raw = max(-32768, min(32767, raw))
    return raw

# Stimulus
LSB=1/16384

def directed_stimulus():
    #Handpicked cases
    return [0.0, 1.0, 0.5, -1.0, 2.0, -2.0, 3.0, -3.0,
            LSB, -LSB, 0.5 * LSB, 2.5 * LSB, -0.5 * LSB]

def random_stimulus(count,seed):
    #Random values between +-3g
    rng = random.Random(seed)
    return [rng.uniform(-3.0,3.0) for _ in range(count)]

#Scoreboard
class Scoreboard:
    def __init__(self,name):
        self.name = name
        self.passed = 0
        self.failed=0
        self.failures=[]
    def check(self,g,dut,ref):
        if dut == ref :
            self.passed+=1
        else:
            self.failed+=1
            if len(self.failures) <5:
                self.failures.append((g,dut,ref))

    def report(self):
        total = self.passed + self.failed
        result = "PASS" if self.failed == 0 else "FAIL"
        print(f"[{self.name}] {result}: {total} checked, {self.failed} failed")
        for g, dut, ref in self.failures:
            print(f"    in={g:+.8f} g   dut={dut:6d}   ref={ref:6d}")

# Running a test

def run_test(name,stimulus):
    sb = Scoreboard(name)
    for g in stimulus:
        dut = accel.read_accel(g)
        ref = reference(g)
        sb.check(g,dut,ref)
    sb.report()

#main
run_test("directed",directed_stimulus())
run_test("Random",random_stimulus(10000, seed=1))