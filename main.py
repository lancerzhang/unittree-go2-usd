import omni

def get_camera_image():
    # Set up the viewport to use the camera
    viewport_interface = omni.kit.viewport.get_default_viewport_window()
    viewport_interface.set_active_camera("/World/Camera")
    
    # Take a screenshot from the camera
    result = viewport_interface.capture_image()
    image = result.get()
    
    # Save the image to a file
    image.save("captured_image.png", "PNG")

def main():
    # Initialize application
    omni.kit.app.get_app().initialize()

    # Load a USD scene
    stage = omni.usd.get_context().get_stage()
    stage.Open("warehouse.usdc")

    # Get an image from the camera
    get_camera_image()

    # Shutdown application
    omni.kit.app.get_app().shutdown()

if __name__ == "__main__":
    main()
