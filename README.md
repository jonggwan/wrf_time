# wrf_time
WRF timing report tool

WRF is Weather Research and Forecast model (http://www.wrf-model.org/).

This file reports Computing(+Halo exchange) and I/O time based on rsl.error.0000 file.

1. This script supports WRF nested domain.
2. This script understand WRF timer's hierachy so there is no duplicated timing for each step and domain in output.
3. If you are using "rsl.error.0000" file just executing this script will work or you can specify filename as argument

Here are sample output for two cases.
