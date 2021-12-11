import numpy as np
from scipy.signal import convolve

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = np.array([list(i) for i in input_data.splitlines()], dtype=np.int32)

    return increase_and_flash(input_data, 100)


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = np.array([list(i) for i in input_data.splitlines()], dtype=np.int32)

    return increase_and_flash(input_data)

def increase_and_flash(octos: np.array = None, stop=np.inf):
    # the frame for convolving over it
    frame = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    count = 0
    step = 0

    new_octos = octos
    while True:
        octos += 1
        step += 1
        flash_mask = octos > 9
        flashed = True

        while flashed:
            neighbour_flashes = convolve(flash_mask, frame, mode='same').astype(int)
            new_octos = octos + neighbour_flashes
            new_flash_mask = new_octos > 9
            flashed = (new_flash_mask & ~flash_mask).sum().sum() > 0
            flash_mask = new_flash_mask

        octos = new_octos
        octos[flash_mask] = 0
        count += new_flash_mask.sum().sum()

        if step == stop:
            return count

        if flash_mask.all().all() and stop==np.inf:
            return step
