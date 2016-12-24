Waffle / Github allows us to have labels to report progress about things.
These are the labels I can think of, and where they lie on the spectrum.

You also might want to check out the emoji examples for context, over
at [//github.com/thetoxicarcade/congredi](https://github.com/Thetoxicarcade/congredi/blob/master/.github/emoji.md).

# help wanted
Sections where nobody's claimed something. If you assigned yourself to an
issue, you can remove the `help wanted` label.

## first-pr / easy pick / beginner `:heart:`
Small problems I shouldn't be focusing on but need fixing eventually.

Example: `setup.py doesn't correctly generate an RST for PyPi`

## tougher `:octocat:`
Big problems I don't know how to approach exactly.

Example: `listenTCP(0) won't work on korora. Possibly a firewall issue?`

# the little things
## bug `trivial - :bug: critical - :ambulance:`
An error in the expected behavior of the application. Can be patched within `_._.x`.

Example: `running congredi in python3 - buffer objects not supported`

## trivial `:microsope:`
Small feature fixes. Patched at `_._.x`.

Example: `Docker image size improvements.`

## feature `:stars:`
New functionality. Can be patched within `_.x.x`.

Example: `OAEP within congredi's packets`

## enhancement `:telescope:`
Improved functionality. Pached at `_.x.x`.

Example: `Use Pycrypto over Cryptography.`

# the big picture
# tests `:warning:`
Adding tests to cover scenarios.

Example: `Require implementer to fail if command is invalid.`

# design `:tophat:`
mockups, interfaces, structuring.

Example: `Git Unified-diff recursion demo.py`

# documentation `:books:`
trying things out (a bit of QA), explaining code

Example: `The 'MONITOR' command.`

# refactoring `beauty - :art: clutter - :fire:`
Increase quality without changing functionality

Example: `unify two classes with a superclass`

# Machine labels
Labels useful to us, but automatic to the platform.
## in progress / ready
Labels used by waffle board
## duplicate / invalid / question / wontfix 
Labels useful to github

