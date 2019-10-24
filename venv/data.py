import numpy as np
import math

class Calculation:
    def angle_bw_apple_snake(self, snake_position, apple_position):
        apple_direction_v = np.array(apple_position) - np.array(snake_position)
        snake_direction_v = np.arrat(snake_position[0]) - np.array(snake_position[1])

        normalized_apple = np.linalg.norm(apple_direction_v)
        normalized_snake = np.linalg.norm(snake_direction_v)
        if normalized_apple == 0:
            normalized_apple = 10
        if normalized_snake == 0:
            normalized_snake = 10

        apple_direction_normalized = apple_direction_v/normalized_apple
        snake_direction_normalized = snake_direction_v/normalized_snake
        angle = math.atan2(apple_direction_normalized[1]*snake_direction_normalized[0]- apple_direction_normalized[0]*snake_direction_normalized[1],apple_direction_normalized[1]*snake_direction_normalized[1] + apple_direction_normalized[0] * snake_direction_normalized[0])/math.pi
        return angle






