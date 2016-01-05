#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import datetime
import os


STATION_IDS = [
    "010", "018", "027", "032", "042", "077", "085", "115",
    "117", "124", "143", "145", "171", "174", "220", "282"
]


def import_station(sos_importer_feeder, station_id):
    """
    Import sensor data for a single station.
    Station ID is used to compile the correct file names.
    """
    # Prepare log file suffix (time stamp)
    now = datetime.datetime.now()
    log_file_suffix = now.strftime('%Y%m%d-%H%M%S')

    # Prepare shell command arguments
    configuration_file = './berlin-station-{0}-52n-sos-import-config.xml' \
        .format(station_id)
    data_file = './berlin-station-{0}.csv' \
        .format(station_id)
    log_file = './berlin-station-{0}-import-{1}.log' \
        .format(station_id, log_file_suffix)

    # Prepare shell command
    command = 'java -jar {0} -c {1} -d {2} > {3}' \
        .format(sos_importer_feeder, configuration_file, data_file, log_file)

    # Run import
    click.secho("Importing data for station #{0} now ..."
                .format(station_id), fg='green')
    click.secho("Command: {0}\n".format(command), fg='white')
    os.system(command)


@click.command()
@click.option('--sos_importer_feeder',
              prompt='Feeder',
              default=os.path.expanduser('./52n-sos-importer-feeder-bin.jar'),
              help='Path to 52n-sos-importer-feeder-bin.jar')
def import_stations(sos_importer_feeder):
    """
    Import sensor data for multiple stations.
    Expect path to the feeder.
    """
    click.secho("\nProcessing {0} stations ...\n"
                .format(len(STATION_IDS)), fg='blue')
    for station_id in STATION_IDS:
        import_station(sos_importer_feeder, station_id)


if __name__ == '__main__':
    print('Working directory = {0}'.format(os.getcwd()))
    import_stations()
