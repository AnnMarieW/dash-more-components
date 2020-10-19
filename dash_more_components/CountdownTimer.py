# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CountdownTimer(Component):
    """A CountdownTimer component.
This component is a countdown timer.  All times (starting duration, 
    remaining duration and countdown interval) are in seconds

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- starting_duration (number; default 60): The amount of time to count down in seconds
- pause (boolean; optional): If True, the counter will no longer update. If False, the timer will resume.
- n_seconds (number; default 0): Number of seconds elapsed
- remaining_duration (number; default 0): remaining time left on countdown timer in seconds"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, starting_duration=Component.UNDEFINED, pause=Component.UNDEFINED, n_seconds=Component.UNDEFINED, remaining_duration=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'starting_duration', 'pause', 'n_seconds', 'remaining_duration']
        self._type = 'CountdownTimer'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'starting_duration', 'pause', 'n_seconds', 'remaining_duration']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CountdownTimer, self).__init__(**args)
