import roboticstoolbox as rtb
import swift
# Define the robot model
robot = rtb.models.Panda()

# Print the robot model
print(robot)

# Visualize the robot


# Create Swift instance
env = swift.Swift()
env.launch(realtime=True)

# Add the robot to the Swift environment
env.add(robot)
env.hold()

# robot.plot(robot.qr, block=True)