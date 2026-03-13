# Replace the file path below with the path to the original surface_parameters.in file from Nautilus 2016. Preferably rename to something that is not "surface_parameters.in"
with open('BATMAN-indene_2.0/surface', 'r') as file:
    lines = file.readlines()
    file.close()

# Create new surface_parameters.in file to be properly formatted with original data
with open('BATMAN-indene_2.0/surface_parameters.in', 'w') as file:
    for line in lines[1:]:
        # Grab each element from lines except for dEb, which isn't used in NAUTILUS 2024. May need to reformat a few lines manually if the spacing is funky
        if line[0] == '!':
            S1 = line[0:13].replace(' ', '')
            S2 = line[13:16].replace(' ', '')
            S3 = line[17:23].replace (' ', '')
            S4 = line[24:29].replace(' ','')
            S5 = line[38:63].rstrip(' ').lstrip(' ')
            S6 = line[63:]
            newline = "{0:<12} {1:>3} {2:>8} {3:>5} {4:1} {5:<24} {6:9}".format(S1, S2, S3, S4,' ', S5, S6)
        else:
            S1 = line[0:12].replace(' ', '')
            S2 = line[12:15].replace(' ', '')
            S3 = line[16:22].replace (' ', '')
            S4 = line[23:28].replace(' ','')
            S5 = line[37:62].rstrip(' ').lstrip(' ')
            S6 = line[62:]
            newline = "{0:<11} {1:>3} {2:>8} {3:>5} {4:1} {5:<24} {6:9}".format(S1, S2, S3, S4, ' ', S5, S6)
        file.write(newline)
    file.close()
