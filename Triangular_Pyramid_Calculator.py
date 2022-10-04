#!/usr/bin/env python3
# Made by Jaydin Madore
# Made on 2022-09-27
# Calculates the volume of a Triangular Pyramid


import math

print("the base of your triangular pyramid must be = to each other.")


def main():
    base = float(input("what is the Base "))
    base_height = float(input("what is the Height "))
    base_area = 1 / 2 * base * base_height
    print("Area of your Triangular base is: {0:.2f}cm^2 ".format(base_area))
    pyramid_height = float(input("what is the Pyramid height "))
    pyramid_area = 1 / 2 * pyramid_height * base
    print(
        "Area of one side of your Triangular Pyramid is: {0:.2f}cm^2".format(
            pyramid_area
        )
    )
    volume = 1 / 3 * base_area * pyramid_height
    print("Volume of your Triangular Pyramid is: {0:.2f}cm^3".format(volume))

    surface_area = base_area + pyramid_area + pyramid_area + pyramid_area
    print("Surface area is: {0:.2f}cm^3".format(surface_area))


if __name__ == "__main__":
    main()
