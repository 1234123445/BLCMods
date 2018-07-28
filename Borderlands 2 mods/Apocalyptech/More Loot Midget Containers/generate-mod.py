#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:
import re
import sys

try:
    from modprocessor import ModProcessor
    mp = ModProcessor()
except ModuleNotFoundError:
    print('')
    print('********************************************************************')
    print('To run this script, you will need to copy or symlink modprocessor.py')
    print('from the parent directory, so it exists here as well.  Sorry for')
    print('the bother!')
    print('********************************************************************')
    print('')
    sys.exit(1)

try:
    from ftexplorer.data import Data
except ModuleNotFoundError:
    print('')
    print('****************************************************************')
    print('To run this script, you will need to copy or symlink the')
    print('"ftexplorer" and "resources" dirs from my ft-explorer project so')
    print('they exist here as well.  Sorry for the bother!')
    print('****************************************************************')
    print('')
    sys.exit(1)

# Copyright (c) 2018, CJ Kucera
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Generates the mod file.  Uses my own ft-explorer data classes to do all
# the introspection to find what needs updating and what doesn't

# Control Vars
mod_name = 'More Loot Midget Containers'
mod_version = '1.1.0'
output_filename = '{}.blcm'.format(mod_name)

# What to change
control = {
        'BL2': [
            ('Arid Nexus - Badlands', 'Stockade_P',
                {
                    'GD_Population_Treasure.Lootables.CardboardBox':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.CardboardBox_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.Dumpster':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Dumpster_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.Laundry_Machine':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Laundry_Machine_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.Crate_Military':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Crate_Military_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.CardboardBox':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.CardboardBox_WeeLoader',
                    'GD_Population_Treasure.Lootables.Storage_Locker':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Storage_Locker_MidgetHyperion',
                }),
            ('Arid Nexus - Boneyard', 'Fyrestone_P',
                {
                    'GD_Population_Treasure.Lootables.CardboardBox':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.CardboardBox_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.HyperionAmmo':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.HyperionAmmo_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.Dumpster':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Dumpster_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.Crate_Military':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Crate_Military_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.Storage_Locker':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Storage_Locker_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.Toilet':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Toilet_MidgetHyperion',
                    'GD_Population_Treasure.TreasureChests.WeaponChest_White':
                        'GD_Population_Treasure.TreasureChestsTrap.MidgetHyperion.WeaponChest_White_MidgetHyperion',
                }),
            ('Frostburn Canyon', 'IceCanyon_P',
                {
                    'GD_Population_Treasure.Lootables.Dumpster':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Dumpster_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Storage_Locker':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Storage_Locker_MidgetBandit',
                    'GD_Population_Treasure.Lootables.BanditCooler':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.BanditCooler_MidgetBandit',
                    'GD_Population_Treasure.TreasureChests.EpicChest_Red':
                        'GD_Population_Treasure.TreasureChestsTrap.MidgetBandit.EpicChest_Red_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Crate_Military':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Crate_Military_MidgetBandit',
                }),
            ('Hero\'s Pass', 'FinalBossAscent_P',
                {
                    'GD_Population_Treasure.Lootables.Storage_Locker':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Storage_Locker_MidgetHyperion',
                }),
            ('Dust', 'Interlude_P',
                {
                    'GD_Population_Treasure.Lootables.Toilet':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Toilet_MidgetBandit',
                    'GD_Population_Treasure.Lootables.BanditCooler':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.BanditCooler_MidgetBandit',
                }),
            ('Opportunity', 'HyperionCity_P',
                {
                    'GD_Population_Treasure.Lootables.HyperionAmmo':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.HyperionAmmo_MidgetHyperion',
                }),
            ('Sawtooth Cauldron', 'CraterLake_P',
                {
                    'GD_Population_Treasure.Lootables.BanditCooler':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.BanditCooler_MidgetBandit',
                    'GD_Population_Treasure.Lootables.CardboardBox':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.CardboardBox_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Dumpster':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Dumpster_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Laundry_Machine':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Laundry_Machine_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Storage_Locker':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Storage_Locker_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Toilet':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Toilet_MidgetBandit',
                    'GD_Population_Treasure.TreasureChests.WeaponChest_BanditPotty':
                        'GD_Population_Treasure.TreasureChestsTrap.MidgetBandit.WeaponChest_BanditPotty_MidgetBandit',
                }),
            ('Thousand Cuts', 'Grass_Cliffs_P',
                {
                    'GD_Population_Treasure.Lootables.HyperionAmmo':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.HyperionAmmo_MidgetHyperion',
                    'GD_Population_Treasure.TreasureChests.WeaponChest_White':
                        'GD_Population_Treasure.TreasureChestsTrap.MidgetBandit.WeaponChest_White_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Dumpster':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Dumpster_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Storage_Locker':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Storage_Locker_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Crate_Military':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Crate_Military_MidgetBandit',
                }),
            ('Tundra Express', 'TundraExpress_P',
                {
                    'GD_Population_Treasure.Lootables.BanditCooler':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.BanditCooler_MidgetBandit',
                    'GD_Population_Treasure.Lootables.CardboardBox':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.CardboardBox_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Dumpster':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Dumpster_MidgetBandit',
                    'GD_Population_Treasure.Lootables.Storage_Locker':
                        'GD_Population_Treasure.LootablesTrap.MidgetBandit.Storage_Locker_MidgetBandit',
                }),
            ('Wildlife Exploitation Preserve', 'PandoraPark_P',
                {
                    'GD_Population_Treasure.Lootables.CardboardBox':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.CardboardBox_WeeLoader',
                    'GD_Population_Treasure.Lootables.StalkerPileCeiling':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.StalkerPileCeiling_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.HyperionAmmo':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.HyperionAmmo_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.StalkerPilePillar':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.StalkerPileCeiling_MidgetHyperion',
                    'GD_Population_Treasure.Lootables.Storage_Locker':
                        'GD_Population_Treasure.LootablesTrap.MidgetHyperion.Storage_Locker_MidgetHyperion',
                }),
            ],
    }

