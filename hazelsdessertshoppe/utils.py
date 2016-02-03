import os
import uuid
from datetime import datetime
import time

DATETIME_FORMAT = '%Y%m%d_%H%M%S_%f'

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def km_to_miles(km):
    return km * 0.62137

def miles_to_km(miles):
    return miles / 0.62137

def get_ext(file_path):
    
    return os.path.splitext(file_path)[1].replace('.','').lower()

def get_base_file_name(file_name):
    
    return os.path.splitext(file_name)[0]

def get_guid32():
    
    return uuid.uuid4().hex

def get_guid64():
    
    return get_guid32() + get_guid32()

def get_guid128():
    
    return get_guid64() + get_guid64()

def get_time_based_file_name():

    return datetime.now().strftime(DATETIME_FORMAT)

def get_media_file_name(ext):
    
    return '{}_{}.{}'.format(get_time_based_file_name(), get_guid32(), ext) 
   
def create_folder_path(folder_path, contains_file_name=False):
    
    if contains_file_name:
        folder_path = os.path.dirname(folder_path)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

if __name__ == '__main__':
    
#     for i in range(10):
#         print(get_guid32())
# 
#     for i in range(10):
#         print(get_guid64())
# 
#     for i in range(10):
#         print(get_guid128())

    for i in range(10):
        time.sleep(.01)
        print(get_time_based_file_name())

    for i in range(10):
        time.sleep(.01)
        print(get_media_file_name('jpg'))
        
