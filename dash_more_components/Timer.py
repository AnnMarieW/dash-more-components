# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Timer(Component):
    """A Timer component.
A component that repeatedly increments a counter `n_intervals`
with a fixed time delay between each increment.
Interval is good for triggering a component on a recurring basis.
The time delay is set with the property "interval" in milliseconds.

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- interval (number; default 1000): This component will increment the counter `n_intervals` every
`interval` milliseconds
- disabled (boolean; optional): If True, the n_interval counter  and the remaining_duration no longer updates.  This pauses the timer.
- n_intervals (number; default 0): Number of times the interval has passed (read-only)
- max_intervals (number; default -1): Number of times the interval will be fired.
If -1, then the interval has no limit (the default)
and if 0 then the interval stops running.
- remaining_duration (number; default -1): Number of milliseconds remaining on the timer.  (read-only)
- countdown_duration (number; default -1): Sets the number of milliseconds the timer will run.  If -1 the duration has no limit (the default)
and if 0 then the timer stops running.
- reset (boolean; default True): starts the timer at the beginning with the given prop settings."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, interval=Component.UNDEFINED, disabled=Component.UNDEFINED, n_intervals=Component.UNDEFINED, max_intervals=Component.UNDEFINED, remaining_duration=Component.UNDEFINED, countdown_duration=Component.UNDEFINED, reset=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'interval', 'disabled', 'n_intervals', 'max_intervals', 'remaining_duration', 'countdown_duration', 'reset']
        self._type = 'Timer'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'interval', 'disabled', 'n_intervals', 'max_intervals', 'remaining_duration', 'countdown_duration', 'reset']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Timer, self).__init__(**args)
