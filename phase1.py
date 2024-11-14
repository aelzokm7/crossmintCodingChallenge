from controllers.polyanet_controller import add_polyanet_to_map
from utils.map_utils import get_current_map_grid, get_goal_map_grid

# Phase 1 #
def phase1(length_of_cross_arm):

    grid = get_goal_map_grid();

    if (grid is None or len(grid) == 0):
        print("Map grid does not exist");
        return;

# Calculate the center of the grid.
# Since the grid is odd, this is straightforward as there is only one center.
# If the matrix was even, it would be more complicated since there isn't one center coordinate.
# However since the even case is not relevant to this challenge, I will skip it.

    center_width_of_grid = len(grid) // 2;
    center_height_of_grid = len(grid[0]) // 2;

# Search through the subgrid that will contain the cross.
# Check at each coordinate if it is diagonal to the center point using the below formula.
# If it is on a diagonal, call the api and populate that coordinate.
    for x in range(center_width_of_grid - length_of_cross_arm, center_width_of_grid + length_of_cross_arm + 1):
        for y in range(center_height_of_grid - length_of_cross_arm, center_height_of_grid + length_of_cross_arm + 1):
            if (abs(x - center_width_of_grid) == abs(y - center_height_of_grid)):
                add_polyanet_to_map(x, y);
    
    print(get_current_map_grid());

# Main Block

if __name__ == "__main__":

    # Input Parameters
    length_of_cross_arm_from_center = 3;

    # function
    phase1(length_of_cross_arm_from_center);



