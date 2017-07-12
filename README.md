# wrf_time
WRF timing report tool

WRF is Weather Research and Forecast model (http://www.wrf-model.org/).

This file reports Computing(+Halo exchange) and I/O time based on rsl.error.0000 file.

1. This script supports WRF nested domain.
2. This script understand WRF timer's hierachy so there is no duplicated timing for each step and domain in output.
3. If you are using "rsl.error.0000" file just executing this script will work or you can specify filename as argument

Here are sample output for two cases.

	$ wrf_time rsl_single_sample
	======================================================
	Computing Time       =     40.10201
	
	 [Domain]         Time    Average     Step
	       1      40.10201    0.22279      180
	======================================================
	I/O Time             =      8.04155
	
	 [Domain]      I/O_Sum         Read        Write
	       1       8.04155      4.07949      3.96206
	 -----------------------------------------------------
	  Domain <  I/O type >         Time    Average  Count
	 -----------------------------------------------------
	     1      read_input       0.81137    0.81137     1
	     1   read_boundary       3.26812    1.08937     3
	     1    write_output       3.96206    0.99052     4
	======================================================
	        ELAPSED TIME =     48.14356
	 (Some init*/final* routines are not included)
	======================================================
	$
	$ wrf_time rsl_3domain_sample
	======================================================
	Computing Time       =    188.73949
	
	 [Domain]         Time    Average     Step
	       1      24.43322    0.40722       60
	       2     109.43017    0.60794      180
	       3      54.87610    0.10162      540
	======================================================
	I/O Time             =     14.83397
	
	 [Domain]      I/O_Sum         Read        Write
	       1       6.39723      3.68931      2.70792
	       2       5.16996      1.66156      3.50840
	       3       3.26678      0.93579      2.33099
	 -----------------------------------------------------
	  Domain <  I/O type >         Time    Average  Count
	 -----------------------------------------------------
	     1      read_input       2.23231    2.23231     1
	     1   read_boundary       1.45700    1.45700     1
	     1    write_output       2.70792    1.35396     2
	 -----------------------------------------------------
	     2      read_input       1.66156    1.66156     1
	     2    write_output       3.50840    1.75420     2
	 -----------------------------------------------------
	     3      read_input       0.93579    0.93579     1
	     3    write_output       2.33099    1.16549     2
	======================================================
	        ELAPSED TIME =    203.57346
	 (Some init*/final* routines are not included)
	======================================================
	
