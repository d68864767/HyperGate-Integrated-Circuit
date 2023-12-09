
import sys
from blueprint_generator import BlueprintGenerator
from input_handler import InputHandler
from utils import load_config

def main():
    # Load the configuration settings
    config = load_config()

    # Create an instance of the input handler to get user input
    input_handler = InputHandler()

    # Get the specifications and requirements for the new hardware component from the user
    specs = input_handler.get_component_specs()
    requirements = input_handler.get_component_requirements()

    # Create an instance of the blueprint generator with the loaded configuration
    blueprint_generator = BlueprintGenerator(config)

    # Generate the KiCAD parts library file based on the user input
    kicad_lib_content = blueprint_generator.generate_blueprint(specs, requirements)

    # Save the generated KiCAD parts library file
    with open('example_component.lib', 'w') as lib_file:
        lib_file.write(kicad_lib_content)

    print("KiCAD parts library file 'example_component.lib' has been generated successfully.")

if __name__ == "__main__":
    main()

