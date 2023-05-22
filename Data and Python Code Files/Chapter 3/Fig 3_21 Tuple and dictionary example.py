# This Python code uses a function to look up
#  code meanings for GSS variables using dictionaries
def code_lookup(codes):
    region, happy = codes
    print("line 5 - region, happy: ", region, happy)
    region_dict = {1:"New England", 2:"Middle Atlantic",
                   3:"East North Central", 4:"West North Central",
                   5:"South Atlantic", 6:"East South Central",
                   7:"West South Central", 8:"Mountain", 9:"Pacific"}
    happy_dict = {1:"Very happy", 2:"Pretty happy", 3:"Not too happy",
                  8:"Don't know", 9:"No answer", 0:"Not applicable"}
    return(region_dict[region], happy_dict[happy])    

codes = 3, 2
print("line 15 - codes: ", codes)
response = code_lookup(codes)
print("line 17 - response: ", response)
print("Interview region: " + response[0])
print("Happiness level: " + response[1])

