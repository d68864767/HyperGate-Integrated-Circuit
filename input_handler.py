import json

def get_user_input():
    """
    Prompts the user for input and returns a dictionary with the component specifications.
    """
    print("Please enter the specifications for the new hardware component.")
    
    # Prompt for basic symbol information
    name = input("Enter the component name: ")
    reference_prefix = input("Enter the reference prefix (e.g., U for integrated circuit): ")
    
    # Prompt for functionality and electrical characteristics
    description = input("Enter a description of the component's functionality: ")
    voltage = input("Enter the operating voltage range (e.g., 3.3-5V): ")
    current = input("Enter the maximum current (e.g., 1A): ")
    
    # Prompt for physical and performance characteristics
    package_type = input("Enter the package type (e.g., DIP, SMD): ")
    dimensions = input("Enter the dimensions (e.g., 10mm x 10mm x 2mm): ")
    performance_specs = input("Enter the performance specifications (e.g., speed, accuracy): ")
    
    # Prompt for environmental and compliance specifications
    environmental_specs = input("Enter the environmental specifications (e.g., temperature range): ")
    compliance = input("Enter the compliance standards (e.g., RoHS, CE): ").split(',')
    
    # Prompt for reliability and budget
    reliability = input("Enter the reliability specifics (e.g., MTBF): ")
    budget = input("Enter the budget limitations (e.g., target cost per unit): ")
    
    # Create a dictionary with the user input
    user_input = {
        "name": name,
        "reference_prefix": reference_prefix,
        "description": description,
        "voltage": voltage,
        "current": current,
        "package_type": package_type,
        "dimensions": dimensions,
        "performance_specs": performance_specs,
        "environmental_specs": environmental_specs,
        "compliance": compliance,
        "reliability": reliability,
        "budget": budget
    }
    
    return user_input

def validate_input(user_input, config):
    """
    Validates the user input against the default values in the config.
    If a field is left empty, it fills it with the default value.
    """
    for key, value in user_input.items():
        if not value:
            default_value = config['default_values'].get(key)
            if default_value:
                user_input[key] = default_value
            else:
                raise ValueError(f"No default value found for {key}, and no value was provided.")
    
    # Validate package type and dimensions
    package_info = config['package_types'].get(user_input['package_type'].upper())
    if package_info:
        user_input['dimensions'] = user_input['dimensions'] or package_info['dimensions']
    else:
        raise ValueError(f"Package type {user_input['package_type']} is not supported.")
    
    return user_input

def main():
    config = load_config()
    user_input = get_user_input()
    validated_input = validate_input(user_input, config)
    return validated_input

if __name__ == "__main__":
    component_specs = main()
    print(json.dumps(component_specs, indent=4))
