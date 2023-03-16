
try:
    import tkinter as tk      
except ImportError:
    import Tkinter as tk
from os.path import join
import tempfile

import zipfile
import math
from pymol import cmd, finish_launching, plugins
from pymol.cgo import *

wd = None
finish_launching()

dirpath = tempfile.mkdtemp()
zip_dir = "out.zip"
wd = os.getcwd()
with zipfile.ZipFile(zip_dir) as hs_zip:
    hs_zip.extractall(dirpath)

os.chdir(dirpath)
cmd.set("normalize_ccp4_maps", "0")
cmd.load("hotspot/apolar.ccp4", "apolar_hotspot")
cmd.isosurface(name="surface_apolar_hotspot", map="apolar_hotspot", level="5")

cmd.color("yellow", "surface_apolar_hotspot")
cmd.set("transparency", 0.2, "surface_apolar_hotspot")
cmd.load("hotspot/donor.ccp4", "donor_hotspot")
cmd.isosurface(name="surface_donor_hotspot", map="donor_hotspot", level="5")

cmd.color("blue", "surface_donor_hotspot")
cmd.set("transparency", 0.2, "surface_donor_hotspot")
cmd.load("hotspot/acceptor.ccp4", "acceptor_hotspot")
cmd.isosurface(name="surface_acceptor_hotspot", map="acceptor_hotspot", level="5")

cmd.color("red", "surface_acceptor_hotspot")
cmd.set("transparency", 0.2, "surface_acceptor_hotspot")
cmd.group("hotspot", members="apolar_hotspot")
cmd.group("hotspot", members="surface_apolar_hotspot")
cmd.group("hotspot", members="donor_hotspot")
cmd.group("hotspot", members="surface_donor_hotspot")
cmd.group("hotspot", members="acceptor_hotspot")
cmd.group("hotspot", members="surface_acceptor_hotspot")
cmd.load("hotspot/buriedness.ccp4", "buriedness_hotspot")
cmd.isosurface(name="surface_buriedness_hotspot", map="buriedness_hotspot", level="3")

cmd.color("gray", "surface_buriedness_hotspot")
cmd.set("transparency", 0.2, "surface_buriedness_hotspot")
cmd.group("hotspot", members="buriedness_hotspot")
cmd.group("hotspot", members="surface_buriedness_hotspot")
cmd.pseudoatom(object="PS_apolar_hotspot_0", pos=(-42.5, -2.5, -2.0), color=(1, 1, 1), label=21.6)

cmd.pseudoatom(object="PS_apolar_hotspot_1", pos=(-43.25, -2.0, 1.0), color=(1, 1, 1), label=20.8)

cmd.pseudoatom(object="PS_apolar_hotspot_2", pos=(-43.5, -2.0, -1.0), color=(1, 1, 1), label=21.6)

cmd.pseudoatom(object="PS_apolar_hotspot_3", pos=(-45.25, -1.0, 0.5), color=(1, 1, 1), label=20.9)

cmd.pseudoatom(object="PS_apolar_hotspot_4", pos=(-45.0, -1.5, -1.0), color=(1, 1, 1), label=21.6)

cmd.pseudoatom(object="PS_apolar_hotspot_5", pos=(-31.25, -18.25, -0.5), color=(1, 1, 1), label=13.9)

cmd.pseudoatom(object="PS_apolar_hotspot_6", pos=(-30.0, -18.25, -2.0), color=(1, 1, 1), label=14.8)

cmd.pseudoatom(object="PS_apolar_hotspot_7", pos=(-29.5, -17.5, 0.0), color=(1, 1, 1), label=16.6)

cmd.pseudoatom(object="PS_apolar_hotspot_8", pos=(-31.5, -18.0, 1.5), color=(1, 1, 1), label=16.6)

cmd.pseudoatom(object="PS_apolar_hotspot_9", pos=(-37.0, -5.0, 8.0), color=(1, 1, 1), label=16.5)

cmd.pseudoatom(object="PS_apolar_hotspot_10", pos=(-51.25, -16.25, -6.25), color=(1, 1, 1), label=12.1)

cmd.pseudoatom(object="PS_apolar_hotspot_11", pos=(-50.0, -16.0, -6.0), color=(1, 1, 1), label=13.9)

cmd.pseudoatom(object="PS_apolar_hotspot_12", pos=(-51.0, -17.5, -7.75), color=(1, 1, 1), label=12.6)

cmd.pseudoatom(object="PS_apolar_hotspot_13", pos=(-49.5, -17.0, -7.0), color=(1, 1, 1), label=13.9)

