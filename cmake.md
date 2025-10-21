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

A more detail version would be

```bash
cmake -B /path/to/build_dir -S /path/to/source [options]
cmake --build /path/to/build_dir [options]
cmake --install /path/to/build_dir [options]
```

If tests are available and integrated with `CMake` framework, use:

```bash
ctest --build-dir /path/to/build_dir
```

Update environmental variable [`CMAKE_PREFIX_PATH`](https://cmake.org/cmake/help/latest/variable/CMAKE_PREFIX_PATH.html) (hence, export it before running the configuration stage) to tell `CMake` where to look for packages when using `find_package()` and alike.

Configuration options (that is, those that can be passed to plain `cmake`):

* Define variables: `-Dvar=value` or `-Dvar:type=value`, e.g.: `-DFOO:STRING=bar`, `-DPIPPO=2`.

* Prefix: `-DCMAKE_INSTALL_PREFIX=path`, or, in recent versions, `--install-prefix path`.

Building options:

* `-j <N>`: equivalent of the namesake `make` option for number of (parallel) jobs.

* `--clean-first`

* `-t <target>`, `--target <target>`: build only recipe `target`.
    To get the list of all available targets, use `--target help`.

Install options:

* `--prefix <dir>`: Override `CMAKE_INSTALL_PREFIX`.

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
    They can be set by the user at configure time with the `-D` handle.
