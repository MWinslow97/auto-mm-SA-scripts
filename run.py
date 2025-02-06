import Tools.GenDirs as dirs
import Tools.GenInputs as Inps


# molname = input("What is the molecule name? ")
# tempFile = input("What is the temp file? ")
molname = "molecules.txt"
tempFile = "temperatures.txt"

paths = dirs.gen_path(molname, tempFile)

# paths = input("What are the paths? ")
# paths = "path_list.txt"
dirs.gen_directs(paths)

Inps.copy_inp()

Inps.edit_inps()

Inps.make_inpts(paths)