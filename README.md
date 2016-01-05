# BLUME SOS adapter

A collection of scripts and configurations files to import air
quality sensor data into a [*52North SOS*][52North-SOS] instance.


## Usage

To export sensor data for each station you have to start up a
[*blume_messnet_api*][blume_messnet_api] instance. Make sure to
use the *52north-sos-importer* branch.
Then run the following script:

```
$ python export.py
```

To import the sensor data from the CSV files you need to start your
*52North SOS* instance (*PostgreSQL* and *Tomcat*).
Further, configuration files must be provided for each station.
Then run the following script:

```
$ python import.py
```

The script produces log files for each station. These provide
information about success or failure of the import.


## Author

* Tobias Preuss


## License

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


[52North-SOS]: https://github.com/52North/SOS
[blume_messnet_api]: https://github.com/johnjohndoe/blume_messnet_api/tree/52north-sos-importer
