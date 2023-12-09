import json
from utils import load_config, generate_symbol_definition

class BlueprintGenerator:
    def __init__(self, config_path='config.json'):
        self.config = load_config(config_path)

    def generate_component(self, specs):
        """
        Generate a complete KiCAD part library entry based on the provided specifications.
        """
        name = specs['name']
        reference_prefix = specs['reference_prefix']
        input_count = specs.get('input_count', 0)
        output_count = specs.get('output_count', 0)
        symbol_defaults = self.config['symbol_defaults']
        footprint_defaults = self.config['footprint_defaults']
        package_type = specs['package_type']

        # Generate symbol definition
        symbol_def = generate_symbol_definition(name, reference_prefix, input_count, output_count, symbol_defaults)

        # Generate footprint definition
        footprint_def = self.generate_footprint_definition(name, package_type, footprint_defaults)

        # Combine symbol and footprint to create the full component definition
        component_def = symbol_def + footprint_def

        return component_def

    def generate_footprint_definition(self, name, package_type, footprint_defaults):
        """
        Generate the footprint definition part of the KiCAD library component.
        """
        footprint_lines = []
        package_info = self.config['package_types'][package_type]

        # Add footprint information
        footprint_lines.append(f"# Footprint Information for {name}")
        footprint_lines.append(f"FP0 \"{name}_{package_type}\" A 0 0 50 H I C CNN")

        # Add pad information based on package type
        pad_shape = footprint_defaults['pad_shape']
        pad_size = footprint_defaults['pad_size']
        # ... (additional footprint details would be added here based on the package type)

        return footprint_lines

    def save_library_file(self, component_definitions, filename='part_library.lib'):
        """
        Save the generated component definitions to a KiCAD library file.
        """
        with open(filename, 'w') as lib_file:
            lib_file.write("EESchema-LIBRARY Version 2.4\n#encoding utf-8\n#\n")
            for component_def in component_definitions:
                lib_file.write('\n'.join(component_def))
                lib_file.write('\n#\n')

# Example usage:
if __name__ == "__main__":
    generator = BlueprintGenerator()
    example_specs = {
        "name": "NEW_IC",
        "reference_prefix": "U",
        "input_count": 2,
        "output_count": 1,
        "package_type": "DIP"
    }
    component_def = generator.generate_component(example_specs)
    generator.save_library_file([component_def])

