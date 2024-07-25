from initialization import *
from lifegame import LifeGameConvolution

def run_with_shape(shape_number, grid_size):
    max_t = 1000
    from_showing_graph = 0

    min_size_dict = {
        1: 5,  # グライダー
        2: 4,  # ブロック
        3: 6,  # ビーハイブ
        4: 6,  # ローフ
        5: 5,  # ボート
        6: 5,  # ブリンカー
        7: 6,  # トード
        8: 17, # パルサー
        9: 38  # ゴスパー・グライダー・ガン
    }

    if grid_size < min_size_dict.get(shape_number, 0):
        raise ValueError(f"Grid size too small for shape {shape_number}. Minimum size is {min_size_dict[shape_number]}.")
    
    if shape_number == 1:
        initial_state = create_glider(grid_size)
    elif shape_number == 2:
        initial_state = create_block(grid_size)
    elif shape_number == 3:
        initial_state = create_beehive(grid_size)
    elif shape_number == 4:
        initial_state = create_loaf(grid_size)
    elif shape_number == 5:
        initial_state = create_boat(grid_size)
    elif shape_number == 6:
        initial_state = create_blinker(grid_size)
    elif shape_number == 7:
        initial_state = create_toad(grid_size)
    elif shape_number == 8:
        initial_state = create_pulsar(grid_size)
    elif shape_number == 9:
        initial_state = create_gosper_glider_gun(grid_size)
    else:
        raise ValueError("Invalid shape number. Please choose a number between 1 and 8.")
    
    game = LifeGameConvolution(grid_size, initial_state=initial_state)
    is_frozen, t, all_state = game.run(max_t, from_showing_graph)
    print(f"Simulation ended at step {t} with frozen state: {is_frozen}")

def run_random():
    size = 256
    max_t = 1000
    from_showing_graph = 0

    probabilities = [0.5, 0.5]
    game = LifeGameConvolution(size, probabilities=probabilities)
    is_frozen, t, all_state = game.run(max_t, from_showing_graph)
    print(f"Simulation ended at step {t} with frozen state: {is_frozen}")

def main():
    shape_number = int(input("Enter shape number (1: Glider, 2: Block, 3: Beehive, 4: Loaf, 5: Boat, 6: Blinker, 7: Toad, 8: Pulsar, 9: Gosper Glider Gun): "))
    grid_size = int(input("Enter grid size: "))
    run_with_shape(shape_number, grid_size)

if __name__ == "__main__":
    main()
