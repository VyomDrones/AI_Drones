from dronekit import connect, VehicleMode
import time

# Connect to the vehicle
host = 'localhost'  # Example host IP
port = 14550  # Example port number
connection_string = f'udp:{host}:{port}'
vehicle = connect(connection_string, wait_ready=True)

# Arm the drone
def arm_drone():
    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    time.sleep(1)  # Wait for the vehicle to arm
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
    print("Vehicle armed")

# Disarm the drone
def disarm_drone():
    print("Disarming motors")
    vehicle.armed = False
    time.sleep(1)  # Wait for the vehicle to disarm
    while vehicle.armed:
        print("Waiting for disarming...")
        time.sleep(1)
    print("Vehicle disarmed")

# Main function
def main():
    try:
        arm_drone()
        time.sleep(5)  # Wait for 5 seconds
        disarm_drone()
    except KeyboardInterrupt:
        print("User interrupted the program.")
    finally:
        vehicle.close()

if __name__ == "__main__":
    main()
