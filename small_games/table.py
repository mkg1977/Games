from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["Alamgir Hossain", "Henry Curran", "Cheol Ho Choi", 
                          "Stephen Dooley", "Ole Swang", "Shigeru Nagase", 
                          "Stephen Klippenstein","Tofail Ahmed", "Mubarak Khan"])
table.add_column("Research Area", ["Heterocyclic", "Combustion", "Theoretical",
                                   "Biomass", "Organometallic", "Theoretical",
                                   "Theoretical", "Organic Synthesis", "Polymer"])
table.add_column("Affiliation", ["Jackson State University", "NUI Galway", 
                                 "Kyungpook National university", "Trinity college Dublin",
                                 "SINTEF", "Inst. for Molecular Sciences",
                                 "Argonne National Laboratory", "University of Dhaka",
                                 "Atomic Energy Commission"])
table.add_column("Country", ["United States", "Ireland", "South Korea", "Ireland",
                             "Norway", "Japan", "United States", "Bangladesh",
                             "Bangladesh"])
#table.align = "l"


print(table)

