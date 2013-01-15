This folder contains OS-specific application icons needed for Archy.

For Windows, at least two icons are needed: a 16x16 icon and a 32x32
icon.  If the user is using Windows XP and chooses to sort their icons
by "Tiles", then XP will display an enormous 48x48 icon; if such an
icon isn't available, it will simply enlarge the 32x32 icon.  All of
these icons need to be compiled into a single .ico file.

Additionally, pygame's pygame.display.set_icon() function can be used
to set the icon at the upper-left hand corner of the Archy window, as
well as the taskbar icon.

The best freeware icon editor for Windows appears to be LiquidIcon XP,
which can be obtained from the following site:

  http://www.x2studios.com/index.php?page=products&id=11

