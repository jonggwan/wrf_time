# wrf_time
WRF timing report tool

WRF is Weather Research and Forecast model (http://www.wrf-model.org/).

This file reports Computing(+Halo exchange) and I/O time based on rsl.error.0000 file.

1. This script supports WRF nested domain.
2. This script understand WRF timer's hierachy so there is no duplicated timing for each step and domain in output.
3. If you are using "rsl.error.0000" file just executing this script will work or you can specify filename as argument

Here are sample output for two cases.

$ wrf_time rsl_single_sample
==========================================
Computing Time            =    44.53653

 |  [Domain 1]            =    44.53653
 \             / 180 Step =     0.24742
==========================================
I/O Time                  =     8.36059
 -----------------------------------------
 + [Domain 1]             =     8.36059
 -----------------------------------------
 |         (Read wrfinput) =     0.98687
 \               /  1 Time =     0.98687
 | (Read lateral boundary) =     3.35651
 \               /  3 Time =     1.11884
 |          (Write wrfout) =     4.01721
 \               /  4 Time =     1.00430
==========================================
   WRF TIME               =    52.89712
  (Some init* routines are not included)
==========================================
$
$ wrf_time rsl_3domain_sample
==========================================
Computing Time            =   621.46620

 |  [Domain 1]            =    72.27226
 \             / 180 Step =     0.40151
 |  [Domain 2]            =   348.31479
 \             / 540 Step =     0.64503
 |  [Domain 3]            =   200.87915
 \             /1620 Step =     0.12400
==========================================
I/O Time                  =    18.14045
 -----------------------------------------
 + [Domain 1]             =     7.99660
 -----------------------------------------
 |         (Read wrfinput) =     0.81861
 \               /  1 Time =     0.81861
 | (Read lateral boundary) =     3.28981
 \               /  3 Time =     1.09660
 |          (Write wrfout) =     3.88818
 \               /  4 Time =     0.97205
 -----------------------------------------
 + [Domain 2]             =     6.47674
 -----------------------------------------
 |         (Read wrfinput) =     1.04015
 \               /  1 Time =     1.04015
 |          (Write wrfout) =     5.43659
 \               /  4 Time =     1.35915
 -----------------------------------------
 + [Domain 3]             =     3.66711
 -----------------------------------------
 |         (Read wrfinput) =     0.63532
 \               /  1 Time =     0.63532
 |          (Write wrfout) =     3.03179
 \               /  4 Time =     0.75795
==========================================
   WRF TIME               =   639.60665
  (Some init* routines are not included)
==========================================



