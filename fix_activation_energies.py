Ea_list = []
# Replace the file path below with the activation_energies.in file for Nautilus 2016
with open('BATMAN-indene/activation_energies.in', 'r') as file:
    for line in file:
        if line[0] == '!':
            pass
        else:
            R1 = str(line[0:10]).replace(' ', '')
            R2 = str(line[11:33]).replace(' ', '')
            P1 = str(line[37:47]).replace(' ', '')
            P2 = str(line[48:70]).replace(' ', '')
            Ea = str(line[93:97])+'0'+str(line[97:101]).replace(' ', '')
            Ea_list.append([R1, R2, P1, P2, Ea])
    file.close()
Rxn_list = [sublist[:-1] for sublist in Ea_list]

# Replace the file path below with the grain_reactions.in file for Nautilus 2016. Ideally rename it to some that isn't "grain_reactions.in"
with open('BATMAN-indene_2.0/grain_reactions_old', 'r') as file:
    lines = file.readlines()
    file.close()

# Create new grain_reactions.in file with the activation energies incorporated as gamma values
with open('BATMAN-indene_2.0/grain_reactions.in', 'w') as file:
    for line in lines:
        if line[0] == '!':
            file.write(line)
        else:
            R1 = str(line[0:10]).replace(' ', '')
            R2 = str(line[11:33]).replace(' ', '')
            P1 = str(line[34:44]).replace(' ', '')
            P2 = str(line[45:55]).replace(' ', '')
            # Reactions accounting for reactive desorption are separate entries with gas-phase products, want those to have the same activation energy as the grain-surface counterpart.
            # Lines below check if the products are gas-phase, and if they are add a J prefix so the code will search for the grain-surface activation energy
            if P1[0] != 'J' and P1[0] != 'K':
                 P1 = 'J' + P1
                 if P2 != '':
                     P2 = 'J' + P2
            if [R1, R2, P1, P2] in Rxn_list:
                index = Rxn_list.index([R1, R2, P1, P2])
                Ea = Ea_list[index][-1]
                new_line = line[0:113] + Ea + line[122:]
                file.write(new_line)
            else:
                file.write(line)
    file.close()


