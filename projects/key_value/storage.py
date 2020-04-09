import os
import tempfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key",  action="store")
parser.add_argument("-v", "--value", action="store", nargs='*')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

#with open(storage_path, 'w') as f:
