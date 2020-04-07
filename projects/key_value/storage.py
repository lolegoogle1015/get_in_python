import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
print(storage_path)
#with open(storage_path, 'w'):
