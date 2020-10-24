# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CurrentLocation(Component):
    """A CurrentLocation component.
The CurrentLocation component gets geolocation of device from the web browser.  See more info here:
https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- local_date (string; optional): The local date and time when the device position was updated.
Format:  MM/DD/YYYY, hh:mm:ss p   where p is AM or PM
- isodate_UTC (string; optional): The UCT (zulu) time  when the device position was updated. ISO Format: YYYY-MM-DDThh:mm:ss
- isodate_local (string; optional): The local time when the device position was updated. ISO Format: YYYY-MM-DDThh:mm:ss
- position (dict; optional): The position of the device. position has the following type: dict containing keys 'latitude', 'longitude', 'altitude', 'accuracy', 'altitudeAccuracy', 'heading', 'speed'.
Those keys have the following types:
  - latitude (number; optional)
  - longitude (number; optional)
  - altitude (number; optional)
  - accuracy (number; optional)
  - altitudeAccuracy (number; optional)
  - heading (number; optional)
  - speed (number; optional)
- position_error (dict; optional): Position error. position_error has the following type: dict containing keys 'code', 'message'.
Those keys have the following types:
  - code (number; optional)
  - message (string; optional)
- watch_position (boolean; default False): (boolean; default False).  If false, position is obtained as an asynchronous request.  If true, then  position data
is updated when either the location changes or more accurate information becomes available
- update_now (boolean; default False): (boolean; default False).  Forces a one-time update to the position data.   If set to True in a callback, the browser
  will update the position data and reset update_now back to False.  This can, for example, to update the position
 with a button click or an interval timer.
- high_accuracy (boolean; default False): (boolean; default False).   If true and if the device is able to provide a more accurate position,
 it will do so. Note that this can result in slower response times or increased power consumption (with a GPS
 chip on a mobile device for example). If false (the default value), the device can take
 the liberty to save resources by responding more quickly and/or using less power."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, local_date=Component.UNDEFINED, isodate_UTC=Component.UNDEFINED, isodate_local=Component.UNDEFINED, position=Component.UNDEFINED, position_error=Component.UNDEFINED, watch_position=Component.UNDEFINED, update_now=Component.UNDEFINED, high_accuracy=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'local_date', 'isodate_UTC', 'isodate_local', 'position', 'position_error', 'watch_position', 'update_now', 'high_accuracy']
        self._type = 'CurrentLocation'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'local_date', 'isodate_UTC', 'isodate_local', 'position', 'position_error', 'watch_position', 'update_now', 'high_accuracy']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CurrentLocation, self).__init__(**args)
