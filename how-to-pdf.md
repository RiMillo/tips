# How to get a `pdf` version

We used to rely on LaTeX, the [original file](deprecated/tips.tex) is still kept.
We recently switched to `markdown` for a better navigation online.
However, for a local, offline navigation, it is still possible to get a `pdf`.
Here is how:
1. Install `Sphinx` and `MyST-parser`

    ```shell
    pyhon3 -m pip install Sphinx~=8.2 myst-parser~=4.0
    ```

2. Get inside the root directory of this repository and simply launch `make latexpdf`.
    One might need to get `latexmk` and some `LaTeX` modules.

3. You will find the result in `_build/latex/tips.pdf`.
