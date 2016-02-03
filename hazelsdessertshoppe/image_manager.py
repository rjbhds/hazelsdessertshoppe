import os
import shutil
import glob
from PIL import Image

from hazelsdessertshoppe.utils import get_ext, get_media_file_name, create_folder_path

class ImageWrapper(object):
    DEFAULT_JPEG_QUALITY = 100
    DEFAULT_JPEG_QUALITY_WEB = 80
    
    FORMAT_JPEG = 'JPEG'
    FORMAT_PNG = 'PNG'
    FORMAT_GIF = 'GIF'
    FORMAT_BMP = 'BMP'
    
    MODE_RGB = 'RGBA'
    
    DEFAULT_BACKGROUND_COLOR = (255, 255, 255, 255) #'white'
    
    EXTS_JPEG = ['jpg','jpeg']
    EXTS_PNG = ['png']
    EXTS_GIF = ['gif']
    EXTS_BMP = ['bmp']
    
    exts = {
        FORMAT_JPEG: EXTS_JPEG,
        FORMAT_PNG: EXTS_PNG,
        FORMAT_GIF: EXTS_GIF,
        FORMAT_BMP: EXTS_BMP
    }
    
    def __init__(self, full_file_path):
        
#         self.optimize = False
        
        self.init(full_file_path)
        
    def __getattr__(self,key):
        
        if key == '_img':
            raise AttributeError()

        return getattr(self._img,key)
    
    def __str__(self):
        
        return self.file_name

    def init(self, full_file_path):
        
        self.full_file_path = full_file_path
        self.folder_path = os.path.dirname(full_file_path)
        self.file_name = os.path.basename(full_file_path)
        self.ext = get_ext(self.full_file_path)
        
        self._img = Image.open(self.full_file_path)
        self.width = self._img.size[0]
        self.height = self._img.size[1]
        self.file_size = os.stat(full_file_path).st_size
        
    def resize(self, new_width=None, new_height=None, antialias=False):

#         print('self.full_file_path = {}'.format(self.full_file_path))
#         
        if not new_width and not new_height:
            raise Exception('Cannot resize without at least a width or height!')
        
        if not new_height:
            wpercent = (new_width/float(self.width))
            new_height = int((float(self.height) * float(wpercent)))

        if not new_width:
            hpercent = (new_height/float(self.height))
            new_width = int((float(self.width) * float(hpercent)))

        if antialias:
            self._img = self._img.resize((new_width,new_height), Image.ANTIALIAS)
        else:
            self._img = self._img.resize((new_width,new_height))

        self._img.save(self.full_file_path)
    
#         self.init(self.full_file_path)
#         
#         return self

    def convert(self, new_format):

        new_ext = self.exts[new_format][0]
        
        new_full_file_path = self.full_file_path.replace('.' + self.ext, '.' + new_ext)
        
        if self._img.format == self.FORMAT_PNG:
            if new_ext in self.EXTS_JPEG:
                if self._img.mode != self.MODE_RGB:
                    self._img = self._img.convert(self.MODE_RGB)
            
        self._img.save(new_full_file_path)
        
        self.init(new_full_file_path)
        
        return self
    
    def crop(self, size_tuple, from_center=False):
        
        box = self._get_box((self.width, self.height), size_tuple, from_center)

        thumb_img = self._img.crop(box)
        thumb_img.save(self.full_file_path)
        
        self.init(self.full_file_path)
        
        return self
    
    def reduce(self, quality=None):
        
        if not quality:
            quality = self.DEFAULT_JPEG_QUALITY
        
        self._img.save(self.full_file_path, optimize=True, quality=quality)
        
        self.init(self.full_file_path)
        
        return self

    def overlay_on_white_background(self, background_width, background_height, centered=False):
        # This presumes that this image is reduced
        # to fit inside the dimensions of the white
        # background.

        box = self._get_box((background_width, background_height),(self.width, self.height), centered)

        bg_img = self._get_white_image(background_width, background_height)
        
        bg_img.paste(self._img, box)

        bg_img.save(self.full_file_path)
        
        self.init(self.full_file_path)
        
        return self
        
    def get_image_info(self):
        retval = []
        
        retval.append('File Name: {}'.format(self.file_name))
        retval.append('File Size: {} bytes'.format(self.file_size))
        retval.append('Format:    {}'.format(self._img.format))
        retval.append('Size:      {}x{}'.format(self.width, self.height))
        retval.append('Mode:      {}'.format(self._img.mode))

        return '\n'.join(retval)

    def _get_box(self, outer_size_tuple, inner_size_tuple, from_center):
            
        left = 0
        top = 0
        right = inner_size_tuple[0]
        bottom = inner_size_tuple[1]

        if from_center:
            left = int((outer_size_tuple[0] - right) / float(2))
            top = int((outer_size_tuple[1] - bottom) / float(2))
            right = left + right
            bottom = top + bottom
        
        box = (left, top, right, bottom)

        return box

    def _get_white_image(self, width, height):
        
        return Image.new(self.MODE_RGB, (width, height), self.DEFAULT_BACKGROUND_COLOR)
    
