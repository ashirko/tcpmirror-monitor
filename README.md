# tcpmirror-monitor

Script for displaying important debug information about [tcpmirror](https://github.com/SatisSoft/tcpmirror) instances.\
Tcpmirror-monitor shows number of connection between tcpmirror instance and data sources, and between tcpmirror instance and each data consumer.

Example of usage:
```
$ ./start_monitor.py example/example.toml
+----------------------------------------------------------+
|                         example                          |
+----------------+-------------+-------------+-------------+
| sources (NDTP) | vis1 (EGTS) | vis2 (NDTP) | vis3 (NDTP) |
+----------------+-------------+-------------+-------------+
|       35       |      1      |      0      |      35     |
+----------------+-------------+-------------+-------------+
```