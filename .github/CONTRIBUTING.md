# How to Contribute
Issues & Pull requests are welcome :D :heart:
This repo handles letting anonymous people reach compromises. Unfortunately the 
codebase doesn't extend to github comments. Don't be any form of oppressive or
slandarous towards another person or group.

Explaining an endpoint allows other people to use it correctly. If the
docs won't match the code anymore, change them too. Use markdown code
blocks for snippets, when in doubt run `mkdocs serve` to try them out.

Before submitting your changes, run `setup.py test` &/|| `docker-compose build`,
just to see that everything superficially checks out. If you'd made changes
outside the scope of the tests, it might not register as failing, but it's
a good, basic step. The testing system currently uses `nose2` & `jasmine`.

Insofar as the editor you use can format, and the test suite used can lint it.
Currently, that's `eslint` & `pylint` (`python setup.py lint`).
In other words, if the machines can both catch and help you, style it that way.

### Commits (from Atom/Contributing)
* Present Tense, Imperative mood `run` ***not*** `ran/runs`
* prefixes (use emojis! :sunglasses:)

# (finally) Submitting Changes

1. Create (or finish creating) an issue referencing what needs to change.
2. Start your pull request (on your honor it's your own code).
3. If the build, documentation, or testing need changes, alert us to them.

> want to change these `.github` docs?

| emoji | source |
| --- |:--- |
|Languages :snake::triangular_ruler::zap::microscope::telescope::lock: |`:snake:``:triangular_ruler:``:zap:``:microscope:``:telescope:``:lock:` -python, angular, Bolt/Neo4j/DB, crypto, loading, security|
|Quality :100::pray::bug::green_heart::white_check_mark::nose::art::fire:|`:pray:``:100:``:bug:``:green_heart:``:nose:``:art:``:white_check_mark:``:fire:`-builds, bugs, tests, CI, Nose2 tests,unit tests, structuredeleted code, clutter|
|Services :heart::octocat::books::pencil2::memo::cloud::chart_with_upwards_trend:|`:chart_with_upwards_trend:``:heart:``:octocat:``:memo: ``:cloud:``:books:``:pencil2:`-docs, git, mkdocs, docker,badgestutorials, methods|
|Releases :arrow_up::tophat::ambulance::beers::warning::heavy_exclamation_mark:| `:tophat:``:ambulance:``:arrow_up:``:beers:``:warning:``:heavy_exclamation_mark:`- BlackHat CVE , Triage / Catastrophic, release - cheers! beta - beta release, versions|
