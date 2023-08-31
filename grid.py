import pygame

class grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.cell_colors = self.get_cell_colors()

    def print_grid(self):
        for _rows_ in range(self.num_rows):
            for _cols_ in range(self.num_cols):
                print(self.grid[_rows_][_cols_],end=" ")
            print()
    
    def get_cell_colors(self):
        # cell colors (Red,Green,Blue)
        dark_grey = (26,31,40)
        green = (47,230,23)
        red = (232,18,18)
        orange = (226,116,17)
        yellow = (237,234,4)
        purple = (166,0,247)
        cyan = (21,204,209)
        blue = (13,64,216)

        return [dark_grey,green,red,orange,yellow,purple,cyan,blue]
    
    # for drawing cells in the displaying screen
    def draw(self, screen):
        for _rows_ in range(self.num_rows):
            for _cols_ in range(self.num_cols):
                cell_value = self.grid[_rows_][_cols_]
                cell_rectangle = pygame.Rect(_cols_*self.cell_size, _rows_*self.cell_size, self.cell_size-1, self.cell_size-1)  # Rect(x coordinate, y coordinate, width, height)
                
                # pygame.draw.rect(surface  to draw on, color, rectangle) method to draw the cells
                pygame.draw.rect(screen, self.cell_colors[cell_value], cell_rectangle)