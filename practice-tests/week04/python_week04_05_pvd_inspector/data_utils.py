
def compute_header_data(datax,datay):
    """Check Number of Data"""
    
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
    """Find Missing Value in CSV"""
    missing_areax = []
    missing_numx = 0
    missing_areay = []
    missing_numy = 0
    for idx, values in enumerate(datax[1:]):
        for row_idx, value in enumerate(values):
            if value.strip() == "" :
                missing_numx += 1
                missing_areax.append([idx,row_idx])
            
    for idx, values in enumerate(datay[1:]):
        for row_idx, value in enumerate(values):
            if value.strip() == "" :
                missing_numy += 1
                missing_areay.append([idx,row_idx])
    
    return missing_areax,missing_areay,missing_numx,missing_numy
