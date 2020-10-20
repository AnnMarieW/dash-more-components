# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Datetimepicker(Component):
    """A Datetimepicker component.
TODO:

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- value (boolean | number | string | dict | list; optional): value is the selected time
- format (string; optional): Input format based on Unicode Technical Standard #35. 
Supported values are: y, M, MM, MMM, MMMM, d, dd, H, HH, h, hh, m, mm, s, ss, a
     
     example:  y-MM-dd h:mm:ss a
- maxDetail (a value equal to: 'hour', 'minute', 'second'; optional): (string, one of 'hour', 'minute', 'second, Default: 'minute')
  The level of detail to show on the datetime picker. View defined here also becomes the one on which
  clicking an item in the calendar will select a date.
- minDetail (a value equal to: "month", "year", "decade", "century"; optional): The least detailed calendar view that the user shall see.
- maxTime (string; optional): Maximum time the user can select
- minTime (string; optional): Minimum time the user can select
- maxDate (string; optional)
- minDate (string; optional)
- disabled (boolean; optional): Whether the time picker should be disables
- disableClock (boolean; optional): When set to true will remove the clock and the button toggling its visibility
- locale (string; optional): Locale that should be used by the time picker and the clock.  Can be any
IEFE language tag. https://en.wikipedia.org/wiki/IETF_language_tag
Default from User's browser settings.
- returnValue (a value equal to: "start", "end", "range"; optional): Which dates shall be passed by the calendar to the onChange function and onClick{Period} functions.
Can be "start", "end" or "range". The latter will cause an array with start and end values to be passed."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, format=Component.UNDEFINED, maxDetail=Component.UNDEFINED, minDetail=Component.UNDEFINED, maxTime=Component.UNDEFINED, minTime=Component.UNDEFINED, maxDate=Component.UNDEFINED, minDate=Component.UNDEFINED, disabled=Component.UNDEFINED, disableClock=Component.UNDEFINED, locale=Component.UNDEFINED, returnValue=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'format', 'maxDetail', 'minDetail', 'maxTime', 'minTime', 'maxDate', 'minDate', 'disabled', 'disableClock', 'locale', 'returnValue']
        self._type = 'Datetimepicker'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'format', 'maxDetail', 'minDetail', 'maxTime', 'minTime', 'maxDate', 'minDate', 'disabled', 'disableClock', 'locale', 'returnValue']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Datetimepicker, self).__init__(**args)
