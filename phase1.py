from classes.Polyanets import Polyanets
from controllers.space_objects_controller import add_space_object_to_map

def phase1(subgrid_offset: int, grid_size: int) -> None:
    """ Function to create a symmetrical X on an Odd-Sized Square Grid. 
        :param subgrid_offset: Determines the height and width of X.
        :param grid_size: The grid size to create the X on.
    """

    # Validate grid_size
    if (grid_size < 0 or grid_size % 2 == 0):
        print("Grid size must be an odd number greater than 0.")
        return;

    # Calculate the center of the grid.
    # Since the grid is odd and square, this is straightforward as there is only one center.
    # If the matrix was even, it would be more complicated since there isn't only one center coordinate.
    # However, since the even case is not relevant to this challenge, I will skip it.
    center: int = grid_size // 2;

    # Validate subgrid_offset
    if (subgrid_offset < 0 or subgrid_offset > center):
        print(f"Subgrid value must be between 0 and {center}");
        return;
 

    # Search through the subgrid that will contain the cross.
    # Check at each coordinate if it is diagonal to the center point using the below formula.
    # If it is on a diagonal, populate that coordinate with a polyanet.
    for x in range(subgrid_offset, grid_size - subgrid_offset):
        for y in range(subgrid_offset, grid_size - subgrid_offset):
            if (abs(x - center) == abs(y - center)):
                polyanets: Polyanets = Polyanets(x, y)
                add_space_object_to_map(polyanets);
    
# Main Block
if __name__ == "__main__":

    # Input Parameters
    subgrid_offset: int = 2;
    grid_size: int = 11;

    phase1(subgrid_offset, grid_size);



