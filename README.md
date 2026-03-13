# BATMAN-2.0
This repository contains input files for the GOTHAM astrochemical model, BATMAN, updated for use with the Nautilus 2.0 code released in 2024. These input files are largely the same as those that can be found in the original BATMAN repository
(https://github.com/cixue/BATMAN), although there are some key differences in file structure and functionality. Some of the more pertinent changes are outlined in the following sections. More information regarding the major changes can be found in 
Wakelam et al. 2024 (https://www.aanda.org/articles/aa/abs/2024/09/aa50606-24/aa50606-24.html) as well as the Nautilus repository (https://forge.oasu.u-bordeaux.fr/LAB/astrochem-tools/pnautilus/-/tree/main/example_simulation?ref_type=heads).

## Parameters.in
There are a few minor changes in this file, but the main ones are that all species are now able to diffuse through quantum mechanical tunneling by default ("grain_tunneling_diffusion = 2", line 40) with a diffusion barrier thickness of 2.5 Angstrom 
("diffusion_barrier_thickness = 2.500E-08", line 73). 

## Activation energies
In the 2016 version of the Nautilus code, activation energies for grain reactions were stored in a separate file called activation_energies.in. In the newest version of the code, this file is now obsolete as this information is now stored as the gamma
(C) values in the grain_reactions.in file. The grain_reactions.in file has been updated accordingly. The activation_energies.in file has been renamed to activation_energies_refs - this file is not used by the code but provides a list of grain reactions
with activation energies and the corresponding references. This repository also contains the script fix_activation_energies.py which can be used to create a new grain_reactions.in file in the Nautilus 2024 convention using old grain_reactions.in
and activation_energies.in files.

## Surface_parameters.in
In the 2024 version of the Nautilus code, the surface_parameters.in file no longer requires a column for dEb. This file has been reformatted so that this column is removed. This repository also contains a script called reformat_surfaceparams.py that
can be used to perform this reformatting procedure for an old surface_parameters.in file.

## Reactions with complementary temperature ranges
In the original BATMAN network, "duplicate" reactions with complementary temperature ranges were commented out as it was found that they would be double counted by the code. The 2024 version of the modeling code will correctly pick the entry that is
appropriate for the given temperature range if the reactions are given the same reaction ID. Currently these reactions are still commented out, but in the future there will be an update to add them back in and adjust the reaction IDs.

## Minimum rate coefficient
If you look at some of the rates outputted by the 2024 code and compare them to the 2016 code, you may see that very slow reactions in the 2016 code (ie. those with rates on the order of 1e-99) are significantly faster in the 2024 code (order of ~1e-50).
This is because the 2024 code now sets a minimum rate coefficient of 1e-50. This should not have any noticeable effect, as reactions this slow should not contribute to the chemistry appreciably.

## Desorption via cosmic-ray sputtering
The 2024 Nautilus code now has the ability to account for cosmic-ray sputtering of grains as a desorption mechanism. To include this you must add a line to the grain_reactions.in file with the surface species as the reactant, the gas-phase species as
the product, and an ITYPE of 77. This mechanism has not yet been added to BATMAN for any species but can be tested in the future.
