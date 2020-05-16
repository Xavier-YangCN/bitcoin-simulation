#!/usr/bin/python
import argparse
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pathlib
import simulation

def main(configuration=0):
    big_simulation_bitcoin()

def big_simulation_bitcoin():
    t_start = 1
    t_end = 2000
    n_iterations = 4000
    plot_first_x_graphs = 0
    #avg_paths_after_n_iterations = [25, 50, 75, 100, 125, 150, 175, 200, 225]
    avg_paths_after_n_iterations = []
    initial_connection_filter = False
    with_evil_nodes = [False]
    y = list()
    initial_min = np.array([4, 8, 16, 24, 32, 48, 64, 96, 128, 192, 220, 256, 300, 700])
    #initial_max = (initial_min / min(initial_min) * 125 / (8 / min(initial_min))).astype('int').tolist()
    x = initial_min.tolist()

    x = [8]
    initial_max = [128]
    # outbound_distributions = ['hacky_1', 'const8_125', 'uniform_1_max', 'normal_mu8_sig4', '1percent',
    #                           'normal_mu_sig_auto', 'const13_125']
    outbound_distributions = ['const8_125']
    connection_strategy = ['stand_bc']
    # connection_strategy = ['stand_bc', 'p2c_min', 'p2c_max', 'geo_bc', 'no_geo_bc]
    max_outbound_connections = [8]
    for outbound_distribution in outbound_distributions:
        for min_init, max_init in zip(x, initial_max):
            for connection_strategy_element in connection_strategy:
                for outbound_number in max_outbound_connections:
                    s = simulation.Simulation(simulation_type='bitcoin_protocol', with_evil_nodes=False,
                                              connection_strategy=connection_strategy_element,
                                              initial_connection_filter=initial_connection_filter,
                                              outbound_distribution=outbound_distribution,
                                              data={'initial_min': min_init, 'initial_max': max_init})
                    y.append(s.run(t_start=t_start, t_end=t_end, n_iterations=n_iterations, plot_first_x_graphs=plot_first_x_graphs,
                                   #avg_paths_after_n_iterations=avg_paths_after_n_iterations,
                                   avg_paths_after_n_iterations=[],
                                   MAX_OUTBOUND_CONNECTIONS=outbound_number, numb_nodes=1000))
                    # if len(y) > 0:
                    #     plot_distribution(initial_min[: len(y)], y)


if __name__=='__main__':
    main()