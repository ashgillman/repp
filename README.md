# Repp - A (very) simple repository manager

`repp` is a super simple repository manager that keeps various git repositories
in what the author considers to be a sane directory structure.

```sh
$ repp --help
Usage: repp [OPTIONS] COMMAND [ARGS]...

  Manage development repositories.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  clone  Clone a new url into the repositories.
  list   List the current repositories.
  test   Run program tests.

$ repp
~/dev
├── CCPPETMR@github.com
│   └── SIRF
├── InsightSoftwareConsortium@github.com
│   ├── ITK
│   └── remotes
├── ashgillman@github.com
│   ├── ashgillman.github.io
│   ├── bst
│   └── systems
├── NixOS@github.com
│   └── nixpkgs
└── pmarkiew@cmiclab.cs.ucl.ac.uk
    └── NiftyPET

$ # can clone by ssh or https clone link, or GitHub repo URL.
$ repp clone https://github.com/ashgillman/repp
Cloning into 'repp'...
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 5 (delta 0), pack-reused 0
Receiving objects: 100% (5/5), done.

$ # We have added ~/dev/ashgillman@github.com/repp
$ repp
~/dev
├── CCPPETMR@github.com
│   └── SIRF
├── InsightSoftwareConsortium@github.com
│   ├── ITK
│   └── remotes
├── ashgillman@github.com
│   ├── ashgillman.github.io
│   ├── bst
│   ├── repp
│   └── systems
├── NixOS@github.com
│   └── nixpkgs
└── pmarkiew@cmiclab.cs.ucl.ac.uk
    └── NiftyPET
```
