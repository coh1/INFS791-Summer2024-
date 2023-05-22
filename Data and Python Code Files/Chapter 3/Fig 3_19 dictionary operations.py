# This Python code creates two dictionaries
gss_respondents = {"years": (1972, 1991, 2014),
                   "counts": (24, 21, 43)}
years = dict([(1972, 24), (1991, 21), (2014, 43)])
print("line5:", gss_respondents)
print("line6:", years)

gss_respondents.update(years)
print("line9:", gss_respondents)

gss_respondents[2014] = 45
print("line12:", gss_respondents)
print("the value for 1992 is: ", gss_respondents.get(1992, "no value"))
print("the value for 1991 is: ", gss_respondents.pop(1991, "no value"))
print("line15:", gss_respondents)

gss_respondents.update(years)
print("line18:", gss_respondents)




