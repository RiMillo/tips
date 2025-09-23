# Shell

There are different version of shells scripting, such as `bash`, `sh`, `zsh`; they have some differences in commands and syntax (but I do not know them `\o/`).
I will use `bash`.

## Shell (`bash`) basics

In this section, we cover basic stuff about the shell.
For useful terminal commands and tools, see the next sub-sections.

For terminal commands, mind that you can access the related *man*ual/help page by running

``` bash
man <cmd>
```

or sometimes

``` bash
<cmd> --help
```

* Official [guide](https://www.gnu.org/software/bash/manual/html_node/index.html) by GNU itself
* Of course I'm not the first to write tips, and certainly not the one who knows the most, so here a couples of tips lists, especially about shortcuts: [here](https://www.techrepublic.com/article/20-terminal-shortcuts-developers-need-to-know/) and [here](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/) and [here](https://devhints.io/bash).
    This [guide](https://github.com/jlevy/the-art-of-command-line) has many tips and seems to be popular on GitHub.

    * Keyword shortcuts: see [here](https://gist.github.com/tuxfight3r/60051ac67c5f0445efee).
        Or get it directly from `man` as suggested [here](https://askubuntu.com/questions/444708/is-there-any-manual-to-get-the-list-of-bash-shortcut-keys): `man bash | grep "(.-.*)$" -A1`.
    * Cut & yank: <kbd>Ctrl</kbd> + <kbd>K</kbd> cut (or *k*ill) from cursor to end of line, <kbd>Ctrl</kbd> + <kbd>U</kbd> cut from cursor to beginning of line, <kbd>Ctrl</kbd> + <kbd>W</kbd> cut (blank-delimited) word just before the cursor, <kbd>Ctrl</kbd> + <kbd>Y</kbd> yank (paste).

    * <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd>: expand alias.
    * <kbd>Ctrl</kbd> + <kbd>R</kbd>: search in the command history while typing.
    * <kbd>Alt</kbd> + <kbd>.</kbd>: insert arguments of the previous (run) command;
    * <kbd>Ctrl</kbd> + <kbd>X</kbd> + <kbd>E</kbd>: continue editing the bash command you are writing in the predefined editor.
    * `!`: repeat stuff as explained [here](https://www.redhat.com/sysadmin/bash-bang-commands).
    * Use braces (curly brackets) `{ }` to save typing.
        Examples:
        * `cp file_{orig,bkp}` expands to `cp file_orig file_bkp`
        * `evince work{1,2,3}.pdf` expands to `evince work1.pdf work2.pdf work3.pdf`

* Variables
    * To set / declare a variable just use implicit declaration: `foo="BAR"`.
    * For strings with whitespaces in them, one should quote them otherwise they will be split and the subsequent parts of the string after a whitespace will be treated as commands.
        For instance: `string="A string with spaces"`
    * To access the value of a variable use the dollar sign, `$`, e.g.
        `foo=bar; echo $foo` prints `bar`
        * It is good practice to put the name of the variable inside braces: `${foo}`.
            This avoids substitution problems.
            E.g., suppose we have `foo=bar` and want to write `baz` just after the value of `foo`
            * The following will try to get the value of variable `foobaz` which does not exist, hence printing nothing

                ```shell
                echo $foobaz
                # Prints nothing
                ```

            * Using braces, one obtains the wished result

                ```shell
                echo ${foo}baz
                # Prints barbaz
                ```

        * Indirect expansion, `${!var}` (you can think of it of double extraction): extract the value of the variable with name the value of `var`

            ```shell
            cat="Miao"
            animal="cat"
            echo "The cry of the cat is ${!animal}"
            # The cry of the cat is Miao
            ```

    * Some variable tricks ([here](https://tldp.org/LDP/abs/html/parameter-substitution.html))

        * The full list on the [official guide](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)
        * `${var-default}`: Use `var` if it is set, otherwise `default`.
        * `${var:-default}`: Use `var` if it is set *and not* null, otherwise `default`.
        * `${var=default}`: If `var` is not set, set it to `default`.
        * `${var:=default}`: If `var` is not set *and not* null, set it to `default`.
        * `${var+alt}`: If `var` is set, use `alt`.
        * `${var:+alt}`: If `var` is set *and not* null, use `alt`.
        * `${var?error}`: If `var` is set, use it, otherwise print `error` and exit with status 1.
        * `${var?error}`: If `var` is set *and not* null, use it, otherwise print `error` and exit with status 1.

  * Scope: the scope of a standard variable is its script.
    But there are way to change this

    * Local variables: variable declared in this way inside a function, are only visible inside the same function: `local foo="Bar"`

    * Environment variables: use `export`

      ``` bash
      # Typical usage
      export $PATH=/new/path:$PATH
      # For a function, use -f
      function foo() { echo "Ciao"; }
      export -f foo
      # Remove export property
      export -n foo
      ```

  * Some built-in variables:

    * `$#`: number of arguments passed to the script

    * `$<n>`: argument `n`.
        It is 1-based, in fact `$0` expands to shell / script’s name

    * `$@`: all arguments.
        You can use it in a list: `for arg in "${@}"`.
        When quoted, it extends to singularly quoted arguments: `"$@"` expands to `"$1" "$2"`...`${@:2}` all arguments starting from the second.
        `${@:2:4}` arguments from the second to the fourth.

    * `$*`: all arguments.
        It is similar to `$@`, however, when quoted, it extends to all arguments quoted inside the same quotes: `"$*"` expands to `"$1 $2 ..."`

    * `$!`: expands to the last run process’s ID

    * `$?`: return value of last command. You can store it `ret_val=$?` or use it directly

      ``` bash
      some_command
      if [ $? -eq 0 ]; then
        echo OK
      else
        echo FAIL
      fi
      ```

  * Variables are not usually typed (there is no distinction between integers, string,...).
    However, sometimes we’d like to have this, one can then use `declare`.
    Some options and tricks:

    * `-r`: declare a *r*eadonly variable

    * `-i`: declare an *i*nteger variable (gives 0 if not integer)

    * `-a`: declare an *a*rray

    * `-f`: declare a *f*unction

    * `-e`: declare an “*e*xport” (that’s actually what `export var`
      does)

    ``` bash
    declare -i n_iter
    n_iter=5
    declare -r ro="readonly"
    ```

  * Command `let <expression>` can be used to define arithmetic variables

    ``` bash
    let "foo = 1" "bar = foo + 2" "foo++"; echo "$foo, $bar" # 2, 3
    ```

* Functions

  ``` bash
  function foo() {
    # Variable
    foo="Foo"
    # Local variable, recommended
    local bar="Bar"
    # Using arguments
    first_arg=$1
    second_arg=$2
  }
  ```

* String manipulation: examples [here](https://tldp.org/LDP/abs/html/string-manipulation.html)

  * The full list on the [official guide](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)

  * String length: `${#string}`

  * Extract characters from position: `${string:<n>}` from `n` to end, `${string:<n>:<m>}` from `n` to `m`, `${string:(-<n>)}` from end (mind the parentheses)

  * Substring removal / replacement

    * `${string#substring}`: Deletes *shortest* match of `substring` from *front* of `string`

    * `${string##substring}`: Deletes *longest* match of `substring` from *front* of `string`

    * `${string%substring}`: Deletes *shortest* match of `substring` from *back* of `string`

    * `${string%%substring}`: Deletes *longest* match of `substring` from *back* of `string`

    * `${string/substring/replace}`: Replace *first* match of `substring` with `replace`

    * `${string//substring/replace}`: Replace *all* matches of `substring` with `replace`

    * `${string/#substring/replace}`: If *prefix* of `substring` matches `substring` replace it with `replace`

    * `${string/%substring/replace}`: If *suffix* of `substring` matches `substring` replace it with `replace`

  * Case

    * `${string^}`: *First* letter uppercase

    * `${string^h}`: *First* letter uppercase *only if* it’s a “h”

    * `${string^^}`: *All* letters uppercase

    * `${string^^[ht]}`: *All* “h” and “t” uppercase

    * `${string,}`, `${string,,}`, ...: As above but lowercase

    * `${string~}`, `${string~~}`, ...: As above but invert case

  * Split: use `read` with appropriate separator

    ``` bash
    macedonia="banana:yellow,apple:red,orange:orange"
    # Split on "," and put it into an array
    IFS="," read -a fruits << $macedonia
    for fruit in ${fruits[@]}; do
      # Split on ":" and put it into an array
      IFS=":" read -a frt_clr << $fruit
      echo "The fruit ${frt_clr[0]} is ${frt_clr[1]}"
    done
    ```

* Default applications: often we don’t know the name of the programs that we use, for instance, for opening a pdf.
    Here some of them

  * `evince` for pdf.

  * `eog` for images.

  * `nautilus` for file explorer.

* Customize your terminal

  * Pimp your `bash` by modifying the file `.bashrc` in your home (load modules that you want by default, set global variables,...) and define personal shortcuts in `.bash_aliases`, again in your home (verify that it is loaded in `.bashrc`).

  * Preceding a terminal command with a backslash will tell the shell to run the command itself and not the alias with the same name if it exists.

  * In `bash`, the keyboard combo <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd> expands aliases and variables that you writing.

* Run in background:

  * Add a `&` after a command to run it back ground, meaning that it won’t block the terminal while running, so that you can still use the terminal window for other stuff.
    This is quite useful when opening GUI programs (e.g. `evince`).

  * Precede your commands with `nohup` in order to have them running ever after the terminal window / session is closed.
    More [here](https://linux.101hacks.com/unix/nohup-command/) or [here](https://hexadix.com/use-nohup-execute-commands-background-keep-running-exit-shell-promt/).

* `echo`: print to screen

  * Change colors: see [here](https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux) (remember `-e` and to “close” the color)

  * Fonts: see [here](https://askubuntu.com/questions/528928/how-to-do-underline-bold-italic-strikethrough-color-background-and-size-i) (see before)

* Operator `*` expands to all the files whose name does not start with "`.`".
    Hence, hidden files (as well as current directory "`.`", and parent directory "`..`" are not included).

* Arithmetic operations: `$((4*n+3))`, notice that once inside the variables do not need the \$ sign.
    As it is the case for operator `[` (cf., [dedicated section](#shell-commands-and-tools)), `((` is a shortcut for a command, precisely [`let`](https://www.computerhope.com/unix/bash/let.htm).
    On shell such as `bash` only integers arithmetics are allowed.
    Many alternatives are available, for instance using [`awk`](#awk) or [`python`](python.md)
    or [`bc`](#shell-commands-and-tools).
    Others may be found [here](https://unix.stackexchange.com/questions/40786/how-to-do-integer-float-calculations-in-bash-or-other-languages-frameworks).

* Pipes: `|` connects standard output of one command to standard input of another.

* File descriptors:

  1.  Standard input

  2.  Standard output

  3.  Standard error

* Use output of commands (for instance, to define a variable or a command)

  * Brackets: `$(cmd)`

  * Backticks: `` `cmd` ``

* [Redirection](https://www.gnu.org/software/bash/manual/bash.html#Redirections): use `>` to redirect, `>&` to duplicate and redirect

  * Redirect `stdout` to `stderr`: `<cmd> 1>&2`

  * Redirect `stdout` and `stderr` to file: first we redirect `stdout` to a file then we tell to copy `stderr` to `stdout`

    ``` bash
    <cmd> > file.log 2>&1
    ```

  * Discard output: `<cmd> > /dev/null`.

  * Pipe `stderr`.
    Aim: discard `stdout` and pipe `stderr`.
    [Actions](https://stackoverflow.com/questions/2342826/how-can-i-pipe-stderr-and-not-stdout): redirect `stderr` to `stdout`, discard `stdout`, pipe.

    ``` bash
    cmd 2>&1 >/dev/null | pipe_receiver
    ```

  * `>` can be used to write to file: `echo "Hello world!" > hello.txt` will write into the provided file.
    If the file already exists it will be replaced, otherwise it will be created.
    If you want to *append* to the file just use `>>`.

  * You may want to check out `tee` [below](#shell-commands-and-tools).

* Input:

  * *Here*-strings: feed the content of a variable to a command with `<<<`: `grep [] <<< $var`

  * *Here*-documents: feed the content of a file created on-the-run to a command with `<<`:

    ``` bash
    grep [] <<EOF
    First line
    Second line
    EOF
    ```

    The keyword `EOF` is arbitrary (one can choose it freely) and delimits the beginning and the end of the document

* Strings manipulation:

  * A quick [guide](https://sookocheff.com/post/bash/bash-string-operators/), or the official [manual](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html).

  * Extract substring: `${string:position:length}`. For more details have a look [here](https://stackoverflow.com/questions/1405611/how-to-extract-the-first-two-characters-of-a-string-in-shell-scripting).

  * Remove pattern

    * Starting match: shortest `${variable#pattern}`; longest `${variable##pattern}`

    * Ending match: shortest `${variable%pattern}`; longest
      `${variable%%pattern}`

  * Replace pattern: first `${variable/pattern/replace}`; all `${variable//pattern/replace}`

  * Operator `=~`: `${string} =~ ${regex}` gives true if `string` matches the provided regex syntax.

* In a script, adding at the beginning `set -e` will make the script exit immediately as soon as one of its commands finishes with a non-zero status (when it fails).

* For option management `getopts` is recommended, see [section below](#shell-commands-and-tools).

* Arrays: have a look [here](https://opensource.com/article/18/5/you-dont-know-bash-intro-bash-arrays).

  * Definition: Use parentheses and whitespace as delimiter:

    ``` bash
    arr=(one two three)
    ```

  * Split string into array

    * If delimiter is whitespace, simply use parentheses

      ``` bash
      str="one two three"
      arr=($str)
      ```

    * Use `read -a`, and `IFS` to set the delimiter (default is whitespace). In recent version of bash, one can use `readarray`

      ``` bash
      str="one,two,three"
      IFS="," read -a arr <<< $str
      ```

  * Access with `${arr[$i]}`

  * Get length: `${#arr[@]}`

* Conditional statements:

  * Typical structure

    ``` bash
    if <cond>
    then
    # These first two lines might be written in only one, join
    # with semi-colon as follows:
    # if <cond>; then
      <cmd>
    else
      <cmd>
    fi
    ```

  * The above `<cond>` can be written in several ways, see [here](https://unix.stackexchange.com/questions/306111/what-is-the-difference-between-the-bash-operators-vs-vs-vs).
    Some examples:

    ``` bash
    if [ <cond> ]
    if test <cond> # Same as above
    if [[ <cond> ]]
    if ((<cond>)) # Arithmetic evaluation
    if (cmd) # Command run in a subshell
    if cmd # Command run
    ```

  * Remember: 0 is true, other is false

  * `test` or operator `[` (square brackets): test if an expression is true.
    A quick [guide](https://www.computerhope.com/unix/test.htm).
    But the `man` page is clear and concise, just use this one.
    A little syntax:

    * Conditional `!` negate, `-a|-o` and/or

    * Strings: `-z|-n` true if zero \| nonzero, compare with `=` and `!=`

    * Integers: `-eq` equal, `-ne` not-equal, `-gt|-ge` (resp. `-lt|-le`) greater than \| greater or equal (resp. less)

    * Files: `-ot|-nt` older\|newer than, `-e` exists, `-f` regular file, `-d` directory

    * Combine: `[ a = a ] && [ b = b ]`, for or use `||`.
        To construct multilevel conditions, one should escape parentheses

    * Mind: variable are split, hence, you might want to put them in quotes. Consider `foo bar` vs. `"foo bar"`

  * Operator `[[` (double square brackets) is a `bash` improvement of `test`, and allows more stuff (see this [comparison](https://stackoverflow.com/a/47576482)), such as:

    * An important difference is that variable are NOT split

    * Combine: `[[ a = a && b = b ]]`

    * `$lhs =~ <regex>`: check if `$lhs` match the given pattern

  * Empty and unset variables:

    * Check for an UNSET variable: `[ -z "${var+x}" ]` (from [here](https://stackoverflow.com/questions/3601515/how-to-check-if-a-variable-is-set-in-bash))

    * Check for an EMPTY variable: `[[ -z $var ]]` or `[[ ! $var ]]` (from [here](https://serverfault.com/questions/7503/how-to-determine-if-a-bash-variable-is-empty))

    * Check out this [comparison](https://stackoverflow.com/questions/3869072/test-for-non-zero-length-string-in-bash-n-var-or-var)

      ``` bash
      if [[ $var ]]; then
        # var is set and it is not empty
      fi
      if [[ ! $var ]]; then
        # var is not set or set to an empty string
      fi
      ```

* Loops:

  * For loops: have a look [here](https://www.cyberciti.biz/faq/bash-for-loop/). Quick examples:

    ``` bash
    for n in one two three; do [...] done
    # {START..END} or {START..END..INCREMENT}
    for n in {1..10}; do [...] done
    for n in {1..10..2}; do [...] done
    # 3-expression form (( INIT; COND; STEP )), C-like
    for (( n=0; n<10; n++ )); do [...] done
    ```

  * While loops: `while []; do [] done`

  * Emulating do-while: see first two answers [here](https://stackoverflow.com/questions/16489809/emulating-a-do-while-loop-in-bash)

  * Combine loops and arrays: some examples

    ``` bash
    for n in (one two three); do [...] done
    #
    list=(one two three)
    for n in ${list[@]}; do [...] done # Items only
    for i in ${!list[@]}; do [...] done # Indices only
    for n in ${list[@]:1}; do [...] done # Items only, skip the first
    ```

* Notifications and dialogue windows: we really like the old-school terminal, but sometimes nice GUI stuffs and visual aides make life easier.
    Consider this: you launch a script which takes a really long time, so from the terminal you switch to do other stuff.
    It would be nice to be alerted when the said script finishes.
    I am still working on an audio signal, but consider these two options:

  * `notify-send "Title" "Body"`: a little notification pop-up

  * More advanced: `zenity`, Achieve notification, pop-up, interactive windows,...
    Some stuff [here](https://renenyffenegger.ch/notes/Linux/shell/commands/zenity).
    Try `zenity --<type> --text "Body"` where `type` can assume `notification`, `info`, `warning`, `error`, `text-info`, `progress`, `file-selection`, `list`, `entry`, `scale` and others.
    All but `notification` stop the flow of the script.

    * Control the size with `--width=<n>` and `--height=<n>`

    * `--window-icon=/pat/to/icon`: choose an icon for your widget

    * `--timeout=<n>`: how long the widget should stay

* Quitting

  * `exit [error_number]`: quit the current section.
    That’s exactly what you wish, if you are in a script or in a `ssh` connection.
    However, if you try it in a terminal or in a function, it will close the terminal.

  * In order to quit a function without closing the terminal / script, use `kill -INT $$`

* Parallelize loops:

  * Use background commands with `&`: see [here](https://unix.stackexchange.com/questions/103920/parallelize-a-bash-for-loop/103922)

    ``` bash
    for {...}; do
      do_something() &
    done
    ```

    Mind that this will spawn as many sub-processes as iterations in the loops, no matter the number of available cores

  * As before, but limiting the number of processes: see [here](https://stackoverflow.com/questions/38774355/how-to-parallelize-for-loop-in-bash-limiting-number-of-processes)

    ``` bash
    num_procs=$1
    # The prompt escape for number of jobs currently running
    num_jobs="\j"
    for {...}; do
      while (( ${num_jobs@P} >= num_procs )); do
        wait -n
      done
      do_something() &
    done
    ```

## Debugging `bash`

* Tools:

  * The [BASH Debugger Project](https://bashdb.sourceforge.net/), or `bashdb` is a debugger (no kidding?!) with syntax similar to `gdb`

  * [Shell Check](https://github.com/koalaman/shellcheck), it can be integrated in `vim`

  * An [extension](https://marketplace.visualstudio.com/items?itemName=rogalmic.bash-debug) for `VisualStudio`

* Some [insights](https://www.linuxtopia.org/online_books/advanced_bash_scripting_guide/debugging.html)

* Native options:

  * What

    * `-e`: exit as soon as an error is detected (command returning non-zero code)

    * `-n`: check for syntax errors without running the script

    * `-v`: echo every command before executing it

    * `-x`: echo the result of each command

    * `-u`: make the script fail if an undefined variables is used

    * `-o pipefail`: prevent error in a pipeline from being masked

  * How

    * As command line options: `sh -v my_script.sh`

    * Add to certain zones only via `set -x; [...] set +x`

      ``` sh
      do_stuff
      set -x # Activate option
      # The option is ON for the following commands
      do_something
      set +x # Deactivate option
      # The option is OFF for the following commands
      do_something_else
      ```

## `sed`

Bases:

* Some info could be found in the [manual](https://www.gnu.org/software/sed/manual/sed.html) or in [this tutorial](http://www.grymoire.com/Unix/Sed.html); [this](https://www.tutorialspoint.com/unix/unix-regular-expressions.htm) could be useful as well.

* A general knowledge of the regex could be very useful.
    Take a look at this [cheatsheet](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)

  * `^pattern`: matches any string that starts with `pattern`.
    `pattern$`: matches any string that ends with `pattern`

* General usage: `sed [options] "[range] <command>" old_file new_file`.
  Double quotes `"..."` may be replaced by single quotes `’...’`.

  * If no `new_file` is given, the result is printed to `stdout`.

Commands:

* Common commands may be found [here](https://www.gnu.org/software/sed/manual/sed.html#Common-Commands), less common ones [here](https://www.gnu.org/software/sed/manual/sed.html#Other-Commands), the [list](https://www.gnu.org/software/sed/manual/html_node/sed-commands-list.html) from the manual

* Search and replace, `s`:

  ``` bash
  sed -i "s/<pattern>/<replaced>/" file
  ```

* Replace all the lines matching `pattern` with `Pattern was here` - this works on the entire line, `c <text>` or `c\<newline><text>`:

  ``` bash
  sed -i "/pattern/c Pattern was here/" file
  ```

* Delete all lines containing `pattern` - this works on the entire line:

  ``` bash
  sed -i "/pattern/d" file
  ```

* Insert before line, `i <text>` or `i\<newline><text>`

  ``` bash
  sed -i "/pattern/i Next line is pattern/" file
  ```

* Append after line, `a <text>` or `a\<newline><text>`

  ``` bash
  sed -i "/pattern/a Previous line was pattern/" file
  ```

* Apply multiple commands at the same time:

  * Separate them with semicolons: `sed 'cmd1 ; cmd2' file`

  * Separate them with `-e`: `sed -e 'cmd1' -e 'cmd2' file`

  * Group sever commands together with braces: `{cmd1 ; cmd2}`

Ranges: ranges are optional and it is the way to tell `sed` to apply the provided commands only to those lines specified by the range.
Some examples

* `4,10`: lines 4 to 10

* `4,+6`: line 4 and the following 6 lines

* `4,10!`: everything except lines 4 to 10

* `4~3`: starting from line 4, every 3 lines

* `/pattern/`: all the lines matching `pattern`

Options and tricks:

* The option `-i[<suffix>]`, `--in-place=[<suffix>]` allows to overwrite the file once it is modified.
    If `suffix` is provided a backup is created with the chosen extension;

  * `-i.bak` creates a backup file,

  * The option `--follow-symlinks`, available only with `-i` activated, enables to modify the original file;

* Option `-n` avoid printing.
    This might be used in combination with the command `p` (print) to have a `grep`-like results where one can also replace.
    [E.g.](https://unix.stackexchange.com/a/278377):

  ``` bash
  # Replace foo by FOO (using groups)
  sed -n "s/^.*foo\([0-9]\+\).*$/FOO\1/p" file
  ```

* If in one line there are more occurrences, only the first one is matched.
    Appending `g` will make `sed` match all the occurrences.

  ``` bash
  sed -i "s/<pattern>/<replaced>/g" file
  ```

* Character `&` expands to matched string.

* Match exactly the word: from regex, `\b` delimits boundaries of the word.
    Hence, (although `\<word\>` seems to work, as well (`vim`, anyone?)):

  ``` bash
  $ echo "bar embarassment" | sed "s/\bbar\b/no bar/g"
  no bar embarassment
  ```

* Parentheses used in regex syntax (for groups `(.)`, repetitions `{.}`) should be escaped by a backslash: e.g., `\(agroup\)`.
    Access groups content with `\<n>` where `n` is the number of the group.
    Or, add option `-E`.

* Use `bash` variables: prefer the double-quotes `"` instead of the single ones `'`:

  ``` bash
  sed "s/${pattern}/${replaced}/" file
  ```

* `$` means last line when dealing with ranges, or end of the line when dealing with patterns.

* Mind that command `d` erases the entire line, if you want to delete only the pattern, you can replace it with an empty string.

* Write at the beginning of the line: match the beginning (special character `^`) and replace.
    For instance, in `C` comments all the lines containing `Comment` (mind that we have to escape character `/`)

  ``` bash
  sed '/Comment/ s/^/\/\//' test.c
  ```

* Replace only the first occurrence of `pattern`: a bit tricky, find the right range (from line zero to first occurrence) then replace

  ``` bash
  sed '0,/pattern/ s/pattern/new pattern/' file
  ```

* Replace only the last occurrence of pattern: I’m still working on that.
    A long and dirty workaround may be to use `tac`, then replace *first* occurrence and finally `tac` again.

## `grep`

`grep [options] <pattern> [files]`

Some useful options:

* `-r`: recursive, then `files` can be a directory;

* `-R`: as above, but follow links;

* `-w`: match only complete *w*ords;

* `-c`: just print the *c*ount of the lines with a match;

* `-v`, `--invert-match`: get lines with that do *not* match the `pattern`;

* `-e`, `--regexp=<pattern>`: look for `pattern`.
    This can be used, for example if `pattern` starts with a dash (`-`); similar options are `-E|F|G|P`

* `-i`, `--ignore-case`: search is case-*i*nsensitive;

* `-I: exclude binary files;`

* `-h`: without filename (mnemonic: *h*ead)

* `-H`: with filename (mnemonic: *H*ead)

* `-n`: show line number;

* `-m <n>`: print only the first `n` occurrences of the `pattern`;

* `-B <n>`: print `<n>` lines *B*efore the match (included);

* `-A <n>`: print `<n>` lines *A*fter the match (included);

* `-C <n>`: print `<n>` lines of the *C*ontext of the match;

* `-l`, `--files-with-matches`: *l*ist only the file names in which at least one match is found;

* `-L`, `--files-without-matches`: *L*ist only the file names in which no match is found;

* `-q`: *q*uiet, return just the exit status code (0 or 1 corresponding to, respectively, true or false) according to whether it have found a match or not;

* `--include=<pattern>`: consider only files matching `pattern`.
    For example for only TeX sources

  ``` bash
  grep --include=\*.tex -r "O Bella Ciao" .
  ```

* `--exclude=<pattern>`: do not consider files matching `pattern`;

* `--exclude-dir=<dir>`: exclude files in directory `dir`;

* `--label=<label>`: show matches from `stdin` as coming from file `label`.
    This is nice to have when combining with [`find`](#find).

Tricks:

* Start from the end: `tac <files> | grep [options] <pattern>` (Add a pipe to `tac` to recover the original order).

* Print even if the match is not found `grep -E '^|<pattern>' <file>` (or `'^\|<pattern>' <file>` and no `-E` option).
    Special character `^` means "beginning of the line", hence it is always found.
    Why should one use it?
    With the option `--color` (usually enabled by default) `grep` highlights the matches.
    Here, the command find the beginning of the line, which cannot be highlighted, hence it prints the line, if it finds the pattern as well it will highlight it.

* Non-greedy: add “`?`” after quantifier: e.g., `^.*?}` everything until first closing brace.

Types:

* `-G`, `--basic-regexp`, simple regexp, default

* `-E`, `--extended-regexp`

* `-P`, `--perl-regexp`

* `-F`, `--fixed-strings`, exclude regexp

`grep`’ing non-text files:

* Archives: The version `zgrep` (with the same options) allows to search into compressed/*z*ipped files.

* PDF: two ways, see this [SO question](https://unix.stackexchange.com/questions/6704/how-can-i-grep-in-pdf-files), they both involve some external utilities

  * Using `pdfgrep`: just use it as you would use `grep`

  * Using `pdftotext`: convert pdf to text, pipe it, and `grep` it.
    By defaults it creates a `.txt` file, so mind the dash which makes it skip this

    ``` bash
    pdftotext to_search.pdf - | grep pattern
    # Combined with find
    find /path -name '*.pdf' -exec sh -c \
      'pdftotext "{}" - | grep -H --label="{}" --color " pattern"' \;
    ```

## `find`

It allows to find files in a tree and apply a command to them:

``` bash
find [options] <path> <command>
```

If no command is given, `-print` is executed. Some examples and options:

* Check if file `filename` is in `mydir` or one of its subdirectories (`-print` is considered, thus it works similarly to `ls`)

  ``` bash
  find <mydir> -name <filename>
  ```

  * In the previous examples, use `-wholename` (instead of simply `-name`) if you provide the path as well

  * `-regex`: similar to `name` but one can use regex syntax to write the pattern.
    The type can be chosen with `-regextype` (ex. `sed`).
    Notice that `find` always prepends `./` to the path so you may want to start your pattern with something like `.*/`

  * Case-insensitive search: use `-iname` or `-iregex` as you would use their parent options

* Filter on the file type: option `-type <t>` where `<t>` can be, for example, `d` (directory), `f` (regular file), `l` (symbolic link)...

* `!`, `-not`: negation of the expression that follows.
    E.g.: `find . -not -name foo` print all the files in the current directory with a name different than `foo`.

  * Exclude a path:

    ``` bash
    find . -name notmyfile -not -path <dir_excl>
    ```

    This is somehow too simple and `find` will still search into the sub-directories of `dir_excl`.
    You may find other solutions [here](https://stackoverflow.com/questions/4210042/how-to-exclude-a-directory-in-find-command) (the accepted answer with `-prune`may not always work).

* `-maxdepth <n>`: limit the tree descent level of the search

* Apply a command to all the matching files: e.g., run a bash script, grep only certain files

  ``` bash
  find . -name "*.log" -exec script.sh {} \;
  find . -name "*.log" -exec script.sh {} +
  find . -name "*.log" -exec grep -Hn --color "pattern" {} +
  ```

  `{}` stands for the matching files; the first version will execute as many calls as the numbers of matching files, the second (tries to) appends all the files in an single list of arguments (hence saving the calls to the script).
  If you would like to use a pipe in your `exec` command, use `sh` like below, or have a look [here](https://stackoverflow.com/questions/307015/how-do-i-include-a-pipe-in-my-linux-find-exec-command).

  ``` bash
  find . -name "*.log" -exec sh -c "tac {} | grep -m1 pattern" \;
  #
  find /path -name '*.pdf' -exec sh -c \
    'pdftotext "{}" - | grep -H --label="{}" --color " pattern"' \;
  ```

  * Mind that `find` does not know the content of `.bashrc` and alike, hence one could not use aliases (its `ls` command might be stripped-down with respect to what one is used to, you may want to consider adding some user-friendly options).

  <!-- -->

  * `-ok`: like `exec` but ask the permission first

  * `-execdir`: like `exec` but run the command from the subdirectory that contains the matched file.

* Delete all the matching files: e.g. delete all the `.log` files `find . -name *.log -delete`

  * `-delete` calls `rm` under the hood, in fact it is practically equivalent to `-exec rm`.
    Hence it will fail if one tries to delete directory.
    In this case, use the long way: `-exec rm -r {} \;`.
    You may add `-prune` to avoid some warnings/errors.
    Moreover, one may add quote around braces to avoid errors with names that contains whitespaces.

* Filter on file-age: `-mtime N`, selects all files older than `N` days.

## Compressing: `tar` & `zip`

### `tar`

`tar` is a utility which creates archives

* Basic usage:

  * `c`, `-c`, `--create`: create.
    Remember to put all the files that you want in your archive in one go.

    ``` bash
    tar -cf archived.tar file/to/archive
    ```

  * `x`, `-x`, `--extract`, `--get`: extract

    ``` bash
    tar -xf archived.tar
    ```

  * As you have already understood, `-f` stands for file(name).

* Additional options:

  * `t`, `-t`, `--list`: list the files.

  * `r`, `-r`, `--append`: add files to an existing archive. Does not work on compressed files.

  * `u`, `-u`, `--update`: add to the archive only the files which are already present and which have been modified.

  * `A`, `-A`, `--catenate`, `--concatenate`: concatenate archives.

  * Symbolic links: by default, `tar` keeps the links.
    If in the archive one wants a *copy* of the *original* file to which the link points to, option `-h|--deeference` should be used.

  * `-C`, `--directory <path>`: execute from `path` (e.g. decompress inside a given directory)

* Compression algorithms:

  * Zip (compress), `-z`, `--gzip`, `--gunzip`, `--ungzip`: use compression algorithms.
    The option has to be used also when extracting compressed archived.
    Usually, compressed archived have `.tar.gz` or `.tgz` as extension.

  * `-j`, `--bzip2`

  * `-J`, `xz`

* Compress an existing tarball: see [here](https://unix.stackexchange.com/questions/457949/how-to-turn-a-tar-file-to-a-tgz-file)

  ``` bash
  gzip < my_files.tar > my_files.tgz
  ```

### `zip`

A cross-platform extension for compressed files is `zip`.

* To compress simply run

  ``` bash
  zip [options] <compressed_file>.zip <files_to_compress>
  ```

  * If `<compressed_file>.zip` already exists, files are added

* To deflate, run `unzip <compressed_file>.zip`

* By default it adds links as hard-files (and not as links).
    Use option `-y` to store as link

* `-r` (mneno: *r*ecursive): include also (sub)directories and their files

* `-j` (mnemo: *j*unk): ignore subdirectory structure

### `gzip`

`gzip` is a compression format for Unixes.

``` bash
gzip [options] <compressed_file>.gz <files_to_compress>
```

### `7zip`

* Base command is `7z*`, it can be installed with `p7zip`

* Create zip

  ``` bash
  7za a <compressed_file>.7z <files_to_compress>
  ```

* Extract zip: `command` can be `e` (extract without directories), or `x` (with full paths)

  ``` bash
  7za <command> <compressed_file>.7z
  ```

## `awk`

`awk` is a text-processing utility that allows to perform easily operations line-by-line with column (here called *fields*) manipulations.
A tutorial is given [here](https://www.tutorialspoint.com/awk/index.htm).

* Basis: `awk [opt] 'BEGIN{[...]} {[...]} END{[...]}' <file>`

  * The commands in the curly brackets after `BEGIN` are executed before starting the reading of the file,

  * The commands in the unnamed curly brackets are executed at each line,

  * The commands in the curly brackets after `END` are executed once the file has been read,

  * Each of these three sections is optional;

* A conditional statement (called *pattern*) may be put just before the unnamed braces.
    Binary operations or comparisons can be used.
    If present, the commands inside are applied only to the rows verifying the pattern; if not, to all the rows.
    E.g.:

  * print the third row: `awk 'NR==3{print;exit}' file.txt`

  * print lines containing `apple`:
    `awk 'BEGIN{print "We eat an"}/apple/' file.txt` (print is implied)

  * More than one pattern might be used. No particular syntax is needed: nothing, a space or a newline will do the trick

    ``` bash
    awk \
      '/apple/{print "Found apple"}/banana/{print "Found banana"}' \
      infile
    ```

* Select the `n`-th field `$<n>`.
    Remark: it is 1-based (first field is indexed by 1), and `$0` expands to the whole line.

* Printing: it is usually achieved by command `print`.
    Some notes

  * Columns are accessed with a dollar `$`, for variables just use their name

    ``` bash
    awk '{print $NF}' file # Print last column only
    awk -v T=8 'END{print "2 times T = " 2*T}' file
    ```

  * One can use redirection such as `>`, `>>` as explained [above](#shell). E.g.:

    ``` bash
    awk 'BEGIN{print Ciao > "ciao.txt"}' file
    ```

  * `print` it also prints a new line stamp at the end

  * `printf`, very similar to the `C` function, it can be used to choose the format. Differently from `print`, it does not insert a new line.
    E.g., (mind the `\n`):

    ``` bash
    awk '{printf("I want %5.2f bananas\n", 1.652)}' file
    ```

* Useful options:

  * The file name is given as argument of the command or with `-f <file>`, or `--file=<file>`.

  * `-F <char>`, `--field-separator="<char>"`: `char` is the column separator (space is default);

  * Pass an argument: `-v var_name=<value>`

  * When using `gawk` (the GNU implementation of `awk`) one can asks for in-place replacement: `-i inplace`.

* Built-in variables:

  * `NF`: number of fields / columns in the current row (hence `$NF` is the last column of the row)

  * `NR`: row number, mind that it is incremented if several files are read (1 based).

  * `FNR`: row number relative to current file.
    It resets to 1 every time a new file is read.

  * `FS`: field separator

  * `FILENAME`: should I explain?

  * `ENVIRON`: array with environment variables (e.g., try `ENVIRON["USER"]`).

* Built-in functions:

  * `toupper(.)`, `tolower(.)`: Upper-, lowercase

  * `cos(.)`, `sin(.)`, `atan2(.)`, `sqrt(.)`, `exp(.)`, `log(.)`, `rand(.)`,

* Tricks:

  * [String-Manipulation functions](https://www.gnu.org/software/gawk/manual/html_node/String-Functions.html)

  * Operator "match", `~` (tilde): `<string>~<pattern>` true if `string` matches `pattern`.
    The negation is `!~`.
    Hence, the following emulates `grep `(well, not exactly since we search in the second column only, but you get the idea)

    ``` bash
    awk '$2~/<pattern>/{print $0}' file.txt
    ```

## Shell commands and tools

* `echo`: print a line to standard output. E.g. `echo "Ciao World"`. It
  includes a newline at the end. It could be used via piping to provide
  an input parameter to a command.

  * Variables can be used. Suppose you have `what="cute puppy"`, then
    one can use

    ``` bash
    echo "I want a ${what}"
    ```

  * For redirection to files have a look [above](#shell).

  * `-n`: do not to insert a new line at the end.

  * `-e`: interpret a backslashed character, e.g. `\n` will be considered as newline

  * Overwrite: use `\b` (needs option `-e`) to go back a character.
    For entire lines, have a look [here](https://stackoverflow.com/questions/11283625/overwrite-last-line-on-terminal).

* [`script`](https://man7.org/linux/man-pages/man1/script.1.html): save a shell session (commands and outputs) to a file

  ``` bash
  script session.log
  [commands here]
  exit
  ```

  * End the recording with `exit`

  * `-q`: quiet mode (do not print `script`-related “greetings”)

  * `-a`: *a*ppend to file

  * `-c <cmd>`: record command `cmd` only (without starting an interactive session)

* `eval [args]`: `args` are concatenated to build and run a command.
  Variables can be used:

  ``` bash
  cmd="ls"
  echo "I will now $cmd in dir"
  eval $cmd dir
  ```

* Working with remote servers:

  * `ssh`

    * Connect to server: `ssh [opt] [user@]server`.
        A new session open (a password may be requested).
        Use option `-X` (or `-Y`) to enable forwarding of the GUI, that is enabling GUI programs on the server

    * For connections that requires an identification, one may skip the typical “insert the password” method by adding a `ssh` key to the authorized one.
        See [here](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server) how:

      ``` bash
      ssh-copy-id username@remote_host
      ```

      or simply add your public key to `$HOME/.ssh/authorized_keys` of the server

    * Run command on a server: `ssh [opt] [user@]server cmd` (or `'cmd'`)

  * Transfer data, `rsync` or `scp`: `rsync file.txt server:/home/user/path/to`.
    Notice the colon.

    * `scp`: it’s the inter-server equivalent of `cp`, it has basically the same options and usage

      * In order to copy hidden files append a dot "`.`". E.g.:

        ``` bash
        scp -r [...] source/. user@server:dest/
        ```

        If `source` is the current directory it is better to do (incompatibility introduced by 2019 standard): `scp -r [...] $(pwd) user@server:dest/`.
        However, a good alternative for this kind of needs is `rsync`

    * `rsync`: has a syntax similar to `mv` or `cp`.
        As the name suggests, it is a sort of synchronization tool, hence you can customize the effect so that only most recent and freshly edited files are moved.
        Indeed, it can be use entirely locally, for instance to update a copy / backup.
        If no destination is provided, `rsync` will behave similarly to `ls`.

      * `--copy-links`: copy as file `vs.` `--links`: copy as link.

      * `--info=progress2`: progress bar for global transfer (not per file)

      * `--exclude=<pattern>`: exclude files matching the pattern.  `--exclude-from=<file>`: read a file where each line is a pattern, if a file matches one of them, it is excluded

      * `--include=<pattern>`: it’s more a *NEVER EXCLUDE* than an include. For an *include-only*–like process, look [here](https://unix.stackexchange.com/questions/2161/rsync-filter-copying-one-pattern-only): basically, exclude everything, then include back and include back again the *only*

        ``` bash
        rsync --include='*.pdf' --include='*/' --exclude='*' \
          src dest
        ```

    * ATTENTION: `scp` and `rsync` load the `.bashrc` and fail if it produces an output to `stdout` (for instance, if they contain commands such as `echo`).
        The workaround is to move those commands into `.bash_profile` (or just send the output to `/dev/null` if it is not important)

* `chmod`: change file permissions. See this [article](https://www.pluralsight.com/blog/it-ops/linux-file-permissions)

  * Typically, when looking at the permission of a file / repository via `ls -l`, the results is given by a 10-character chain divided

    * The first character indicates the type of file: `-` regular file, `d` directory or `l` link

    * The remaining characters are subdivided in 3 groups: the first refers to the permissions of the owner of the files, the second to the permission of the group, the third to the permissions of other users

    * The first element of each group refers to reading permission, `r` if granted, `-` otherwise; the second element to the writing one, `w` or `-`, the third to the execution permission, `x` or `-`

    * E.g., `drwxr-xr--` signifies a directory on which the owner has reading, writing and execution permissions; the group reading and execution; other users reading only

  * Typical commands:

    * Extended format: `chmod [options] <target><operator><permission> filename`

      * `target` can be one of or a combination of the following characters: `u` to change user permissions, `g` group, `o` other permissions, `a` is valid and is equivalent to `ugo`

      * `operator` is one of the followings: `+` to add permissions, `-` to remove, `=` to force permission to be exactly what provided

      * `permission` is one of or a combination of the following characters: `r` to express reading permission, `w` writing one, `x` execution one.

      * `-R` option to recursively apply in the case of a directory

      * E.g., `chmod ug+x foo`: add to file `fool` execution permission for user and group

    * Numerical format: `chmod <X><Y><Z> filename`

      * `X` is a digit that refers to user permissions, `Y` to group ones, `Z` to other users one

      * In numerical format, no permission (e.g., `-`) corresponds to 0, execution permission to 1, writing to 2, and reading to 4

      * Sums are allowed, hence 5=1+4 means execution and reading permissions

      * This command sets the permissions, hence is equivalent to the usage of `=` from the previous format

      * To obtain `-rwxr-xr--` one should use 754

* Download with command line: `wget` and `curl`

  * Basic stuff [here](https://linuxconfig.org/download-file-from-url-on-linux-using-command-line)

  * With proxy [here](https://www.cyberciti.biz/faq/linux-unix-curl-command-with-proxy-username-password-http-options/); `-x` option with `curl`; with `wget` you may want to export environmental variable `http[s]_proxy`.

* `date [+"FMT"]`: get current date/time.
    Some of the instructions to build the format string follow:

  * `%H`, `%M`, `%S`: hours, minutes, seconds

  * `%T`, `%r`, `%R`: `%H:%M:%S`, hour in 12-hours format, hour in 24-hours format

  * `%Y` (`%y`), `%m`, `%W`, `%d`: year (last two digits only), month, week, day

  * `%F`, `%D`: equivalent to `%Y-%m-%d` and `%m/%d/%y` respectively

  * `%x`, `%X`: respectively, date and hours according to region setting

* Send email from terminal (because, why not. And yes, I have tried it in order to transfer a file from the cluster to my machine): look [here](https://www.tecmint.com/send-email-attachment-from-linux-commandline/), a quick [tutorial](https://www.interserver.net/tips/kb/linux-mail-command-usage-examples/).

  ``` bash
  echo "Message Body Here" | \
      mailx -s "Subject Here" -a attachment.txt user@example.com
  echo "Message Body Here" | \
      mail -s "Subject Here" -A attachment.txt user@example.com
  ```

  * Other useful options:

    * `-c me@me.me`: CC-address

    * `-b me@me.me`: BCC-address

    * `-r me@me.me`: sender address

  * Use file as body of the message: option `-q file.txt`.
    **However**, this might not work as expected: if the command finds non-standard charcters, even new-lines (!) instead of using the text it will attach it as a binary file.
    The following might work (see this [SO discussion](https://unix.stackexchange.com/a/522868/502731)):

    ``` bash
    tr -cd "[:print:]\n" < file.txt | \
        mailx -s "Subject Here" user@example.com
    ```

* `wc`: `shell` command to perform some basic counting operations on a file (mnemonic: *w*ord *c*ount):

  ``` bash
  wc [options] <file>
  ```

  * `-c`: print number of bytes;

  * `-w`: print number of words;

  * `-l`: print number of lines;

  * `-m`: print number of characters;

  * `-L`: print max line length;

  * It usually (at least with `-l`) re-prints the file name.
    To avoid use: `wc -l < file.txt` (notice `<`);

* `sort [OPTIONS] [FILE]`

  * if `FILE` is `-` or not given, it uses `stdin`

  * `-r`: `r`everse

  * `-u`: `u`nique

  * `-t <SEP>`: use `SEP` instead of blank space as field separator

  * `-f`: case insensitive

  * ...and many others, check the man.

* `uniq`: filter for repeated adjacent lines. Let me stress: only adjacent lines are checked

  * `-c`: prefix line with number of occurrences

  * `-d`: print repeated lines only

  * `-u`: print unique lines only

* `touch <file>`: modify the file access and/or modification date.
    If the file doesn't exist, an empty one will be created (unless specific options are given).
    For more details and all the options, have a look at its `man` page.
    Why should one use it?

  * Changing the modification date of a file will force a smart compiler such as `make` to re-run the compilation.

* [`convert`](http://www.imagemagick.org/script/convert.php): very powerful tool for manipulating images (part of the [`ImageMagick`](https://imagemagick.org/index.php) suite, some [tips](http://www.imagemagick.org/script/command-line-processing.php))

  * Convert: `convert test.<ext1> test.<ext2>` the extension can be `pdf`, `jpg`, `png`,...

  * Rotate: `-rotate <deg>`

  * Put images side by side: use [`montage`](https://legacy.imagemagick.org/Usage/montage/) (which is part of the `ImageMagick` suite, [indeed](https://imagemagick.org/script/montage.php)), see [here](https://stackoverflow.com/questions/20737061/merge-images-side-by-side-horizontally).
    E.g., `montage img_[01234].png -tile 2x2 -geometry 10x10 out.png`, where `-tile` gives set the structure of the final image and `-geometry` the spacing between images

  * Choose density\|quality (and hence the final size): option `-density <n>` (its unit is `dpi`)

  * Reduce size: `-size <n>%` the output will have be the `n`% of the initial size

  * Mirror image: `-flip` vertical (meaning top becomes bottom) axis, `-flop` horizontal axis (meaning right becomes left)

  * Extract images from an animated `gif`: `convert in.gif out.png` and it will save images like `out-0.png`, `out-1.png`, `out-2.png`...

  * Write text on image: see [here](https://stackoverflow.com/questions/23236898/add-text-on-image-at-specific-point-using-imagemagick)

* See node architecture: [`lstopo`](https://linux.die.net/man/1/lstopo)

  ``` bash
  # Try also png for instance
  lstopo --output-format svg > topology.svg
  # Without graphic support
  lstopo-no-graphics --output-format txt > topology.txt
  ```

* [`pdfjam`](https://github.com/DavidFirth/pdfjam#using): nice and easy utility to modify `pdf` files

  * Extract and/or merge: Examples of accepted ranges: `’1,6-9’`, `’-2,4,6’`

    ``` bash
    pdfjam [options] -- file_1.pdf ['<page_range>'] \
                       [file_2.pdf ['<page_range>'] ...]
    ```

  * Rotate: Commands specified for certain angles are available: `pdf90|180|270 <in.pdf>`

  * Landscape mode: `--landscape`

  * Keep size: `--fitpaper true`

  * Autorotate oversized pages: `--totateoversize true`

  * More than one page per page: `--nup <cols>x<rows>`, e.g.,
    `--nup 2x1`

  * In fact, under the hood `pdfjam` calls LaTeX and loads the pdf into a page.
    This is enough most of the time, however, if the pdf has non-standard dimensions, let say smaller than A4, this will result in a blank A4 page with the pdf at the center.
    To fit to the size, use `ghostscript` (for the pages, the option `-sPageList` is also available and accepts ranges)

  * A similar utility with a wider range of capabilities is [`ghostscript`](https://www.ghostscript.com/doc/current/Use.htm)

    * `ghostscript` can output in many forms, called *devices* (even OCR!), [here’s how](https://ghostscript.com/docs/9.54.0/Devices.htm)

  ``` bash
  gs -dBATCH -dNOPAUSE -dSAFER -sDEVICE=pdfwrite -dPSFitPage \
     -dFirstPage=2 -dLastPage=5 -o out.pdf in.pdf
  ```

* Job management:

  * `kill [options] <job_ID>`: kill (send `SIGTERM` to) the job denoted by `<job_ID>`.

  * `pgrep [options] <pattern>`: print info, especially the job-IDs, of all the jobs matching `<pattern>`.
    Option `-l` lists the names as well (and not only the IDs).

  * `pkill [options] <pattern>`: as `kill` but looks for matches in job names before (as `pgrep`).

  * Options for `pgrep|pkill`

    * `-c`: count

    * `-l|-a`: lists names/fully

    * `-n|-o`: newest/oldest only

    * `-x`: select if name is exact

    * `-u UID`: only for user `UID`

    * `-s SIG`: send signal `SIG`

* `[h]top`: `top` (and its user-friendly version `htop`) gives an overview of a running system. One can find, for instance and just to name the most useful features, which jobs are running and how much memory or processors are used.

  * Filter: use option `-p <ID>`.
    Using the job name instead of the ID is more convenient: have a look at [this](https://unix.stackexchange.com/a/347544): `` top -p `pgrep -d "," <name>` ``.

* `du`: shows the space used by the directories (and files) (mnemonic: *d*isc *u*sage)

  * `-a|--all`: show the space of every files, not only the directories

  * `-h|--human-readable`: use convenient units (MB,GB,...)

  * `-d|--max-depth=<n>`: how many levels down the directory-tree `du` should search

  * `--exlude=<pattern>`: well, I think you get it

* `df`: check disk space info about the system (mnemonic: *d*isk *f*ree / *f*ilesystem)

* `time`: run programs and summarize system resource usage (from `man`).
    `time my_script.sh`; get the execution time of the script.
    More insight [here](https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1/556411#556411).

* `uname`: print system info

* “Safely remove” disks from command line: use `udisksctl` as explained [here](https://askubuntu.com/questions/532586/what-is-the-command-line-equivalent-of-safely-remove-drive):

  ``` bash
  udisksctl unmount -b /dev/sdX
  udisksctl power-off -b /dev/sdX
  ```

* Con*cat*enate files and print to standard output (basically print the content to screen)

  * `cat [<opt>] file [file2 [...]]`

  * `tac [<opt>] file [file2 [...]]` as above but reverse order of the lines

* Print a small part of a file

  * `head`: print the first part of a file

    * `-n [-]N`: first `N` lines; if `-` given, all but the last `N`

    * `-c [-]N`: as above but bytes instead of lines

  * `tail`: print the last part of a file

    * `-n [+]N`: last `N` lines; if `+` given, all but the first `N`

    * `-c [+]N`: as above but bytes instead of lines

    * `-f`: output appended as file grows (kinda of syncing)

* `cp [options] <source> [dest]`: copy `source` into `dest` (if omitted, "`.`")

  * `-t`: target. `cp -t dest -- <source>` is equivalent to `cp <source> [dest]`

  * `-r`: recursive, useful for directories

  * `-u`: copy only if there is no file with the same name in `dest` or if `source` is newer (mnemonic: *u*nique)

  * `-p`: preserve mode, ownership, and time-stamps

  * `-l`: (hard) link source instead of copy

  * `-L`: if `source` is a (symbolic) link, copy the file it points to instead of copying the link

* `crontab`: job scheduling.
    It allows one to regularly run some commands or scripts.
    Tutorial [here](https://www.adminschoice.com/crontab-quick-reference) or [here](https://www.computerhope.com/unix/ucrontab.htm).

* `tee`: read from standard input and write to standard output **&** files.
    Useful when you want to save the output of a command to file but you still want to read it on screen.
    E.g.:

  ``` bash
  echo "This'll be printed to screen and inside f.txt" | tee f.txt
  ```

  * `-a`: append to file.

  * Print to screen & pipe: `./script | tee /dev/tty | ./script_with_pipe`

* `bc`: shell calculator (mnemonic: `b`asic `c`alculator)

  * Some examples [here](https://www.geeksforgeeks.org/bc-command-linux-examples/).

  * How to

    * Simply run `bc` and an interactive interface will open (similar to what you get when you run `python`).
    Type `quit` for...yeah, quitting.

    * If you do not need extensive calculation but have just a one-liner expression, just pass it to `bc`: `echo "20+5" | bc` or `bc <<< "20+5"`

  * Operators like `++`, `*=`, etc. are accepted

  * Give option `-l` to load the standard math library and, for instance, deal with floating point calculation and use standard functions (e.g. sine `s(x)`).

* `tr`: *tr*anslate, squeeze and/or delete characters from standard input.
    Basically performs string operations on standard input.
    Some options and examples

  * `echo Maaan | tr a e`: change `a`’s into `e`’s, hence the result is `Meeen`.

  * `-d`: *d*elete. `echo Maaan | tr -d a` gives `Mn`

  * `-s`: *s*queeze. `echo Maaan | tr -s a e` replaces each sequence of repeated `a`’s with a single occurrence of `e`, hence it gives `Men`.

  * Change case: `echo "$str" | tr "[:lower:]" "[:upper]"`

* `xargs`: use standard output to build commands (you can think of it as a more powerful way of piping).
    Have a look at some tutorials [here](https://shapeshed.com/unix-xargs/) and [here](https://www.thegeekstuff.com/2013/12/xargs-examples/).
    Typical call is (the 0-related flags deal with files with spaces in their names)

  ``` bash
  find . -name foo -print0 | xargs -0 rm
  ```

  * `-t`: print the command

  * `-p`: prompt a user-confirmation before executing the command

  * `-n <n>`: group the inputs by `n`.
    That is, instead of (braces added for the sake of explanation) `{1} {2} {3} {4}`, with `-n 2` one gets `{1 2} {3 4}`.

  * `-I`: enables `xargs` to execute multiple commands.
    In this case, `%` is the placeholder for the input (sort of `{}` in `find -exec`)

  * `-a <file>`: read from `file` instead of standard output

* `cut`: cut out part of the content of the input.
    Typical call is:

  ``` bash
  cut -f 2-5 text.txt
  ```

  print only columns (`f`ields) 2 to 5 of the content of file `text.txt`.

  * `-f <list>` (or `--fields`): print only fields in the list

  * `-b <list>` (or `--bytes`): same as above but with bytes

  * `-c <list>` (or `--characters`): same as above but with characters

  * `-d <,>`: use `<,>` as delimiter for fields

  * List examples: `n` or `n-m` or `-n` or `n-`

* `comm`: compare two files: `comm -<n> <(sort file_1) <(sort file_2)`

  * Files must be **sorted**

  * Variable `n` is a combination of `1`, `2`, and `3`. `1` / `2` means suppress lines unique to `file_1/2`, `3` means suppress shared lines

  * Keep lines from `file_1` only `comm -23 <(sort file_1) <(sort file_2)`

  * Keep lines from `file_2` only `comm -13 <(sort file_1) <(sort file_2)`

  * Typically, one calls `while getopts ":<option_list>" opt; do [...] done`.
    One may want to use a `case` environment to deal with the options.

  * Here above, `option_list` contains the list of accepted options.
    If the option is followed by a `:` (colon) it means that it requires arguments.
    The argument is stored in the macro `$OPTARG`.

  * `\?` stands for an invalid/unknown option, `:` (colon) for an option for which an argument is required but not provided.

* Extract from path (considered as a string): `dirname` (root) and `basename`.
    E.g.: consider the following `path/to/file.txt`.
    Then `dirname` returns `path/to`, whereas `basename` `file.txt`.

* Convert from HEX to RGB colors from command line

  ``` bash
  hex="11001A"
  printf "%d %d %d\n" 0x${hex:0:2} 0x${hex:2:2} 0x${hex:4:2}
  ```

* [`pandoc`](https://pandoc.org/): convert from and to (almost) any markup languages, such as LaTeX, `markdown`, `html`, Word, `reStructured Text`, `epub`, `pdf`,...

* `getopts`: built-in command of `bash` which allows to parse options and arguments passed to a script.
    Two quick and well-done tutorials can be found [here](https://www.computerhope.com/unix/bash/getopts.htm) and [here](https://sookocheff.com/post/bash/parsing-bash-script-arguments-with-shopts/).
    We provide a hand-made example below.

```bash
#!/bin/bash

usage () {
  echo "Usage: script.sh [ -p prefix ] [ -s suffix ]"
}

prfx=""
sffx=""

OPTIND=1 # Variable used by getopts, reset if it has already been used

while getopts ":hp:s:" opt; do
  case "${opt}" in
    h )
      usage
      exit 0
      ;;
    p )
      prfx=${OPTARG}
      ;;
    s )
      sffx=${OPTARG}
      ;;
    : )
      echo "-${OPTARG}: An argument is required" 1>&2
      usage
      exit 1
      ;;
    \? )
      echo "-${OPTARG}: Unknown option" 1>&2
      usage
      exit 1
      ;;
  esac
done

shift $((OPTIND-1)) # Shift processed options

echo "PFX = ${prfx}"
echo "SFX = ${sffx}"
```
