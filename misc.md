# Miscellaneous

* \[Linux\] Add personal apps to regular menu: It comes down to create `your_app.desktop` file in <a href="~/.local/share/applications" class="uri">~/.local/share/applications</a>.
    You can get inspiration from other similar files that are already there or in <a href="/usr/share/applications" class="uri">/usr/share/applications</a>.
    Another idea is to use the user-interface `alacarte`, see [here](https://askubuntu.com/questions/79583/adding-custom-applications-to-gnome-3-launcher):
    this produces a `.desktop` file, usually the name is little something like `alacarte-n.desktop`, so it might be hard to see which file corresponds to which app.

* \[Linux\] Install without root rights.
    * **DEB**. Following [this SO answer](https://askubuntu.com/a/350):

        ```bash
        dpkg -x package.deb dir
        ```

    * **RPM**. Following [this SO answer](https://superuser.com/questions/209808/how-can-i-install-an-rpm-without-being-root):

        ```bash
        # Optional but advised since it extract inplace
        mkdir foo
        cd foo
        rpm2cpio foo.rpm | cpio -idv
        ```

* `PETSc` [manual](https://www.mcs.anl.gov/petsc/petsc-current/docs/manual.pdf)

  * Use `MatView(Mat a, PETSC_VIEWER_DRAW_WORLD)` or with any another `PetscViewer` to draw the nonzero structure of a matrix.

* Create QR-codes: [here](https://www.qrcode-monkey.com/) is a pretty simple, 100% free and highly customizable QR-code generator.