class ImageManager(object):
    
    DEFAULT_ORIG_FOLDER_NAME = 'orig'
    DEFAULT_THUMBNAIL_FOLDER_NAME = 'thumbs'
    DEFAULT_CAROUSEL_FOLDER_NAME = 'carousel'

    DEFAULT_CAROUSEL_SIZE = (800,356)
    DEFAULT_THUMBNAIL_SIZE = (72,72)
    
    def __init__(self):
        
        self.verbose = False
    
    def resize_image(self, full_file_path, new_width=None, new_height=None, antialias=False):
        
        if not new_width and not new_height:
            raise Exception('Cannot resize without at least a width or height!')
        
        img = ImageWrapper(full_file_path)
        
        if self.verbose:
            print('==== Before Resize ====')
            print(img.get_image_info())
        
        img = img.resize(new_width, new_height, antialias)
        
        if self.verbose:
            print('==== After Resize ====')
            print(img.get_image_info())
        
        return img

    def resize_all_in_folder(self, folder_path, file_name_pattern, new_width=None, new_height=None, antialias=False):
        
        folder_pattern = os.path.join(folder_path, file_name_pattern)
        file_list = glob.glob(folder_pattern)
        
        for full_file_path in file_list:

            self.resize_image(full_file_path, new_width, new_height, antialias)
    
    def convert_image(self, full_file_path, new_format, delete_orig=False):
        
        img = ImageWrapper(full_file_path)
        
        if self.verbose:
            print('==== Before Convert ====')
            print(img.get_image_info())
        
        img = img.convert(new_format)
        if self.verbose:
            print('==== After Convert ====')
            print(img.get_image_info())

        if delete_orig:
            os.remove(full_file_path)
        
        return img

    def convert_all_in_folder(self, folder_path, file_name_pattern, new_format, delete_orig=False):
        
        folder_pattern = os.path.join(folder_path, file_name_pattern)
        file_list = glob.glob(folder_pattern)
        
        for full_file_path in file_list:

            self.convert_image(full_file_path, new_format, delete_orig)
    
    def crop_image(self, full_file_path, size_tuple, from_center=False):
        
        img = ImageWrapper(full_file_path)
        
        if self.verbose:
            print('==== Before Crop ====')
            print(img.get_image_info())
        
        img = img.crop(size_tuple, from_center)
        
        if self.verbose:
            print('==== After Crop ====')
            print(img.get_image_info())
        
        return img

    def reduce_image(self, full_file_path, quality=None):
        
        if not quality:
            ImageWrapper.DEFAULT_JPEG_QUALITY
            
        img = ImageWrapper(full_file_path)
        
        if self.verbose:
            print('==== Before Reduce ====')
            print(img.get_image_info())
        
        img = img.reduce(quality)
        
        if self.verbose:
            print('==== After Reduce ====')
            print(img.get_image_info())
        
        return img

    def overlay_image_on_white_background(self, full_file_path, background_width, background_height, centered=False):

        img = ImageWrapper(full_file_path)
        
        if self.verbose:
            print('==== Before Overlay ====')
            print(img.get_image_info())
        
        img = img.overlay_on_white_background(background_width, background_height, centered)
        
        if self.verbose:
            print('==== After Overlay ====')
            print(img.get_image_info())
        
        return img

    def process_image(self, full_file_path, create_thumbnail=False, create_carousel=False):
        
        # Get the pieces of the file and path that
        # we need to process the file.
        folder_root_path = os.path.dirname(full_file_path)
        ext = get_ext(full_file_path)
        orig_file_name = get_media_file_name(ext)
        carousel_file_name = orig_file_name.replace('.' + ext, '_carousel.{}'.format(ext))
        thumb_file_name = orig_file_name.replace('.' + ext, '_thumb.{}'.format(ext))
        
        orig_full_file_path = os.path.join(folder_root_path, self.DEFAULT_ORIG_FOLDER_NAME, orig_file_name)
        create_folder_path(orig_full_file_path, contains_file_name=True)
        shutil.copy2(full_file_path, orig_full_file_path)

        if create_carousel:
            carousel_full_file_path = os.path.join(folder_root_path, self.DEFAULT_CAROUSEL_FOLDER_NAME, carousel_file_name)
            create_folder_path(carousel_full_file_path, contains_file_name=True)
            shutil.copy2(full_file_path, carousel_full_file_path)
            
            img = ImageWrapper(carousel_full_file_path)
            if self.verbose:
                print('==== Before Create Carousel ====')
                print(img.get_image_info())

            img = self.resize_image(carousel_full_file_path, new_width=None, new_height=self.DEFAULT_CAROUSEL_SIZE[1], antialias=True)

            img = self.overlay_image_on_white_background(carousel_full_file_path, self.DEFAULT_CAROUSEL_SIZE[0], self.DEFAULT_CAROUSEL_SIZE[1], centered=True)
        
            img = self.reduce_image(carousel_full_file_path, ImageWrapper.DEFAULT_JPEG_QUALITY_WEB)
                    
            if self.verbose:
                print('==== After Create Carousel ====')
                print(img.get_image_info())
            
        if create_thumbnail:
            thumb_full_file_path = os.path.join(folder_root_path, self.DEFAULT_THUMBNAIL_FOLDER_NAME, thumb_file_name)
            create_folder_path(thumb_full_file_path, contains_file_name=True)
            shutil.copy2(full_file_path, thumb_full_file_path)
            
            img = ImageWrapper(thumb_full_file_path)

            if self.verbose:
                print('==== Before Create Thumbnail ====')
                print(img.get_image_info())

            if img.height > img.width:
                img = self.resize_image(thumb_full_file_path, new_width=self.DEFAULT_THUMBNAIL_SIZE[0], new_height=None, antialias=True)
            else:
                img = self.resize_image(thumb_full_file_path, new_width=None, new_height=self.DEFAULT_THUMBNAIL_SIZE[1], antialias=True)
            
            img = self.crop_image(thumb_full_file_path, self.DEFAULT_THUMBNAIL_SIZE, from_center=True)
        
            img = self.reduce_image(thumb_full_file_path, ImageWrapper.DEFAULT_JPEG_QUALITY_WEB)
                    
            if self.verbose:
                print('==== After Create Thumbnail ====')
                print(img.get_image_info())

        os.remove(full_file_path)
            
    def process_all_images_in_folder(self, folder_path, file_name_pattern=None, create_thumbnail=False, create_carousel=False):
        
        if file_name_pattern:
            folder_path_pattern = os.path.join(folder_path, file_name_pattern)
        else:
            folder_path_pattern = os.path.join(folder_path, '*')
        
        file_list = glob.glob(folder_path_pattern)
        
        for full_file_path in file_list:
            if os.path.isfile(full_file_path):
                self.process_image(full_file_path, create_thumbnail, create_carousel)
                
        return 'Done'

        
