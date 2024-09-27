from collections import deque
from src.DriveInterface import DriveInterface
from src.DriveState import DriveState
from src.Constants import DriveMove, SensorData
from src.Utils import manhattan_dist_2D

class Alexandru(DriveInterface):

    def __init__(self, game_id: int, is_advanced_mode: bool):
        """
        Constructor for YourAgent

        Arguments:
        game_id -- a unique value passed to the player drive, you do not have to do anything with it, but will have access.
        is_advanced_mode -- boolean to indicate if the game is in advanced mode or not.
        """
        self.game_id = game_id
        self.need_to_find_target_pod = is_advanced_mode
        self.picked_up = False

    # This is the main function the simulator will call each turn
    def get_next_move(self, sensor_data: dict) -> DriveMove:
        """
        Main function for YourAgent. The simulator will call this function each loop of the simulation to see what your agent's
        next move would be. You will have access to data about the field, your robot's location, other robots' locations and more
        in the sensor_data dict argument.

        Arguments:
        sensor_data -- a dict with state information about other objects in the game. The structure of sensor_data is shown below:
            sensor_data = {
                SensorData.FIELD_BOUNDARIES: [[-1, -1], [-1, 0], ...],
                SensorData.DRIVE_LOCATIONS: [[x1, y1], [x2, y2], ...],
                SensorData.POD_LOCATIONS: [[x1, y1], [x2, y2], ...],
                SensorData.PLAYER_LOCATION: [x, y],
                SensorData.GOAL_LOCATIONS: [[x1, y1], [x2, y2], ...],  # List of goal locations
                SensorData.GOAL_LOCATION: [x, y],  # Kept for compatibility
                SensorData.TARGET_POD_LOCATION: [x, y],  # Only used for Advanced mode
                SensorData.DRIVE_LIFTED_POD_PAIRS: [[drive_id_1, pod_id_1], [drive_id_2, pod_id_2], ...]  # Only used in Advanced mode for seeing which pods are currently lifted by drives
            }

        Returns:
        DriveMove - return value must be one of the enum values in the DriveMove class:
            DriveMove.NONE – Do nothing
            DriveMove.UP – Move 1 tile up (positive y direction)
            DriveMove.DOWN – Move 1 tile down (negative y direction)
            DriveMove.RIGHT – Move 1 tile right (positive x direction)
            DriveMove.LEFT – Move 1 tile left (negative x direction)

            (Advanced mode only)
            DriveMove.LIFT_POD – If a pod is in the same tile, pick it up. The pod will now move with the drive until it is dropped
            DriveMove.DROP_POD – If a pod is in the same tile, drop it. The pod will now stay in this position until it is picked up
        """

        def bfs(destination, obstacles, user_x, user_y):
            queue = deque()
            visited = {user_x, user_y}
            queue.append((DriveMove.UP, user_x, user_y + 1))
            queue.append((DriveMove.RIGHT, user_x + 1, user_y))
            queue.append((DriveMove.DOWN, user_x, user_y - 1))
            queue.append((DriveMove.LEFT, user_x - 1, user_y))

            while len(queue) != 0:
                direction, x, y = queue.popleft()
                if (x, y) in visited or [x, y] in obstacles:
                    continue
                if [x, y] in destination:
                    return direction
                if (0 <= x < 40) and (0 <= y < 40):
                    visited.add((x, y))
                    queue.append((direction, x, y + 1))
                    queue.append((direction, x + 1, y))
                    queue.append((direction, x, y - 1))
                    queue.append((direction, x - 1, y))
            return DriveMove.NONE

        user_x, user_y = sensor_data[SensorData.PLAYER_LOCATION]
        if self.need_to_find_target_pod and not self.picked_up:
            if [user_x, user_y] == sensor_data[SensorData.TARGET_POD_LOCATION]:
                self.picked_up = True
                return DriveMove.LIFT_POD
            return bfs([sensor_data[SensorData.TARGET_POD_LOCATION]], sensor_data[SensorData.DRIVE_LOCATIONS], user_x,
                       user_y)
        if self.picked_up:
            return bfs(sensor_data[SensorData.GOAL_LOCATIONS],
                       sensor_data[SensorData.DRIVE_LOCATIONS] + sensor_data[SensorData.POD_LOCATIONS], user_x, user_y)
        return bfs(sensor_data[SensorData.GOAL_LOCATIONS], sensor_data[SensorData.DRIVE_LOCATIONS], user_x, user_y)