level_transforms = {}
lines = []
for game, levelnames in control.items():
    lines.append('BL2')
    lines.append('#<{}>'.format(mod_name))
    lines.append('')
    lines.append('    # {} v{}'.format(mod_name, mod_version))
    lines.append('    # by Apocalyptech')
    lines.append('    # Licensed under Public Domain / CC0 1.0 Universal')
    lines.append('    #')
    lines.append('    # For levels which support loot-midget-spawning containers, converts')
    lines.append('    # all possible containers to loot-midget-spawning varieties.  Some')
    lines.append('    # levels (such as Thousand Cuts) already have every possible container')
    lines.append('    # set to have loot midget spawns.')
    lines.append('    #')
    lines.append('    # Note that this mod has been superceded by mopioid\'s "Loot Midget World!"')
    lines.append('    # https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/mopioid/LootMidgetWorld.blcm')
    lines.append('')
    data = Data(game)
    for (english, levelname, transforms) in levelnames:
        
        # Get the info on what objects we need to load.
        level_packages = ['{}.TheWorld:PersistentLevel'.format(levelname)]
        node = data.get_node_by_full_object('{}.TheWorld'.format(levelname))
        for childname, child in node.children.items():
            if childname[:14].lower() == 'levelstreaming':
                childstruct = child.get_structure()
                if childstruct['LoadedLevel'] != 'None':
                    level_packages.append(childstruct['LoadedLevel'].split("'", 2)[1])

        # Now loop through 'em to get all the population definitions
        got_hit = False
        for package in level_packages:
            package_obj = data.get_node_by_full_object(package)
            for childname, child in package_obj.children.items():
                if (childname[:33].lower() == 'willowpopulationopportunitypoint_' or
                        childname[:27].lower() == 'populationopportunitypoint_'):
                    childstruct = child.get_structure()
                    if childstruct != {}:
                        if childstruct['PopulationDef'] != 'None':
                            popdef = childstruct['PopulationDef'].split("'", 2)[1]
                            if popdef in transforms:
                                if not got_hit:
                                    lines.append('    #<{}>'.format(english))
                                    lines.append('')
                                    got_hit = True
                                if english not in level_transforms:
                                    level_transforms[english] = 1
                                else:
                                    level_transforms[english] += 1
                                lines.append("        level {level} set {objectname} PopulationDef PopulationDefinition'{popdef}'".format(
                                    level=levelname,
                                    objectname='{}.{}'.format(package, child.name),
                                    popdef=transforms[popdef],
                                    ))
                                lines.append('')

        if got_hit:
            lines.append('    #</{}>'.format(english))
            lines.append('')

    lines.append('#</{}>'.format(mod_name))

# Write out to the file
mp.human_str_to_blcm_filename("\n".join(lines), output_filename)
print('Wrote mod to {}'.format(output_filename))

# A bit of reporting at the end
print('')
for english, count in sorted(level_transforms.items()):
    print('{}: {}'.format(english, count))