cmd.pseudoatom(object="PS_apolar_hotspot_14", pos=(-49.0, -15.0, -5.0), color=(1, 1, 1), label=13.9)

cmd.pseudoatom(object="PS_apolar_hotspot_15", pos=(-28.5, -3.25, -3.25), color=(1, 1, 1), label=12.1)

cmd.pseudoatom(object="PS_apolar_hotspot_16", pos=(-29.0, -3.25, -1.6666666666666643), color=(1, 1, 1), label=11.3)

cmd.pseudoatom(object="PS_apolar_hotspot_17", pos=(-29.0, -2.5, -5.0), color=(1, 1, 1), label=13.4)

cmd.pseudoatom(object="PS_apolar_hotspot_18", pos=(-51.0, -13.5, -6.0), color=(1, 1, 1), label=13.3)

cmd.pseudoatom(object="PS_apolar_hotspot_19", pos=(-38.5, -12.5, 13.5), color=(1, 1, 1), label=12.6)

cmd.pseudoatom(object="PS_apolar_hotspot_20", pos=(-40.0, -12.0, 15.5), color=(1, 1, 1), label=12.6)

cmd.pseudoatom(object="PS_apolar_hotspot_21", pos=(-40.5, -12.75, 13.75), color=(1, 1, 1), label=10.6)

cmd.pseudoatom(object="PS_apolar_hotspot_22", pos=(-42.0, -12.25, 15.75), color=(1, 1, 1), label=11.5)

cmd.pseudoatom(object="PS_apolar_hotspot_23", pos=(-42.5, -13.0, 14.0), color=(1, 1, 1), label=12.6)

cmd.pseudoatom(object="PS_apolar_hotspot_24", pos=(-30.75, -6.0, 4.5), color=(1, 1, 1), label=11.0)

cmd.pseudoatom(object="PS_apolar_hotspot_25", pos=(-32.0, -6.0, 3.0), color=(1, 1, 1), label=11.3)

cmd.pseudoatom(object="PS_apolar_hotspot_26", pos=(-24.0, -10.75, -2.25), color=(1, 1, 1), label=7.6)

cmd.pseudoatom(object="PS_apolar_hotspot_27", pos=(-26.5, -7.5, -3.0), color=(1, 1, 1), label=9.5)

cmd.pseudoatom(object="PS_apolar_hotspot_28", pos=(-25.5, -10.0, -3.0), color=(1, 1, 1), label=9.5)

cmd.pseudoatom(object="PS_apolar_hotspot_29", pos=(-25.0, -8.25, -2.25), color=(1, 1, 1), label=7.1)

cmd.pseudoatom(object="PS_apolar_hotspot_30", pos=(-23.5, -9.0, -1.5), color=(1, 1, 1), label=9.5)

cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_0")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_0")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_1")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_1")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_2")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_2")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_3")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_3")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_4")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_4")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_5")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_5")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_6")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_6")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_7")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_7")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_8")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_8")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_9")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_9")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_10")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_10")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_11")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_11")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_12")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_12")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_13")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_13")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_14")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_14")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_15")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_15")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_16")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_16")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_17")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_17")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_18")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_18")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_19")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_19")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_20")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_20")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_21")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_21")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_22")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_22")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_23")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_23")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_24")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_24")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_25")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_25")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_26")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_26")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_27")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_27")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_28")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_28")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_29")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_29")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_30")
cmd.group("label_apolar_hotspot", members="PS_apolar_hotspot_30")
cmd.pseudoatom(object="PS_donor_hotspot_0", pos=(-35.5, -6.5, 3.5), color=(1, 1, 1), label=30.7)

cmd.pseudoatom(object="PS_donor_hotspot_1", pos=(-44.5, -2.5, -2.0), color=(1, 1, 1), label=21.4)

cmd.pseudoatom(object="PS_donor_hotspot_2", pos=(-41.0, -5.0, 5.0), color=(1, 1, 1), label=21.0)

cmd.pseudoatom(object="PS_donor_hotspot_3", pos=(-49.5, -14.5, -5.0), color=(1, 1, 1), label=18.0)

cmd.pseudoatom(object="PS_donor_hotspot_4", pos=(-32.0, -8.0, 1.5), color=(1, 1, 1), label=16.2)

cmd.pseudoatom(object="PS_donor_hotspot_5", pos=(-26.5, -4.0, -0.5), color=(1, 1, 1), label=15.1)

cmd.pseudoatom(object="PS_donor_hotspot_6", pos=(-30.0, -2.0, -4.0), color=(1, 1, 1), label=15.0)

cmd.pseudoatom(object="PS_donor_hotspot_7", pos=(-31.5, -4.5, -0.5), color=(1, 1, 1), label=14.4)

