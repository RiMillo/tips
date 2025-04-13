# `C` & `C++`

## `C`

Just some tricks.

* ATTENTION - Memory management.
    To some pointers and functions related to them such as `malloc`, `realloc` and `free`, are some of the most confusing things about `C`.
    Here, I do not pretend to explain everything, but let me tell you this, which should be a golden rule for developing in `C`: for every `malloc` that you call, remember to call also its related `free`.
    The impact of non-freed memory may be insignificant on certain problems, but it could quickly snowballing into something really dangerous and crash the run.

* It is advised by someone to use preprocessor false statements as a comment zone in which one can put anything (s)he wants to

  ``` c
  #if 0
    This part won't be seen by the preprocessor
    Anything you want, no special caratchers needed
    Although some warning may be issued, for instance
    for unbalanced parantheses
  #endif
  ```

* Operator `?` (ternary operator): it is a shortcut for a simple `if` statement.

    ``` c
    /* condition */ ? /* if true, do this */ : /* otherwise, this */
    ```

    For instance it could be useful when one wants to define a `const` variable which however depends on a certain condition.

    ``` c
    const int max = (n > m) ? n : m;
    ```

    Notice that in this case, if `m` or `n` are calls to functions, they are evaluated twice, one for the comparison, and one for the assignment.
    Hence, if the calls are time-consuming, you might want to use temporary variables.

