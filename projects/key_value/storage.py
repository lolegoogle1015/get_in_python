import os
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key",  action="store")
parser.add_argument("-v", "--value", action="store", nargs='*')
args = parser.parse_args()
data = dict()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


if (args.key and not args.value) and os.stat(storage_path).st_size == 0:
    print("The file is empty !")
else:
    if args.key and args.value:
        if os.path.exists(storage_path):
            with open(storage_path, 'r') as f:
                data = json.load(f)
        with open(storage_path, 'w') as f:
            if args.key in data:
                data[args.key].extend(args.value)
            else:
                data[args.key] = []
                data[args.key].extend(args.value)

            json.dump(data, f, indent=2)

    elif args.key and  not args.value:
        with open(storage_path, 'r') as f:
            data = json.load(f)
            if args.key in data:
                print(', '.join(data[args.key]))
            else:
                print(None)

    else:
        print("You should pass some arguments")
