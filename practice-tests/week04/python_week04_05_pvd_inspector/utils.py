


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
    
    
    
    
    