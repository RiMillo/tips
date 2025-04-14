# `R`

* Docs

  * `R` [manuals](https://cran.r-project.org/manuals.html)

  * An [intro](https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf) to `R`

  * Other [docs](https://www.r-project.org/other-docs.html)

  * [Browse](https://www.rdocumentation.org/) functions and packages

* The [`tidyverse`](https://www.tidyverse.org/): a collection of useful library for data science.
    Here they are, find related cheat-sheets at the provided links

  * [`ggplot2`](https://ggplot2.tidyverse.org/): plotting

  * [`dplyr`](https://dplyr.tidyverse.org/): data manipulation

  * [`tidyr`](https://tidyr.tidyverse.org/): create and manage tidy data

  * [`readr`](https://readr.tidyverse.org/): utilities for reading data

  * [`purrr`](https://purrr.tidyverse.org/): working with functions and vectors (basically, stuff as `map()`)

  * [`tibble`](https://tibble.tidyverse.org/): modern version of data sets

  * [`stringr`](https://stringr.tidyverse.org/): working with strings

  * [`forcats`](https://forcats.tidyverse.org/): working with factors

* Install given version of package: from package `devtools` use, for instance,

      install_version("ggplot2",version="0.9.1"[,repos="http://cran.us.r-project.org"])

* [`reticulate`](https://github.com/rstudio/reticulate): get the best of `python` in `R`

* `R` is **1-based** (access first element of something with 1, `a[1]`)

* Unload a package: `detach('package:<pkg>', unload=TRUE)`

* `cbind` / `rbind`: combine by columns or rows, respectively

* Data frames:

  * Extract rows - use positional index: `row <- df[1:5,10:15]`

  * Extract columns - use headers: as lists / vectors `df$col1` (use dollar sign to access), as data frame `cols <- data.frame(df$col1, df$col2)`

* Statistical analysis

  * An [intro](https://cran.r-project.org/web/packages/HSAUR/vignettes/Ch_introduction_to_R.pdf) (well, at least a chapter)

  * A cheat-sheet [*for dummies*](https://www.dummies.com/programming/r/statistical-analysis-with-r-for-dummies-cheat-sheet/)

* Plotting and stuff: we will use [`ggplot2`](https://ggplot2.tidyverse.org/)

  * Basics:

    ```r
    plt <- ggplot(data = <data>) +
           <function>(mapping = aes(<args>)) [+
           <theme> [+ <color> [ +
           ggtitle('.') [+ xlab('.') [+ ylab('.')]]
           ]]]
    plt
    ```

    * `function` can be, for instance, `geom_point` for scatter-plots, `geom_boxplot`,...

    * `aes` sets the aesthetic of the plot, for instance, `linetype`, `color`... For instance, with scatter-plots, if you want to color the points according to a categorical variable `cat`, you can use `color = cat`

    * `theme`: choose the theme of the current plot: `theme_classic()`, `theme_bw()`,...

    * `color` sets additional colors, basically, `scale_fill_manual` or `scale_color_manual` according to the type of plot

    * `ggtitle`, `x|ylab`: plot title and x/y labels

  * Colors: a couple of [tutorials](http://www.sthda.com/english/wiki/ggplot2-colors-how-to-change-colors-automatically-and-manually#change-colors-by-groups) with [examples](https://www.datanovia.com/en/blog/ggplot-colors-best-tricks-you-will-love/)

  * Themes: set and [pimp](https://bookdown.org/rdpeng/RProgDA/building-a-new-theme.html) [your theme](https://ggplot2.tidyverse.org/reference/theme_get.html) (all options [here](https://ggplot2.tidyverse.org/reference/theme.html))

  * Nice tricks about [scatter-plots](http://www.sthda.com/english/wiki/ggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization).

* `Rstudio` is possibly the most well-known and used IDE for `R`

  * The `notebook` mode provide a very handy way of working with `R`.
    It is really similar to the one proposed with `jupyter` and `python`.
    Indeed, one can add the `R` engine to `jupyter`.
    However, the `R`-notebooks use the [`Rmarkdown`](https://rmarkdown.rstudio.com/index.html) language (here is a [cheat-sheet](https://raw.githubusercontent.com/rstudio/cheatsheets/master/rmarkdown-2.0.pdf) and a [reference guide](https://www.rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf), both are also available in the `Help` tab of `Rstudio`), which is indeed similar to [`markdown`](markdown.md)

  * `Rmarkdown` and plots: plots are usually included in the rendering.
    However, issues may arise when plots are inside loops.
    In this case, force them to appear with a `print` statement

  * [Debugging](https://support.rstudio.com/hc/en-us/articles/200713843?version=1.4.1717&mode=desktop) with `Rstudio`

    ```r
    for (i in 1:n) {
      plt <- <your_plot>
      print(plt)
    }
    ```

* Read from any file: use [`read.table`](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/read.table.html).
  One may choose between lots of options: `header`, `sep`, `dec`, `na.strings`, `comment.char`,...

* [Formatting strings](https://stackoverflow.com/questions/46085274/is-there-a-string-formatting-operator-in-r-similar-to-pythons)

* [Several ways](https://www.geeksforgeeks.org/printing-output-of-an-r-program/) of printing

* [Factors](https://www.datamentor.io/r-programming/factor/): a class for categorical variables

* Two packages may contain functions with the same names, hence the function from the most recently loaded package will prevail and mask the others.
  [Here](https://stackoverflow.com/questions/39137110/what-does-the-following-object-is-masked-from-packagexxx-mean) is a brief explanation.
  See a work around to specify the function: `<package>::foo`

* `lapply(lst, foo[, args])`: apply to every element of list or vector `lst` function `foo` with arguments `args` if provided / needed.
    It returns a list / vector with the same dimension as `lst`.
    Linked functions:

  * `sapply`: more user-friendly version of `lapply` returning vector, matrix or array

  * `vapply`: as `sapply` but the return value will have a pre-defined type, the same as `foo`

  * An alternative is the `map` function from `purrr`: [here](https://stackoverflow.com/questions/45101045/why-use-purrrmap-instead-of-lapply) is a comparison.
    Basically, `map` is more user-friendly, it is smart, meaning that it can interpret more compact inputs hence saving you some keystrokes, all the related functions are more consistent (among the `*apply`-like functions, some has the function as first arguments, others the functions)

## Notes on statistics and data analysis

* QQ-plots and how to analyze them: [here](https://www.ucd.ie/ecomodel/Resources/QQplots_WebVersion.html)
