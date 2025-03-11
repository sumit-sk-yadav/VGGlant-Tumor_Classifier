import os
from box.exceptions import BoxValueError 
import yaml
from cnnClassifier import logger # because cnnClassifier is the local package so no need to include src in the import sentence
import json
import joblib
from ensure import ensure_annotations 
from box import ConfigBox # helps in accessing structured data as a dictionary as well as a configuration style calling
from pathlib import Path
from typing import Any
import base64

@ensure_annotations # decorator helps in maintaining the given input and output types and throws an error whenever they dont match with the predefined types
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns the content as a configbox

    Args:
        path_to_yaml (Path): _description_

    Raises:
        ValueError: if yaml file is empty
        e: empty file 

    Returns:
        ConfigBox: returns configbox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """creates directories given in the list

    Args:
        path_to_directories (list): list of paths to create directories at
        verbose (bool, optional): ignore if multiple directories are to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """ saves the contents of a dictionary into a json file

    Args:
        path (Path): path to where the json is to be saved
        data (dict): name of the dictionary that contains the data to be saved
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'json file saved at: {path}')

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """loads a given json file from its path

    Args:
        path (Path): path to the json file that needs to be opened

    Returns:
        ConfigBox: data as class attributes insted of a dict
    """
    with open(path) as f:
        content = json.load(f)
        logger.info(f'json file loaded successfully from: {path}')
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    """saves binary file at a given path location

    Args:
        data (Any): data to be saved in the binary file
        path (Path): path to where the binary file is to be saved
    """
    joblib.dump(value = data, filename=path)
    logger.info(f'binary file saved at: {path}')

@ensure_annotations
def load_bin(path:Path) -> Any:
    """loads a binary file from a given path

    Args:
        path (Path): path to the binary file that is to be loaded

    Returns:
        Any: any object stored in the binary file
    """
    data = joblib.load(path)
    logger.info(f'binary file loaded from; {path}')
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """get size of a file in KB

    Args:
        path (Path): path to a file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring, fileName):
    """decode an image string

    Args:
        imgstring (_type_): image string
        fileName (_type_): name to be saved as
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

@ensure_annotations
def encodeImageIntoBase64(croppedimagepath:Path):
    with open(croppedimagepath, 'rb') as f:
        return base64.b64encode(f.read())