if __name__ == '__main__':
    
    im = ImageManager()
    im.verbose = True
    
#     file_folder = 'C:\\Users\\rjbde\\Google Drive\\development\\quinnrose\\quinnrose\\static\\quinnrose\\images'
#     file_name = 'record_not_found.png'
#     full_file_path = os.path.join(file_folder, file_name)
#     im.convert_image(full_file_path, ImageWrapper.FORMAT_JPEG, delete_orig=True)
    
#     file_folder = 'C:\\Users\\rjbde\\Google Drive\\development\\quinnrose\\quinnrose\\static\\quinnrose\\images\\cc_icons'
#     file_name_pattern = '*.png'
#     im.convert_all_in_folder(file_folder, file_name_pattern, ImageWrapper.FORMAT_JPEG, delete_orig=True)

#     file_folder = 'C:\\Users\\rjbde\\Google Drive\\development\\quinnrose\\artist\\static\\artist\\images'
#     file_name = 'gray-star.jpg'
#     full_file_path = os.path.join(file_folder, file_name)
#     im.resize_image(full_file_path, 40, antialias=True)

    file_folder = 'C:\\Users\\rjbde\\Google Drive\\development\\quinnrose\\quinnrose\\static\\quinnrose\\images\\cc_icons'
    file_name_pattern = '*.png'
    im.resize_all_in_folder(file_folder, file_name_pattern, new_width=40, antialias=False)

#     file_folder = 'C:\\Temp\\temp'
#     im.process_all_images_in_folder(file_folder, create_thumbnail=True, create_carousel=True)
    
#     file_name = '77533_orig.jpg'
#     full_file_path = os.path.join(file_folder, file_name)
#     im.process_image(full_file_path)

    