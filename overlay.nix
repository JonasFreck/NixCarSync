self: super: {
  myPythonEnv = super.python3.withPackages (ps: with ps; [
    # Add other Python packages your script needs
  ]);

  myEnv = super.buildEnv {
    name = "myEnv";
    paths = [
      self.myPythonEnv
      super.rsync
    ];
  };
}
