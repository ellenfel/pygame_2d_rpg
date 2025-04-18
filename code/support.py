from csv import reader
from os import walk
import pygame
import os

def import_csv_layout(path):
    terrain_map = []
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, path)
    
    with open(full_path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list = []
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, path)

    for _, __, img_files in walk(full_path):
        print(f"Found files: {img_files}")
        for image in img_files:
            image_path = os.path.join(full_path, image)
            image_surf = pygame.image.load(image_path).convert_alpha()
            surface_list.append(image_surf)

    print(f"Loaded {len(surface_list)} images from {full_path}")
    return surface_list