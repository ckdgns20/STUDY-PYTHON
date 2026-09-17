import csv

def load_csv(args):
    """Read CSV file and return all rows and the material name"""
    material = args.split(".csv")[0].split("_")[-1]
    
    with open(args,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
        #print(f"{args} header:{rows[0]}") 
        #print(f"{args} data:{rows[1:]}") 
        
    return rows , material

