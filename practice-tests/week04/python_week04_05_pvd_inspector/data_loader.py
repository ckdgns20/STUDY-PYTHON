import csv

def load_csv(args):
    material = args.split(".csv")[0].split("_")[-1]
    
    with open(args,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
        print(f"{args} header:{rows[0]}") 
        print(f"{args} data:{rows[1:]}") 
        
    return rows , material

