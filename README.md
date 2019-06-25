# RHGL Library

This library allows you to render vector graphics on a terminal.

# Requirements

* Python 3.x
* NumPy
* Terminal Emulator must support Unicode, as graphics is depicted using unicode blocks.
 * It is also advisable to decrease font size to allow higher resolutions.
* In order to render the full RGB colour range, a terminal with VT Colour must be used. This includes a majority of terminal emulators on Linux and recent versions of powershell

# Features

* 2D/3D Vector graphics.
* Well optimized matrix transformations. ( Thanks Numpy.. )
* Unoptimized as fuck line drawing algorithm. ( Bresenham mode is completely broken, so don't use that )
* RGB Colour Range support.

