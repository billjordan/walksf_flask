from intersection import loadIntersections
import json
def main():
    streets_in_grid = ["SACRAMENTO ST", "BAKER ST", "SUTTER ST", "STEINER ST", "PERINE PL", "WILMOT ST", "BRODERICK ST", "DIVISADERO ST", "SCOTT ST", "PIERCE ST", "CALIFORNIA ST", "PINE ST", "BUSH ST"]
    int_dic = loadIntersections(toPrint=False)
    ints_in_grid = {}
    #if both streets for intersection are in grid, add the intersection to ints_in_grid
    for key in int_dic.keys():
        if int_dic[key].get_streets()[0] in streets_in_grid and int_dic[key].get_streets()[1] in streets_in_grid:
            ints_in_grid[key] = int_dic[key]
            
#     for key in ints_in_grid.keys():
#         print(key, "\n", ints_in_grid[key])
    makeIntersectionJSAA(ints_in_grid)

def makeIntersectionJSAA(dic):
    """
    makes a js file with a js assosiative array from a dictionary of intersections
    """
    fout = open("intersections.js", "w")
    fout.write("var intersections = {\n")
    for key in sorted(dic.keys()):
        fout.write("\t"+dic[key].get_cnn()+": {\n")
        fout.write("\t\tlatitude:\t"+dic[key].get_loc().getLatStr()+",\n");
        fout.write("\t\tlongitude:\t"+dic[key].get_loc().getLongStr()+",\n");
        fout.write("\t},\n\n")
        
    fout.write("};")
    fout.close()
    
if __name__ == '__main__':main()