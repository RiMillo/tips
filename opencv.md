# Computer Vision with `OpenCV`

`OpenCV` is available for `C`, `python`, `Java`, and even `Android`.
We’ll try to be consistent and use `python` code examples, however, some of the provided links may concern other languages.
In any case, the tip will give the function to use and, if it is not the language of your predilection, you just have to adapt the call to the function to the language.
In fact, most of the time, we deal with general question about computer vision and not with the subtleties of a particular implementation.

Another popular computer vision `python` library is [`scikit-image`](https://scikit-image.org/).

* Docs and tutorials:

  * [Official documentation](https://docs.opencv.org/3.4/index.html) with tutorials and Doxygen with all functions

    * There are also nice [`ReadTheDocs` tutorials](https://opencv24-python-tutorials.readthedocs.io/en/latest/index.html).
      It dates back to 2016, but the general and basic ideas remains the same.

  * O’Reilly books

    * [With `C`](https://www.bogotobogo.com/cplusplus/files/OReilly%20Learning%20OpenCV.pdf)

    * [With `python`](http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf)
      (draft)

  * [`pyimagesearch`](https://www.pyimagesearch.com/): it is one of the best and well-known pages online for learning and working with computer vision problems (included machine learning techniques applied to vision applications)

    * You may want to check put its `python` library, [`imutils`](https://github.com/jrosebr1/imutils) which simplifies using `OpenCV`

  * [`GeeksForGeeks`](https://www.geeksforgeeks.org/) has nice tutorials on `OpenCv`

* The bases.
    `OpenCV` images are simply `numpy` matrices where each element of the matrix correspond to a pixel.
    However, there are some things that are worth mentioning explicitly.
    Let `W` and `H` be, respectively, the width and height in pixels of an image:

  * The origin, the pixel (0, 0), is the top left corner of the image

  * The vertical direction, let’s call it `y`, grows downwards: `y=0` corresponds to top edge, `y=H` corresponds to the bottom edge

  * `x` and `y` coordinates are switched, hence: `im[y,x,:]`

  * For one-channel images (e.g. gray scale), the matrix dimension is 2, that means that the shape is `(H,W)`; for `RGB` (however, see below) and `HSV` is 3, last dimension being 3, that means that the shape is `(H,W,3)`.

  * `OpenCV` uses `BGR` instead of the *usual* `RGB` structure.
    Hence, if you want to use `matplotlib` to show an image, one should convert it, here are two possible ways to perform the conversion

        # Use OpenCV functions
        img_cvt = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        # Use python: inverse order of last dimensionim[:,:,::-1]
        img_cvt = im[:,:,::-1]

  * Extract the green channel of an image: `green = im[:,:,1]`.
    Use `0` for blue, or `2` for red

  * Crop an image: simply use `numpy` slices

        crop = im[y_0:y_1, x_0:x_1, :]

  * `GBR` formats accepts values in $[0,\,255]^3$, `HSV` in $[0,\,120]\times[0,\,255]\times[0,\,255]$

  * The type of an element of a standard image is `numpy.uint8`

* [Morphological transformations](https://docs.opencv.org/4.5.2/d9/d61/tutorial_py_morphological_ops.html): erosion (separate zones), dilation (merge zones), opening (erosion then dilation), closing (dilation then erosion),...

* Thresholding: roughly speaking, in its simplest case, one chooses a threshold `T`, then all pixels with values less than `T` are set to `0`, the others to a user-defined value.
    See [these](https://docs.opencv.org/3.4/db/d8e/tutorial_threshold.html) [three](https://www.pyimagesearch.com/2021/04/28/opencv-thresholding-cv2-threshold/) [tutorials](https://www.pyimagesearch.com/2021/05/12/adaptive-thresholding-with-opencv-cv2-adaptivethreshold/).

      # Simplest thresholding
      T = 125; final_value = 255
      _, th = cv.threshold(im, T, final_value, cv.THRESH_BINARY)

* Color-range–based segmentation.
    We give the rule of thumb for using `inRange` as presented in the [tutorials](https://docs.opencv.org/3.1.0/df/d9d/tutorial_py_colorspaces.html): let `clr[RGB]` (or whatever other color code) the target color; transform it into `HSV`, `clr[HSV]` (usually, it has full `S` and `V` values, which in `OpenCV` translates to 255: for instance `blue[HSV]=[120,255,255]`); then use as lower bound `[clr[HSV][H]-D, L, L]` and as upper bound `[clr[HSV][H]+D, 255, 255]` with `D=10` and `L=50`. You may adjust `D` and `L`.

      clr = cv.cvtColor(np.uint8([[[R,G,B]]]), cv.COLOR_RGB2HSV)
      D = 10; L = 100
      lower = np.uint8([clr[0,0,0]-D,  L,  L])
      upper = np.uint8([clr[0,0,0]+D,255,255])
      # Segmentation
      mask = cv.inRange(hsv.copy(), lower, upper)

  * Red colors can be hard to extract, see for instance [here](https://stackoverflow.com/a/32523532)

  * Segmentation with black and white can be a little tricky.
    One may try to use simple thresholding, otherwise see this [answer](https://stackoverflow.com/a/25401596).

* Histogram and histogram / lighting correction: see [here](https://docs.opencv.org/4.5.0/d5/daf/tutorial_py_histogram_equalization.html)

  * Histogram equalization, `equalizeHist` works globally on the image.
    Sometimes, the results does not meet the expectations

  * CLAHE works locally, on a small windows, `createCLAHE([clip,tile])`.
    The results are often more natural than those obtained with the histogram equalization.
    CLAHE needs two parameters: the tile is the window, the clip is a threshold.
    If an histogram bin is above this limit, the related pixels are redistributed uniformly.

* Intensity transformation: see [here](https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/) and [here](https://docs.opencv.org/4.5.0/dc/dfe/group__intensity__transform.html) for the functions already included in `OpenCV` but only in `C`

* Example of image matching and alignment: [here](https://www.pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/)

* Camera calibration:

  * Simple camera calibration, that is, for instance, fix lens deformations: use chessboard and/or AruCo, see basic stuff, insights and small tutorial [here](https://docs.opencv.org/master/dc/dbb/tutorial_py_calibration.html)

  * Fisheye cameras is trickier.
    Have a look at this [medium post](https://medium.com/@kennethjiang/calibrate-fisheye-lens-using-opencv-333b05afa0b0), this [tutorial](https://docs.opencv.org/3.2.0/dd/d12/tutorial_omnidir_calib_main.html) but also this [SO answer](https://stackoverflow.com/a/53500300) (and its referenced [link](http://paulbourke.net/dome/fish2/))
