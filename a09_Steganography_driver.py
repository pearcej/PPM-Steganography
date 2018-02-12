######################################################################
# Author: Dr. Jan Pearce      TODO: Change this to your name(s)
# Username: pearcej           TODO: Change this to your username(s)
#
# Assignment: A09: PPM Steganography
#
# Note: This assignment may be completed alone or in a pair or programmers, but not more than 2.
# If you work in a pair, both partners must make committs to the repo
#
# Purposes:
# - deepen comfort in use of classes
# - use triply nested lists, considering memory management issues of shallow copy vs. deep copy
# - design algorithms for encryption/decryption and compute Big-O for each
# ######################################################################
# Acknowledgements:
#
# Original code written by Dr. Jan Pearce with modifications by Dr. Scott Heggen and additional
# modificatitons by Dr. Jan Pearce
#
# Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
# working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from ppm import *
# HINT: Be sure you work with a single ppm object at a time


def main():
    # The following interaction is just for testing.  You will improve this.

    wn = PPM_set_up()   # To use the PPM class, this must appear at the beginning of your program. You'll pass wn into
                        # the class init method when creating new PPM objects

    print("\nWelcome to the PPM introduction!\n")

    # Example using the default file
    ppmdefault = PPM(wn)
    ppmdefault.PPM_display()            # NOTE: This displays the image, but it's really small! It may be hard to find.
    print("---")

    # Example using a user-defined file
    filename = input("Please input name of PPM-P3 file: ")
    ppmobject = PPM(wn, filename)
    ppmobject.PPM_display()


    # TODO Add your own method calls for the methods you are completing/creating from scratch


    print("\nPush the Quit button to exit all files.")

    PPM_render(wn) # needed to render all of the images you have instantiated
    pass

main()
