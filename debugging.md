# Debugging tools

## `valgrind`

Some useful options:

* Log file: `--log-file=<filename>`

* Check and track memory leaks: `--leak-check=full` `--track-origins=yes`

  * Reachable / possibly-lost: `--show-reachable=yes|no --show-possibly-lost=yes|no`

* Profiling: `--tool=callgrind`.
    A file with a name similar to (where `pid` is a long number) is created with all the events registered.
    One can open it with `qcachegrind` or `kcachegrind`

  * [Manual](https://www.cs.cmu.edu/afs/cs.cmu.edu/project/cmt-40/Nice/RuleRefinement/bin/valgrind-3.2.0/docs/html/cl-manual.html)

  * [How to interpret `qcachegrind`](https://stackoverflow.com/a/50781312/12152457)

  * Profiling a subset of the program: one might be interested in profiling only a part of the program, or even only a function (for instance to have results that are not polluted by other functions, to speed up a little bit).
    This can be done in several ways:

    * Add `callgrind` macros to the code, see [here](https://cta-redmine.irap.omp.eu/projects/gammalib/wiki/How_to_use_valgrind) (use option `--collect-atstart=no`)

      ``` c
      #include <valgrind/callgrind.h>

      int main()
      {
        foo1();
        CALLGRIND_START_INSTRUMENTATION;
        CALLGRIND_TOGGLE_COLLECT;
        bar1();
        CALLGRIND_TOGGLE_COLLECT;
        CALLGRIND_STOP_INSTRUMENTATION;
        foo2();
      }
      ```

    * Toggle the collection at entry/exit of a function: use options `--collect-atstart=no` `"--toggle-collect=bar1(int, int)"`.
        It is very picky, hence keep the quotes, put the full signature with arguments separated by a comma and a space; for class methods:
        `Foo::bar1()`.
        See [here](https://valgrind-users.narkive.com/2YLNcvE8/callgrind-toggle-collect-on-a-class-function) and [here](https://stackoverflow.com/questions/13688185/callgrind-profile-a-specific-part-of-my-code)

    * Start the program and activate with `callgrind_control -i on`

## `gdb`

* Calling functions such as `fabs`, `sin`,...: `((double(*)(double))<foo>)(x)`

* Setting watchpoints which stay after the end of the current function:

      $ print pt
        (double *) 0x75e12
      $ watch *(double *) 0x75e12

* Print all current variables: `info args` (try also `info locals`)

* Logging output [here](https://sourceware.org/gdb/onlinedocs/gdb/Logging-Output.html)

  * Enable/Disable logging: `$ set logging on|off`

  * Change name of the log file (default is `gdb.txt`): `$ set logging file <name>`

  * Overwrite: `$ set logging overwrite on|off`

  * Redirect only to file: `$ set logging redirect on|off`
