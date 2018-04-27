class Vehicle:
    count=0

    def __init__(self,veh_id, veh_type, user, checkin, checkout=None):
        self.veh_type=veh_type
        self.veh_id=veh_id
        self.user = user
        self.checkin = checkin
        self.checkout = checkout
      
    def show_info(self):
        print("Vehicle Registration No :  ", self.veh_id)
        print("Vehicle Type           :  ", self.veh_type)

class ParkingLot:

    def __init__(self,parking_capacity, valid_vehicles):
        import copy
        self.levels = len(parking_capacity)
        self.valid_vehicle = valid_vehicles
        self.parking_capacity = parking_capacity
        self.parking_status = copy.deepcopy(parking_capacity)
        for level in self.parking_status:
            for veh in list(level):
                level[veh]=0

    def check_space(self, veh_type):
        for level in range(0,self.levels):
            if self.parking_capacity[level][veh_type] > self.parking_status[level][veh_type]:
                return 1
        return -1

    def add_vehicle(self,vr,vt):
        v1=Vehicle(vr,vt)
        if v1.veh_type not in self.valid_vehicle:
            print('Vehicle Type Not Valid')
        else:
            for level in range(0,len(self.parking_status)):
                if self.parking_status[level][v1.veh_type] <= self.parking_capacity[level][v1.veh_type]:
                    self.parking_status[level][v1.veh_type] += 1
                    self.parked_vehicles.append(v1)
                    return
                else:
                    print('No Parking Space')
            
    def check_valid_vehicle(self, veh_type):
        if veh_type not in self.valid_vehicle:
            return -1
        else:
            return 1

    def show_parking_capacity(self):
        print(self.parking_capacity)
        
    def show_parking_status(self):
        print(self.parking_status)
        
    def list_parked_vehicles(self):
        for vehicle in self.parked_vehicles:
            print(vehicle.show_info)
