import copy

class Vehicle:
    veh_type=''
    veh_id=0
    
    def __init__(self,veh_type,veh_id):
       self.veh_type=veh_type
       self.veh_id=veh_id
      
    def show_info(self):
        print("Vehicle Reistration No :  ", self.veh_id)
        print("Vehicle Type           :  ", self.veh_type)

class ParkingLot:
    parking_capacity=[]
    parking_status=[]
    valid_vehicle=['bike','car']
    levels=0
    parked_vehicles=[]
    capacity={}
    
    def __init__(self,levels,pc):
        self.levels = levels
        self.parking_capacity = pc.copy()
        self.parking_status = copy.deepcopy(pc)
        for i in self.parking_status:
            for j in i.keys():
                i[j]=0
 
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
            
            
    def show_parking_capacity(self):
        print(self.parking_capacity)
        
    def show_parking_status(self):
        print(self.parking_status)
        
    def list_parked_vehicles(self):
        for vehicle in self.parked_vehicles:
            print(vehicle.show_info)
        
    def add_new_level(self,capacity):
        self.parking_capacity = self.parking capacity.append(capacity)
        empty=copy.deepcopy(self.capacity)
        self.parking_status.append
        
p1=ParkingLot(2,[{'bike':2,'car':3},{'bike':5,'car':8}])
p1.show_parking_capacity()
p1.add_vehicle('bike',2)
p1.show_parking_status()