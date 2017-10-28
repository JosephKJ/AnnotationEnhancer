import os
import cv2
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from lib.map import HeatMap

class Enhancer:
    def __init__(self, path_to_images, path_to_annotations, path_to_enhanced_annotations, img_file_extension='jpg'):
        self.heatmap_obj = HeatMap()
        self.img_path = path_to_images
        self.annotation_path = path_to_annotations
        self.dest_annotation_path = path_to_enhanced_annotations
        self.img_file_extension = img_file_extension
        self._validate_paths()

    def _validate_paths(self):
        # Can check whether the number of files in the annotations is the same as the number of images
        pass

    def _assert_path(self, path, error_message):
        assert os.path.exists(path), error_message

    def _display_image(self, image):
        # plt.axis('off')
        frame = plt.gca()
        frame.axes.get_xaxis().set_ticks([])
        frame.axes.get_yaxis().set_ticks([])
        plt.imshow(image)
        plt.show()

    def _display_images(self, images):
        plt.figure()
        # plt.figure(figsize=(20, 10))
        columns = 10
        for i, image in enumerate(images):
            plt.subplot(len(images) / columns + 1, columns, i + 1)
            frame = plt.gca()
            frame.axes.get_xaxis().set_ticks([])
            frame.axes.get_yaxis().set_ticks([])
            plt.imshow(image)
        plt.show()

    def enhance(self):
        # Read each annotation
        for annotation_file in os.listdir(self.annotation_path):
            if os.path.isfile(os.path.join(self.annotation_path, annotation_file)):

                # Read the corresponding image
                file_name, _ = annotation_file.split('.')
                image_path = os.path.join(self.img_path, file_name + '.' + self.img_file_extension)
                self._assert_path(image_path, 'The corresponding image file for annotation not found at: ' + image_path)

                image = cv2.imread(image_path, cv2.IMREAD_COLOR)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # Parse the xml annotation
                annotation_xml = open(os.path.join(self.annotation_path, annotation_file), 'r')
                tree = ET.parse(annotation_xml)
                root = tree.getroot()

                # For each bb-annotation in annotation:
                patches = []
                heatmaps = []
                for annotation in root.findall('./object'):
                    xmin = int(annotation.find('./bndbox/xmin').text)
                    ymin = int(annotation.find('./bndbox/ymin').text)
                    xmax = int(annotation.find('./bndbox/xmax').text)
                    ymax = int(annotation.find('./bndbox/ymax').text)

                    # Crop the patch
                    patch = image[ymin:ymax, xmin:xmax]
                    patches.append(patch)

                    # Get the objectness
                    heat_map = self.heatmap_obj.get_map(patch)
                    heatmaps.append(heat_map)

                self._display_images(patches)
                self._display_images(heatmaps)

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
