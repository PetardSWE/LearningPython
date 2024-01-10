import os
import glob
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")
icafiles = glob.glob(downloads_path + "/*.ica")
logfiles = glob.glob(downloads_path + "/*.log")
filecounter = len(icafiles + logfiles)

print(f"\nTar bort {len(icafiles)} .ica-filer")

for icafile in icafiles:
    print(f"Tar bort: {icafile[26:]}")
    os.remove(icafile)

print(f"\nDet finns {len(logfiles)} .log-filer i downloads-mappen")

for logfile in logfiles:
    answer = input(f"Ta bort: {logfile[26:]}? y/n: ")
    if answer == "y":
        os.remove(logfile)

if filecounter == 0:
    print(f"\nDet fanns inga filer.")

else:
    print(f"\nFärdigt!")
