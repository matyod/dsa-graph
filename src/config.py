import os, sys

# Get the root directory
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

# Get the path to directories
DATA_DIRECTORY = os.path.join(ROOT, 'data')