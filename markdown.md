# `markdown`

* `markdown` files are usually used for `README` and such.

* Common extension: `.md`, `.markdown`

* Compile them with `pandoc` in order to get an `html` or a `pdf`, for instance, that you can open with a browser.

    ```shell
    pandoc --from=markdown --to=html -o out.html in.md
    ```

* Guides, cheat-sheets and tutorials: [official `markdown`](https://daringfireball.net/projects/markdown/syntax), [`GitHub`-flavoured](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax), [`GitLab`-flavoured](https://docs.gitlab.com/ee/user/markdown.html), [`GitHub` cheat-sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), quick [cheat-sheet](https://commonmark.org/help/) and a [tutorial](https://agea.github.io/tutorial.md/) and [cheat sheet again](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf).

* Special text: *italic* `*italic*` or `_italic_`; **bold** `**bold**` or `__italic__`; code / `typewriter` `` `typewriter` `` (backticks); ~~strikethrough~~ `~strikethrough~` or `~~strikethrough~~`

    * Superscript: `html`-tag `1<sup>st</sup>`. Subscript: same with tag `sub`

* Links: e.g. `[Shown label](https://link.to)`

  * One can even link sections of the current file (notice: all lowercase letters, blanks converted into dashes):

    ```markdown
    # Section One
    Here is a section.
    # Section Two
    Here is a [link](#section-one) to the previous section.
    ```

  * Alternative:

    ```markdown
    A [text][id].

    [id]: https://url.com "The title"
    ```

  * [Footnotes](https://github.blog/changelog/2021-09-30-footnotes-now-supported-in-markdown-fields/):

    ```markdown
    A simple footnote[^1]. Some text after.

    [^1]: The long footnote
    ```

  * Bibliography: with standard syntax (plus a bit of `html`), see [here](https://stackoverflow.com/questions/26587527/cite-a-paper-using-github-markdown-syntax)

    ```markdown
    "...the **go to** statement should be abolished..." [[1]](#1).

    ## References
    <a id="1">[1]</a>
    Dijkstra, E. W. (1968).
    Go to statement considered harmful.
    Communications of the ACM, 11(3), 147-148.
    ```

* Images: similar to links, prepend a “!”: `![Alternative description text](path/to/img.png)`

  * The image is rendered **inline**

  * Without the “!”, it will be a link

  * URLs are accepted as valid path, especially in READMEs for online repositories.

  * See [this section](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images) of the GitHub documentation for notions about relative paths

  * Centering images: `markdown` does not support it and one should switch to `html` syntax. Mind that not all `markdown` interpreters can deal with `html`, however, rest assure, GitHub and GitLab can.
    See [here](https://stackoverflow.com/questions/12090472/how-do-i-center-an-image-in-the-readme-md-file-on-github)

    ```markdown
    <div align="center">
    <img src="path/to/img.png" alt="Alternative description text"/>
    </div>
    ```

    Sometimes using `<p align="center"> ... </p>` works as well

* Render code: main idea use backticks, “`‘`”

  * [GitHub docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#quoting-code) (for more [advanced settings](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks))

  * Display: three backticks with, optionally, the language of the code to highlight syntax as well.
    E.g., python and terminal (see [here](https://stackoverflow.com/a/49004070/12152457)) examples:

    <pre><code>```python
    for i in range(5):
        if i % 2 == 0:
            print("Even")
        else:
            pass
    ```</code></pre>

    <pre><code>```console
    foo@bar:~$ whoami
    foo
    ```</code></pre>

    * [Official list](https://github.com/github-linguist/linguist/blob/3c3b037910006fc2f1a9bb34b2c4e9cde062206c/lib/linguist/languages.yml) of languages supported by GitHub and their definitions.
    For a non-official but user-friendly (and possible incomplete) list, see [here](https://github.com/jincheng9/markdown_supported_languages?tab=readme-ov-file#heres-a-full-list-of-supported-languages)

  * Inline: one backtick `` `code goes here` ``

    * Syntax highlighting is not available for inline code with default renderers. However, some extensions can, see this [SO question](https://stackoverflow.com/questions/23226224/inline-code-syntax-highlighting-in-github-markdown): `` `a = None`{:.python} `` or `` `a = None`{.python} ``

* Citations, references, bibliography: similar to links, see [here](https://stackoverflow.com/questions/26587527/cite-a-paper-using-github-markdown-syntax).

  * Reference sections

    ```markdown
    # A section
    ...
    [Link to the section](#a-section)
    ```

  * Reference a point: create an anchor with `html`, `<a name="ref"></a>` then reference it.
    See [here](https://stackoverflow.com/a/7335259/12152457)

  * Reference a enumeration item: that’s not that straight-forward and take advantage of `html` syntax, have a look [here](https://stackoverflow.com/a/37148268/12152457)

* Math&Equations:

  * `GitLab`:

    * Inline: dollar+backticks, e.g., `` $`\alpha`$ ``

    * Display: double dollar, e.g., `$$ \alpha $$` or code-block

      <pre><code>```math
      \alpha
      ```</code></pre>

  * `GitHub`

    * [Official docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)

    * Inline: dollar, e.g., `$\alpha$`

    * Display: double dollar, e.g., `$$ \alpha $$` or code-block

      <pre><code>```math
      \alpha
      ```</code></pre>

    * \[Deprecated workaround\] However, there seems to be some workarounds, see [here](https://stackoverflow.com/questions/11256433/how-to-show-math-equations-in-general-githubs-markdownnot-githubs-blog) (linking to third-party render) or [here](https://gist.github.com/cyhsutw/d5983d166fb70ff651f027b2aa56ee4e) (write LaTeX code inside a `jupyter` notebook, for tips about LaTeX and `jupyter` see [`python` page](python.md), and/or [here](https://jupyterbook.org/content/math.html))

* Render keyboard keys: use `html` tag `kbd`: `Select all: <kbd>Ctrl</kbd> + <kbd>A</kbd>`.

* Warning, note, tip,...: see [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)
  (also [this SO question](https://stackoverflow.com/questions/50544499/how-to-make-a-styled-markdown-admonition-box-in-a-github-gist)).
  Available keywords: `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION`.
  Every keyword has its own rendering style.
  Example:

      > [!NOTE]
      > Useful information that users should know, even when skimming content.

* `grip`: `python`-based script which allows you to have a `GitHub` rendering of your documents (needs internet to send request for translation to `GitHub`).

* Draw graphs and charts with [`mermaid`](https://mermaid-js.github.io/mermaid/#/): all the info about syntax and configuration are in the link

  * A [live editor](https://mermaid-js.github.io/mermaid-live-editor)

* Collapsed section: use `html` tags `<details>` and `<summary>`.
    Tested on [GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections)

      <details>

      <summary>Tips for collapsed sections</summary>

      ### You can add a header

      You can add text within a collapsed section.
      You can add an image or a code block, too.

      </details>
