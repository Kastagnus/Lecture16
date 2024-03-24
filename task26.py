import unittest
from .vehicle import Vehicle, ElectricVehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        """Test Vehicle"""
        self.vehicle = Vehicle("Toyota", "Corolla", 2020)

    def test_initial_fuel_level(self):
        """Test fuel level is zero."""
        self.assertEqual(self.vehicle.fuel_level, 0)

    def test_fuel_up(self):
        """Test that fueling up works."""
        self.vehicle.fuel_up
        self.assertEqual(self.vehicle.fuel_level, self.vehicle.gaz_tank_size)

    def test_drive(self):
        """Test-driving."""
        expected_output = "The Corolla is now driving."
        self.assertEqual(self.vehicle.drive, expected_output)



class TestElectricVehicle(unittest.TestCase):
    def setUp(self):
        """Set up a test electric vehicle."""
        self.electric_vehicle = ElectricVehicle("Tesla", "Model S", 2019)

    def test_initial_charge_level(self):
        """Test starting that charge level is zero."""
        self.assertEqual(self.electric_vehicle.charge_level, 0)

    def test_charge(self):
        """Test that charging sets the charge level to 100%."""
        self.electric_vehicle.charge  # Note: charge is a property, so we don't call it like a method.
        self.assertEqual(self.electric_vehicle.charge_level, 100)

    def test_fuel_up(self):
        """Test that fuel_up on an electric vehicle indicates no fuel tank."""
        self.assertEqual(self.electric_vehicle.fuel_up, "This vehicle has no fuel tank!")

    def test_drive(self):
        """Test-driving"""
        expected_output = "The Model S is now driving."
        self.assertEqual(self.electric_vehicle.drive, expected_output)


if __name__ == "__main__":
    unittest.main()
