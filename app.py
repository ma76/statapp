import sys
import os 
import glob 
import shutil

# CONST
OUTPUT_DIR = os.getcwd()
FORMAT_DIRECTORIES_MAP = {
    'text': 'notes',
    'video': 'videos',
    'image': 'pcitures',
    'zip': 'compressed',
    'doc': 'documents',
    'unknown': 'other'
}
FORMATS_EXT_MAP = {
    'zip':   ['rar', 'zip'],
    'text':  ['txt', 'md', 'csv'],
    'video': ['mp4', 'mkv', 'avi'],
    'image': ['jpg', 'jpeg', 'png', 'gif'],
    'doc':   ['pdf', 'djvu', 'docx', 'xlsx']
}

# helper
def get_output_path(path):
    return os.path.join(OUTPUT_DIR, path)

def move_file(src, dist):
    shutil.move(src, dist)

def get_ext(path):
    return path.split(".").pop()

def get_format(path):
    ext = get_ext(path)
    assert ext, 'Extenstion must be available'

    for format, extenstions in FORMATS_EXT_MAP.items():
        if ext in extenstions:
            return format

    return 'unknown'


def get_dist(format, output_dir=None):
    ext_dir = FORMAT_DIRECTORIES_MAP[format]
    ext_dir = ext_dir[0].upper() + ext_dir[1:]
    if output_dir is None:
        return get_output_path(ext_dir)
    return os.path.join(output_dir, ext_dir)

if __name__ == '__main__':
    root_dir = r'test' 
    output_dir = root_dir # or change if you want
    for (file_path,_,file_names) in os.walk(root_dir):
        for path in file_names:
            format = get_format(path)
            dist = get_dist(format, output_dir)
            os.makedirs(dist, exist_ok=True)
            move_file(
                get_output_path(os.path.join(file_path, path)), 
                dist
            )



