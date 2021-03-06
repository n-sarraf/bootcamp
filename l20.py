import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def xa_to_diameter(xa):
    '''
    Convert an array of cross-sectional areas to diameters with commensurate units.
    '''

    # Compute diameter from areas
    # A = pi * d^2 / 4
    diameter = np.sqrt(xa *4 / np.pi)

    return diameter


def easy_reshape(obj, ncols, order='C'):
    '''
    Guarantee that reshaping works by defining only one shape parameter.
    '''

    # Reshape

    arr = np.reshape(obj, (ncols, len(obj)/ncols, len(obj)/ncols, len(obj)/ncols))

    return arr
