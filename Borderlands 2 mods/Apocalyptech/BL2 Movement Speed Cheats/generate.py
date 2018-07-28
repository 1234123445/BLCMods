#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

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

###
### Constants
###

mod_name = 'BL2 Movement Speed Cheats'
mod_version = '1.3.0'
output_filename = '{}.blcm'.format(mod_name)

###
### Generation
###

segments = {}

# Loop through a number of control vars
for (profile_name, profile_desc,
            (ground_speed, air_speed, injured_speed, crouched_pct, jump_z, air_control_pct, ladder_speed)
            ) in [
        ('reasonable', 'Reasonable Improvements', (650,  700,  300, 1,   750, .8, 400)),
        ('extreme',    'Extreme Improvements',    (1000, 1100, 500, 1,   900, .9, 600)),
        ('stock',      'Stock Values',            (440,  500,  150, 0.5, 630, .11, 200))]:

    char_segments = {}
    for (name, streaming_obj, player_obj) in [
            ('Axton', 'GD_Soldier_Streaming.Pawn_Soldier', 'GD_Soldier.Character.CharClass_Soldier'),
            ('Gaige', 'GD_Tulip_Mechro_Streaming.Pawn_Mechromancer', 'GD_Tulip_Mechromancer.Character.CharClass_Mechromancer'),
            ('Krieg', 'GD_Lilac_Psycho_Streaming.Pawn_LilacPlayerClass', 'GD_Lilac_PlayerClass.Character.CharClass_LilacPlayerClass'),
            ('Maya', 'GD_Siren_Streaming.Pawn_Siren', 'GD_Siren.Character.CharClass_Siren'),
            ('Salvador', 'GD_Mercenary_Streaming.Pawn_Mercenary', 'GD_Mercenary.Character.CharClass_Mercenary'),
            ('Zero', 'GD_Assassin_Streaming.Pawn_Assassin', 'GD_Assassin.Character.CharClass_Assassin'),
            ]:
        (pkg, shortobj) = streaming_obj.split('.', 1)
        mp.register_str('GroundSpeed',
            'demand {} set {} GroundSpeed {}'.format(pkg, streaming_obj, ground_speed))
        mp.register_str('GroundSpeedBaseValue',
            'demand {} set {} GroundSpeedBaseValue {}'.format(pkg, streaming_obj, ground_speed))
        mp.register_str('AirSpeed',
            'demand {} set {} AirSpeed {}'.format(pkg, streaming_obj, air_speed))
        mp.register_str('AirSpeedBaseValue',
            'demand {} set {} AirSpeedBaseValue {}'.format(pkg, streaming_obj, air_speed))
        mp.register_str('JumpZ',
            'demand {} set {} JumpZ {}'.format(pkg, streaming_obj, jump_z))
        mp.register_str('JumpZBaseValue',
            'demand {} set {} JumpZBaseValue {}'.format(pkg, streaming_obj, jump_z))
        mp.register_str('CrouchedPct',
            'demand {} set {} CrouchedPct {}'.format(pkg, streaming_obj, crouched_pct))
        char_segments[name] = """#<{name}>

                # The set statements apply the settings initially

                set {player_obj} GroundSpeed {ground_speed}

                set {player_obj} AirSpeed {air_speed}

                set {player_obj} CrouchedPct {crouched_pct}

                set {player_obj} JumpZ {jump_z}

                # The hotfixes apply once you respawn or exit FFYL
                # (These may be a bit overboard.  Not sure if you need the BaseValue
                # ones, or if the BaseValue ones are the only ones you need, etc.)

                {mp:GroundSpeed}

                {mp:GroundSpeedBaseValue}

                {mp:AirSpeed}

                {mp:AirSpeedBaseValue}

                {mp:JumpZ}

                {mp:JumpZBaseValue}

                {mp:CrouchedPct}

            #</{name}>""".format(
                name=name,
                player_obj=player_obj,
                ground_speed=ground_speed,
                air_speed=air_speed,
                crouched_pct=crouched_pct,
                jump_z=jump_z,
                mp=mp,
                )

    segments[profile_name] = """#<{profile_desc}>

            {axton}

            {gaige}

            {krieg}

            {maya}

            {salvador}

            {zero}

            #<Global Movement Vars>

                # These variables aren't player-specific, and don't seem to require hotfixes
                # to apply post-death-or-FFYL

                set GD_PlayerShared.injured.PlayerInjuredDefinition InjuredMovementSpeed {injured_speed}

                set GD_Globals.General.Globals PlayerAirControl {air_control_pct}

                set Engine.Pawn LadderSpeed {ladder_speed}

            #</Global Movement Vars>

        #</{profile_desc}>""".format(
            profile_desc=profile_desc,
            axton=char_segments['Axton'],
            gaige=char_segments['Gaige'],
            krieg=char_segments['Krieg'],
            maya=char_segments['Maya'],
            salvador=char_segments['Salvador'],
            zero=char_segments['Zero'],
            injured_speed=injured_speed,
            air_control_pct=air_control_pct,
            ladder_speed=ladder_speed,
            )

mod_str = """BL2
#<{mod_name}>

    # {mod_name} v{mod_version}
    # by Apocalyptech
    # Licensed under Public Domain / CC0 1.0 Universal
    #
    # Ups the movement speed of all characters (including while crouched and during
    # FFYL), increases jump height a bit, and provides much more air control.

    #<Movement Speed Buffs (Pick One)><MUT>

        {reasonable}

        {extreme}

        {stock}

    #</Movement Speed Buffs (Pick One)>

#</{mod_name}>""".format(
    mod_name=mod_name,
    mod_version=mod_version,
    reasonable=segments['reasonable'],
    extreme=segments['extreme'],
    stock=segments['stock'],
    )

mp.human_str_to_blcm_filename(mod_str, output_filename)
print('Wrote mod file to: {}'.format(output_filename))
