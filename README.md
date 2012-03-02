JSLint support for Sublime Text 2 by using jslint4java
========================

Sublime Text 2 (http://www.sublimetext.com/2) is a sophisticated text editor for code, html and prose. You'll love the slick user interface and extraordinary features.

JSLint4Java (http://code.google.com/p/jslint4java/) is a java wrapper around the fabulous tool by Douglas Crockford, [jslint](http://jslint.com). It provides a simple interface for detecting potential problems in JavaScript code.

This project provide a plugin to add JSLint support for Sublime Text 2.

Features
-------------

- JSLint: Run JSLint (ctrl+j), or run jslint on save

- JSLint: Show JSLint Result

- Highlight error line by click on the result view

- Cross platform: support Windows, Linux and Mac OS X

Requirements
-------------

- java, and make sure java has been added to PATH

Installation
-------------

- Using Package Control http://wbond.net/sublime_packages/package_control

    > Install Package: sublime-jslint

- Download and extract to Sublime Text 2 Packages folder

    > Windows:  %APPDATA%\Sublime Text 2\Packages
    
    > Mac OS X: ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    
    > Linux:    ~/.config/sublime-text-2/Packages

How to use?
-------------

- Using the Command Palette (Windows and Linux: Ctrl+Shift+P, OSX: Command+Shift+P) then search for:

    - JSLint: Run JSLint (ctrl+j)
    - JSLint: Show JSLint Result

Open up a .js file and hit ctrl+j to run JSLint. An new output panel will appear giving you the JSLint results:

Screenshots
-------------

![](https://github.com/fbzhong/sublime-jslint/raw/master/images/screenshot.png)

Settings
-------------

Settings can be opened via the Command Palette, or the Preferences > Package Settings > JSLint > Settings – User menu entry.

    {
        // Path to the jslint jar.
        // Leave blank to use bundled jar.
        "jslint_jar": "",

        // Options pass to jslint.
        "jslint_options": "",

        // Ignore errors, regex.
        "ignore_errors":
        [
            // "Expected an identifier and instead saw 'undefined' \(a reserved word\)"
        ],

        // run jslint on save.
        "run_on_save": false,

        // debug flag.
        "debug": false
    }

The available jslint_options: https://github.com/fbzhong/sublime-jslint/wiki/Available-jslint4java-options

New BSD License
-------------

Copyright (c) 2011, Robin Zhong <fbzhong@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Robin Zhong nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
