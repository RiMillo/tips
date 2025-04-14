# `python`

(I used to be better with `python` but I don’t use it so much now, so these tips here are not many nor much useful.
I’m sorry.
If you agree, please contribute!)

* Debugging, info [here](https://docs.python.org/2/library/pdb.html): `python -m pdb script.py`.
    Commands are similar to [`gdb`](debugging.md#gdb).

* Virtual environments: have look [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) or [here](https://docs.python.org/3/tutorial/venv.html).

  1.  Create: `python3 -m venv <env_name>`.
    The argument `env_name` is arbitrary: below, we’ll use `test`

  2.  Activate: `source test/bin/activate`.
    From now on the python version of the virtual element is loaded, you may check this with `which python`.
    Hence, for instance, `pip` will install packages in the virtual environment only

  3.  If needed, install any desired module as usual (see `pip` below).

      * **Remarks:** mind that `venv` will try install everything, even those modules that are already in your `$HOME/.local/lib/pythonX.Y/site-packages`.
        However, if you want to reuse them, use the dedicated option when creating the environment

        ``` bash
        python3 -m venv --system-site-packages <env_name>
        ```

  4.  Deactivate: `deactivate`

  5.  Remove: just `rm -rf <env_name>`

* `pip`: allows you to download and update python libraries

  * Typical call: `pip install <package>`.
    Add options `--upgrade|-U` to upgrade.
    In recent versions, `python3 -m pip [...]` is advised.

    * For the sake of brevity, below we will often use `pip` instead of the form with `python`

  * Select a specific version of the package: `python3 -m pip install package==6.66`

  * Selecting the sources: `pip` can handle several types of sources

    * The first is of course `PyPI`, that is the open, online data-base where the great majority of packages are published.
        In this case, one just need to pass the name of the package

      ``` bash
      pip install numpy
      ```

    * One can also tell `pip` to look for a package in an online `git` repository.

      * Two ways are accepted: either by http or by SSH.

      * Use the same addresses used for cloning.

      * **Warning**: when using SSH, replace the colon “`:`” after the
        server name by a simple slash “`/`”, see example below

      * If the repository is protected and using http, credential are asked.

      ``` bash
      # https
      pip install git+https://github.com/foo/bar.git
      # SSH
      pip install git+ssh://git@github.com/foo/bar.git
      # hhtps abd specify a branch
      pip install git+https://github.com/foo/bar.git@my_branch
      ```

    * When one has the sources, just provide the path.

      ``` bash
      cd /path/to/my_package
      # Mind the dot at the end
      pip install .
      ```

  * Extras: sometimes packages have extras.
    Example: package `foo` can be installed by itself, with a GUI and/or with a complementary series of developer packages.
    One or more extras can be put inside brackets.
    For the sake of simplicity, we supposed the extras are called `gui` and `dev`

    ``` bash
    pip install foo           # foo only
    pip install foo[gui]      # foo with GUI
    pip install foo[dev]      # foo with dev environment
    pip install foo[gui,dev]  # foo with both GUI and dev
    pip install foo[all]      # foo with all extras
    ```

    * When installing from `git` or from sources:

      ``` bash
      pip install ".[gui]"
      pip install "foo[gui] @ git+https://github.com/foo/bar.git"
      ```

  * One may add a configuration file, see [here](https://pip.pypa.io/en/stable/topics/configuration/)

  * You’ll need access to some directories, thus it is advised to have a local install: pass option `--user`.

  * Choose installation prefix: `--target <install_dir>`.
    All the necessary dependencies will be installed in the given directory even if, for instance, they are already installed in the usual path.

  * Skip dependencies: `--no-deps`

    * *Why this is useful.*
        Imagine you want to install a package with some dependencies in a custom path; suppose also that all the dependencies are already installed in the reference path (say, `.local`).
        Without `--no-deps` all the dependencies will be installed in the custom path, even if they are already available, thing that one may want to avoid.

  * When installing a custom package (e.g., developed by ourselves), you may want to use option `-e`.
    That enables *editable* mode: roughly speaking, instead of copying the package in the target directory, `pip` will create links so that if you modify the package, the changes are considered.
    More info [here](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).

    ``` bash
    pip install -e .
    ```

  * Proxy: pass the option `--proxy=user@server.dom:port`.
    However, it might not work if some dependencies have to be downloaded as well.
    In that case, try exporting the shell variables `HTTP_PROXY=<proxy>` and `HTTPS_PROXY=<proxy>`.
    It might be helpful to add a line in the configuration file as explained [here](https://stackoverflow.com/questions/43473041/how-to-configure-pip-per-config-file-to-use-a-proxy-with-authentification)

  * Get list of outdated packages: `pip list --outdated`.

  * Get a list of currently installed packages with versions: `pip freeze > [file.txt]`

  * Install from a requirements file (see freezing just above): `pip install -r [file.txt]`

  * When installing/upgrading problems may occur with older versions of the `C` compiler, `GCC`: try and force `C99` standard by setting `CFLAGS` before installing: `export CFLAGS='-std=c99'`

* Packaging a module: this will enable your package to be installed by, say, `pip`

  * [The official tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

  * The advised way nowadays is to do the setup via a `pyproject.toml`, file that can also be used to configuring other tools for, for instance, format and linting.
    Some guidelines for [writing such a file](https://packaging.python.org/en/latest/guides/writing-pyproject-toml)

  * Common backends are: [`hatchling`](https://hatch.pypa.io/dev/why/#build-backend), [`setuptools`](https://setuptools.pypa.io/en/latest/index.html), [`PDM`](https://pdm-project.org/en/latest/)

* A nice [post](https://medium.com/@anushkhabajpai/top-data-science-cheat-sheets-ml-dl-python-r-sql-maths-statistics-5239d4568225) with cheat-sheets for several `python` libraries (as well as `R` and ML)

* Load custom modules: one takes advantage of `sys.path` which is a list of directories where `python` looks for module.
    Suppose that you want to import module `myMod` which is in `/path/to`, then a typical call would be

  ``` python
  import sys
  sys.path.append('/path/to')
  # or...
  sys.path.insert(0, '/path/to')
  # Now one can import
  import myMod  # noqa: E402
  ```

  The comment to the import allows to avoid warnings / errors from linters if you use them

* Format strings: several ways are available, have a look [here](https://realpython.com/python-string-formatting/), but also [here](https://pyformat.info/) and to the [doc](https://docs.python.org/3.10/library/string.html#format-string-syntax)

  * Old-style, “`%`”: `'Hi, %s!' % 'Bob'`

    * `"Hi, %s! It's %s" % ('Bob','Alice')`

    * `"Hi, %(v1)s! It's %(v2)s" % {'v1':'Bob','v2':Alice'}`

  * New-style, `str.format()`: `'Hi, {}!.format('Bob')'`, `'Hi, {:s}!'.format('Bob')`

    * `"Hi, {0}! It's {1}".format('Bob','Alice')` (or `{<n>:s}` for instance))

    * `"Hi, {v1}! It's {v2}".format(v1='Bob',v2='Alice')` (or `{<var>:s}` for instance)

    * `d={'v1':'Bob','v2':'Alice'}; "Hi, {v1}! It's {v2}".format_map(d)` equivalent to above item

  * `f`-strings, `f'[.]'`: `who='Bob'; greet=f'Hi, {who}!'` (or `greet = f'Hi, {who:s}!'`)

    * `v1='Bob'; v2='Alice'; greet="Hi, {v1}! It's {v2}"`

    * Braces need to be escaped: e.g. `fr'{3}'` gives `3`, `fr'{{3}}'` gives `{3}`.
        Moreover, with variables:

      ``` python
      test = "TEST"
      print(f"That's a {test}")
      # That's a TEST
      print(f"That's a {{test}}")
      # That's a {test}
      print(f"That's a {{{test}}}") # 2 for escaping, 1 for variable
      # That's a {TEST}
      ```

  * Raw-strings: identified by `r`, the backslash is interpreted as backslash (automatically escaped).
    For instance, `'\n'` leads to a newline, `r'\n'` leads to `\n`.

  * Combine `f`- and `r`-strings: just use `fr'...'`

* Mutable vs. immutable types

  * **Mutable**: `list`, `dictionary`, `set`, `bytearray`, user-defined classes

  * **Immutable**: `int`, `float`, `decimal`, `complex`, `bool`, `string`, `tuple`, `range`, `frozenset`, `bytes`.

  * An example

    ``` python
    aList, aSet = [1, 2, 3], (1, 2, 3)
    print(id(aList), id(aSet))
    # 44045192 43989032
    aList += [4, 5]
    aSet += (4, 5)
    print(id(aList), id(aSet))
    # 44045192 30323024
    # The set ID changed!
    ```

* `pass`: does nothing.
    But it is useful as place holder

  ``` python
  class This:
    pass # Remember to write this
  ```

* `try ... expect` and alike: An example

  ``` python
  try:
      # Code here
  except:
      # If error happens in try zone, this code is run...
  else:
      # ... otherwise, if no exception caught, run this
  finally:
      # This code is always run, with or without exception
  ```

  * One can use several `except` zones to catch different exceptions

    ``` python
    except Exception_1:
        # If error of type Exception_1
    except Exception_2:
        # If error of type Exception_2
    except Exception:
        # If any other error type, except Keyboard interrupt
    ```

  * Print traceback with `traceback.format_exc()` from module `traceback`

* Variables and members, taken from [here](https://stackoverflow.com/questions/7969949/whats-the-difference-between-globals-locals-and-vars)

  * `globals()` always returns the dictionary of the module namespace.
    The dictionary typically contains all the variables defined in the *global* scope.

  * `locals()` always returns a dictionary of the current namespace.
    Basically, as above but with *local* scope.

  * `vars()` returns either a dictionary of the current namespace (if called with no argument, equivalent to `locals()`) or the dictionary of the argument (that is, let `a` be an instance of a class, then `vars(a)` would provide all the attributes, members and/or method, of `a`).

* Unpacking operators: `*` iterable unpacking, and `**` dictionary unpacking, see [here](https://geekflare.com/python-unpacking-operators/)

* Underscore and naming convention: see [here](https://dbader.org/blog/meaning-of-underscores-in-python) and [here](https://realpython.com/python-double-underscore/).
    Here is the gist of it:

  * Plain “`_`”: placeholder for unused arguments / returns

    ``` python
    lst = [1 for _ in range(3)]  # = [1, 1, 1]
    ```

    * It can be unpacked with `*` (see above)

      ``` python
      a = [1, 2, 3, 4, 5]
      first, *_, last = a
      print(first, last) # 1 5
      ```

  * *One* leading underscore, `_var`: Naming convention indicating a name is meant for internal use.
    Generally not enforced by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only.

  * *One* trailing underscore, `var_`: Avoid naming conflicts.

  * *Double* leading underscore, `__var`: Triggers name mangling when used in a class context.
    Enforced by the Python interpreter.
    The name of the class is added in order to avoid the variable being overridden by inheritance.

    ``` python
    >>> class Test:
    >>>     def __init__(self):
    >>>         self.__foo
    >>> dir(Test())
    ['_Test__foo']  # Plus others
    ```

  * *Double* leading *and* trailing underscore, `__var__`: Name mangling is not triggered.
    However, this convention is reserved to special methods, e.g., `__init__`, `__call__`

* [Generators](https://wiki.python.org/moin/Generators): Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
    This is faster than creating lists on purpose.
    Brief [intro](https://www.programiz.com/python-programming/generator).
    Generators do not *return*, they *yield*. An example

  ``` python
  def zero_or_square(n):
    for i in range(-n, n):
      if i <= 0:
        yield 0
      else:
        yield i**2

  for i in zero_or_square(5):
    print(i)
  ```

* Ternary operator:

  ``` python
  msg = "True" if condition else "False"
  ```

  or suppose that you have an argument which can be passed or not (hence in this case equal to `None`)

  ``` python
  msg = arg_msg or "Your message here"
  ```

* Default function arguments: if containers or complex types, prefer using `None` as default parameter then defining it inside the function.
    See [here](https://www.geeksforgeeks.org/default-arguments-in-python/).
    This allows to avoid the following (often unwanted) behaviour (it happens also with mutable containers such as dictionaries):

  ``` python
  def foo(l = [], a = 5):
    l.append(0)
    a += 1
    print(a, l)
  foo() # Prints: 6 [0]
  foo() # Prints: 6 [0,0]
  ```

* Classes:

  * The hidden members `__dict__` holds a dictionary with all the members of the class/instance.
    It’s basically equivalent to `vars` (see above)

  * Operations with members:

    * Get / Set: `getattr(<obj>, <mmbr>[, <dflt>])` / `setattr(<obj>, <mmbr>, <val>)`

    * Delete: `delattr(<obj>, <mmbr>)`

    * Interrogate for existence (works with methods too): `hasattr(<obj>, <mmbr>)`

  * Random stuff about classes (hidden) methods

    * `@staticmethod` vs `@classmethod`: some info [here](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)

    * `__init__(self[,args])`: creator

    * `__call__(self[,args])`: overload operator `( )`

    * `__getitem__(self, key)`: overload evaluation with operator `[ ]`, e.g. `a = obj[n]`

    * `__setitem__(self, key, val)`: overload assignment with operator `[ ]`, e.g. `obj[n] = a`

    * `__add__(self, other)`: overload operator `+`, see [here](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types).

      * You may overload also `-` with `__sub__`, `*` with `__mult__`, etc...

      * `a + b` is interpreted as `a.__add__(b)`.
        However, lets say that `a` is not an instance of your class, but `b` is.
        In this case, only be `b + a` work.
        In order to take into account also the Reverse case, define also `__radd__` (`__rsub__`,...).
        Most of the time, if the operation is symmetric, one can simply put `__radd__ = __add__`.

      * The in-place versions of the above mentioned operators are: `__iadd__` for `+=`, `__isub__` for `-=`,...

    * `__int__(self)`: overload cast `int(<n>)`. Same applies for `str`, `float`

      * The cast to `str` allows one to use function `print()` directly

    * `__eq__(self,other)`: overload `==`. Similarly, `__ne|lt|le|gt|ge__`

      * If `eq` not present, `==` is ensured by `is` (checks the ID)

      * As long as there is a `==`, you can use the `[not] in` keyword

* Printing colors: e.g.

  ``` python
  class Bcolors:
      HEADER = '\033[95m'
      OKBLUE = '\033[94m'
      OKCYAN = '\033[96m'
      OKGREEN = '\033[92m'
      WARNING = '\033[93m'
      FAIL = '\033[91m'
      ENDC = '\033[0m'
      BOLD = '\033[1m'
      UNDERLINE = '\033[4m'
  print(f'{Bcolors.FAIL}FAILED{Bcolors.ENDC}')
  ```

* Profiling: see [here](https://docs.python.org/3/library/profile.html), basically use `cProfile`.
    One can use it as script to profile another script:

  ``` bash
  python -m cProfile script.py
  ```

  * Options: `-s <stat>` sort by statistic `stat` (e.g., time, number of calls,...), `-o output.log` output file

* Memory profiling: [`memory_profiler`](https://github.com/pythonprofilers/memory_profiler)

* Copying in `python`, shallow- vs. deep-copy: [here](https://www.programiz.com/python-programming/shallow-deep-copy)

  * See [this SO answer](https://stackoverflow.com/a/46939443) for an example of create a method `copy` for a custom class

* Function arguments: have a look [here](https://www.python-course.eu/python3_passing_arguments.php)

  * *by-value* or *by-reference*? Basically if immutable *by-value*, otherwise *by-reference*. In fact, the real mode is *by object reference*!

  * Using `*` (star) and `**` double-star

  * ...similarly for `args` and `kwargs`: have a look [here](https://realpython.com/python-kwargs-and-args/)

  * Consider these examples

    ``` python
    def foo(a, *args, b=4, **kwargs):
        print(f"{a=}, {args=}, {b=}, {kwargs=}")
    foo(3           ) # a=3, args=(),    b=4, kwargs={}
    foo(3,5         ) # a=3, args=(5,),  b=4, kwargs={}
    foo(3,5,  6     ) # a=3, args=(5,6), b=4, kwargs={}
    foo(3,5,b=6     ) # a=3, args=(5,),  b=6, kwargs={}
    foo(3,5,b=6,c=10) # a=3, args=(5,),  b=6, kwargs={'c': 10}

    def bar(a, b, *args, **kwargs):
        print(f"{a=}, {args=}, {b=}, {kwargs=}")
    bar(3           ) # Error: b required
    bar(3,5         ) # a=3, args=(),    b=5, kwargs={}
    bar(3,5,  6     ) # a=3, args=(6,),  b=5, kwargs={}
    bar(3,5,b=6     ) # Error: multiple b
    bar(3,b=6,5     ) # Error: positional after keyword
    bar(3,  6,5     ) # a=3, args=(5,),  b=6, kwargs={}
    bar(3,  6,5,c=10) # a=3, args=(5,),  b=6, kwargs={'c': 10}
    bar(3,  6,  c=10) # a=3, args=(),    b=6, kwargs={'c': 10}
    ```

* `python` is nice, `C` is better: hence why not [`Cython`](https://cython.readthedocs.io/en/latest/index.html)?

* Dealing with `zip` files: module [`zipfile`](https://docs.python.org/3/library/zipfile.html).
    See a discussion [here](https://realpython.com/python-zipfile/).
    For instance, use without extracting

  ``` python
  with zipfile.ZipFile('my_file.zip', mode='r') as archive:
    # Get list of files in archive
    fl = archive.namelist()
    for f in fl:
      with open(f, 'r') as op_f:
        # Do something
  ```

* Run shell commands from `python` script

  * `os.system('echo Ciao')`

  * It is advised to used the
    [`subprocess`](https://docs.python.org/3/library/subprocess.html) module and its `run` function or the more flexible `Popen` class

    * One should provide a list of strings which, joined, form the command.
        One might use [`shlex`](https://docs.python.org/3/library/shlex.html) to avoid errors

        ``` python
        list_dir = subprocess.Popen(["ls", "-l"])
        # or
        list_dir = subprocess.Popen(shlex.split("ls -l"))
        ```

    * Other arguments:

      * `cwd`: working directory, otherwise the current one

      * `env`: a dictionary to be used as system environment. For instance, to update to `PATH`

        ``` python
        import os
        mod_env = os.environ.copy()
        mod_env["PATH"] += os.pathsep + "/path/to/foo"
        subprocess.Poen(["echo", "$PATH"], env=mod_env)
        ```

      * `shell`: whether to run the command through the shell.
        That is to say, with true, `Popen(["ls"])` calls `/bin/sh -c ls` (notice the call to default shell).
        Default is false.

      * `stdin`, `stdout`, `stderr`: specify the executed program’s standard input, standard output and standard error file handles, respectively.
        Valid values are `None`, `PIPE`, `DEVNULL` (constants defined in the module), an existing file descriptor (a positive integer), and an existing file object with a valid file descriptor.
        With the default settings of `None`, no redirection will occur.
        `PIPE` indicates that a new pipe to the child should be created.
        `DEVNULL` indicates that the special file `os.devnull` will be used.
        Additionally, `stderr` can be `STDOUT`, which indicates that the `stderr` data from the child process should be captured into the same file handle as for `stdout`. See below for examples.

      * If `encoding` or `errors` are specified, or `text` (also known as `universal_newlines`) is true, the file objects `stdin`, `stdout` and `stderr` will be opened in text mode using the encoding and errors specified in the call or the defaults for `io.TextIOWrapper`.

    * These [two](https://stackoverflow.com/questions/13332268/how-to-use-subprocess-command-with-pipes) [examples](https://stackoverflow.com/questions/295459/how-do-i-use-subprocess-popen-to-connect-multiple-processes-by-pipes) address the piping. For instance, one can store the output in a `PIPE` object so that it can be fed to a second command

        ``` python
        ps = subprocess.Popen(('ps', '-A'), stdout=subprocess.PIPE)
        output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
        ```

    * Mind that, differently from `os.system`, `subprocess` does not wait for the command to finish, hence the python script continues.
        In order to wait use the `wait` method.
        Another way to obtain that is to use `subprocess.run`, see below.

        ``` python
        list_dir = subprocess.Popen(["ls", "-l"])
        list_dir.wait()
        ```

  * `subprocess.run`: similar to `Popen` but directly run the command and wait for its completion.

    * Arguments:

      * All those of `Popen`

      * `capture_stdout`: store the output (better to use this in combination with `text=True`)

        ``` python
        # cmd = [...]
        res = subproces.run(cmd, capture_output=True, text=True)
        # Add .decode() in text=False
        print("STDOUT:", res.stdout)
        print("STDERR:", res.stderr)
        ```

      * `check`: whether to check if the command completes.
        If not, it raises a `python` exception

* [`numpy`](https://numpy.org/doc/stable/index.html) (In the examples below we suppose it has been loaded as `np`)

  * Products:

    * An [introduction](https://mkang32.github.io/python/2020/08/30/numpy-matmul.html)

    * The usual *star* product, “`*`”, alias of `np.multiply`, acts element-wise

      ``` python
      a = numpy.array([1, 2, 3])
      b = numpy.array([4, 5, 6])
      a * b  # Gives [4, 10, 18]
      ```

    * [`np.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html)

      * For 1D arrays, it is the usual dot (or inner) product.
        One can also use `np.inner`

        ``` python
        numpy.dot(a, b)  # Gives 32
        # or
        a.dot(b)
        ```

      * For 2D arrays, it is the usual matrix-matrix or matrix-vector product

        ``` python
        A = np.random.rand((2,2))
        assert np.allclose(A, np.dot(A, np.eye(2)))
        ```

      * In higher dimensions, if `a` is an $`N`$-D array and `b` is an $`M`$-D array (where $`M\geq2`$), it is a sum product over the last axis of `a` and the second-to-last axis of `b`: $`dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])`$

    * Operator `at`, “`@`”, alias of `np.matmul` is the usual matrix-matrix or matrix-vector product

      ``` python
      A = np.random.rand((2,2))
      assert np.allclose(A, A @ np.eye(2))
      ```

    * [`np.outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html): outer product of two vector $`(outer(a, b))_{ij} = a_i b_j`$

    * [`np.einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum): Evaluates the Einstein summation convention on the operands

    * [`np.vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html): dot product for arrays but with complex conjugate

    * [`np.tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html): dot product for tensors

  * `numpy` and the `axis` keyword

    * TL;DR: `axis=0` acts over a column, `axis=1` over a row. Hence,

      ``` python
      x=numpy.ones([3,4])
      x.sum(axis=0) # Gives [3, 3, 3, 3]
      x.sum(axis=1) # Gives [4, 4, 4]
      ```

    * The value of `axis` indicate on which dimension the operation is done (in a certain sense, which direction collapses after the
      operation).

    * The value correspond to the index of the direction in the result of `size()`, for instance.
        Think about it: above `x` was a 3-rows and 4-columns matrix.
        Then, `x.size() # =(3,4)`

  * From matrix to array:

    * `flatten` returns a copy

    * `ravel` does it in place

  * `numpy` and memory: here is an interesting [article](https://pythonspeed.com/articles/numpy-memory-views/)

  * To complete the above item, see the [official doc](https://numpy.org/doc/stable/user/basics.copies.html) about views and copies

  * Sorting & alike

    * Get a indexes with `np.argmin` and `np.argsort`

  * Types

    * Change type with `.astype(<type>)`.
        It usually copy the array, hence allocating memory, however one can avoid this by adding arguments `copy=False`

    * A `np` array can have type string, however all the elements have to have the same length.
        If it is not the case, one may try generic type `object`

* [`functools`](https://docs.python.org/3/library/functools.html): functions for callable objects (e.g. functions)

  * `partial(foo, *args, **kwargs)`: Return a new partial object which when called will behave like `foo` called with the positional arguments `args` and keyword arguments `kwargs`.

    ``` python
    def foo(a,b): print(f'a:{a}, b:{b}')
    ptf_a = partial(foo, 3) # argument a is 3
    ptf_a(4) # print a:3, b:4
    ptf_b = partial(foo, b=3) # argument b is 3
    ptf_b(4) # print a:4, b:3
    ```

    * For class methods use `partialmethod`

  * `reduce(foo, iter)`: reduce iterable `iter` by function `foo`.
    For instance if `foo` is addition, then reducing will be equivalent to accumulate

* [`timeit`](https://docs.python.org/3/library/timeit.html): useful built-in module to measure performances

  * `timeit.timeit(stmt='pass', setup='pass', number=1000000, globals=None)`: run `stmt` `number` times after having run `setup` as a pre-process step and return the elapsed time

    * Time in seconds

    * Time include all the `number` iterations

    * Suppose that you want to measure function `foo.bar(baz))` from module `foo` and which needs a parameter `baz`.
        Then, should import the module and create the parameter in the setup:

      ``` python
      setup = """
      import foo
      baz = foo.Baz()
      """
      timeit.timeit("foo.bar(baz)", setup=setup)
      ```

    * If you want to use objects inside the same scope, pass the current globals

      ``` python
      def foo(n): return list(range(n))
      N = 200
      timeit.timeit("foo(N)", globals=globals())
      ```

  * `timeit.repeat(<as above>, repeat=5)`: call `timeit` `repeat` times

    * Return a list of length `repeat` with the result of each `timeit` call

    * See this note from the developers:

       > “It’s tempting to calculate mean and standard deviation from the result vector and report these.
       > However, this is not very useful.
       > In a typical case, the lowest value gives a lower bound for how fast your machine can run the given code snippet; higher values in the result vector are typically not caused by variability in Python’s speed, but by other processes interfering with your timing accuracy.
       > So the min of the result is probably the only number you should be interested in.
       > After that, you should look at the entire vector and apply common sense rather than statistics.

  * It can be used as command-line tool: `python3 -m timeit [OPT] [stmt]`

    * `-s`: setup

    * `-n`: number

    * `-r`: repeat

    * `-u`: unit

  * An idea (notice: it evaluates the statement and return what it gets):

    ``` python
    REPEAT = 20
    N_LOOPS = 10_000

    def run_perf_analysis_eval(
        statement, label, repeat=REPEAT, n_loops=N_LOOPS
    ):
        measures = timeit.repeat(
            statement, repeat=repeat,
            number=n_loops, globals=globals(),
        )
        measures = np.array(measures) / n_loops
        print(
            f"* {label:15}: {np.mean(measures):>5.1f} mus"
            f" +- {np.std(measures):>6.2f} mus,"
            f" in [{np.min(measures):>5.1f},"
            f" {np.max(measures):>5.1f}]"
        )
        return eval(statement), measures
    ```

* [`itertools`](https://docs.python.org/3/library/itertools.html): functions for creating iterators for efficient looping

  * `reduce(foo, iter)`: as `map` but will star elements of `iter` (that is `*iter[0]`)

* [`tkinter`](https://docs.python.org/3/library/tkinter.html): manage windows and dialogue

  * [Calendar](https://tkcalendar.readthedocs.io/en/stable/index.html)

* Concurrency, Parallelization, Threading, Asynchronous programming: Couple of resources:

  * An [intro](https://www.machinelearningplus.com/python/parallel-processing-python/) with simple examples.

  * Overviews of [concurrency](https://realpython.com/python-concurrency/) and [asynchronous programming](https://realpython.com/async-io-python/)

  * [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) module.

    * Get ID of pool workers: [here](https://stackoverflow.com/questions/10190981/get-a-unique-id-for-worker-in-python-multiprocessing-pool)

    * Use proxy-objects and `Manager`’s if you want objects to be modified inside the parallel functions (for instance if you want to append to lists,...)

  * [`threading`](https://docs.python.org/3/library/threading.html) module.

  * [`asyncio`](https://docs.python.org/3/library/asyncio.html) module.

* `matplotlib`

  * An example showing the basics

    ``` python
    x  = np.linspace(0,1,20)
    y1 = 2*x + 1
    y2 = x**2
    plt.plot(x, y1, marker="o", color = "red", linestyle='dashed')
    plt.plot(x, y2, marker="*", color = "green") # Same plot
    plt.legend([r"$y=2*x+1$", r"$y=x^2$"])
    # or directly, then just called legend
    plt.plot(x, y1, label=r"$y=2*x+1$")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(r"Title with LaTeX $\alpha$")
    plt.tight_layout()
    plt.savefig("myfig.jpg", dpi=400) # dpi ~ quality
    # or
    plt.savefig("myfig.png", dpi=400, transparent=True)
    # consider also...
    plt.semilogx(...)
    plt.semilogy(...)
    plt.loglog(...)
    ```

  * List of accepted key for `rcParams` [here](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams)

  * `matplotlib.ion()` switch the interaction with the plot on, so that `plt.plot()` is not blocking and the plot can be kept and redrawn multiple times.
    This of course works in a plot environment, if you use it on a script the plot will disappear as soon as the script reaches its end.

  * Equal unit-length for x and y-axis: `plt.gca().set_aspect('equal', adjustable = 'box')`

  * Remove axis (no axis, no ticks, no labels, etc): `ax.axis('off')`

  * Every names color [here](https://matplotlib.org/stable/gallery/color/named_colors.html)

  * 3D plots.
    A nice introduction can be found [here](https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html).
    To activate 3D-plotting (scatter, surface, mesh plot or any other) the axis should be called with `projection='3d'` which should be imported as follows: `from mpl_toolkits import mplot3d`

  * Interactive plots: [legend picking](https://matplotlib.org/stable/gallery/event_handling/legend_picking.html), [grids moving with the mouse](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html), in general, checkout the whole [event handling](https://matplotlib.org/stable/gallery/event_handling/index.html) session

* Argument parsing: [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse)

* Working with datasets:

  * [`pandas`](https://pandas.pydata.org/docs/user_guide/10min.html)

  * [`xarray`](http://xarray.pydata.org/en/stable/user-guide/index.html)

* `pandas`

  * Access data: `df.loc[row,col]` works with labels.
    Slices, arrays, booleans are accepted. `df.at[row,col]`, same but can access a scalar value only (no slices), hence its faster.
    There are also equivalent version that works with index: `df.iloc[]`, `df.iat[]`.
    See [here](https://stackoverflow.com/questions/28754603/indexing-pandas-data-frames-integer-rows-named-columns) for hybrid access.

    * Pay attention to whether the function returns a view or a copy, see [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-view-versus-copy)

  * Build dataframe from dict of dict: just pass it to default constructor, or use `from_dictionary`, see [here](https://stackoverflow.com/questions/33157522/create-pandas-dataframe-from-dictionary-of-dictionaries)

* Progress bar: [`tqdm`](https://github.com/tqdm/tqdm#manual)

  * [here](https://www.analyticsvidhya.com/blog/2021/05/how-to-use-progress-bars-in-python/) is a nice show of what is capable

  * Standard usage: `for i in tqdm.tqdm(range(6))`, `for l in tqdm.tqdm(my_list)`

  * Manual usage, with `with`: `with tqdm.tqdm(...) as bar: [iterate] bar.update()`.
    In this case you have to update manually

  * It could deal with parallel code, it uses a wrapper to `multiprocessing`, have a look [here](https://tqdm.github.io/docs/contrib.concurrent/)

* Statistics and data analysis:

  * `scipy.stats`: hypothesis testing and all the basics.

  * `statsmodels`: regressions.

  * [`seaborn`](https://seaborn.pydata.org/introduction.html): powerful data visualization tool.

* Do you know about `module`, as the command used to manage optional programs and modification of environment via modulefiles?
    There exists a python wrapper around it, so that you can use it.

  * [An initialization](https://modules.readthedocs.io/en/latest/module.html#examples-of-initialization) for python is needed:

    ``` python
    import os
    exec(open("/usr/share/Modules/init/python.py").read(), globals())
    ```

  * After that, you can use it as always.
    Hence, the following call will update the environment according to the chosen module

    ``` python
    module("load", "my_package")
    ```

  * The actual command are run in a subprocess, hence, it won’t be possible to keep the output (at least, I couldn’t).
    That is, running the line below will print to screen but you won’t be able to captured it

    ``` python
    module("show", "my_package")
    ```

## Data structures

Let us discuss the native data structures.
The [manual](https://docs.python.org/3/library/stdtypes.html) of all the predefined types.

### General intro

The most common types (and how to create them) are:

* Dictionaries: `d = {'key':item}`

* Lists: `l = [1, 2]`

* Tuples: `t = (1, 2)`. ATTENTION: tuples are similar to lists, however they are immutable, for instance, you won’t be able to do: `t[0] = 2`

* Sets: `s = {1, 2}`. Unordered, unique elements.

  * Frozen sets: `f = frozenset{[1, 2]}`. As sets, but immutable.

### Access and indexing

* Operator square brackets, 0-based, separate dimensions with commas “`,`”

* Negative indices means starting from the end, hence `a[-1]` is the last element

* `a[start:end:range]`: `a[i:j:n]` gives every `n`-th elements starting from `i` to `j`. If `i` (resp. `j`) is omitted, defaults to first, `0`, (resp. last, `-1`) element. E.g.: `a[::2]` yields every other element.

* `a[start:end]`: `a[i:j]`: elements from `i` to `j`. If `i` (resp. `j`) is omitted, defaults to first, `0`, (resp. last, `-1`) element

* If `n` is negative, then `i` should be greater then `j` and the order is reversed.
    Some examples:

  * `a[::-1]` list in reversed order

  * `a[-1:-5:-1]` last five elements in reversed order

  * `a[10:0:-2]` (equivalent to `a[10::-2]`, notice `0` omitted): from tenth to first element

* “`:`”: everything. `a[:,n]`: the `n`-th column

* Use objects `slice` to build indexing instances:

  * `slice(N)`: from beginning to `N`, equivalent to “`:N`”

  * `slice(N, M)`: from `N` to `M`, equivalent to “`N:M`”

    * `slice(None, M)`: equivalent to `slice(M)`

    * `slice(N, None)`: equivalent to “`N:`”

  * `slice(N,M,q)`: from `N` to `M` but only every `q` elements, equivalent to “`N:M:q`”

    * Usage of `None` instead of `N` and/or `M` leads to the same behaviour as the item above

Dictionaries are different since they work with a hash table and on can access the elements with the related key.

### Lists

Lists, let `l` be a list of natural integers for the sake of simplicity (notation: `i` stands for index, `n` for natural integer)

* Insertion, elimination: `l.append(n)`, `l.insert(i,n)` `l.remove(n)`, `l.pop(i)` (remove `i`-th element, default 0). Methods `append` and `remove` return `None`.

* It accepts `l.max()`

  * Argmax:

    ``` python
    index_max = max(range(len(l)), key = l.__getitem__)
    # or
    from operator import itemgetter
    index_max = max(range(len(l)), key = itemgetter)
    ```

* Loop both on indices and values: `for i, v in enumerate(l):`

* Initialize (list comprehension): `l = [0 for _ in range(3)]`

* Search for: `l.index(n)`

* Reverse: `l.reverse()` in-place, `l[::-1]`

* Sorting: `l.sort()` in-place, `sorted(l)` returns a new list

  * Argsort:

    ``` python
    l = sorted(range(len(l)), key = l.__getitem__)
    # or
    from operator import itemgetter
    l = sorted(range(len(l)), key = itemgetter)
    ```

* List comprehension: [here](https://www.programiz.com/python-programming/list-comprehension).

### Dictionaries

Have a look [here](https://realpython.com/python-dicts/)

* In recent versions, they are ordered

* Create: empty `d = {}` or `d = dict()`; not empty `d={key:value}` or `dict()` plus list of tuples. `key` has to be hashable and `value` can be of any type.

* Add new item or update existing:

  * `d[key] = value`

  * `d.update(<>)`: accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two).
    If keyword arguments are specified, the dictionary is then updated with those key/value pairs: `d.update(red=1, blue=2)`

* Access: by key `d[k]=val`; by index `d[2]=val`; `d.get(<key>[, <default>])` returns the value if `k` is a key (otherwise, `default`)

* `d.items()`: returns a list of key-value pairs

* `d.keys()`: returns a list of keys

* `d.values()`: returns a list of values

* `d.pop(k,[default])`: If `k` is in the dictionary, removes it and return its value, else return `default`

* `d.clear()`: remove everything

* `for k in d` loops over keys

### Sets

Operation and stuff (see [here](https://realpython.com/python-sets/))

* Union (any element): `s1 | s2` or better `s1.union(s2)`

* Intersection (elements in both): `s1 & s2` or `s1.intersection(s2)`

* Difference (elements in `s1` only): `s1 - s2` or `s1.difference(s2)`

* Symmetric difference (not in intersection): `s1 ^ s2` or `s1.symmetric_difference(s2)`

* And many others: `s1.isdisjoint(s2)`, `s1.issubset(s2)` or `s1 <= s2` or `s1 < s2` for proper subset...

### Tuples

* Tuples are immutable

* Addition extends tuples

    ``` python
    (1, 0) + (0,-1) # Gives (1, 0, 0, -1)
    ```

* Tuples have support for comparisons and it works element-wise.
    Hence, a “`t1` greater than `t2`” (for two-elements tuples) works roughly as follows:

    ``` python
    def tuple_gt(t1, t2):
        if t1[0] > t2[0]:
            return True
        elif t1[0] < t2[0]:
            return False
        else:
            # Here t1[0] = t2[0]
            return t1[1] > t2[1]
     ```

## `argparse`

Have a look at the official [documentation](https://docs.python.org/3/library/argparse.html) and [tutorial](https://docs.python.org/3/howto/argparse.html).
Otherwise, below a very basic example:

``` python
import argparse

# CREATING A PARSER
parser = argparse.ArgumentParser(
  # Optional
  prog="ProgName",
  usage="Describe the usage",
  desciption="Description of the program",
  epilog="Test displayed after argument help",
)

# ADD ARGUMENTS
# Help option added by default
# Positional argument
parser.add_argument(
  "FOO",  # Name
  help="A nice little foo",  # Description of option
)
# Flag argument (mind the name starts with -)
# Commonly used for optional argument
parser.add_argument(
  "-t", "-T",  # short name
  "--test", "--Test",  # Full name
  dest="myTest",  # Name of the member in which the value will be stored
  help="Activate test mode",  # Description of option
)

# PARSING ARGUMENTS
args = parser.parse_args()
# or
import sys
args = parser.parse_args(sys.argv[1:])
# Actually, any sequence of strings
args = parser.parse_args(["--test"])

# USING STORED ARGUMENTS
print(args.myTest)
```

[Options for `add_argument`](https://docs.python.org/3/library/argparse.html#quick-links-for-add-argument) (they are all optional):

* `dest`: Specify the attribute name used in the result namespace.
    It can be the same for more than one argument.

* `help`: Help message for an argument.

* `required`: Indicate whether an argument is required or optional.

* `nargs`: Number of times the argument can be used. Valid options:

  * `N` (an integer): `N` options will be consumed and gathered into a list.

  * `"?"`: One argument will be consumed from the command line if possible, and produced as a single item. If no command-line argument is present, the value from default will be produced.

  * `"*"`: All command-line arguments present are gathered into a list.

  * `"+"`: As `"*"`, but raises an error if no argument is found.

* `default`: Default value used when an argument is not provided (default is `None`).

* `const`: Store a constant value.

  * It is required by some `nargs` and `action`.

  * When `nargs="?"`, it’s the value that will taken when the argument is passed but without a value.

* `choices`: Limit values to a specific set of choices.
    E.g.: `["one", "un", "uno"]`.

* `type`: Automatically convert an argument to the given type.
    Valid options:

  * Standard types, e.g., `int`, `float`,...

  * A callable function that returns a value or raises `argparse.ArgumentTypeError` if argument is not valid.

  * A `argparse.FileType` object (for file IO).

* `action`: Specify how an argument should be handled: Valid options:

  * `"store"`: Store the argument’s value (the default).

  * `"store_const"`: Store the argument specified by `const` keyword; commonly used with optional arguments that specify some sort of flag.

  * `"store_true"` and `"store_false"`: These are special cases of `store_const` used for storing the values `True` and `False` respectively

  * `"append"`: This stores a list, and appends each argument value to the list.
    It is useful to allow an option to be specified multiple times.

  * `"append_const"`: This stores a list, and appends the value specified by the `const` keyword argument to the list.

  * `"count"`: This counts the number of times a keyword argument occurs.

  * `"help"`: This prints a complete help message for all the options in the current parser and then exits.

  * `"version"`: This expects a `version=` keyword argument in the `add_argument` call, and prints version information and exits when invoked.

  * `"extend"`: This stores a list, and extends each argument value to the list.

* `metavar`: Alternate display name for the argument as shown in help

Tips&Tricks:

* Mutually exclusive arguments: create a related group

  ``` python
  parser = argparse.ArgumentParser()
  mutEx = parser.add_mutually_exclusive_group()
  mutEx.add_argument("--foo")
  mutEx.add_argument("--bar")
  ```

* Sub-parsers:

  ``` python
  # create the top-level parser
  parser = argparse.ArgumentParser(prog='PROG')
  parser.add_argument('--foo', action='store_true', help='foo help')
  subparsers = parser.add_subparsers(help='sub-command help')

  # create the parser for the "a" command
  parser_a = subparsers.add_parser('a', help='a help')
  parser_a.add_argument('bar', type=int, help='bar help')

  # create the parser for the "b" command
  parser_b = subparsers.add_parser('b', help='b help')
  parser_b.add_argument('--baz', choices='XYZ', help='baz help')
  ```

* Parse only known arguments

  ``` python
  parser = argparse.ArgumentParser()
  parser.add_argument('--foo', action='store_true')
  parser.add_argument('bar')
  parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
  # Gives (Namespace(bar='BAR', foo=True), ['--badger', 'spam'])
  ```

* `default` vs. `const`: Consider the following 3 examples (mind the presence or absence of `default` and `const` in the parser definition)

  ``` python
  p = argparse.ArgumentParser()
  p.add_argument(
      "-f",
      dest="f"
      nargs="?",
      default=4,
  )
  # Not passed
  a = p.parse_args([])
  print(a.f) # 4 (default)
  # Passed but no value
  a = p.parse_args(["-f"])
  print(a.f) # None (const)
  a = p.parse_args(["-f", "12"])
  print(a.f) # 12
  ```

  ``` python
  p = argparse.ArgumentParser()
  p.add_argument(
      "-f",
      dest="f"
      nargs="?",
      const=8,
  )
  # Not passed
  a = p.parse_args([])
  print(a.f) # None (default)
  # Passed but no value
  a = p.parse_args(["-f"]
  print(a.f) # 8 (const)
  a = p.parse_args(["-f", "12"])
  print(a.f) # 12
  ```

  <div class="center">

  ``` python
  p = argparse.ArgumentParser()
  p.add_argument(
      "-f",
      dest="f"
      nargs="?",
      default=4,
      const=8,
  )
  # Not passed
  a = p.parse_args([])
  print(a.f) # 4 (default)
  # Passed but no value
  a = p.parse_args(["-f"])
  print(a.f) # 8 (const)
  a = p.parse_args(["-f", "12"])
  print(a.f) # 12
  ```

  </div>

* More than one argument with the same destination:

  ``` python
  p = argparse.ArgumentParser()
  p.add_argument("-t", dest="boolean", action="store_true")
  p.add_argument("-f", dest="boolean", action="store_false")
  a = p.parse_args(["-t"])
  print(a.boolean) # True
  a = p.parse_args(["-f"])
  print(a.boolean) # False
  a = p.parse_args(["-f", "-t"])
  print(a.boolean) # True (last one prevails)
  ```

## `os`

Some useful members and functions of `os`:

* `os.pardir`: when used in paths, what stands for parent directory, that is, “`..`”

* `os.sep`: when used in paths, what is used for separating directories, e.g., in Unix “`/`”

* `os.pathsep`: when used in paths, what is used for separating each parts of search paths (e.g., `PATH`), e.g., in Unix “`:`”

* `os.linesep`: what signifies line termination, e.g., “`\n`” in Unix and “`\r\n`” on Windows

* `os.path.join`: join paths together

## `pathlib`

[`pathlib`](https://docs.python.org/3/library/pathlib.html) and `Path`: filesystem paths.
Similarities and differences w.r.t. `os` module [here](https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module).
Examples below

``` python
from pathlib import Path
Path()  # .
p = Path("path")
# Operator / overloaded
foo = p / "to" / "foo.py"  # path/to/foo.py
# Some functions
Path.cwd(), Path.home()
foo.exists(), foo.is_dir(), foo.is_file(), foo.is_symlink()
# Properties
foo.parts  # ("path", "to", "foo.py")
foo.name  # foo.py == os.path.basename == bash basename
foo.parent  # path/to == os.path.dirname == bash dirname
foo.parent.parent  # path
foo.parents[1]  # path, as above
foo.suffix  # .py
tgz = Path("t.tar.gz")
tgz.suffix  # ".gz"
tgz.suffixes  # [".tar", ".gz"]
foo.stem  # foo final component without suffix
foo.match("*.py")
foo.relative_to(other)
foo.with_suffix(".txt")  # path/to/foo.txt
foo.open()
foo.rename("new.py"), foo.replace("new.py")
# Similarly with_stem(), with_name()
drc = Path("a/directory")
drc.glob("*.py")
for child in drc.iterdir(): pass
# Path as string
str(foo), f"{foo}"
# Consider this file tree
# dir
#   |_ foo
#   |    |_ toto
#   |    |_ bar.py
#   |_ __pycache__
#   |    |_ ...
#   |_ baz.txt
for root, dirs, files in Path("dir").walk():
    print(f"Dir {root} contains",
          f"sub-dirs {dirs},",
          f"files {files}")
    if "__pycache__" in dirs:
        dirs.remove("__pycache__")
# Dir "dir" contains sub-dirs ["foo"] and files ["baz.txt"]
# Dir "dir/foo" contains sub-dirs ["toto"] and files ["bar.py"]
# Dir "dir/foo/toto" contains sub-dirs [] and files []
```

## `re`, regex’ing

Base notions and various tips:

* [Official page](https://docs.python.org/3/library/re.html)

* Main functions:

  * `re.search(pattern, string)`: Search *anywhere* in the string.

  * `re.match(pattern, string)`: Search at the *beginning* of the string.

  * `re.fullmatch(pattern, string)`: The *whole* string should math the pattern.

  * `re.sub(pattern, repl, string)`: Replace the pattern with the alternative text.

  * The functions take a key argument for flags. E.g.:

    ``` python
    # Case-insensitive
    re.search(ptrn, string, flag=re.I)
    # Multi-line
    re.search(ptrn, string, flag=re.M)
    ```

* One can compile a regex in advance, then use the usual functions:

  ``` python
  foo_re = re.compile("foo")
  foo_re.search("Foo foo bar")
  ```

* `re.escape(pattern)`: escape all the ambiguous characters

  ``` python
  foo_re = re.compile(re.escape("/foo.bar"))
  ```

* Matches&Groups: The above-mentioned function return a *match* object

  * Access full match and groups with brackets

    ``` python
    m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    m[0]  # The entire match
    # 'Isaac Newton'
    m[1]  # The first parenthesized subgroup.
    ```

  * Access groups with group ad-hoc function:

    ``` python
    m.group(0)  # The entire match
    # 'Isaac Newton'
    m.group(1)  # The first parenthesized subgroup.
    # 'Isaac'
    m.group(1, 2)  # Multiple arguments give us a tuple.
    # ('Isaac', 'Newton')
    ```

  * Access groups with names: one should use a special constructor `(?P<foo>pattern)` (yes, angle brackets `<...>` are necessary).

    ``` python
    m = re.match(
    r"(?P<name>\w+), (?P<surname>\w+)",
    "Isaac Newton, physicist",
    )
    m.group("name")
    # 'Isaac'
    m.group("surname")
    # 'Newton'
    ```

  * All the groups as tuple: `m.groups(default=None)` (default value is for groups that did not participate to the match).

  * All the groups as dict: `m.groupdict(default=None)`, to use in case where one gave name to a group (see `name` and `surname` above).

## Files&Co

Open’n’Close

* Open: `f = open('path/to/file.txt', 'w')`

  * The second argument is the mode.
    For instance, `w` for writing (creates file if it doesn’t exist), `a` for appending (creates file if it doesn’t exist), `r` for reading (error if file doesn’t exist), `x` for creating a file (error if file already exists), `t` for using text mode (default) or `b` for using binary mode.
    For instance, for reading in binary use `'rt'`

* Close `f.close()`

* Use the `with` construction which closes the file by itself

    ``` python
    with open('path/to/file.txt', 'w') as f:
        # [do stuff]
    ```

Reading

* Read one line and store it: `line = f.readline()`

* Read *all* the lines and store them in a list: `lines = f.readlines()`

* Read the content and store it in a string: `cont = f.read()`

  * Pass a number to specify how many characters to read: `c = f.read(5)`

* Conveniently loop line by line: `for line in f:` (also `enumerate`, for instance)

Writing

* Write a string: `f.write(s)`

* Write a list of strings: `f.writlines(l)`

  * It does NOT automatically add the newline after each string

## Type hints

One can provide types to variable, arguments and return values of a function.
These hints **won’t** be used by `python` (e.g. it isn’t `C`).
Type hints are for developers and for IDEs: basically they make the code simpler to read (very useful when developing code to which other user will interface) and help IDEs to infer types of objects in order to offer better prediction.

* To go further: [here](https://stackoverflow.com/a/32558710), [here](https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html)

* Use module [`typing`](https://docs.python.org/3/library/typing.html)

* For built-in structures, in older versions use, e.g., `Dict`, `Tuple`, `List`; otherwise in newer version just standard is accepted, e.g., `dict[str, str]`

  * For more generic constructions, one can use `Mapping` and `Sequence` from `collections.abc` for, respectively, `dict` and `list`

* `Any` is the joker value, it’s compatible with every type.

* For more than one possible types, use `Union`.
    In recent versions, “`|`” (pipe, like in *or*) is accepted as well

* For optional arguments that can assume `None` or another type, use `Optional`

* An example below

  ``` python
  # The following is deprecated in > 3.10,
  # just use plain list, dict
  from typing import List, Dict
  # Variables: the followings are equivalent
  n: int = 10
  #
  n: int
  n = 10
  #
  n = 10 # type: int # Another comment
  #
  l : List[int] = list(range(5))
  #
  d : Dict[str, int] = {'Brazil': 5, "Italy": 4, "France": 2}
  # Functions
  def fib(n : int, label : str) -> int:
  a, b = 0, 1
  while b < n:
  a, b = b, a + b
  print(label)
  return a
  ```

* Aliases and custom types:

  * define them with `TypeAlias` (or simply `type` in python $\geq3.12$)

    ``` python
    from typing import TypeAlias
    Vector: TypeAlias = list[float]
    # Actually TypeAlias is not necessary
    Vector = list[float]
    # or in python >= 3.12
    type Vector = list[float]
    ```

  * Above are aliases, but one can create also new type which will be regarded as a subclass of the parent type

    ``` python
    from typing import NewType
    UserId = NewType('UserId', int)
    def foo(uid: UserId) -> None:
    # Do something
    foo(UserId(123))  # OK
    foo(123)  # KO
    ```

* Annotating *self* in classes methods: see [here](https://stackoverflow.com/a/33533514).
    Basically: in python $`\geq3.11`$ use `typing.Self`; in python $`\geq3.7`$ future annotations; in old python use strings

  ``` python
  # python 3.11+
  from typing import Self
  class Foo:
  def __add__(self: Self, other: Self) -> Self:
      # In this case, it is better to do something like the
      # following because one has to be sure to return
      # _exactly_ the same type as self
      return type(self)(...)
  # python 3.7+
  from __future__ import annotations
  class Bar
  def __add__(self: Bar, other: Bar) -> Bar:
      return ...
  # Old pythons, use string
  class Baz
  def __add__(self: "Baz", other: "Baz") -> "Baz":
      return ...
  ```

* Functions&Callables: use `typing.Callable` or `collections.abc.Callable`

  ``` python
  from collections.abs import Callable
  # A function that takes a string and a integer and
  # returns a string
  foo: Callable[[str, int], str]
  ```

* Generators: use `Generator[YieldType, SendType, ReturnType]`.
    Typical example:

  ``` python
  from collections.abs import Generator
  def infinite_stream(start: int) -> Generator[int, None, None]:
  while True:
      yield start
      start += 1
  # or also
  from collections.abc import Iterator
  def infinite_stream(start: int) -> Iterator[int]:
  while True:
      yield start
      start += 1
  ```

* Generic functions (sort of template): two ways, one direct, the other relies on `Typevar`

  ``` python
  from collections.abc import Sequence
  # Function is generic over the TypeVar "T"
  def first[T](l: Sequence[T]) -> T:
  return l[0]

  # Second way
  from typing import TypeVar
  # Declare type variable "U"
  U = TypeVar('U')
  # Function is generic over the TypeVar "U"
  def second(l: Sequence[U]) -> U:
  return l[1]
  ```

* Type for types: `typing.Type` or simply `type`

  ``` python
  a = 3         # Has type ``int``
  b = int       # Has type ``type[int]``
  c = type(a)   # Also has type ``type[int]``
  #
  class User: ...
  class ProUser(User): ...
  class TeamUser(User): ...

  def make_new_user(user_class: type[User]) -> User:
  # ...
  return user_class()

  # OK
  make_new_user(User)
  # OK: type[ProUser] is a subtype of type[User]
  make_new_user(ProUser)
  # Still fine
  make_new_user(TeamUser)
  # Error: expected type[User] but got User
  make_new_user(User())
  # Error: type[int] is not a subtype of type[User]
  make_new_user(int)
  ```

* `NoReturn`: use it in functions that never returns, for instance for throwing errors

  ``` python
  from typing import NoReturn
  def stop() -> NoReturn:
  raise RuntimeError('no way')
  ```

* Let us be clear: `python` basically discards type hints, hence the following won’t raise any warnings nor errors: `name : int = 'Ajeje'`

* [`mypy`](https://mypy.readthedocs.io/en/stable/index.html): write annotations indicating the types of your variables, parameters, and return values, then run `mypy` to check if your code is coherent (are you assigning a list to a variable that should a dictionary? and so on...).
    The annotations do not interfere with the code when you are running directly the script.

  * Skip line from checks: add comment `# type: ignore`

## Working with `jupyter` notebooks

* `jupyter-lab`: advanced browser-based (it uses a browser, but no need to be online) environment for editing and running notebooks

* Plots and semi-prints (I mean what you get when in a `python` interface you run "`a`", `a` being a variable, and not "`print(a)`") overwrite.
    To make them stay, use `plt.show()` for plots or simply `print()` for other stuff

* `jupyter` magic:

  * [Some info](https://ipython.readthedocs.io/en/stable/interactive/reference.html#magic)

  * Complete built-in [list](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

  * [Online example](https://nbviewer.org/github/ipython/ipython/blob/1.x/examples/notebooks/Cell%20Magics.ipynb)

  * `[%]%timeit`: compute performances

    * Starts the cell with `%%timeit` to run the performance analysis on the whole cell

    * `%timeit`: same as above, but inline, hence only for the current line

    * Option `-r <N>`: repeat `N` times

    * Option `-o`: capture output. E.g., `res = %timeit -o -r 5 foo()`

      * Access data: `res.average`, `res.stdev`, ...

      * If in whole-cell mode (i.e., `%%timeit`), results are stored in underscore operator, “`_`”

  * `%%matplotlib`: Interactive support with `matplotlib`

    * Intro [here](https://matplotlib.org/stable/users/explain/figure/interactive.html#ipython-integration)

    * Add `%%matplotlib widget` at the beginning of the selected code-cell

    * Needs dependency `ipympl`

  * `%%bash`: run in `bash` all the commands in the cell

* Download images:

  * "(Shift + ) Right click \> Save image as..." easy-peasy.

  * Download images in batch: [`junix`](https://github.com/damienmarlier51/JupyterNotebookImageExporter)

  * Here the gist (used by the `junix` above): images are stored as ASCII strings in base64.
    Recover the data-string associated with an image: open the `ipynb` with a simple editor, there you will find a structure composed of dictionaries and lists, find the items associated to the image, they are inside a `data` cell and their key is `image/<type>` with `type` being `png`, for instance.
    Mind to remove `\n` at the end if present.
    Use base64 utilities to convert the string into image: you can use `base64` `bash` command with option `-d` (see [here](https://askubuntu.com/questions/907540/how-to-decode-an-image-string-using-base64-in-command-line)) or `python` `base64.b64decode`

* Use LaTeX commands, see [here](https://stackoverflow.com/questions/13208286/how-to-write-latex-in-ipython-notebook) or, even better, [here](https://jupyterbook.org/content/math.html)

* Sub-command [`jupyter nbconvert`](https://nbconvert.readthedocs.io/en/latest/usage.html): it enables one to convert notebooks in several format directly from command line. Options:

  * `--to <fmt>`: choose the output format. Available: pdf, latex, markdown, python, asciidoc, html, notebook (see executing below),...

  * `--output <ouname>`: basename for output

  * `--no-input`: do not render code-cells (but do render their output)

  * `--execute`: execute the notebook before converting it

    * It format notebook is chosen, then a new one is generated with the results with the following name `basename.nbconvert.ipynb`

    * `--inplace`: Save in-place instead of into a new file

## Writing documentation

We give here some tips about writing documentation for your `python` code using [`sphinx`](https://www.sphinx-doc.org/en/master/index.html), basic ideas are [here](https://docs.python-guide.org/writing/documentation/).
The main features of `sphinx` are that it provides building procedures, it is highly customizable, it uses reStructured Text (a markup language similar to [`markdown`](markdown.md), and can automatically process the docstrings.

First of all, here some info about docstrings, defined [here](https://www.python.org/dev/peps/pep-0257/).
They are the comment-like lines just after function / class declarations, included in triple single- or double-quotes (`'''` or `"""`), that are read by python when invoking `help( )` or `doc( )`, [here](https://www.geeksforgeeks.org/python-docstrings/) is basic stuff, also [here](https://www.programiz.com/python-programming/docstrings).

There are docstrings conventions that can be read and processed by `sphinx` so that it can generate automatically the documentation.
The two most well-known and used are [Google style](https://www.programiz.com/python-programming/docstrings) (example [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)), and the [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html) (example [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy), mind that this format needs an additional extension of `sphinx`, we’ll come back on this later).
In short, choose one of the styles, used it coherently, so that you may create your doc in no times.
In order for the docstrings to be understood by `sphinx`, you may use `sphinx` directive, like [this](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#an-example-class-with-docstrings), but the docstrings are a little less readable.

Now comes the real part about using `sphinx`.
I am no wiz, I just figured out a couple of tricks by trial’n’error.
Before getting into the detail myself, let me just give some web posts which (somehow) details the procedure: [here](https://betterprogramming.pub/auto-documenting-a-python-project-using-sphinx-8878f9ddc6e9), [here](https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/), [here](https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365) (keep this for `automodule` / `autodoc`), [here](https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b).

1.  Install `sphinx` if you don’t have it with `pip install Sphinx`.
    It is advised to use virtual environments.

2.  `sphinx` uses a configuration file `conf.py`.
    The default configuration may be set up by running `sphinx-quickstart` and answering its question.
    You may want to activate the `autodoc` (automatically generates from docstrings), `intersphinx` (generates links within documentations), `coverage` (checks if you forgot to document something), `viewcode` (provides links to the code), and possibly even `doctest` (runs some examples found in the docstrings) extensions.
    The `Makefile` is quite useful, too. Now, you have set your doc up.

3.  You should say to `sphinx` where your scripts are.
    Open `conf.py` and uncomment the first imports (`os` and `sys`) and the path insertion: default is current directory, adjust with the path which is right for you.

4.  In the `conf.py`, you may also change a number of settings and extensions:

    * Theme: default is “alabaster”.
        See [here](https://sphinx-themes.org/) for a gallery.
        Among the most used ones, is the ReadTheDocs theme: `sphinx_rtd_theme`

    * Extensions: the above mentioned `autodoc`, `intersphix`,...are already loaded if you asked for them in the quickstart.
        If using the NumPy style, you should activate also the Napoleon extension, hence add `sphinx.ext.napoleon` to the list.

    * And a lot of more stuff

5.  If you want `sphinx` to automatically generate the doc from your docstrings, you should tell it in the `index.rst` file as explained in item 8 [here](https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b) or [here](https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365).

    * This enables `sphinx` to do it all by itself, otherwise, you can also do it yourself using the utility `sphinx-apidoc` as mentioned [here](https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/).

6.  Now, if you asked for the `Makefile`, you just need to run `make html` (or `latexpdf`, or anything that pleases you) and your doc is generated in the `[]_build` directory.

7.  That’s it.
