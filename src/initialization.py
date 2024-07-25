import numpy as np

def create_glider(grid_size):
    glider = np.zeros((grid_size, grid_size), dtype=int)
    glider[1, 2] = glider[2, 3] = glider[3, 1] = glider[3, 2] = glider[3, 3] = 1
    return glider

def create_block(grid_size):
    block = np.zeros((grid_size, grid_size), dtype=int)
    block[1, 1] = block[1, 2] = block[2, 1] = block[2, 2] = 1
    return block

def create_beehive(grid_size):
    beehive = np.zeros((grid_size, grid_size), dtype=int)
    beehive[1, 2] = beehive[1, 3] = beehive[2, 1] = beehive[2, 4] = beehive[3, 2] = beehive[3, 3] = 1
    return beehive

def create_loaf(grid_size):
    loaf = np.zeros((grid_size, grid_size), dtype=int)
    loaf[1, 2] = loaf[1, 3] = loaf[2, 1] = loaf[2, 4] = loaf[3, 2] = loaf[3, 4] = loaf[4, 3] = 1
    return loaf

def create_boat(grid_size):
    boat = np.zeros((grid_size, grid_size), dtype=int)
    boat[1, 1] = boat[1, 2] = boat[2, 1] = boat[2, 3] = boat[3, 2] = 1
    return boat

def create_blinker(grid_size):
    blinker = np.zeros((grid_size, grid_size), dtype=int)
    blinker[2, 1] = blinker[2, 2] = blinker[2, 3] = 1
    return blinker

def create_toad(grid_size):
    toad = np.zeros((grid_size, grid_size), dtype=int)
    toad[2, 2] = toad[2, 3] = toad[2, 4] = toad[3, 1] = toad[3, 2] = toad[3, 3] = 1
    return toad

def create_pulsar(grid_size):
    pulsar = np.zeros((grid_size, grid_size), dtype=int)
    coords = [
        (4, 6), (4, 7), (4, 8), (4, 12), (4, 13), (4, 14),
        (6, 4), (6, 9), (6, 11), (6, 16),
        (7, 4), (7, 9), (7, 11), (7, 16),
        (8, 4), (8, 9), (8, 11), (8, 16),
        (9, 6), (9, 7), (9, 8), (9, 12), (9, 13), (9, 14),
        (11, 6), (11, 7), (11, 8), (11, 12), (11, 13), (11, 14),
        (12, 4), (12, 9), (12, 11), (12, 16),
        (13, 4), (13, 9), (13, 11), (13, 16),
        (14, 4), (14, 9), (14, 11), (14, 16),
        (16, 6), (16, 7), (16, 8), (16, 12), (16, 13), (16, 14)
    ]
    for x, y in coords:
        pulsar[x, y] = 1
    return pulsar

def create_gosper_glider_gun(grid_size):
    if grid_size < 38:
        raise ValueError("Grid size too small for Gosper Glider Gun. Minimum size is 38.")
    
    gun = np.zeros((grid_size, grid_size), dtype=int)
    
    coords = [
        (5, 1), (5, 2), (6, 1), (6, 2),
        (3, 13), (3, 14), (4, 12), (4, 16), (5, 11), (5, 17), (6, 11), (6, 15), (6, 17), (6, 18), (7, 11), (7, 17),
        (8, 12), (8, 16), (9, 13), (9, 14),
        (1, 25), (2, 23), (2, 25), (3, 21), (3, 22), (4, 21), (4, 22), (5, 21), (5, 22), (6, 23), (6, 25), (7, 25),
        (3, 35), (3, 36), (4, 35), (4, 36)
    ]
    
    for x, y in coords:
        gun[x, y] = 1
    
    return gun
