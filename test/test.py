from dronekit import connect, VehicleMode
import time

# Set up connection to the vehicle (Modify the connection string according to your setup)
connection_string = '/dev/ttyUSB0'  # Modify this with the appropriate port
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True, baud=57600)

# Function to arm the drone
def arm_drone():
    print("Arming motors")
    # Change vehicle mode to GUIDED
    vehicle.mode = VehicleMode("LOITER")
    # Arm the drone
    vehicle.armed = True
    # Wait for arming to complete
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
    print("Drone armed!")

# Function to disarm the drone
def disarm_drone():
    print("Disarming motors")
    # Disarm the drone
    vehicle.armed = False
    # Wait for disarming to complete
    while vehicle.armed:
        print("Waiting for disarming...")
        time.sleep(1)
    print("Drone disarmed!")

try:
    # Arm the drone
    arm_drone()
    # Wait for 5 seconds
    time.sleep(5)
    # Disarm the drone
    disarm_drone()

except Exception as e:
    print("Error: %s" % str(e))

finally:
    # Close vehicle object before exiting script
    vehicle.close()
    print("Vehicle object closed")
