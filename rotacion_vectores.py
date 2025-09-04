import numpy as np


def rot_x(x:float, y:float, z:float, theta:float):
    '''
    Descripcion

    Parameters:
        x (float): Coordenada x del punto original
        y (float): Coordenada x del punto original
        z (float): Coordenada x del punto original
        theta (float): Angulo de rotacion en radianes

    Returns:
        Vector rotado de (x, y, z)
    '''

    p = np.array([x, y, z])
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

    return np.matmul(R, p)

def rot_y(x:float, y:float, z:float, theta:float):
    '''
    Descripcion

    Parameters:
        x (float): Coordenada x del punto original
        y (float): Coordenada x del punto original
        z (float): Coordenada x del punto original
        theta (float): Angulo de rotacion en radianes

    Returns:
        Vector rotado de (x, y, z)
    '''

    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

    return np.matmul(R, p)

def rot_z(x:float, y:float, z:float, theta:float):
    '''
    Descripcion

    Parameters:
        x (float): Coordenada x del punto original
        y (float): Coordenada x del punto original
        z (float): Coordenada x del punto original
        theta (float): Angulo de rotacion en radianes

    Returns:
        Vector rotado de (x, y, z)
    '''

    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    
    return np.matmul(R, p)

def rotar(x:float, y:float, z:float, theta:float, axis str):
    '''
    Descripcion
    Rota en un punto 3D al rededor de un eje

    Parameters:
        x (float): Coordenada x del punto original
        y (float): Coordenada x del punto original
        z (float): Coordenada x del punto original
        theta (float): Angulo de rotacion en radianes
        axis (str): Eje de rotacion

    Returns:
        Vector rotado de (x, y, z)
    '''
    axis = axis.lower()
    if axis == 'x':
        return rot_x(x, y, z, theta)
    elif axis == 'y':
        return rot_x(x, y, z, theta)
    elif axis == 'z':
        return rot_x(x, y, z, theta)
    else: 
        raise ValueError("Eje invialido, usa x, y o z")