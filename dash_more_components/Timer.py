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
- disabled (boolean; optional): If True, the n_interval counter  and the timer no longer updates.  This pauses the timer.
- n_intervals (number; default 0): Number of times the interval has passed (read-only)
- max_intervals (number; default -1): Number of times the interval will be fired.
If -1, then the interval has no limit (the default)
and if 0 then the interval stops running.
- timer (number; default 0): When in countdown mode, the timer will count down to zero from the starting `duration` and will show the number
 of milliseconds remaining.
 When in stopwatch mode, the timer will count up from zero and show the number of milliseconds elapsed.
 (read-only)
- mode (a value equal to: 'stopwatch', 'countdown'; default 'countdown'): The timer will count down to zero in `countdown` mode and count up from zero in `stopwatch` mode
- duration (number; default -1): Sets the number of milliseconds the timer will run.  If -1 the timer will not be limited by the duration. (the default)
and if 0 then the timer stops running but may be reset.
- reset (boolean; default True): This will start the timer at the beginning with the given prop settings.
- repeat (boolean; default False): When True, the  timer repeats once it reaches the target.
- messages (dict; optional): Timer messages to be displayed by the component rather than the timer. It is a dictionary in the form of:
 { integer: string} where integer is the time in milliseconds of when the `string` message is to be displayed.
for example, {10000 : "updating in 10 seconds"} will display the message "updating in 10 seconds" once the
timer equals 10000
Note:  `timer_format` will override `messages`.
- timer_format (dict; optional): If a timer is displayed, it will override timer `messages`.  This formats the timer (milliseconds) into human
readable formats.  For example: 1337000000 milliseconds will display as: '15d 11h 23m 20s'.  This may be changed
using the following options:. timer_format has the following type: dict containing keys 'display', 'compact', 'verbose', 'colonNotation'.
Those keys have the following types:
  - display (boolean; optional): if False, then no timer will be displayed.  Timer `messages` will be displayed (if any)  Default: False
  - compact (boolean; optional): Shows a compact timer display.  default: False
If True, it will only show the first unit: 1h 10m → 1h.
  - verbose (boolean; optional): Verbose will display full-length units. default: False
 Example - if true: 5h 1m 45s → 5 hours 1 minute 45 seconds
  - colonNotation (boolean; optional): Display time in a colon notation. default: False
Example - if true:  5h 1m 45s → 5:01:45.
Will always shows time in at least minutes: 1s → 0:01
Useful when you want to display time without the time units, similar to a digital watch."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, interval=Component.UNDEFINED, disabled=Component.UNDEFINED, n_intervals=Component.UNDEFINED, max_intervals=Component.UNDEFINED, timer=Component.UNDEFINED, mode=Component.UNDEFINED, duration=Component.UNDEFINED, reset=Component.UNDEFINED, repeat=Component.UNDEFINED, messages=Component.UNDEFINED, timer_format=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'interval', 'disabled', 'n_intervals', 'max_intervals', 'timer', 'mode', 'duration', 'reset', 'repeat', 'messages', 'timer_format']
        self._type = 'Timer'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'interval', 'disabled', 'n_intervals', 'max_intervals', 'timer', 'mode', 'duration', 'reset', 'repeat', 'messages', 'timer_format']
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