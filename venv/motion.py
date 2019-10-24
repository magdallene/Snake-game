class Move:

    def collision_with_walls(self,snake_head):
        self.snake_head = snake_head
        if self.snake_head[0] >= 500 or self.snake_head[0] < 0 or self.snake_head[1] >= 500 or self.snake_head[1] <0:
            return 1
        else:
            return 0


    def collision_with_self(self,snake_pstn,snake_head):
        self.snake_pstn = snake_pstn
        self.snake_head = snake_head
        snake_head = snake_pstn[0]
        if snake_head in snake_pstn[1:]:
            return 1
        else:
            return 0

