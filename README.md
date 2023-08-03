## AUTONOMUS MOBILE ROBOTS 2022-2023 SPRING FINAL PROJECT REPORT

INSTRUCTOR			: Assoc. Prof. Dr. Ahmet Çağdaş SEÇKİN

STUDENT NAME		: Buse Latife Beker

STUDENT ID			: 181805067

 

ENGINNERING FACULTY - COMPUTER ENGINEERING DEPARTMENT



#	HOUSE/MAZE PLAN
## Indoor Model in the Coppeliasim Simulator

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/83f53fe1-d387-428a-be80-ca8d089dedf6)

## Mobile Robot

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/02e4045c-b632-4d23-b888-6622d3cd5a2b)

## 2D Map of the House Plan

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/af525554-3187-4f40-b14a-3b9afff85604)

#	METHOD

## Python Code for Mapping

Necessary imports

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/f6cb5af2-a3bf-4bcf-a68c-24ce5bcafd1c)

Codes were written for robot connection. Object definitions were made using the `Vrep.simxGetObjectHandle` function. These objects can include sensors, motors, and other items.

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/f19a68c9-0e28-400f-95aa-cfcb9df15cb4)

First, the empty lists `px` and `py` are created. These lists will be used to store the x and y coordinates of the data received from the lidar sensor.
An empty string variable named `statuskey` is created. This variable will be used to hold the state of the key pressed from the keyboard.
A function named `key_press` is defined. This function will be called when a key is pressed from the keyboard and will update the `statuskey` variable with the value of the pressed key. This function is passed to `keyboard.Listener` which is used to listen for keyboard input.
A function called `rotate_vector` is defined. This function is used to rotate a given data vector by a specified angle. The function returns the incoming data vector at the specified angle and returns the returned vector.
The element `keyboard.Listener` is connected to the `key_press` function with the `on_press` parameter. This starts a listener to receive key input from the keyboard.
The `time.sleep(1)` command causes the program to wait for 1 second. This gives the listener some time to receive key input from the keyboard.
An empty list named `lidarmap` is created. This list will be used to store the map of the data received from the lidar sensor.
This piece of code provides the necessary constructs to process data from the lidar sensor and receive keyboard input from the user. The `rotate_vector` function can be used to map the data received from the lidar sensor and the key input from the keyboard can be tracked via the `statuskey` variable.

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/0bc678bf-fe92-4760-96f7-0d8895b96bc5)

First, the `if(activate):` statement checks the value of the `activate` variable. If `activate` is True, the rest of the code is executed. This allows the code to continue if the connection was successful.
Calling `plt.close('all')` closes all existing graphic windows.
Interactive mode is enabled by calling `plt.ion()`. This allows the graphics to be updated instantly.
An infinite loop is started (`while(1)`). This loop continues to control the robot's movement and visualize it by receiving data from the lidar sensor.
With the `vrep.simxGetObjectPosition` function, the position of the object named `hokuyo` is taken and assigned to the variable `pos`.
With the `vrep.simxGetObjectPosition` function, the position of the object named `vsensor` is taken and assigned to the variable `pos_dir`.
The variables `dr_x` and `dr_y` are calculated. These variables represent the x- and y-directed distance between `vsensor` and `hokuyo` objects.
Using the `math.atan2` function, the angle (`dangle`) between `dr_y` and `dr_x` is calculated and converted to degrees.
The values `pos[0]` and `pos[1]` are added to the `px` and `py` lists. This stores the x and y positions of the robot in the `px` and `py` lists.
The last inserted position is printed as the last elements of the lists `px` and `py` (`px[-1]` and `py[-1]`).
If the first elements of the lists `px` and `py` are equal to zero, the first elements (`px[0]` and `py[0]`) are omitted. This clears the zero position in lists that represent the track of the moving robot.
With the `vrep.simxGetStringSignal` function, a signal named "measuredDataAtThisTime" is received and assigned to the `data` variable.
The length of the `data` list is checked. If `data` is not empty, that is, `len(data) > 0` it is entered in the if block. This check is to check whether the data from the lidar sensor is being received. If `data` is empty, that is, no data has been received, the if block is skipped and the program continues.
The current chart is cleared by calling `plt.clf()`.
Using the `vrep.simxUnpackFloats` function, the `data` variable is unpacked and assigned to the `measuredData` variable. This enables data from the lidar sensor to be analyzed.
Two new arrays named `lx` and `ly` are created. These arrays take data in x and y coordinates from the `measuredData` array.
An array named `ldata` is created. This array is formed by combining `lx` and `ly` strings.
Using the `rotate_vector` function, the `ldata` array is rotated with a `dangle` angle and assigned to the variable `rotated_data`.
In a `try-except` block inside the loop, each point in the `rotated_data` array is checked. If the point is not in the `lidarmap` list, it is added to the `lidarmap` list.
The `lidarmap` list is converted to a numpy array and visualized with a scatter plot using the matplotlib library.
The `px` and `py` lists are also visualized with a scatter plot.
 Using the `plt.arrow` function, an arrow is drawn indicating the direction of movement of the robot.
