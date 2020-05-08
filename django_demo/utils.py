import os
from typing import List, Optional

def getenv_bool(name : str, default : bool = False) -> bool:
    """Converts environment variable to True/False value

    Args:
        name - The environment variable to look at
        default - The default value to return if name is not found or is not
                  True/False type value. 
        
    Returns:
        Assumes the environment variable will be a string of 'true'
        or 'false' in any case. All other values will return the default. 

    Raises:
        ValueError - if parameters are invalid types. 
    """
    if type(name) is not str:
        raise ValueError("name must be of type str")

    if type(default) is not bool:
        raise ValueError("default must be of type bool")

    envvalue = os.getenv(name)

    if envvalue is None:
        return default

    envvalue = str(envvalue).lower()

    if envvalue == 'true':
        return True
    elif envvalue == 'false':
        return False
    else:
        return default

def getenv_list(name : str) -> List[str]:
    """Builds a list from an environment variable

    The environment variable must be a comma separated value string.

    Args:
        name - The environment variable to look at
        
    Returns:
        A list of values split using CSV format. If environment variable
        is not set an empty list will be returned. 
    
    Raises:
        ValueError - if parameter is invalid types. 
    """
    if type(name) is not str:
        raise ValueError("name must be of type str")
    
    envvalue = os.getenv(name)

    if envvalue is not None:
        return envvalue.split(',')
    else:
        return []

class EnvironmentVariableNotSetException(Exception):
    pass

def getenv(name : str, raise_exception : bool = True) -> Optional[str]:
    """Retrieves an environment variable and optionally raises exception if not found

    Args:
        name - Environment variable name
        raise_exception - If true (default) an exception is raised. If False no exception
                          will be raised.
    
    Returns:
        The value of an environment variable. If raise_exception is set to False and the
        environment variable is not set None will be returned. 

    Raises:
        ValueError
            If parameters are invalid types
        EnvironmentVariableNotSetException
            If environment variable is not set and raise_exception is True
    """
    if type(name) is not str:
        raise ValueError("name must be of type str")
    
    if type(raise_exception) is not bool:
        raise ValueError("raise_exception must be of type bool")

    envvalue = os.getenv(name)

    if envvalue is None and raise_exception:
        raise EnvironmentVariableNotSetException(f"Environment variable {name} was not found")
    elif envvalue is None:
        return None
    else:
        return envvalue