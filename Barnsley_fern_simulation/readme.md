## Theory

The Barnsley fern is a fractal named after the British mathematician Michael Barnsley who first described it in his book Fractals Everywhere. He made it to resemble the black spleenwort, Asplenium adiantum-nigrum.

The fern code developed by Barnsley is an example of an iterated function system (IFS) to create a fractal. This follows from the collage theorem. He has used fractals to model a diverse range of phenomena in science and technology, but most specifically plant structures.


# Pseudo_Code

draw all pixels on screen

x = 0.0
y = 0.0
t = 0.0
xn = 0.0
yn = 0.0
while t < maximum iterations:
    r = random() between 0 and 1
    if r < 0.01:
        xn = 0.0
        yn = 0.16 * y
    else if r < 0.86:
        xn = 0.85 * x + 0.04 * y
        yn = -0.04 * x + 0.85 * y + 1.6
    else if r < 0.93:
        xn = 0.2 * x - 0.26 * y
        yn = 0.23 * x + 0.22 * y + 1.6
    else:
        xn = -0.15 * x + 0.28 * y
        yn = 0.26 * x + 0.24 * y + 0.44
    draw green pixel on screen at (xn, yn)
    x = xn
    y = yn
    increment t

## Output
The animated output of the barnsley fern simulation can be observed as below:
<img width="593" height="782" alt="Screenshot 2025-11-24 at 21 29 43" src="https://github.com/user-attachments/assets/11e6a8d4-ad5b-4dc7-b8a0-d68902d72d71" />


The output of basic illustrated barnsley fern output can be observed as below:
![Screenshot 2025-11-24 at 21 30 42](https://github.com/user-attachments/assets/df3d180b-7b30-4bb8-8358-ac3a2c127b47)