Graphic boundaries are set, labels are added, and a title is assigned.
The graph and axes are shown.
A wait time is added by calling `plt.pause(0.0001)`. This takes a while for the graphics to update and the interface to react.
The robot's right and left wheel speeds are assigned to the variables `wR` and `wL`. These speeds are updated as the key is pressed.
By controlling the `statuskey` variable, movement speeds are adjusted according to the key input.
The `statuskey` variable is reset.
Speed values are sent to the motors using the `vrep.simxSetJointTargetVelocity` function.
When `Key.esc` is pressed, the loop is terminated and the program is completed.
The columns of the `lmnp` array are saved in the `lmnpx.npy` and `lmnpy.npy` files.
This piece of code controls the robot's motion, receives data from the lidar sensor, visualizes the data, and allows the user to control the robot's motion with keyboard keys. The lidar data and the robot's position are displayed graphically using the matplotlib library. In this way, the user can detect obstacles around the robot and monitor the robot's movement in real time. Lidar data is added to the 'lidarmap' list and this data is displayed on the graph as a scatter plot. The robot's track is stored in the `px` and `py` lists and is indicated by a red line on the graph. The movement of the robot is controlled by keyboard input: it can be moved up, left, right or down. At the end of the code, the `lmnp` string is saved in the `lmnpx.npy` and `lmnpy.npy` files with numpy's `np.save` function. These files hold the x and y coordinates of the lidar data. 

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/ccb2272f-062d-4d59-981e-ef312e341aba)
![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/ce05d552-e3be-46cd-89be-2b1afc6848da)
![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/473bbb68-36d5-4e7a-9e7e-cfc22dcc1725)

## Start (Cycle) and End (X) Points

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/06117c9f-e3f9-49df-bc97-72fe5f2f4d00)

# Python Code for Path Planning
## Shortest Paths Between the Points A and B

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/e498067e-af04-4fca-8f34-cc7227a74112)

Start and end points, grid size and robot radius importing

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/3026df0b-68cf-49fa-b19c-15dcb72b65d1)

Loading map data

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/070b3c78-c533-41e8-b719-920ae0773149)

## Shortest Path Between the Points A and B with A* Algorithm

This piece of code performs a planning process using the A* algorithm and graphically visualizes the result. The `show_animation` variable must be set to `True` for the code to run.
First, it needs the obstacle coordinates (`ox` x coordinates,`oy` y coordinates) and cell size (`grid_size`) and robot radius (`robot_radius`) stored in lists named `ox` and `oy`.
An object (`a_star`) of class `AStarPlanner` is created and initialized with the values `ox`, `vote`, `grid_size` and `robot_radius`.
Then, a path is made between the starting (`sx`, `sy`) and destination (`gx`, `gy`) points using the `planning` method of the `a_star` object. As a result of the planning, the x and y coordinates of the planned path are assigned to the `rx` and `ry` lists.
Using the `interpolate.splprep` function, a smoothing operation is performed on the lists `rx` and `ry` and a function `f` representing the smoothed curve and control points `u` are returned.
Using the `np.linspace` function, 100 points are created on the flattened curve and the x and y coordinates of these points are assigned to the `xint` and `yint` lists.
Finally, using the `plt.plot` function, obstacle points (`ox`, `oy`), starting point (`sx`, `sy`), target point (`gx`, `gy`) and smoothed curve (` xint`, `yint`) are plotted on the chart.
`plt.grid(True)` displays the grid lines and `plt.axis("equal")` equalizes the scale of the x and y axes.
Finally, the graph is displayed with `plt.show()`.

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/b87da468-0158-41d7-b32a-6b293ba42997)

