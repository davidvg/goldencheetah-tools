# Segments in GoldenCheetah

[Back](../README.md)

This file explains how user-defined segments are stored in the database.

## What info is in which file?

### Segments list

A list of all defined segments is stored in `config/routes.xml`, inside the athlete's folder.

This file has the following structure:

```xml
<routes>
    <route>
        <name>La Campa (por Villaviciosa)</name>
        <id>{cb6233a5-366f-46c4-bec6-c3a38aff714}</id>
        <points>
            <point><lat>42.8058</lat><lon>-5.64202</lon></point>
            ...
        </points>
    </route>
    <route>
        ...
    </route>
</routes>
```

However, there's no information about the activities containing each route (segment).


### Segments in activity files

Each json file in `activities` has a `INTERVALS` key where all the intervals (laps) are listed. These intervals can be generated in-route, by pressing the Lap button, or created in GoldenCheetah.

### Statistics on each segment

The file `<athlete>/cache/rideDB.json` stores all the metrics and data for all the activities and segments.

This file can be used to:

- Generate a list of all the activities containing a segment.
- Obtain the metrics for that segment's repetition.


## So, which file do I need?

- To generate a list of all segments: `config/routes.xml`.
- To know how many repetitions I've done for a segment: `cache/rideDB.json`.
- To know when I did a repetition for a segment: `cache/rideDB.json`, or search though all the activity files in `activities/`.
- To get metrics for a segment: `cache/rideDB.json`.
