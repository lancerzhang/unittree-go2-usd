import omni
from pxr import UsdGeom, Gf
import carb

def create_cube_and_camera(stage):
    # Create a new Cube Primitive at the origin
    cube = UsdGeom.Cube.Define(stage, '/World/Cube')
    cube.GetPrim().GetAttribute("size").Set(2.0)

    # Create a camera
    camera = UsdGeom.Camera.Define(stage, '/World/Camera')
    camera.GetPrim().GetAttribute("focalLength").Set(50)
    camera.GetPrim().GetAttribute("horizontalAperture").Set(20.4)
    camera.GetPrim().GetAttribute("verticalAperture").Set(15.3)

    # Position the camera in front of the cube
    camera.GetPrim().GetAttribute("xformOp:translate").Set(Gf.Vec3d(10, 0, 0))

def get_camera_image():
    # Set up the viewport to use the camera
    viewport_interface = omni.kit.viewport.get_default_viewport_window()
    viewport_interface.set_active_camera("/World/Camera")
    
    # Take a screenshot from the camera
    result = viewport_interface.capture_image()
    image = result.get()
    
    # Save the image to a file
    image.save("/mnt/data/captured_image.png", "PNG")

def main():
    # Initialize application
    omni.kit.app.get_app().initialize()

    # Load a USD scene
    stage = omni.usd.get_context().get_stage()
    stage.Open("warehouse.usdc")

    # Create cube and camera
    create_cube_and_camera(stage)

    # Get an image from the camera
    get_camera_image()

    # Shutdown application
    omni.kit.app.get_app().shutdown()

if __name__ == "__main__":
    main()
