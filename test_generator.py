import unittest
from blueprint_generator import BlueprintGenerator

class TestBlueprintGenerator(unittest.TestCase):
    def setUp(self):
        # Initialize the BlueprintGenerator with the default config path
        self.generator = BlueprintGenerator()

    def test_generate_component(self):
        # Define a set of specifications for a test component
        test_specs = {
            'name': 'TEST_IC',
            'reference_prefix': 'U',
            'input_count': 2,
            'output_count': 1,
            'package_type': 'DIP'
        }

        # Generate the component definition
        component_def = self.generator.generate_component(test_specs)

        # Check if the generated component definition contains the expected parts
        self.assertIn('DEF TEST_IC U', component_def)
        self.assertIn('F0 "U"', component_def)
        self.assertIn('F1 "TEST_IC"', component_def)
        self.assertIn('DRAW', component_def)
        self.assertIn('ENDDRAW', component_def)
        self.assertIn('X IN1 1', component_def)
        self.assertIn('X OUT 3', component_def)
        self.assertIn('FP0 "TEST_IC_FN"', component_def)

    def test_generate_footprint_definition(self):
        # Define a name and package type for a test footprint
        test_name = 'TEST_FOOTPRINT'
        test_package_type = 'DIP'

        # Use the default footprint settings from the config
        footprint_defaults = self.generator.config['footprint_defaults']

        # Generate the footprint definition
        footprint_def = self.generator.generate_footprint_definition(test_name, test_package_type, footprint_defaults)

        # Check if the generated footprint definition contains the expected parts
        self.assertIn('FP0 "TEST_FOOTPRINT_FN"', footprint_def)

if __name__ == '__main__':
    unittest.main()

