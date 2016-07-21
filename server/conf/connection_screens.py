# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets.UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = \
"""{b=============================================================={n
 Welcome to {g%s{n, version %s!

 .oOOOo.                    o                    `OooOOo.  OooOOo.  ooOoOOo 
o     o                   O                      o     `o O     `O    O    
O.                        o                      O      O o      O    o    
 `OOoo.                   o                      o     .O O     .o    O    
      `O .oOo. 'OoOo. .oOoO  .oOo. `OoOo.        OOooOO'  oOooOO'     o    
       o O   o  o   O o   O  OooO'  o            o    o   o           O    
O.    .O o   O  O   o O   o  O      O            O     O  O           O    
 `oooO'  `OoO'  o   O `OoO'o `OoO'  o            O      o o'       ooOOoOo 
{b=============================================================={n""" \
 % (settings.SERVERNAME, utils.get_evennia_version())