## Shortest Path Between the Points A and B with Dijkstra Algorithm

This piece of code performs a planning process using the Dijkstra algorithm and graphically visualizes the result. The `show_animation` variable must be set to `True` for the code to run.
First, the obstacle coordinates (`ox` x coordinates, `oy` y coordinates) and cell size (`grid_size`) and robot radius (`robot_radius`) stored in lists named `ox` and `oy` are needed.
An object of class `dijkstra` (`dijkstra`) is created and initialized with the values `ox`, `oy`, `grid_size` and `robot_radius`.
Next, a path plan is made between the starting (`sx`, `sy`) and destination (`gx`, `gy`) points using the `planning` method of the `dijkstra` object. As a result of the planning, the x and y coordinates of the planned path are assigned to the `rx` and `ry` lists.
Using the `interpolate.splprep` function, a smoothing operation is performed on the lists `rx` and `ry` and a function `f` representing the smoothed curve and control points `u` are returned.
Using the `np.linspace` function, 100 points are created on the flattened curve and the x and y coordinates of these points are assigned to the `xint` and `yint` lists.
Finally, using the `plt.plot` function, obstacle points (`ox`, `oy`), starting point (`sx`, `sy`), target point (`gx`, `gy`) and smoothed curve (` xint`, `yint`) are plotted on the chart.
`plt.grid(True)` displays the grid lines and `plt.axis("equal")` equalizes the scale of the x and y axes.
Finally, the graph is displayed with `plt.show()`.

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/e4db8ce5-e759-41f9-bf3f-11d4f402800a)

## Shortest Path Between the Points A and B with D* Algorithm

### Numbers must be bigger than 0 and they must be integer in this algorithm
This piece of code performs a planning process using the D* Lite algorithm and graphically visualizes the result. The `show_animation` variable must be set to `True` for the code to run.
First, a `Map` object (`m`) is created from the `d_star_module` module. This `Map` object represents the position of obstacles and target in a grid. When building, the grid dimensions are set to 100x100.
Next, the obstacle coordinates (`n_ox` x coordinates, `n_oy` y coordinates) in the `n_ox` and `n_oy` lists are assigned to the `ox` and `vote` lists. However, a transformation is performed on these coordinates. Each coordinate is multiplied by 10, rounded up, and added by 52. This operation moves the coordinates to a new origin.
Using the `set_obstacle` method of the `m` object, the obstacle points are set with `[(i, j) for i, j in zip(ox, oy)]`.
The starting and target points (`sx`, `sy`) and (`gx`, `gy`) are determined.
If the variable `show_animation` is `True`, then using the `plt.plot` function obstacle points (`ox`, `oy`), starting point (`sx`, `sy`), target point (`gx`, `gy`) is plotted on the chart and `plt.axis("equal")` equalizes the scale of the x and y axes.
The `Dstar` algorithm is run on the `m` object. This is the part where the D* Lite algorithm works. The `run` method is called using the start and destination points and the x and y coordinates of the planned path are assigned to the lists `rx` and `ry`.
If the `show_animation` variable is `True`, the planned path (`rx`, `ry`) is plotted using the `plt.plot` function and the graph is displayed with `plt.show()`.
The `rx` and `ry` lists are saved using the `np.save` function.

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/e888ff02-5af2-4189-a0da-fb4c54ca414e)

# SIMULATION RESULTS
## 2D Map of the House Plan

![image](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/62cc7b65-454a-4d89-b65d-d435c8c03c26)

## Shortest Path Between the Points A and B with A* Algorithm

![a_star](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/9a8ac03f-7658-41ae-abe0-276cb4ecede3)

![a_star](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/f2df47e0-b543-4c91-8d95-eb80f92cd8f5)

## Shortest Path Between the Points A and B with Dijkstra Algorithm

![dijkstra](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/91f40434-87ed-4f5a-bdba-069956d03a23)

![dijkstra](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/9f31977e-c848-46d3-b8a5-940611edd28a)

## Shortest Path Between the Points A and B with D* Algorithm

![d_star](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/92bf1d83-7dc3-44b9-b849-5f27532a4852)

![d_star](https://github.com/BuseBeker/Autonomus-Mobile-Robots/assets/72763515/63d5f8a7-da69-486a-9944-fe367cc423c6)
