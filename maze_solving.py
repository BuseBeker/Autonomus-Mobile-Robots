import vrep
import matplotlib.pyplot as plt
import time
import numpy as np
import math
from pynput import keyboard

ip = "127.0.0.1"
port = 19999

print('Connecting')
vrep.simxFinish(-1)
clientID = vrep.simxStart(ip, port, True, True, 5000, 5)
activate = True
if(clientID == -1):
    print("Not connected")
    activate = False
print("Connected")

_, camLeft = vrep.simxGetObjectHandle(clientID, "LeftSensor", vrep.simx_opmode_oneshot_wait)
_, camMid = vrep.simxGetObjectHandle(clientID,"MiddleSensor", vrep.simx_opmode_oneshot_wait)
_, camRight = vrep.simxGetObjectHandle(clientID, "RightSensor", vrep.simx_opmode_oneshot_wait)
_, motorRight = vrep.simxGetObjectHandle(clientID, "DynamicRightJoint", vrep.simx_opmode_oneshot_wait)
_, motorLeft = vrep.simxGetObjectHandle(clientID, "DynamicLeftJoint", vrep.simx_opmode_oneshot_wait)
_, vsensor = vrep.simxGetObjectHandle(clientID, "Vision_sensor", vrep.simx_opmode_oneshot_wait)
_, ultra = vrep.simxGetObjectHandle(clientID, "Proximity_sensor", vrep.simx_opmode_oneshot_wait)
_, linetracer = vrep.simxGetObjectHandle(clientID,"LineTracer", vrep.simx_opmode_oneshot_wait)
_, hokuyo = vrep.simxGetObjectHandle(clientID,"fastHokuyo", vrep.simx_opmode_oneshot_wait)

_, laserF = vrep.simxGetObjectHandle(clientID,"LaserFront", vrep.simx_opmode_oneshot_wait)
_, laserB = vrep.simxGetObjectHandle(clientID,"LaserBack", vrep.simx_opmode_oneshot_wait)

px = []
py = []

statuskey = ""

def key_press(key):
    global statuskey
    statuskey = str(key)

def rotate_vector(data, angle):
    # make rotation matrix
    theta = np.radians(angle)
    co = np.cos(theta)
    si = np.sin(theta)
    rotation_matrix = np.array(((co, -si), (si, co)))
    # rotate data vector
    rotated_vector = data.dot(rotation_matrix)
    # return index of elbow
    return rotated_vector

listener = keyboard.Listener(on_press=key_press)
listener.start()

time.sleep(1)
lidarmap = []

if(activate):
    print("begin")
    plt.close('all')
    plt.ion()
    # fig=plt.figure()

    while(1):
        ep, pos = vrep.simxGetObjectPosition(clientID, hokuyo, -1, vrep.simx_opmode_streaming)
        ep, pos_dir = vrep.simxGetObjectPosition(clientID, vsensor, -1, vrep.simx_opmode_streaming)

        dr_x = pos_dir[0]-pos[0]
        dr_y = pos_dir[1]-pos[1]

        dangle = math.atan2(dr_y, dr_x)*180/np.pi
        
        px.append(pos[0])
        py.append(pos[1])
        
        print(px[-1],py[-1])

        if (px[0] == 0) and (py[0] == 0):
            px.pop(0)
            py.pop(0)
            
        data = vrep.simxGetStringSignal(clientID, "measuredDataAtThisTime", vrep.simx_opmode_streaming)

        if len(data) > 0:
            plt.clf()

            measuredData = vrep.simxUnpackFloats(data[1])

            lx = np.array(measuredData[1::3])
            ly = np.array(measuredData[0::3])
            ldata = np.vstack((lx, ly)).T
            rotated_data = rotate_vector(ldata, dangle)+[pos[1], pos[0]]

            try:
                for r in rotated_data:
                    if r.tolist() not in lidarmap:
                        lidarmap.append(r.tolist())
                lmnp = np.array(lidarmap)
                plt.scatter(lmnp[:, 1], lmnp[:, 0], alpha=0.5, label="lidar")
            except:
                print("map not appended")

            plt.scatter(px,py,c="r", alpha=0.5,label="robot")
            plt.arrow(x=pos[0], y=pos[1], dx=dr_x, dy=dr_y, width=.005)
            plt.xlim([-10, 10])
            plt.ylim([-10, 10])
            
            plt.xlabel("X axis")
            plt.ylabel("Y axis")
            plt.title('Initial Lidar Map')
            plt.grid()
            plt.legend()

        plt.grid()
        plt.show()
        plt.pause(0.0001)

        wR = 3
        wL = 3
        if statuskey == "Key.esc":
            break
        elif statuskey == "Key.up":
            wR = 5
            wL = 5
        elif statuskey == "Key.left":
            wR = 0.25
            wL = -0.25
        elif statuskey == "Key.right":
            wR = -0.25
            wL = 0.25
        elif statuskey == "Key.down":
            wR = -0.9
            wL = -0.9
        elif statuskey == "Key.enter":
            wR = 0
            wL = 0
        statuskey = ""

        vrep.simxSetJointTargetVelocity(clientID, motorRight, wR, vrep.simx_opmode_oneshot)
        vrep.simxSetJointTargetVelocity(clientID, motorLeft, wL, vrep.simx_opmode_oneshot)

    vrep.simxFinish(clientID)
    
np.save('lmnpx.npy', lmnp[:, 1], allow_pickle=True)
np.save('lmnpy.npy', lmnp[:, 0], allow_pickle=True)