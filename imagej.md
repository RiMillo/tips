# `ImageJ` - `Fiji`

`ImageJ` is a `Java`-based image processing program especially adapted to scientific researches.
`Fiji` Is Just `ImageJ`, with many many plugins (you are advised to use this latter).
Just a couple of tools that I have used (so that I don’t forget them)

* Rotate: `Image > Transform > Rotate`

* Set origin: usually the origin (the point (0,0)) is the upper left corner of the image.
    You can however change it: `Image > Transform > Properties > Origin` (do you need the `Global` case?)

* Since the origin point is by default at the top of the image, the y axis, that is the vertical one, has positive values towards the bottom.
    Sometimes is destabilizing.
    Change it with `Analyze > Set measurements > Invert y`

* Set a dimension scale from a part of the image whose dimension is known: draw a line than `Analyze > Set scale`

* Perspective: `Plugins > Transform > Interactive perspective`

* Make points from two different images correspond.
    Consider this.
    You have some photo of the same thing but you are a bad photographer and all the pictures have their own perspective and angle.
    Well, choose a reference photo than make all the other correspond to it with `Plugins > Transform > Landscape correspondences`

* Macros: in order to automate your process, you may write your own macros.
    See `Plugins > Macros > [...]`
