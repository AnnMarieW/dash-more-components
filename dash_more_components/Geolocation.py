# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Geolocation(Component):
    """A Geolocation component.
The CurrentLocation component gets geolocation of the device from the web browser.  See more info here:
https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- local_date (string; optional): The local date and time when the device position was updated.
Format:  MM/DD/YYYY, hh:mm:ss p   where p is AM or PM
- timestamp (number; optional): The Unix timestamp in seconds from when the position was updated
- position (dict; optional): The position of the device.  `lat`, `lon`, and `accuracy` will always be returned.  The other data will be included
when available, otherwise it will be NaN.

      `lat` is latitude in degrees.
      `lon` is longitude in degrees.
      `accuracy` is the accuracy of the lat/lon in meters.    *

      `alt` is altitude above mean sea level in meters.
      `altAccuracy` is the accuracy of the altitude  in meters.
      `heading` is the compass heading in degrees.
      `speed` is the  speed in meters per second. position has the following type: dict containing keys 'lat', 'lon', 'accuracy', 'alt', 'altAccuracy', 'heading', 'speed'.
Those keys have the following types:
  - lat (number; optional)
  - lon (number; optional)
  - accuracy (number; optional)
  - alt (number; optional)
  - altAccuracy (number; optional)
  - heading (number; optional)
  - speed (number; optional)
- position_error (dict; optional): Position error. position_error has the following type: dict containing keys 'code', 'message'.
Those keys have the following types:
  - code (number; optional)
  - message (string; optional)
- show_alert (boolean; default False): If true, error messages will be displayed as an alert
- update_now (boolean; default False): Forces a one-time update of the position data.   If set to True in a callback, the browser
  will update the position data and reset update_now back to False.  This can, for example, be used to update the
 position with a button or an interval timer.
- high_accuracy (boolean; default False): If true and if the device is able to provide a more accurate position,
 it will do so. Note that this can result in slower response times or increased power consumption (with a GPS
 chip on a mobile device for example). If false (the default value), the device can save resources by
 responding more quickly and/or using less power.
- maximum_age (number; default 0): The maximum age in milliseconds of a possible cached position that is acceptable to return. If set to 0,
it means that the device cannot use a cached position and must attempt to retrieve the real current position.
If set to Infinity the device must return a cached position regardless of its age. Default: 0.
- timeout (number; default Infinity): The maximum length of time (in milliseconds) the device is allowed to take in order to return a position.
The default value is Infinity, meaning that data will not be return until the position is available."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, local_date=Component.UNDEFINED, timestamp=Component.UNDEFINED, position=Component.UNDEFINED, position_error=Component.UNDEFINED, show_alert=Component.UNDEFINED, update_now=Component.UNDEFINED, high_accuracy=Component.UNDEFINED, maximum_age=Component.UNDEFINED, timeout=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'local_date', 'timestamp', 'position', 'position_error', 'show_alert', 'update_now', 'high_accuracy', 'maximum_age', 'timeout']
        self._type = 'Geolocation'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'local_date', 'timestamp', 'position', 'position_error', 'show_alert', 'update_now', 'high_accuracy', 'maximum_age', 'timeout']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Geolocation, self).__init__(**args)