cmd.pseudoatom(object="PS_donor_hotspot_8", pos=(-29.0, -7.0, 1.5), color=(1, 1, 1), label=14.2)

cmd.pseudoatom(object="PS_donor_hotspot_9", pos=(-27.5, -1.0, 0.5), color=(1, 1, 1), label=14.0)

cmd.pseudoatom(object="PS_donor_hotspot_10", pos=(-43.0, -2.5, 6.5), color=(1, 1, 1), label=14.0)

cmd.pseudoatom(object="PS_donor_hotspot_11", pos=(-27.5, -4.5, -4.5), color=(1, 1, 1), label=13.7)

cmd.pseudoatom(object="PS_donor_hotspot_12", pos=(-40.5, -13.5, 12.5), color=(1, 1, 1), label=13.4)

cmd.pseudoatom(object="PS_donor_hotspot_13", pos=(-42.5, -14.0, 12.5), color=(1, 1, 1), label=13.3)

cmd.pseudoatom(object="PS_donor_hotspot_14", pos=(-44.0, -13.5, 16.0), color=(1, 1, 1), label=11.0)

cmd.pseudoatom(object="PS_donor_hotspot_15", pos=(-31.5, -9.0, 5.0), color=(1, 1, 1), label=10.9)

cmd.pseudoatom(object="PS_donor_hotspot_16", pos=(-27.0, -5.5, 3.5), color=(1, 1, 1), label=10.8)

cmd.pseudoatom(object="PS_donor_hotspot_17", pos=(-43.0, -3.5, 9.0), color=(1, 1, 1), label=8.9)

cmd.pseudoatom(object="PS_donor_hotspot_18", pos=(-22.5, -10.0, -3.5), color=(1, 1, 1), label=8.6)

cmd.pseudoatom(object="PS_donor_hotspot_19", pos=(-37.0, -12.5, 9.5), color=(1, 1, 1), label=7.7)

cmd.group("label_donor_hotspot", members="PS_donor_hotspot_0")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_0")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_1")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_1")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_2")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_2")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_3")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_3")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_4")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_4")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_5")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_5")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_6")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_6")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_7")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_7")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_8")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_8")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_9")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_9")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_10")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_10")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_11")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_11")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_12")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_12")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_13")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_13")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_14")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_14")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_15")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_15")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_16")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_16")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_17")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_17")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_18")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_18")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_19")
cmd.group("label_donor_hotspot", members="PS_donor_hotspot_19")
cmd.pseudoatom(object="PS_acceptor_hotspot_0", pos=(-40.0, -4.0, -3.0), color=(1, 1, 1), label=21.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_1", pos=(-47.5, -2.0, -0.5), color=(1, 1, 1), label=20.8)

cmd.pseudoatom(object="PS_acceptor_hotspot_2", pos=(-40.0, -2.0, 1.5), color=(1, 1, 1), label=19.5)

cmd.pseudoatom(object="PS_acceptor_hotspot_3", pos=(-25.5, -4.5, -3.0), color=(1, 1, 1), label=18.2)

cmd.pseudoatom(object="PS_acceptor_hotspot_4", pos=(-45.0, -0.5, 4.5), color=(1, 1, 1), label=16.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_5", pos=(-47.5, -2.5, 5.5), color=(1, 1, 1), label=16.3)

cmd.pseudoatom(object="PS_acceptor_hotspot_6", pos=(-34.0, -17.5, 0.0), color=(1, 1, 1), label=15.8)

cmd.pseudoatom(object="PS_acceptor_hotspot_7", pos=(-35.5, -7.0, 5.5), color=(1, 1, 1), label=15.4)

cmd.pseudoatom(object="PS_acceptor_hotspot_8", pos=(-38.5, -1.5, 7.5), color=(1, 1, 1), label=14.7)

cmd.pseudoatom(object="PS_acceptor_hotspot_9", pos=(-37.5, -3.0, -1.5), color=(1, 1, 1), label=14.7)

cmd.pseudoatom(object="PS_acceptor_hotspot_10", pos=(-51.0, -12.5, -6.0), color=(1, 1, 1), label=14.5)

cmd.pseudoatom(object="PS_acceptor_hotspot_11", pos=(-49.0, -17.0, -6.5), color=(1, 1, 1), label=13.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_12", pos=(-42.5, -11.5, 16.5), color=(1, 1, 1), label=12.8)

cmd.pseudoatom(object="PS_acceptor_hotspot_13", pos=(-31.5, -17.0, 2.5), color=(1, 1, 1), label=12.3)

cmd.pseudoatom(object="PS_acceptor_hotspot_14", pos=(-29.0, -4.0, -6.0), color=(1, 1, 1), label=12.0)

cmd.pseudoatom(object="PS_acceptor_hotspot_15", pos=(-32.5, -5.5, 4.5), color=(1, 1, 1), label=11.3)

cmd.pseudoatom(object="PS_acceptor_hotspot_16", pos=(-30.5, -19.5, 1.5), color=(1, 1, 1), label=10.7)

cmd.pseudoatom(object="PS_acceptor_hotspot_17", pos=(-32.0, -3.5, -1.0), color=(1, 1, 1), label=10.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_18", pos=(-30.5, -19.5, -3.0), color=(1, 1, 1), label=10.6)

cmd.pseudoatom(object="PS_acceptor_hotspot_19", pos=(-34.0, -7.5, 3.5), color=(1, 1, 1), label=9.8)

cmd.pseudoatom(object="PS_acceptor_hotspot_20", pos=(-38.0, -14.0, 11.0), color=(1, 1, 1), label=9.8)

cmd.pseudoatom(object="PS_acceptor_hotspot_21", pos=(-27.5, -7.5, -1.0), color=(1, 1, 1), label=9.1)

cmd.pseudoatom(object="PS_acceptor_hotspot_22", pos=(-32.5, -7.5, 6.0), color=(1, 1, 1), label=8.4)

cmd.pseudoatom(object="PS_acceptor_hotspot_23", pos=(-52.0, -13.0, -9.5), color=(1, 1, 1), label=7.7)

cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_0")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_0")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_1")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_1")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_2")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_2")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_3")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_3")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_4")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_4")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_5")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_5")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_6")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_6")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_7")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_7")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_8")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_8")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_9")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_9")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_10")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_10")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_11")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_11")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_12")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_12")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_13")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_13")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_14")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_14")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_15")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_15")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_16")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_16")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_17")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_17")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_18")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_18")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_19")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_19")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_20")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_20")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_21")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_21")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_22")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_22")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_23")
cmd.group("label_acceptor_hotspot", members="PS_acceptor_hotspot_23")
cmd.group("labels_hotspot", members="label_apolar_hotspot")
cmd.group("labels_hotspot", members="label_donor_hotspot")
cmd.group("labels_hotspot", members="label_acceptor_hotspot")
cmd.load("hotspot/protein.pdb", "protein_hotspot")
cmd.show("cartoon", "protein_hotspot")
cmd.hide("line", "protein_hotspot")
cmd.show("sticks", "organic")


