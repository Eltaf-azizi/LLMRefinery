import os
import gzip
import shutil
from concurrent.futures import ProcessPoolExecutor
import time


YEAR = 2016
START = time.time()


total_files_decompressed = 0


compressed_dir = f"{YEAR}_j_c"
decompressed_dir = f"{YEAR}_j"



# Create the decompressed directory if it doesn't exist
if not os.path.exists(decompressed_dir):
    os.makedirs(decompressed_dir)

