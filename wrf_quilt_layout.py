#!/usr/bin/env python3
import argparse
import math

def calculate_wrf_layout(total_mpi, nio_groups, nio_tasks_per_group):
    # Calculate I/O and Compute tasks
    total_io = nio_groups * nio_tasks_per_group
    compute_tasks = total_mpi - total_io

    if compute_tasks <= 0:
        raise ValueError("Total MPI tasks must be greater than the total I/O tasks.")

    # Find all possible (X, Y) integer factor pairs for the compute_tasks
    factors = []
    for i in range(1, int(math.sqrt(compute_tasks)) + 1):
        if compute_tasks % i == 0:
            x1, y1 = i, compute_tasks // i
            factors.append((x1, y1))
            if x1 != y1:
                factors.append((y1, x1))

    # Rule 1: nproc_y MUST be >= nio_tasks_per_group
    valid_factors = [f for f in factors if f[1] >= nio_tasks_per_group]

    if not valid_factors:
        raise ValueError(
            f"Error: {compute_tasks} compute tasks cannot be decomposed "
            f"into a grid where nproc_y >= {nio_tasks_per_group}."
        )

    # Rule 2: For perfect load balancing, nproc_y should be perfectly divisible by nio_tasks_per_group
    optimal_factors = [f for f in valid_factors if f[1] % nio_tasks_per_group == 0]

    # Helper function to find the most "square" grid
    def closest_to_square(factor_list):
        return min(factor_list, key=lambda f: abs(f[0] - f[1]))

    # Selection Logic
    if optimal_factors:
        best_x, best_y = closest_to_square(optimal_factors)
        status = "OPTIMAL (nproc_y perfectly evenly distributes to I/O servers)"
    else:
        best_x, best_y = closest_to_square(valid_factors)
        status = "SUBOPTIMAL (Warning: nproc_y leaves uneven I/O patches, WRF may fall back to serial I/O)"

    return best_x, best_y, compute_tasks, status

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate WRF nproc_x and nproc_y from MPI tasks.")
    parser.add_argument("-t", "--total_mpi", type=int, required=True, help="Total number of MPI ranks")
    parser.add_argument("-g", "--nio_groups", type=int, default=1, help="Number of nio_groups (default: 1)")
    parser.add_argument("-n", "--nio_tasks", type=int, required=True, help="nio_tasks_per_group")

    args = parser.parse_args()

    try:
        nproc_x, nproc_y, compute, status = calculate_wrf_layout(
            args.total_mpi, args.nio_groups, args.nio_tasks
        )

        print("-" * 50)
        print(" WRF DECOMPOSITION CALCULATOR")
        print("-" * 50)
        print(f" Total MPI Ranks     : {args.total_mpi}")
        print(f" Quilt I/O Ranks     : {args.nio_groups * args.nio_tasks} "
              f"({args.nio_groups} groups of {args.nio_tasks})")
        print(f" Compute Ranks       : {compute}")
        print("-" * 50)
        print(f" Calculated nproc_x  : {nproc_x}")
        print(f" Calculated nproc_y  : {nproc_y}")
        print("-" * 50)
        print(f" Layout Status       : {status}")
        print("-" * 50)

    except ValueError as e:
        print(e)
