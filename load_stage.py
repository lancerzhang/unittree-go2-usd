from omni.isaac.kit import SimulationApp
import omni

# Configuration for the simulation application
CONFIG = {"width": 1280, "height": 720, "sync_loads": True, "headless": False, "renderer": "RayTracedLighting"}

# Initialize the simulation application
kit = SimulationApp(launch_config=CONFIG)

usd_path = 'unittree-go2-scene/simple.usd'

# Load the USD stage
omni.usd.get_context().open_stage(usd_path)
print("Loading stage...")

# Wait until the stage finishes loading
from omni.isaac.core.utils.stage import is_stage_loading
while is_stage_loading():
    kit.update()

print("Loading Complete")
omni.timeline.get_timeline_interface().play()

# Run the simulation until manually stopped
while kit.is_running():
    kit.update()

# Stop the simulation and clean up
omni.timeline.get_timeline_interface().stop()
kit.close()
