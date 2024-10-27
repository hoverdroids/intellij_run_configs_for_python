import os

from PyOneLiner import OneLiner
from os import system

working_directory = os.getcwd()
example_1_filepath = os.path.join(working_directory, r"Examples/example_1.py")

oneliner = OneLiner(example_1_filepath, type_="python")

bytes = oneliner.bytes
print(bytes)

bytes_str = str(bytes)
print(bytes_str)

oneliner.normal()
oneline_result = oneliner.done()#done throws an error if a command was not run (e.g. normal, xor, ascii85, lzma, binary, base16, bz2)
print(oneline_result)

oneliner.base64()
oneliner_result = oneliner.done()
print(oneliner_result)
exit()

# oneliner.xor()
# oneline = oneliner.done()
# exec(oneline)

# oneliner.ascii85()
# oneline = oneliner.done()
# exec(oneline)
#
# oneliner = OneLiner("script.py", type_="bash") # Linux
# oneliner.lzma()
# oneline = oneliner.done()
# system(oneline)
#
# oneliner.binary()
# oneline = oneliner.done()
# system(oneline)

# oneliner = OneLiner("script.py", type_="batch") # Windows
# oneliner.base16()
# oneline = oneliner.done()
# system(oneline)
#
# oneliner.bz2()
# oneline = oneliner.done()
# system(oneline)