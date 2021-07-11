# AUTO GENERATED FILE - DO NOT EDIT

export timer

"""
    timer(;kwargs...)

A Timer component.
The Timer component has all the functionality of the Interval component plus
the following additional features:

Operate in either `countdown` or `stopwatch` (count up) modes.
Display custom messages, or start/stop jobs at specified times.
Convert milliseconds into human readable times.
Update messages clientside to help improve app performance.
Specify the elapsed times to fire a callback rather than every interval
Keyword arguments:
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `interval` (Real; optional): This component will increment the counter `n_intervals` every
`interval` milliseconds
- `disabled` (Bool; optional): If True, the n_interval counter  and the timer no longer updates.  This pauses the timer.
- `n_intervals` (Real; optional): Number of times the interval has passed (read-only)
- `max_intervals` (Real; optional): Number of times the interval will be fired.
If -1, then the interval has no limit (the default)
and if 0 then the interval stops running.
- `timer` (Real; optional): When in countdown mode, the timer will count down to zero from the starting `duration` and will show the number
 of milliseconds remaining.
 When in stopwatch mode, the timer will count up from zero and show the number of milliseconds elapsed.
 (read-only)
- `mode` (a value equal to: 'stopwatch', 'countdown'; optional): The timer will count down to zero in `countdown` mode and count up from zero in `stopwatch` mode
- `duration` (Real; optional): Sets the number of milliseconds the timer will run.  If -1 the timer will not be limited by the duration. (the default)
and if 0 then the timer stops running.
- `reset` (Bool; optional): This will start the timer at the beginning with the given prop settings.
- `fire_times` (Array of Reals; optional): A list of the time(s) in milliseconds at which to fire a callback. This can be used to start a task at a given
time rather than using the timer. Since the timer is typically set at a small interval like one second, using
fire_times can reduce the number of times a callback is fired and can increase app performance. The time(s) must be a
multiple of the interval.
- `at_fire_time` (Real; optional): This number is updated when the timer it reaches a time in the  fire_times property. (Read only)
- `rerun` (Bool; optional): When True, the timer repeats once the timer has run for the number of milliseconds set in the duration.
- `messages` (Dict; optional): Timer messages to be displayed by the component rather than showing the timer. It is a dictionary in the form of:
{integer: string} where integer is the time in milliseconds of when the string message is to be displayed.
Note: timer_format will override messages. For example, {10000 : "updating in 10 seconds"} will display the message
"updating in 10 seconds" once the timer equals 10000.
- `timer_format` (a value equal to: 'none', 'display', 'compact', 'verbose', 'colonNotation'; optional): If a timer is displayed, it will override timer `messages`.  This formats the timer (milliseconds) into human
readable formats.  The options are:
 `'none'`: no timer will be displayed;
 `'display'`:  example - 1337000000 milliseconds will display as: '15d 11h 23m 20s';
 `'compact'`: will show only the first unit: 1h 10m → 1h ;
 `'verbose'`: will show full-length units. Example --  5 hours 1 minute 45 seconds
 `'colonNotation'`: Useful when you want to show time without the time units, similar to
                  a digital watch. Will always shows time in at least minutes: 1s → 0:01.
                  Example - 5h 1m 45s → 5:01:45.
- `style` (Dict; optional): The messages styles
- `class_name` (String; optional): The class  name of the messages container
"""
function timer(; kwargs...)
        available_props = Symbol[:id, :interval, :disabled, :n_intervals, :max_intervals, :timer, :mode, :duration, :reset, :fire_times, :at_fire_time, :rerun, :messages, :timer_format, :style, :class_name]
        wild_props = Symbol[]
        return Component("timer", "Timer", "dash_more_components", available_props, wild_props; kwargs...)
end

