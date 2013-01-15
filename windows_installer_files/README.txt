How to set up a Windows self-executing installer for Archy
----------------------------------------------------------

First of all, you'll need to get InnoSetup from this website:

  http://www.jrsoftware.org/isinfo.php

Then follow these instructions.

1) Run 'python setup.py py2exe' in the root directory.

2) Ensure that all required DLL's and other files are in the
   newly-created 'dist' subdirectory.

3) Enter the 'windows_installer_files' subdirectory.

4) Run 'iscc archy.iss'.  (Before doing this, ensure that
   the Inno Setup folder is in your PATH environment
   variable!)

5) The resultant file, 'setup.exe', will be placed in the
   'windows_installer_files/Output' subdirectory.  This is an
   executable self-installer that has the ability to install itself,
   create Start Menu and Desktop shortcuts, uninstall itself, and then
   some all on its own.
