# `CMake`

`CMake` is a software build system, that is, a tool that help you build your projects, especially if they are written in `C[++]`.

An [introduction](https://cmake.org/cmake/help/latest/manual/cmake.1.html) and a [tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html) are available online.

The standard “configure-make-install” framework translates in `CMake` terms to

```bash
cmake [options] /path/to/source
make
make install
```

where one typically still relies on good old `make`.
However, one can also use

```bash
cmake [options] /path/to/source
cmake --build .
cmake --install .
```

A more detailed version would be

```bash
cmake -B /path/to/build_dir -S /path/to/sources [options]
cmake --build /path/to/build_dir [options]
cmake --install /path/to/build_dir [options]
```

If tests are available and integrated with `CMake` framework, use:

```bash
ctest --build-dir /path/to/build_dir
```

Update environmental variable [`CMAKE_PREFIX_PATH`](https://cmake.org/cmake/help/latest/variable/CMAKE_PREFIX_PATH.html) (hence, export it before running the configuration stage) to tell `CMake` where to look for packages when using `find_package()` and alike.

Configuration options (that is, those that can be passed to plain `cmake`):

* Define variables: `-Dvar=value` or `-Dvar:type=value`, e.g.: `-DPIPPO=2`, `-DFOO:STRING=bar`.

* List available configuration variables (see [SO](https://stackoverflow.com/questions/16851084/how-to-list-all-cmake-build-options-and-their-default-values)): `cmake -LH` (add `-A` for "advanced" variables but it might get messy).

* Prefix: `-DCMAKE_INSTALL_PREFIX=path`, or, in recent versions, `--install-prefix path`.

* In recent versions (>3.24), use `--fresh` to clear configuration cache before reconfiguring.

Building options:

* `-j <N>`: equivalent of the namesake `make` option for number of (parallel) jobs.

* `--clean-first`.

* `-t <target>`, `--target <target>`: build only recipe `target`.
    To get the list of all available targets, use `--target help`.

Install options:

* `--prefix <dir>`: Override `CMAKE_INSTALL_PREFIX`.

Some things to keep in mind:

* Commands are generated during configure stage, hence, they might not reflect the current status and need a reconfiguration to be updated.
    An example.
    A custom command that runs `foo`:

    ```cmake
    add_custom_command(COMMAND "PATH=$ENV{PATH} foo")
    ```

    (OK it does not make much sense like this, but just for the sake of example).
    When configuring you forgot to include the path to `foo`.
    `$ENV{PATH}` is _evaluated_ and _hard-written_ at configure stage, hence without the path to `foo`.
    If, for instance, it is later changed, the changes are not repercuted into the command.
    Consider the sequence:

    ```bash
    cmake [...]  # ENV{PATH} is evaluated and stored now!
    make  # You forgot foo, it fails
    module load foo
    make  # It _STILL_ fails because the command has not been updated
    ```

    A new reconfiguration step is necessary.

* To have a look at what targets and commands actually do, check out `make` files, and in particular `<build_dir>/CMakeFiles/Makefile.cmake` and `<build_dir>/CMakeFiles/<target>.dir/build.cmake`.

* About [CMake Cache](https://cmake.org/cmake/help/book/mastering-cmake/chapter/CMake%20Cache.html), which is stored in `<build_dir>/CMakeCache.txt`.

A developer tells `CMake` what to do by writing a `CMakeLists.txt` file.
Typically one defines the project, where the sources are, which additional libraries have to be included and/or linked,...
A custom language has been developed.

* Commands and variables are case-INsensitive.

* [All commands](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html).

* Conditional statements: `if()`, `elseif()`, `else()` `endif()`.

* Loops: `foreach()` and `endforeach()`, `while()` and `endwhile()`, `break()`, `continue()`.

* Functions: `function()` and `endfunction()`, `macro()` and `endmacro()`.

      ```cmake
      # Define
      function(foo bar baz)
        # ...
      endfunction()
      # Call
      foo("bar" "baz")
      ```

* Variables:

  * Define custom ones with `[un]set()`: `set(<variable> <value>[... <type> <docstring>])`.

  * Some are [already](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html) [defined](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html).
    E.g.: `PROJECT_NAME`, `CMAKE_BUILD_TYPE`.

  * Call `include(GNUInstallDirs)` to use variables such as `CMAKE_INSTALL_LIBDIR|INCLUDEDIR`.

* Options: `option(<variable> "<help_text>" [value])`.
    They can be set by the user at configure time with the `-D` handle, see above.
