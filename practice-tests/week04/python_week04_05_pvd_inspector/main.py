import argparse
import utils
from data_loader import load_csv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--Xfile_path", type= str, default= "./data/pvd_data/X_pvd_AlCu.csv", 
        help= "X 파일 경로"
    )
    parser.add_argument(
            "--Yfile_path", type= str, default= "./data/pvd_data/Y_pvd_AlCu.csv", 
            help= "Y 파일 경로"
        )
    arguments = parser.parse_args()
    
    xrows, material = load_csv(arguments.Xfile_path)
    yrows, _ = load_csv(arguments.Yfile_path)
    total_info = utils.compute_header_data(xrows,yrows)
    missing_areax,missing_areay,missing_numx,missing_numy = utils.find_missing_value(xrows,yrows)
    utils.summary(material, xrows, yrows, total_info, missing_areax, missing_areay, missing_numx, missing_numy)

