import json

def load_config(config_path='config.json'):
    """
    Load the configuration file containing default values and settings.
    """
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def generate_symbol_definition(name, reference_prefix, input_count, output_count, symbol_defaults):
    """
    Generate the symbol definition part of the KiCAD library component.
    """
    symbol_lines = []
    symbol_lines.append(f"DEF {name} {reference_prefix} 0 40 Y Y 1 F N")
    symbol_lines.append("DRAW")
    
    # Add graphical representation of the symbol
    symbol_lines.append(f"S 0 -100 100 100 0 0 {symbol_defaults['line_width']} {symbol_defaults['fill']} N")
    
    # Add pins
    for i in range(input_count):
        symbol_lines.append(f"X IN{i+1} {i+1} -{symbol_defaults['pin_length']} 0 {symbol_defaults['pin_length']} {symbol_defaults['pin_orientation']} {symbol_defaults['pin_number_text_size']} {symbol_defaults['pin_name_text_size']} 1 1 I")
    
    for i in range(output_count):
        symbol_lines.append(f"X OUT{i+1} {i+1+input_count} {symbol_defaults['pin_length']} 0 {symbol_defaults['pin_length']} L {symbol_defaults['pin_number_text_size']} {symbol_defaults['pin_name_text_size']} 1 1 O")
    
    symbol_lines.append("ENDDRAW")
    symbol_lines.append("ENDDEF")
    
    return '\n'.join(symbol_lines)

def generate_footprint(name, footprint_defaults):
    """
    Generate the footprint information part of the KiCAD library component.
    """
    footprint_lines = []
    footprint_lines.append(f"FP0 \"{name}\" A 0 0 50 H I C CNN")
    # Additional footprint details would be added here based on the footprint_defaults
    # and the specific requirements of the component.
    
    return '\n'.join(footprint_lines)

def format_component_description(description):
    """
    Format the description of the component's functionality and properties.
    """
    formatted_description = []
    for key, value in description.items():
        formatted_description.append(f"{key}: {value}")
    
    return '\n'.join(formatted_description)

# Additional utility functions can be added here as needed for the project.
