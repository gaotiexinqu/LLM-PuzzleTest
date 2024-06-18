from data_generation import create_data

class_list = [
    "circle_size_number","color_grid","color_hexagon","color_number_hexagon","color_overlap_squares", # ok
    "color_size_circle","grid_number_color","grid_number","polygon_sides_color","polygon_sides_number",
    "rectangle_height_color","rectangle_height_number","shape_morph","shape_reflect","shape_size_grid",
    "shape_size_hexagon","size_cycle","size_grid","triangle","venn"
]

for i in class_list:
    create_data(i, limit=200, unique=True)
print("finish generation!")

