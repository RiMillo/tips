# `gnuplot`

* Keep the plot-windows open after closing the platform / having run the script: `gnuplot --persist`

* Scripts: A script is just a sequence of `gnuplot` commands.

  * There is no official extension, although the most common are: `gpi` (recognized by `vim`), `plt`, `gp`, `gnu`.

  * To launch: `gnuplot script.gpi` from terminal, or `load 'script.gpi'` inside a `gnuplot` session

* Variables: simply `var = 8.5`, or `var = 'smth'`

* New figure: `set term xterm <n>` where `n` is the ID

* Basic plotting from file: e.g. use column 1 as x and 2 as y (mind `u` is equivalent to `using`)

      plot "file.dat" using 1:2 [options]

* Size of the picture: `set <width>,<height>`

* Multiple plots in the same picture. Usually, when executing `plot`, the old picture is cleared. To plot several curves separate them with a comma or use `replot`. Indeed, the following

      plot "file.dat" u 1:2 [options], "file2.dat" u 1:3 [options]

  is equivalent to

      plot "file.dat" u 1:2 [options]
      replot "file2.dat" u 1:3 [options]

* Subplots: `set multiplot <n_rows>,<n_cols>` dispose the following plots in `n_rows`$\times$`n_cols` structure.
    Each `plot`-like command will automatically switch to the following slot in the structure.

* Save:

  1.  Change terminal to the chosen output: `set term postscript`, for `.ps` files.
    Use `png` for `.png` files instead.
    In this latter case, you can choose the size in pixels: `set term png size 600,400`

  2.  Choose name (according to the output): `set output "plot.ps"`

  3.  Plot into file: `replot`

  4.  Go back to initial terminal: `set term x11`

* Column separator: for instance, with a `.csv` file one would use `set datafile separator ','`

* Column names/headers: if columns has names/headers, you can use them instead of indices, using `(column('name'))`.
    Yes, the brackets are necessary

      plot file u (column('time')):(column('price'))

* If a plot is already shown, and you run a `set <cmd>` command, this will be active starting from the next `plot`-like command only.
    Hence, you may want to run a `replot` to update the figure with the new setting.

* Log scale: `set log x|y`

* Plot title: `set title 'Plot title'`

* Axis labels: `set x|ylabel 'Label'`

* Legend:

  * Deactivate: `unset key` or `set nokey`

  * Place: `set key <pos>` where `pos` may assume: `left top`,..., `outside`

  * If columns have names and you want to use as legend labels: `set key autotitle columnhead`

* Axis limits: `set x|yrange [<min>:<max>]` or simply put `[<xmin>:<xmax>] [<ymin>:<ymax>]` after plot

* Color cycles: `set colorsequence default|classic|podo`

* Loops: have a look [here](https://stackoverflow.com/a/18592561) and [here](https://stackoverflow.com/a/14947085).
    From the first link (`word` extract a word from a string)

      colors = "red green #0000FF"
      files = "file1 file2 file3"
      plot for [i=1:words(files)] word(files, i).'.dat' lc rgb word(colors, i)

Useful options of `plot`-like commands:

* `linecolor|lc`: e.g. `lc "black"`.
    For more advance setting: `linetype rgb "<parameters>"`

* `with|w`: lines and marks `linespoints`, lines/marks only `lines|points`, `impulses` (default: `points` only)

* `pointtype <n>` (or `pt`): set style `n` for the point.
    There are also `pointsize` (or `ps`)

* `title "<legend_entry>"`. If columns have names, `title columnhead`

* `linewidth|w`

* Solid/dashed lines: `dashtype` or `dt`

  * `dt N`: predefined type

  * `dt "<pattern>"`: custom pattern where `pattern` is a combination of dots, hyphens, underscores and spaces

  * ATTENTION: set dash type before giving line type: `plot x:sin(x) dt 1 w linespoints`

* Check out `linetype|lt` too (doc [here](http://www.gnuplot.info/docs_4.2/node62.html))

General coding tips:

* Define variables: `var="this_is_a_var"`, `list="this is a list"`

* Concatenate, “`.`” (dot): `"var holds '".var."'"`

* Number of words in a list: `words(list)`

* Loops:

  * General structure

        do for [j=1:10] {
          # do something
        }

  * Even inside commands: `plot for [i=1:100] 'data'.i.'.dat' u 1:2 title 'Flow '.i`
