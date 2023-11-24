import pytest


class TestBus:
    @pytest.fixture(autouse=True)
    def setup_data(self, bus_instance):
        self.bus_instance = bus_instance
        yield
        # Any cleanup code can go here if needed

    def test_owner(self):
        self.bus_instance.owner('BO', 45, 90000)
        assert self.bus_instance.o_name == 'BO'

    def test_driver(self):
        self.bus_instance.driver('BD', 32, 78000)
        assert self.bus_instance.d_name == 'BD'

    def test_conductor(self):
        self.bus_instance.conductor('BC', 35, 78000)
        assert self.bus_instance.c_name == 'BC'

    def test_total_salary(self):
        self.bus_instance.owner('BO', 45, 90000)
        self.bus_instance.driver('BD', 32, 78000)
        self.bus_instance.conductor('BC', 35, 78000)
        assert self.bus_instance.total_salary() == 246000