class IsoLevel(tk.Variable):
    def __init__(self, master, name, level):
        tk.Variable.__init__(self, master, value=level)
        self.name = name
        self.trace('w', self.callback)

    def callback(self, *args):
        cmd.isolevel(self.name, self.get())

    def increment(self, event=None, delta=0.1):
        self.set(round(float(self.get()) + delta, 2))

    def decrement(self, event=None):
        self.increment(None, -0.1)


surface_list = {'hotspot': {'fhm': ['surface_apolar_hotspot', 'surface_donor_hotspot', 'surface_acceptor_hotspot'], 'buriedness': ['surface_buriedness_hotspot']}}
surface_max_list = {'hotspot': {'fhm': 30.7, 'buriedness': 8}}

top = tk.Toplevel(plugins.get_tk_root())

master = tk.Frame(top, padx=10, pady=10)
master.pack(fill="both", expand=1)

for child in list(master.children.values()):
    child.destroy()


row_counter = 0
for identifier, component_dic in surface_list.items():
    # add calculation identifier
    tk.Label(master, text=identifier).grid(row=row_counter, column=0, sticky="w")
    row_counter += 1
    
    for component_id, surfaces in component_dic.items():
        # add collection label, e.g. superstar or hotspot etc.
        tk.Label(master, text=component_id).grid(row=row_counter, column=1, sticky='w')
        row_counter += 1
        
        for i, surface in enumerate(surfaces):
            # add grid type label
            probe = surface.split("_")[-2]
            tk.Label(master, text=probe).grid(row=row_counter, column=2, sticky="w")
            
            # slider code 
            v = IsoLevel(master, surface, 5)
            e = tk.Scale(master, orient=tk.HORIZONTAL, from_=0, to=surface_max_list[identifier][component_id],
                         resolution=0.1, showvalue=0, variable=v)
            e.grid(row=row_counter, column=3, sticky="ew")

            e = tk.Entry(master, textvariable=v, width=4)
            e.grid(row=row_counter, column=4, sticky="e")
            master.columnconfigure(3, weight=1)
            row_counter += 1




cmd.bg_color("white")
if wd:
    os.chdir(wd)