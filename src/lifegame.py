import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt

class LifeGameConvolution:
    def __init__(self, size, probabilities=None, initial_state=None):
        self.size = size
        self.probabilities = probabilities
        self.current_state = self._initialize_automaton(size, probabilities, initial_state)
        self.state_list = []
        self.all_state = [self.current_state]

    def _initialize_automaton(self, size, probabilities, initial_state):
        if initial_state is not None:
            return initial_state
        elif probabilities is not None:
            assert sum(probabilities) == 1, "Probabilities must sum to 1"
            assert len(probabilities) == 2, "Length of probabilities must match cnt_states"
            return np.random.choice(2, size=(size, size), p=probabilities)
        else:
            raise ValueError("Either initial_state or probabilities must be provided")

    def _is_frozen(self):
        current_state = self.current_state.copy()
        self.state_list.append(current_state)

        if len(self.state_list) < 2:
            return False

        slow_ptr, fast_ptr = 0, 1

        while fast_ptr < len(self.state_list):
            if np.array_equal(self.state_list[slow_ptr], self.state_list[fast_ptr]):
                return True
            slow_ptr += 1
            fast_ptr += 2

        max_states = 2
        if len(self.state_list) > max_states:
            self.state_list.pop(0)

        return False

    def _update_generation(self):
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        neighbor_count = convolve(self.current_state, kernel, mode='wrap', cval=0)
        new_state = ((neighbor_count == 3) | ((self.current_state == 1) & (neighbor_count == 2))).astype(int)
        self.current_state = new_state
        self.all_state.append(self.current_state)

    def _plot_current_state(self, img, ax, step, is_frozen):
        img.set_data(self.current_state)
        ax.set_title(f"Step: {step}")
        print(f"\r Current Step: {step+1}, Frozen: {is_frozen}", end="")
        plt.draw()
        plt.pause(0.01)

    def run(self, max_t, from_showing_graph=0):
        plt.ion()
        fig, ax = plt.subplots()
        img = ax.imshow(self.current_state, cmap='binary')
        plt.show()
        is_frozen = False
        for t in range(1, max_t):
            self._update_generation()
            is_frozen = self._is_frozen()
            if t > from_showing_graph:
                self._plot_current_state(img, ax, t, is_frozen)
            if is_frozen:
                break
        print("")
        plt.ioff()
        plt.close()
        return is_frozen, t, self.all_state
