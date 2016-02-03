import os
import shutil

from django.conf import settings

from hazelsdessertshoppe.config import PRODUCT_IMAGE_MAX_LONG_SIDE, PRODUCT_IMAGE_PROFILE_WIDTH, PRODUCT_IMAGE_LIST_WIDTH
from hazelsdessertshoppe.image_manager import ImageWrapper
from hazelsdessertshoppe.utils import get_base_file_name, get_ext

# def handle_uploaded_file(file_object):
#     
#     if not os.path.exists(settings.MEDIA_ROOT):
#         os.mkdir(settings.MEDIA_ROOT)
#         
#     full_file_path = os.path.join(settings.MEDIA_ROOT, file_object.name)
#     
#     with open(full_file_path, 'wb+') as destination:
#         for chunk in file_object.chunks():
#             destination.write(chunk)

def generate_file_url(file_url, suffix):
    
    url_arr = file_url.split('/')
    
    file_name = url_arr[len(url_arr)-1]
    new_file_name = '{}_{}.{}'.format(
        get_base_file_name(file_name),
        suffix,
        get_ext(file_name)
    )
    
    retval = file_url.replace(file_name, new_file_name)
#     print('retval = {}'.format(retval))

    return retval
    
def resize_image(image_url):
    """
    Change the size of the downloaded file if it's really big.
    """
    
#     print('settings.BASE_DIR = {}'.format(settings.BASE_DIR))
#     print('image_url = {}'.format(image_url))
    full_file_path = settings.BASE_DIR + image_url
    iw = ImageWrapper(full_file_path)
    
    if max([iw.width, iw.height]) > PRODUCT_IMAGE_MAX_LONG_SIDE:
        if iw.width > iw.height:
            iw.resize(new_width=PRODUCT_IMAGE_MAX_LONG_SIDE, antialias=True)
        elif iw.height > iw.width:
            iw.resize(new_height=PRODUCT_IMAGE_MAX_LONG_SIDE, antialias=True)

def create_image_version(image_url, version_type):
    
    if version_type == 'profile':
        max_width = PRODUCT_IMAGE_PROFILE_WIDTH
    elif version_type == 'thumb':
        max_width = PRODUCT_IMAGE_LIST_WIDTH
    else:
        raise Exception('Could not create image for version type = {}'.format(version_type))
    
    full_file_path = settings.BASE_DIR + image_url
#     print('full_file_path = {}'.format(full_file_path))

    new_image_url = generate_file_url(image_url, version_type)
    new_full_file_path = settings.BASE_DIR + new_image_url
#     print('new_full_file_path = {}'.format(new_full_file_path))
    
    shutil.copy2(full_file_path, new_full_file_path)
    
    iw = ImageWrapper(new_full_file_path)

    if iw.width > max_width:
        iw.resize(new_width=max_width, antialias=True)
