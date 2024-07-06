{ pkgs ? import <nixpkgs> { overlays = [(import ./overlay.nix)]; } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.myEnv
  ];

  shellHook = ''
    echo "Environment with Python and rsync set up. You can run your script now."
  '';
}
