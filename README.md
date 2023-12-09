# KiCAD Parts Blueprint Generator

The KiCAD Parts Blueprint Generator is a tool designed to assist in the creation of unique and potentially patentable hardware components for use in KiCAD. It generates `.lib` files based on user-provided specifications and requirements, ensuring that the generated blueprints are not based on pre-existing designs or infringing on existing patents.

## Features

- Generates KiCAD parts library files (`.lib`) from specifications.
- Prompts for hardware blueprint creation with necessary parameters.
- Ensures uniqueness and potential for patentability in designs.
- Supports various package types and default settings through a configuration file.

## Project Structure

- `config.json`: Contains default values and settings for the generator.
- `utils.py`: Utility functions to support the generation process.
- `part_library.lib`: The generated parts library file for KiCAD.
- `blueprint_generator.py`: Core script for generating the blueprint.
- `input_handler.py`: Handles user input and validation.
- `main.py`: The main entry point for the application.
- `README.md`: Documentation and usage instructions.
- `example_component.lib`: An example of a generated component library file.
- `test_generator.py`: Tests to ensure the generator works as expected.

## Usage

To use the KiCAD Parts Blueprint Generator, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Modify the `config.json` file to set your desired default values and package types.
4. Run `main.py` and follow the prompts to input your hardware specifications and requirements.
5. The tool will generate a `.lib` file with your new component definition.

## Configuration

The `config.json` file contains default values and settings that the generator uses to create new components. You can modify this file to change the default electrical characteristics, package types, symbol defaults, and footprint defaults.

Example configuration snippet:
```json
{
    "default_values": {
        "voltage_range": "3.3-5V",
        "current_max": "1A",
        "operating_temperature_range": "-40 to 85 degrees Celsius",
        ...
    },
    ...
}
```

## Dependencies

- Python 3.x
- KiCAD (to use the generated `.lib` files)

## Contributing

Contributions to the KiCAD Parts Blueprint Generator are welcome. Please ensure that you test your changes thoroughly and follow the existing code structure and style.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is provided as-is, and while it aims to assist in creating potentially patentable designs, the responsibility for ensuring that generated designs do not infringe on existing patents lies with the user.

## Contact

For any questions or feedback regarding the KiCAD Parts Blueprint Generator, please open an issue in the project's GitHub repository.

