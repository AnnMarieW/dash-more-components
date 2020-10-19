# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Timepicker(Component):
    """A Timepicker component.
TODO:  Remove https://github.com/arqex/react-datetime - it takes a lot of space. 

           necessary to add className?  if sim test array of strings - classname
           how to use{...}  ?
           necessary to specify all vars in div in return?

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- value (string; optional): value is the selected time
- format (string; optional): Input format based on Unicode Technical Standard #35. Supported values are: H, HH, h, hh, m, mm, s, ss, a.
     example: h:m:s a
- maxDetail (a value equal to: 'hour', 'minute', 'second'; optional): (string, one of 'hour', 'minute', 'second, Default: 'minute')
  The level of detail to show on the time picker.
- maxTime (string; optional): Maximum time the user can select
- minTime (string; optional): Minimum time the user can select
- disabled (boolean; optional): Whether the time picker should be disables
- disableClock (boolean; optional): When set to true will remove the clock and the button toggling its visibility
- locale (string; optional): Locale that should be used by the time picker and the clock.  Can be any
IEFE language tag. https://en.wikipedia.org/wiki/IETF_language_tag
Default from User's browser settings."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, format=Component.UNDEFINED, maxDetail=Component.UNDEFINED, maxTime=Component.UNDEFINED, minTime=Component.UNDEFINED, disabled=Component.UNDEFINED, disableClock=Component.UNDEFINED, locale=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'format', 'maxDetail', 'maxTime', 'minTime', 'disabled', 'disableClock', 'locale']
        self._type = 'Timepicker'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'format', 'maxDetail', 'maxTime', 'minTime', 'disabled', 'disableClock', 'locale']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Timepicker, self).__init__(**args)
