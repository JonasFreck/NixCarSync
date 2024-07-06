{ pkgs ? import <nixpkgs> { overlays = [(import ./overlay.nix)]; } }:


pkgs.mkShell {

  
  buildInputs = [
    pkgs.myEnv
  ];

  shellHook = ''
    export SOURCE_PATH="source/directory"
    export DESTINATION_PATH="destination/directory"
    echo "Environment with Python and rsync set up. You can run your script now."
  '';
}
