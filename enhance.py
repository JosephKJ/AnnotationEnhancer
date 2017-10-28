import os


class Enhancer:
    def __init__(self, path_to_images, path_to_annotations):
        self.img_path = path_to_images
        self.annotation_path = path_to_annotations
        self._validate_paths()

    def _validate_paths(self):
        # Can check whether the number of files in the annotations is the same as the number of images
        pass

if __name__ == '__main__':
    img_db_path = os.path.join('./data/images')
    annotation_path = os.path.join('./data/annotations')
    e = Enhancer(img_db_path, annotation_path)