* [Casting](https://www.improgrammer.net/type-casting-c-language/): it is a way to change the type of a variable.

  * Sometimes it is hidden: `float a = 1;`.
    Because of its format, `1` is actually interpreted as an integer and then cast into a floating-point number.

  * Casting could be done explicitly:

    ``` c
    old_type a = [...];
    new_type b = (new_type)a;
    ```

  * The compiler will always try to cast, but if there is no correlation between the two data types unexpected behaviour and loss of precision may happen.
    Consider for instance

    ``` c
    float a  = 1.1;
    int   ab = (int) a;
    ```

* Memory / arrays tricks

  * Fastest (?, possibly if one runs sequentially) to reset an array:

    ``` c
    memset(dest, 0, dest_len*sizeof(<dest_type>))
    ```

    (destination, value to copy, number of bits to consider).
    Notice that since it works on the single bits, this works only with zero, namely that would not work to fill an array with ones (or any value, indeed).
    Mnemonic: `dest = 0`.

  * Fastest (?, possibly if one runs sequentially) to copy an array into another: structure similar to the one above.
    Mnemonic: `receive = send`

    ``` c
    memcpy(receive, send, <n_element_to_copy>*sizeof(<send_type>))
    ```

* Booleans:

  * Originally, `0` means false and `1` (well, actually, any integer different than zero) means true.

  * Since `C99`, the type `_Bool` is introduced.

  * The standard library `stdbool.h` introduces `bool` (which expands to `_Bool`), `false` (expands to `0`) and `true` (expands to `1`).

* Loops:

  * `break` exits the innermost loop only (`for` or `while`).
    If one wants to exit all of them, a flag (a `_Bool`/`bool`) should be used.

  * `continue` skips the rest of the current iteration, increases the counter and goes to the next iteration (stays in the loop!)

* File reading/writing: [here](https://www.programiz.com/c-programming/c-file-input-output).

* Preprocessor

  * Compile with `-E` to get the source file preprocessed.

  * [*Stringizing*](https://gcc.gnu.org/onlinedocs/gcc-7.5.0/cpp/Stringizing.html)

    * Macro to make something a string, use `#`: `#define str(s) #s`

    * Double it if you want to make the content of another macro a string

      ``` c
      #define foo 4.0
      #define str(s)  #s
      #define xstr(s) str(s)
      // Now use xstr(foo) -> "4.0"
      ```

  * Append / Concatenate: use operator `##`.
    Consider this[^1]

    ``` c
    float pow2(float x){return x*x;}
    float pow3(float x){return x*x*x;}
    #define _p(a,b) pow##b(a)
    [...]
    float var = 42.;
    float var_square = _p(var,2); // Expands to pow2(var)
    float var_cube   = _p(var,3); // Expands to pow3(var)
    ```

### Poorman optimizations

Here are some simple optimizations that you can consider, you can think of them as good practices.
They won’t certainly have much of an impact on the total runtime (in fact, especially with the loops, the compiler will try do anticipate what you want to do and optimize it), but it is useful to have them in mind and of course, it is definitely better to use them.
A great deal of them deals with cache optimizations and avoiding cache-misses, it could be interesting to have a look at how a cache is and works and how to get the most out of it.
Anywho, here are some optimizations:

* Constant variables.
    You need to define a variable and you know for sure from the beginning that its values will not change in the current scope.
    It is then advisable to define them as constant: the compiler will take into consideration this piece of information and use it to optimize the program.
    In order to make a variable constant, just prepend `const` to the usual definition `const int n = 10;`.
    You try to modify a value of a constant value, you’ll get an error or at least a warning.
    You can also make the arguments of a function constant, this may be beneficial in three ways: optimization, allow the user to identify input and output parameter, and avoid error like modifying a value that you are not supposed to.
    However, it is usually not advised to make an argument of a function constant if it’s one value (`int`, `float`,...) since in this case the performance gains will be null.
  Still it could be beneficial for the lecture.

* Data locality: try to define variables as close as possible to where you are going to use them.
    Basically, it is sometimes better to redefine a variable in a loop at each iteration rather than define it outside and change it at each iteration.

* Array accessibility.
    Somehow related to the previous point, you are looping through a huge array with hundreds or thousands of elements.
  If you are going to use the value several times, redefine a pointer that points just the current item.
  For instance,

  ``` c
  for (int i=0; i < 10000; i++){
    double *a_i = a + i;
    // use now a_i[0]
  }
  ```

  This can be pretty useful if you are dealing with coordinates, for instance

  ``` c
  for (int i=0; i < 10000; i++){
    double *a_i = a + 3*i;
    // a_i[0] will be the x-coordinate of the i-th point
    // a_i[1] the y one and a_i[2] the z one
  }
  ```

  Why that?
  Well, it actually takes some time to move in the memory to recover a value so accessing `v[1]` is (slightly) faster than `v[1000]`, having to doing it several thousands of times may impact the performances.

* Prefer arrays to matrices: using `a[i][j]` is convenient but if the dimensions are large is pretty slow, the reason is somehow related to the previous item.
    Anyway, the bottom line is: A unique array is much faster: `a[n_cols*i+j]` (if you have to choose only one optimization to remember, choose this one, big times)

* Prefer looping by columns rather than by rows.
    Another tips about memory and matrices, the reason of it is the cache: when the computer access a location in the memory, it also loads some chunks of memory that are just next to the one it actually needs.
    In this way, if it will need this additional piece of memory in the next iterations (as it is often the case), it already has it and avoid loading it thus saving some time.
    When looping by rows, the data that we request are (often) too far away from each other and a load at each iteration is almost certain.
    Bottom line: (notice the switch of the indexes and, most importantly, which loop is the innermost) this

  ``` c
  for (int i=0; i < n_rows; i++)
    for (int j=0; j < n_cols; j++)
      a[i*n_cols+j] *= 2;
  ```

  is better than

  ``` c
  for (int j=0; j < n_cols; j++)
    for (int i=0; i < n_rows; i++)
      a[i*n_cols+j] *= 2;
  ```

* Loop unrolling.
    Well, that is almost useless since the compiler will sometimes try do it even without being asked.
    However, a `for` loop has an overhead.
    So if it is not much of a fuss, you can try to write yourself by hand the iterations.
    Again, nowadays loop unrolling is practically useless but it is interesting to know how things work.

* Keep loops as straight as possible.
    The compiler will try to guess what the next operation will be, try to (almost) perform consecutive iterations at the same time, load some memory which is adjacent to the one you are requesting,...
    you get the idea. If it does not manage, the program has to do unload what it thought and load what you really asked, and that takes time.
    Hence, avoid `if` statement in loops as much as possible, avoid jumping around an array, basically keep a straight path.

* Short types.
    Sometimes you know that a certain variables will not exceed a threshold, you can then using short types, which takes less memory than standard types.
    For instance, looping through the components of a vector, use `short int`

  ``` c
  for (short int i=0; i < 3; i++){
    // Do something
  }
  ```

  (You may wonder, so why not use it all the times?
  Well, the maximum number that a short integer can represent is not that much and you may never reach the bound of the loop)

* Inline function.
    If a function is less than a dozen line long, consider inlining it.
    If this concept is new to you, know that: he code of an inline functions is copied as is where it is requested, so that by using inlined functions we don’t get the overhead for the call to a function.
    Calling a long inlined function many times makes the executable larger (many lines of code) and that is something to avoid, hence, a dozen lines is a good thumb-rule.

* If dealing with synchronization in parallel mode, try to call those functions as less as possible.
    Instead of doing `n` times a synchronization of a vector of 3 values, prefer only one synchronization of a vector of `3*n` values.

## `C++`

Some stuff that are different from plain `C`

* Pointers vs. References: this [SO answer](https://stackoverflow.com/a/57492/12152457), this [post](https://www.geeksforgeeks.org/when-do-we-pass-arguments-by-reference-or-pointer/) about usages in functions, mind also [this](https://www.tutorialspoint.com/cplusplus/returning_values_by_reference.htm) concerning references and return values.

* lvalues vs. rvalues (what we are going to say is not 100% correct, but it gives a good idea of what those two are.
    Moreover, technically, there are two types of rvalue: prvalue and xvalue)

  * Originally, in the plain `C` days, lvalue was an expression the may appear on the *left*- or right-hand side of an assignment; rvalues *can only* appear at the *right*-hand side of an assignment

  * Simply (but not entirely exactly) put: an lvalue is an expression that refers to a memory location and allows us to take the address of that memory location via the `&` operator.
    An rvalue is an expression that is not an lvalue.

  * Some rules

    * If a function returns a value that value is considered an rvalue.

    * If a function returns a lvalue reference (const or non-const) that value is considered an lvalue.

    * If a function returns a rvalue reference (but there is normally no reason to do so!), that value is an rvalue.

  * Examples

    * An rvalue cannot be used to initialize a non-const lvalue reference, while it can be used to initialize const references

      ``` c++
      double & pi =3.14;// wrong! A literal expr is a rvalue
      double const & pi =3.14;// Ok!
      ```

    * An rvalue expression can be used to initialize a variable, but it cannot be “initialized”

      ``` c++
      int pippo();
      int & pluto(int& a);
      int & pluto2(const int & a);
      auto p=pippo();   // ok
      int & c=pluto(p); // ok function returns a lvalue here!
      int & d=pluto(3); // NO! 3 is an rvalue cannot be assigned
                        // to a (lvalue) reference
      int & e=pluto2(3); // ok, mind the const
      // lvalues:
      int i = 42;
      i = 43; // ok , i is an lvalue
      int* p = &i ; // ok, i is an lvalue
      int& foo() ;
      foo() = 42; // ok, foo() is an lvalue
      int* p1 = &foo() ; // ok, foo() is an lvalue
      // rvalues:
      int foobar() ;
      int j = 0;
      j = foobar() ; // ok, foobar() is an rvalue
      int* p2 = &foobar() ; // error: cannot take the
                            // address of an rvalue
      j = 42; // ok, 42 i s an rvalue
      ```

* Type qualifiers

  * `const`: A `const` variable cannot be modified by the code.

  * `volatile`: `volatile` variables may be modified by an external device / piece of code / hardware,...
    This will tell the compiler that, even if in the code the such a variable does not change, it could at anytime as effect as an unknown operation, so that the compiler won’t make optimizations.

  * `const volatile`: a variable that cannot be modified by the code but can still be modified by an external action.

* `const` member methods & `mutable` attributes: A method can be defined as `const`, this means that the function cannot change the attributes of the object (you can see this as forcing the pointer `this` to be `const`)... *UNLESS* an attribute was declared `mutable`: in that case it can be modified even in `const` methods

* [Lambda functions](https://en.cppreference.com/w/cpp/language/lambda): `[ captures ] ( params ) <qualifier> -> ret_type { body }`

  * `captures`: The capture list defines the outside variables that are accessible from within the lambda function body.
    The list may starts with a default capture, `&` by reference, or `=` by copy

  * `params`, `body`: as any functions

  * The qualifier `mutable` tells that the things captured by copy are modifiable

  * The return type `ret_type` is not mandatory, otherwise it is inferred from the `return` statement.

* `->` in function definition: it is used to define the return type, see above with lambda functions.
    This is necessary, for instance, when one wants to use `decltype` with one of the parameters.
    See [here](https://stackoverflow.com/a/22515589/12152457)

  ``` c++
  template <typename T1, typename T2>
  auto foo(T1 a, T2 b) -> decltype(a + b);
  ```

* Smart pointers: they were implemented to help developers with data-leaks since their main features is that no `delete` function has to be called since **the freeing is done automatically** at the end of the variable scope.
    Sources: [here](https://www.geeksforgeeks.org/smart-pointers-cpp/), [here](https://www.internalpointers.com/post/beginner-s-look-smart-pointers-modern-c), and [here](https://docs.microsoft.com/en-us/cpp/cpp/smart-pointers-modern-cpp?view=msvc-170).

  * Three types:

    * `unique_ptr`,

    * `shared_ptr`,

    * `weak_ptr`

* Literals for numbers (`<n>` tells the position of the digits so that one understands if its a pre- or suffix):

  * `<n>f`: float (Attention: the default is double)

  * `<n>l(l)`: long (long) double or integer

  * `<n>u`: unsigned integer, may be combined with `l(l)`

  * `<n>b`: binary

  * `0x<n>`: hex

  * `0<n>`: octal

  * `<n>e<n>`: exponent form, may be combined with `l`, `f`

### Data structures

* `map` & `unordered_map`: Ordered (resp. unordered) associative container that contains key-value pairs with unique keys.

  * `operator[key]`: access value associated to the given key. If the given key does not exist, it adds it, even if it is a right-hand call, as in, `a = m[k]`

  * `at(key)`: access value associated to the given key. If the given key does not exist, it throws.

  * When looping, `for(auto e : m)`, the elements are pairs, so that the key is accessed with `e.first` and the value `e.second`.
    In recent versions, one can even use

    ``` c++
    for (auto & [key, value] : m) {
      // Do stuff
    }
    ```

  * Lookup: `count(key)` returns the number of elements matching specific key, `find(key)` returns an iterator to the element (pair) with key equivalent to the given one, if it is not found, `end()` is returned.

  * When using the unordered version, there is no guarantee about the order used when iterating as in `for(auto e : m)`, hence the result is not deterministic/not repeatable, although it is the same when during the same run

### Some tips about Object-Oriented Programming

* Design pattern: some resources [here](https://www.tutorialspoint.com/design_pattern/design_pattern_overview.htm) and [here](https://sourcemaking.com/design_patterns)

* Functor: an object that acts like a function.

  ``` c++
  class Add {
  private:
      int num;
  public:
      Add(int n) : num(n) {  }

      // This operator overloading enables calling
      // operator function () on objects of Add
      int operator () (int add_num) const {
          return num + add_num;
      }
  };
  [...]
  Add add_10 = Add(10)
  int res = add_10(5) // 15
  ```

## `OpenMP`

`OpenMP` or `OMP` is a shared-memory interface for `C`/`C++` (and `Fortran` as well) for parallel computing. *Shared-memory*, simply put, means that the memory may be accessed, read, and modified by any thread at any given moment. Most of the times, parallelize a piece of code with `OMP` comes down to prepend dedicated pragmas (`#pragma omp [...]`) to `for` loops (the last two sentences were *very* wrong, but it might get you on the right direction if this is the first time you have heard of parallelism and `OMP`).
Now that you have the bigger picture and you are thinking "Well, that was easy, I can do it!", welcome to the hardest part, where not so rarely you have to change your piece of code in order not to have threads modifying each other’s work.

* A nice training is available on the IDRIS [website](http://www.idris.fr/formations/openmp/).

* A [cheat-sheet](https://www.openmp.org/wp-content/uploads/OpenMP-4.0-C.pdf) (for version 4.0).

* Unless dedicated instruction are provided (see a couple of items below), every line of code inside a parallel zone is executed by *all* the threads.

* A killer feature is the `reduction`s: compute sums, find max/min, or any operation you’d like (as long as you define it).

* This is something that is true generally for any parallel framework not only `OMP`: parallel code and I/O operations (reading/writing) can become tricky pretty easily, be advised (Remember: several threads working on the same thing? Too many cooks spoil the broth).

* It is important to have in mind which commands are *blocking*, meaning that have a hidden barrier at the end (a point at which all the threads have to meet before they are allowed to continuing the execution of the program).
    For instance, `#pragma omp [parallel] for` is blocking (however, keep in mind the `nowait` clause).

* Sometimes one need that one thread only may work on something at the same time.
    This is where `#pragma omp critical` and `#pragma omp atomic` come into play, where the last one provide better performances but allows only very few operations like reading, writing, and updating (e.g. `sum += a[n];`).

* In parallel mode but this particular piece of code should be executed once and once only?
    Put it in dedicated pragmas like `#pragma omp master` (only the master thread, usually the one with ID 0, is allowed to execute the code) or with `#pragma omp single` (only the first threads arrived at that point executes it, this is your best choice most of the times).
    They have no barriers.

* Just to get it right, let us recap the difference between the last two points.
    With `critical` or `atomic` all the threads execute the command, but one at the time. With `single` or `master` the code is executed only once.

[^1]: Did you actually believe that
    [42](https://hitchhikers.fandom.com/wiki/42) was not going to appear
    here?! You fool!
