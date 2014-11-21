JSLint support for Sublime Text 2 by using jslint4java
======================================================

[Sublime Text 2](http://www.sublimetext.com/2) is a sophisticated text editor for code, HTML and prose. You'll love its slick user interface and extraordinary features.

[JSLint4Java](http://code.google.com/p/jslint4java/) is a Java wrapper around the fabulous tool by Douglas Crockford, [JSLint](http://jslint.com). It provides a simple interface for detecting potential problems in JavaScript code.

This project is a plugin to add JSLint support for Sublime Text 2.

Features
--------

* JSLint: Run JSLint (Ctrl+J), or run JSLint on save
* JSLint: Show JSLint results
* Highlight error line by click in the result view
* Cross-platform: supports Windows, Linux and Mac OS X

Requirements
------------

Java - also ensure that it has been added to PATH

Installation
------------

* Using [Package Control](http://wbond.net/sublime_packages/package_control):
    * Install Package: sublime-jslint
* Download and extract to Sublime Text 2 Packages folder
    * Windows: %APPDATA%\Sublime Text 2\Packages
    * Mac OS X: ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    * Linux: ~/.config/sublime-text-2/Packages

How to use?
-----------

Open the Command Palette (Windows and Linux: Ctrl+Shift+P, OSX: Command+Shift+P), then search for:

* JSLint: Run JSLint (Ctrl+J)
* JSLint: Show JSLint Result

Open up a .js file and hit Ctrl+J to run JSLint. An new output panel will appear giving you the JSLint results:

Screenshots
-----------

![](https://github.com/fbzhong/sublime-jslint/raw/master/images/screenshot.png)

Settings
--------

Settings can be opened via the Command Palette, or via the Preferences/Package Settings/JSLint/Settings – User menu entry.

```javascript
{
    //Uses system installed jslint.js (node.js based), instead of bundled JSLint jar
    "use_node_jslint": false,

    //Path to the jslint.js
    //Leave blank to use default JSLint path
    "node_jslint_path": "",

    //Options passed to jslint.js
    "node_jslint_options": "",

    //Path to the JSLint jar.
    //Leave blank to use bundled jar.
    "jslint_jar": "",

    //Options passed to JSLint.
    "jslint_options": "",

    //Errors and RegEx to be ignored
    "ignore_errors":
    [
        //"Expected an identifier and instead saw 'undefined' \(a reserved word\)"
    ],

    //Run JSLint on save.
    "run_on_save": false,

    //Debug flag.
    "debug": false
}
```

All available jslint_options can be found [here](https://github.com/fbzhong/sublime-jslint/wiki/Available-jslint4java-options).

License
-------

sublime-jslint is released under the New  BSD License, which may be found [here](https://github.com/fbzhong/sublime-jslint/blob/master/LICENSE.md).