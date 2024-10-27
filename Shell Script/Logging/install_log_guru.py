import subprocess
import sys
print("... Loguru Run Config Start ...")
subprocess.check_call([sys.executable,"-m","pip","install","loguru"])
print("... Loguru Run Config End ...")