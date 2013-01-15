---------------------
SDL PATCHES FOR ARCHY
---------------------

Archy requires a slightly modified version of SDL for it to operate
properly.  Within this directory are GNU diff patches, intended to be
applied to the latest stable release of SDL.

Note that these patches were originally modifications from SDL-1.2.8
sources; since they're contextual diffs, they should apply without
problems to future releases of SDL, but if applying a patch causes any
diff conflicts, you may want to retrieve the original SDL-1.2.8
sources and patch those.

How to apply a patch
--------------------

Before applying a patch, you need to make sure you have the GNU diff
and patch utilities.  These should be installed on your computer by
default if you use a Unix-based system, but Windows users should
probably get cygwin (http://www.cygwin.com/).

The best way to apply a patch is to first obtain the latest stable SDL
sources from http://www.libsdl.org.

Now, as an example, to apply the patch located in '~/mypatch.diff',
enter the SDL distribution's root directory (e.g. 'SDL-1.2.8') and
enter the following command from a shell prompt:

  patch -p1 < ~/mypatch.diff

The program should tell you it's patching a file (or multiple files).

The 'sdl-numcapslock' patches
-----------------------------

These patches were created to fix the way SDL deals with the caps lock
and num lock keys.  The main problem is that, under SDL, the up/down
state of these keys is dictated by their modal state, rather than
their physical state: if the operating system's caps lock mode is
activated, then the caps lock key is reported as being pressed down,
and caps lock is reported as being released if the caps lock mode is
not active.  Similarly, key-down and key-up events are sent when the
caps lock mode is activated and deactivated, respectively, rather than
when the caps lock key is physically pressed and released.  What this
means is that it's impossible to actually detect when the caps lock
key is physically released; for the purposes of Archy, this prevents
caps lock from being used as a quasimodal key.

The reason for this behavior is apparently because some X servers only
report the modal state of caps and num lock keys; they cannot report
their physical states.  In an effort to make behavior consistent across
all platforms, the authors of SDL chose to maintain this behavior
across all operating systems, even if many of the platforms (including
Windows, many X-Servers, and probably OS X) actually support reading
the physical state of the keys.

As a result, there exists code in SDL that intentionally intercepts
the physical caps lock keypress information from the operating
system's native multimedia API and "twists" it to report information
about the state of the caps lock mode rather than the physical state
of the key.

The diff patch 'sdl-numcapslock-base.diff' fixes this behavior for all
platforms, so that all events and state information related to the
num/caps lock keys is indicative of their physical state rather than
their modal state.

However, each OS's multimedia API also has its own api-specific code
that sets the initial state of the caps/num lock keys at application
startup, as well as modifying the state of these keys whenever the
application regains focus.  This is so that, for instance, the caps
lock key is reported as being already "pressed down" if the caps lock
mode is active when an application starts.  Separate patches for each
multimedia API are needed to fix this problem:

  'sdl-numcapslock-windows.diff'
    Fix for the Microsoft Windows OS.

  'sdl-numcapslock-x11.diff'
    Fix for the Unix X11 driver.

The 'sdl-windx5-exclusive-kbd-mode' patch
-----------------------------------------

This patch is for SDL's Windows DirectX 5 driver, and actually uses
DirectInput 8 to initialize the keyboard in exclusive mode (instead of
the default non-exclusive mode).  What this means for any application
that uses SDL's DirectX driver is primarily that the Windows key will
not operate normally while the application is in focus; this is
particularly useful for full-screen applications (including Archy),
during which the press of the Windows key would normally cause the
application to minimize itself and the Start Menu to go into focus,
which is extremely disorienting when done accidentally (which is
nearly always the case).

It should also be noted that applying this patch will cause the SDL
library to require DirectX 8 to be present on the host system, rather
than DirectX 5 (which is the normal requirement).

To get this patch to compile properly in Microsoft Visual C, you will
also have to link the DirectInput 8 library to the project.  This can
be done by loading the project, going to the "Project" menu, selecting
"Properties", selecting the "Linker" folder, selecting the "Input"
category under that folder, and adding the file "dinput8.lib" to the
"Additional Dependencies" section.
