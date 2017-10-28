import os


class Enhancer:
    def __init__(self, path_to_images, path_to_annotations, path_to_enhanced_annotations):
        self.img_path = path_to_images
        self.annotation_path = path_to_annotations
        self.dest_annotation_path = path_to_enhanced_annotations
        self._validate_paths()

    def _validate_paths(self):
        # Can check whether the number of files in the annotations is the same as the number of images
        pass

    def enhance(self):
        # Read each annotation

        # Read the corresponding image
        # For each bb-annotation in annotation, crop the patch, get the objectness, check retention criteria,
        #   make BB tight, add to the annotation list.
        # Write back the annotation
        pass

if __name__ == '__main__':
    img_db_path = os.path.join('./data/images')
    annotation_path = os.path.join('./data/annotations')
    dest_annotation_path = os.path.join('./data/enhanced_annotations')

    e = Enhancer(img_db_path, annotation_path, dest_annotation_path)
    e.enhance()
