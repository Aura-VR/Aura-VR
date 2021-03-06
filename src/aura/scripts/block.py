#!/usr/bin/env python3

import numpy as np


class Block:
    block_index = 0
    row = 0
    column = 0
    block_info = None
    reshape_block_info = None
    width = 0
    height = 0
    block_width = 0
    block_height = 0

    def __init__(self, block_index, block_info, height, width):
        self.block_index = block_index
        self.row = block_index // 16
        self.column = block_index % 16
        self.block_info = np.asarray(block_info)
        self.block_height = height // 16
        self.block_width = width // 16
        self.width = width
        self.height = height
        self.reshape_block_info = np.asarray(block_info).reshape(height // 16, width // 16)

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def go_up(self):
        return (self.row - 1) * 16 + self.column

    def go_down(self):
        return (self.row + 1) * 16 + self.column

    def go_right(self):
        return self.row * 16 + self.column + 1

    def go_left(self):
        return self.row * 16 + self.column - 1

    def get_neighbors(self):
        return [self.go_up(), self.go_right(), self.go_down(), self.go_left()]

    def get_block(self):
        return self.block_info

    def get_reshaped_block(self):
        return self.reshape_block_info

    def has_unkown(self):
        if len(self.block_info[self.block_info == -1]) == 0:
            return False
        return True

    def get_unkown(self):
        return np.where(self.block_info == -1)

    def get_unkown_reshaped(self):
        return np.where(self.reshape_block_info == -1)

    def is_out_of_map(self):
        block_info = np.asarray(self.block_info).reshape(self.block_width, self.block_height)
        i = np.sum(block_info, axis=0)
        j = np.sum(block_info, axis=1)
        element = 100 * self.block_height
        if element in i:
            return True
        elif element in j:
            return True
        else:
            return False

    def __str__(self):
        return str(self.block_info)
