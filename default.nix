with import <nixpkgs> {};

let repp =
  { stdenv
  , buildPythonPackage
  , fetchFromGitHub
  , isPy3k
  , click
  }:

  buildPythonPackage rec {
    pname = "repp";
    version = "1.0.0";
    disabled = !isPy3k;

    src = ./.;

    propagatedBuildInputs = [ click ];

    meta = with stdenv.lib; {
      homepage = https://github.com/ashgillman/repp;
      description = "A very simple repository manager";
      license = licenses.mit;
    };
  };

in python3.pkgs.callPackage repp {}
