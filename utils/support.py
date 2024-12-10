from inspect import stack
from os import walk
from pygame import Surface
from pygame.image import load as load_image
from typing import Optional, Union
from json import load as _load

def get_graphics_images_from_folder(folder_path: str) -> Optional[list[Surface]]:
    try:
        images: list[Surface] = []
        for _, __, img_files in walk(folder_path):
            for image in img_files:
                image_path: str = f'{folder_path}/{image}'
                image_surface: Surface = load_image(image_path).convert_alpha()
                images.append(image_surface)
                
        return images
                
    except Exception as error:
        error_name: str = type(error).__name__
        print(f'[Exception]::[{error_name} occured in import_graphics_images_from_folder: {error}]')
        for item in stack():
            print(item.function)
        return None
    

def read_item_data_from_json(data_type: str) -> Optional[list[dict[str, Union[str, int]]]]:
    try:
        file_path: str = f'./data/item_data/{data_type}.json'

        with open(file=file_path, mode='r') as file:
            data = _load(file)

            return data

    except Exception as error:
        error_name: str = type(error).__name__
        print(f'[Exception]::[{error_name} occured in read_item_data_from_json: {error}]')
        for item in stack():
            print(item.function)
        return None