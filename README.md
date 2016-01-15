What Is This?
=============
This utility spits all information gathered from the [CrystalDiskInfo](http://crystalmark.info/software/CrystalDiskInfo/index-e.html) program into a parsable JSON file.

Why?
====
I'm used to writing shell scripts on my FreeNAS box that do this by interfacing with [smartctl](https://github.com/mirror/smartmontools). On Windows I tend to use CrystalDiskInfo to diagnose / inspect my drives. However, CrystalDiskInfo is purely a GUI application, so being able to output to JSON makes the utility much more extensible. For example, you could use this utility to take snapshots of your drive statuses on a frequent basis, and then use a D3 web application to visualize this output or an alert application that notifies you of SMART health thresholds or errors.

Example
=======
This repo includes [an example set of sample output with serial numbers censored out](https://github.com/xioustic/CrystalDiskInfoParser/blob/master/SAMPLE.json).

Dependencies
============
Everything is raw Python 2.7. The only dependency is the DiskInfo.exe application and CdiResource folder, which is included with this repository. If you want to drop the raw Python 2.7 dependency, consider building a standalone executable for distribution using [PyInstaller](https://github.com/pyinstaller/pyinstaller).

Usage
=====
This utility MUST be run as administrator. The DiskInfo.exe application requires it to get low level access to drive information, and this utility requires DiskInfo.exe to produce the initial output.

Worried?
========
A responsible system administrator will not run any binary or unreviewed code as administrator. The Python code for the utility is short to review, so your primary concern should be the DiskInfo.exe binary. The original binary and source for DiskInfo.exe is made available at the author's website (here)[http://crystalmark.info/download/index-e.html]. It might be a good idea to use his binary instead of mine, or even try building it from his source after reviewing.

License
=======
[MIT all the way down.](https://github.com/xioustic/CrystalDiskInfoParser/blob/master/LICENSE.md)
