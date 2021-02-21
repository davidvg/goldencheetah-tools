# Activity file structure

[Back](../README.md)

This file explains the structure of the JSON file for an activity.

All the analysis is done in a [Jupyter Notebook](../notebooks/json-structure.ipynb).


## The `RIDE` key

The JSON file has a root key called `RIDE`, with the following subelements:

- `STARTTIME`
- `RECINTSECS`
- `DEVICETYPE`
- `IDENTIFIER`
- `TAGS`
- `INTERVALS`
- `SAMPLES`

### Start Time (`STARTTIME`)

The date and time when the activity starts.

It's stored as a `string` with the following format:

```
'2020/08/21 09:26:28 UTC '
```

> **Important**: there is a trailing space in the string. This happens with all the attributes that are stored in strings.

### Recording interval (`RECINTSECS`)

The recording interval, in seconds.

It's stored as an `int`. In most devices, defaults to 1 second.

### Device (`DEVICETYPE`)

The recording device. Stored as a `string`, with a trailing whitespace:

```
'Polar V650 '
```

### Identifier (`IDENTIFIER`)

Unused. A `string` object, just a whitespace.

### Tags (`TAGS`)

Contains a dictionary, storing multiple metrics for the ride (athlete, average power, elevation gain...). Each of its elements, each *tag* value, is stored as a `string` with a trailing whitespace:

```
tags[key] = "value "
```

Depending on the tag, the value should be converted to a more suitable type: `int`, `float`, `list` (for example, to store the changes history), `datetime`, `string`, etc.

### Intervals (`INTERVALS`)

A list of dictionaries, each of them defining an interval (lap). Some of these intervals will be converted to segments (routes) by defining them as such in GoldenCheetah, and appended to `<athlete>/config/routes.xml`.

Each interval defines the following elements:

- `NAME`: the name of the interval. Defaults to `Int N`, being `N` an increasing index. Trailing whitespace.
- `START`: the total seconds count for the first point in the interval. Stored as an `int`.
- `STOP`: the total seconds count for the last point in the interval. Stored as an `int`.
- `COLOR`: the color it will show in the interface. Stored as a `string` with the format `#nnnnnn`.
- `PTEST`: whether the interval is a performance test or not. Stored as a `string` containing `true` or `false`.

### Samples (`SAMPLES`)

A list of every trackpoint for the activity. A trackpoint is stored as a dictionary with elements:

- `SECS`: total seconds from the beginning of the activity (`float`).
- `KM`: total accumulated distance from the beginning of the activity, in km (`float`).
- `WATTS`: instantaneous power, in Watts (`int`).
- `CAD`: instantaneous cadence, in rpm (`int`).
- `KPH`: instantaneous speed, in km/h (`float`).
- `HR`: instantaneous heart rate, in beats per minute (`int`).
- `ALT`: elevation for this point, in meters (`float`).
- `LAT`: latitude for this point, in degrees (North-positive (`float`))
- `LON`: longitude for this point, in degrees (East-positive (`float`))
- `SLOPE`: computed slope for this point, in percentage (`float`).
