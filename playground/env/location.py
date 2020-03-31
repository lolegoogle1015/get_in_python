import requests

def get_location_info():
    return requests.get("http://api.ipstack.com/46.119.189.100?access_key=f3c99710f700b423132ad655fd699516").json()

if __name__ == '__main__':
    print(get_location_info())
