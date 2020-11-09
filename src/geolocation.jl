# AUTO GENERATED FILE - DO NOT EDIT

export geolocation

"""
    geolocation(;kwargs...)

A Geolocation component.
The CurrentLocation component gets geolocation of the device from the web browser.  See more info here:
https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `local_date` (String; optional): The local date and time when the device position was updated.
Format:  MM/DD/YYYY, hh:mm:ss p   where p is AM or PM
- `timestamp` (Real; optional): The Unix timestamp in seconds from when the position was updated
- `position` (optional): (dict)The position of the device.  Lat, lon, and accuracy will always be returned.  The other data will be included
when available, otherwise it will be NaN.
A dictionary with the following keys:
      lat:  latitude in degrees,
      lon: longitude in degrees,
      accuracy: accuracy of the lat/lon in meters,

      When available:
      alt:  altitude above mean sea level in meters,
      altAccuracy:  accuracy of the altitude  in meters,
      heading: compass heading in degrees,
      speed:  speed in meters per sec,. position has the following type: lists containing elements 'lat', 'lon', 'accuracy', 'alt', 'altAccuracy', 'heading', 'speed'.
Those elements have the following types:
  - `lat` (Real; optional)
  - `lon` (Real; optional)
  - `accuracy` (Real; optional)
  - `alt` (Real; optional)
  - `altAccuracy` (Real; optional)
  - `heading` (Real; optional)
  - `speed` (Real; optional)
- `position_error` (optional): Position error. position_error has the following type: lists containing elements 'code', 'message'.
Those elements have the following types:
  - `code` (Real; optional)
  - `message` (String; optional)
- `show_alert` (Bool; optional): If true, error messages will be displayed as an alert
- `watch_position` (Bool; optional): (boolean; default False).  If false, position is obtained as an asynchronous request.  If true, then  position data
is updated when either the location changes or more accurate information becomes available
- `update_now` (Bool; optional): (boolean; default False).  Forces a one-time update to the position data.   If set to True in a callback, the browser
  will update the position data and reset update_now back to False.  This can, for example, be used to update the
 position with a button or an interval timer.
- `high_accuracy` (Bool; optional): (boolean; default False).   If true and if the device is able to provide a more accurate position,
 it will do so. Note that this can result in slower response times or increased power consumption (with a GPS
 chip on a mobile device for example). If false (the default value), the device can save resources by
 responding more quickly and/or using less power.
- `maximum_age` (Real; optional): The maximum age in milliseconds of a possible cached position that is acceptable to return. If set to 0,
it means that the device cannot use a cached position and must attempt to retrieve the real current position.
If set to Infinity the device must return a cached position regardless of its age. Default: 0.
- `timeout` (Real; optional): The maximum length of time (in milliseconds) the device is allowed to take in order to return a position.
The default value is Infinity, meaning that data will not be return until the position is available.
"""
function geolocation(; kwargs...)
        available_props = Symbol[:id, :local_date, :timestamp, :position, :position_error, :show_alert, :watch_position, :update_now, :high_accuracy, :maximum_age, :timeout]
        wild_props = Symbol[]
        return Component("geolocation", "Geolocation", "dash_more_components", available_props, wild_props; kwargs...)
end

