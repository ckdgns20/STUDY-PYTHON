
def compute_header_data(datax,datay):
    
    
    sensor_num = len(datax[0])
    point_num = len(datay[0])
    
    if len(datax[1:]) == len(datay[1:]):
        wafer_num = len(datax[1:])
    else:
        print(f"x,y 데이터 실험 수가 맞지 않음(x :{datax[1:]}, y : {datay[1:]})")
    
    total_info = {
        'Number of sensor' : sensor_num,
        'Number of point' : point_num,
        'Number of wafer' : wafer_num
    }
    return total_info

def find_missing_value(datax,datay):
    missing_areax = []
    missing_numx = 0
    missing_areay = []
    missing_numy = 0
    for idx, values in enumerate(datax[1:]):
        for row_idx, value in enumerate(values):
            if value == None :
                missing_numx += 1
                missing_areax.append([idx,row_idx])
            
    for idx, value in enumerate(datay[1:]):
        for row_idx, value in enumerate(values):
            if value == None :
                missing_numy += 1
                missing_areay.append([idx,row_idx])
    
    return missing_areax,missing_areay,missing_numx,missing_numy

def summary(material, datax, datay, total_info, missing_areax, missing_areay, missing_numx, missing_numy):
    print("========================================")
    print("PVD Semiconductor Process Data Inspector")
    print("========================================",end='\n\n')
    print(f"Material        : {material}")
    print(f"Nuber of sample : {total_info['Number of wafer']}",end='\n\n')
    print("[Input Data]")
    print(f"Number of Sensor     : {total_info['Number of sensor']}")
    print(f"Sensors              : {datax[0]}")
    print(f"Sensor Features      : {datax[1:]}",end='\n\n')
    print("[Output Data]")
    print(f"Number of Point      : {total_info['Number of point']}")
    print(f"Points               : {datay[0]}")
    print(f"Point Features       : {datay[1:]}",end='\n\n')
    print("[Missing Values]")
    print(f"Number of X Missing  : {missing_numx}")
    print(f"Number of Y Missing  : {missing_numy}")
    print(f"X Missing Area       : {missing_areax}")
    print(f"Y Missing Area       : {missing_areay}",end='\n\n')
    print("========================================")
    
    
    
    
    