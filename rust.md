# `Rust`

* Some docs: [official `Rust` book](https://doc.rust-lang.org/book/title-page.html), [a guide for `C++` developers](https://github.com/nrc/r4cppp/tree/master)

* Installation: [see here](https://www.rust-lang.org/tools/install).
    By default, the command will install also the doc, which is quite heavy and consists in thousands of files. One can ask for a [*minimal* installation](https://github.com/rust-lang/rustup/issues/998#issuecomment-542332509) (otherwise, one can [remove it afterwards](https://github.com/rust-lang/rustup/issues/998#issuecomment-542363707))

    ``` bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | \
        sh -s -- -y --profile minimal --default-toolchain stable
    ```

* Variables

  * Declared with keyword `let`

  * Can be typed (annotated) or not: `let x: u32 = 5;` unsigned 32-bit integer

  * Immutable by default. To make it mutable `let mut x: u32 = 5;`

  * Shadowing: one can re-declare a variable, even immutable ones and even with a different type.
    In this case the previous is “deleted”

    ``` Rust
    let x = 5;
    let x = x * 2;
    ```

* Functions

    ``` Rust
    fn plus_two(x : isize) -> isize {
      x + 2
    }
    ```

  * They do not need the `return` keyword if the last line of the function already “returns” a value

  * Return type declared with `->`.
    Omit everything or use `-> ()` for void (“()” is the void type)

* Constants: defined with `const`

  * Differently from immutable variables:

    * must be typed (annotated) from the declaration.

    * must be set only to a constant expression.

* Pointers

  * Owning (unique) pointers

    * `let x: Box<i32> = Box::new(75);`

    * Freed automatically when they go out of scope

    * Mutability of the data follows the mutability of the pointer: if one is mutable the other is, too.

    * If passed as argument or assigned to variable, they can no longer be accessed

      ``` Rust
      fn bar(y: Box<isize>) { }

      fn foo() {
          let x = Box::new(75);
          bar(x);
          // x can no longer be accessed
          // let z = *x;   // Error.
      }
      ```

    * Method calls automatically dereference, so there is no need for a `->` operator or to use `*` for method calls.
        For instance, assuming type `Foo` has method `foo()` the following is possible:

      ``` Rust
      fn bar(x: Box<Foo>, y: Box<Box<Box<Box<Foo>>>>) {
          x.foo();
          y.foo();
      }
      ```

  * Borrowed pointers

    * Defined with `&`.
        It does not allocate memory: one can only create a *borrowed* reference to an existing value.
        When it goes out of scope, no memory is deleted.

    * This might be used to replace `C++` references for function arguments.

    * Mutable borrowed references are unique.

    * Differently than unique pointers, the mutableness of reference and value are not linked: we can a have an immutable reference to mutable data.

    * If a mutable value is borrowed, it becomes immutable for the duration of the borrow.
        Once the borrowed pointer goes out of scope, the value can be mutated again.
        This is in contrast to unique pointers, which once moved can never be used again.

    * Unlike `C++`, `Rust` won’t automatically reference a value for you.
        So if a function takes a parameter by reference, the caller must reference the actual parameter.
        However, pointer types will automatically be converted to a reference

  * Data types

    * Structs: similar to a `C++` struct but *without* methods

      ``` Rust
      struct S {
          field1: i32,
          field2: SomeOtherStruct,  // Ending comma can be omitted
      }
      ```
