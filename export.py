#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os


STATION_IDS = [
    "010", "018", "027", "032", "042", "077", "085", "115",
    "117", "124", "143", "145", "171", "174", "220", "282"
]


def export_station(host_address, station_id):
    """
    Export sensor data for a single station
    """
    # Prepare shell command arguments
    server_path = '{0}/api/v1/stations/{1}/csv' \
        .format(host_address, station_id)
    csv_file = 'berlin-station-{0}.csv'.format(station_id)

    # Prepare shell command
    command = 'curl {0} > {1}'.format(server_path, csv_file)

    # Run import
    click.secho("Exporting data for station #{0} now ..."
                .format(station_id), fg='green')
    click.secho("Command: {0}\n".format(command), fg='white')
    os.system(command)


@click.command()
@click.option('--host_address',
              prompt='Host address',
              default=os.path.expanduser('http://localhost:4567'),
              help='Host address of the Blume API.')
def export_stations(host_address):
    """
    Export sensor data for multiple stations.
    """
    click.secho("\nProcessing {0} stations ...\n"
                .format(len(STATION_IDS)), fg='blue')
    for station_id in STATION_IDS:
        export_station(host_address, station_id)


if __name__ == '__main__':
    print('Working directory = {0}'.format(os.getcwd()))
    export_stations()
