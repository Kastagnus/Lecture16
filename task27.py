import pytest
from vehicle import Vehicle, ElectricVehicle

#Vehicle class
def test_vehicle_initial_fuel_level():
    vehicle = Vehicle("Toyota", "Corolla", 2020)
    assert vehicle.fuel_level == 0, "Initial fuel level 0"

def test_vehicle_fuel_up():
    vehicle = Vehicle("Toyota", "Corolla", 2020)
    vehicle.fuel_up  # Note: fuel_up is a property
    assert vehicle.fuel_level == vehicle.gaz_tank_size, "Fuel level should match tank size after fuel up"

def test_vehicle_drive():
    vehicle = Vehicle("Toyota", "Corolla", 2020)
    expected_output = "The Corolla is now driving."
    assert vehicle.drive == expected_output, "Drive method should return correct driving message"

#ElectricVehicle class
def test_electric_vehicle_initial_charge_level():
    electric_vehicle = ElectricVehicle("Tesla", "Model S", 2019)
    assert electric_vehicle.charge_level == 0, "Initial charge level should be 0"

def test_electric_vehicle_charge():
    electric_vehicle = ElectricVehicle("Tesla", "Model S", 2019)
    electric_vehicle.charge  # property
    assert electric_vehicle.charge_level == 100, "Charge level should be 100% after charge"

def test_electric_vehicle_fuel_up():
    electric_vehicle = ElectricVehicle("Tesla", "Model S", 2019)
    expected_message = "This vehicle has no fuel tank!"
    assert electric_vehicle.fuel_up == expected_message, "Fuel up should indicate no fuel tank for electric vehicles"

def test_electric_vehicle_drive():
    electric_vehicle = ElectricVehicle("Tesla", "Model S", 2019)
    expected_output = "The Model S is now driving."
    assert electric_vehicle.drive == expected_output, "Drive method should return correct driving message for electric vehicles"
