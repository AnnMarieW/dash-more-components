# AUTO GENERATED FILE - DO NOT EDIT

export timer

"""
    timer(;kwargs...)

A Timer component.
A component that repeatedly increments a counter `n_intervals`
with a fixed time delay between each increment.
Interval is good for triggering a component on a recurring basis.
The time delay is set with the property "interval" in milliseconds.
Keyword arguments:
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `interval` (Real; optional): This component will increment the counter n_intervals every
`interval` milliseconds
- `disabled` (Bool; optional): If True, the n_interval counter  and the timer no longer updates.  This pauses the timer.
- `n_intervals` (Real; optional): Number of times the interval has passed (read-only)
- `max_intervals` (Real; optional): Number of times the interval will be fired.
If -1, then the interval has no limit (the default)
and if 0 then the interval stops running.
- `timer` (Real; optional): Number of milliseconds remaining on the timer. in countdown mode  or
Number of milliseconds on timer until the target duration (read-only)
- `mode` (a value equal to: 'stopwatch', 'countdown'; optional): Whether the timer is a countdown or stopwatch timer
- `duration` (Real; optional): Sets the number of milliseconds the timer will run.  If -1 the duration has no limit (the default)
and if 0 then the timer stops running.
- `reset` (Bool; optional): starts the timer at the beginning with the given prop settings.
- `repeat` (Bool; optional): the timer timer repeats once it reaches zero.
- `messages` (Dict | String; optional): messages
- `timer_format` (Bool | Real | String | Dict | Array; optional): display_timer:  Formats the timer from milliseconds into human readable formats.  If a dictionary is used
for messages prop, then no timer will be displayed.
The default display example: milliseconds: 1337000000 will display as: '15d 11h 23m 20s'.  This may be changed
using the following options:
"""
function timer(; kwargs...)
        available_props = Symbol[:id, :interval, :disabled, :n_intervals, :max_intervals, :timer, :mode, :duration, :reset, :repeat, :messages, :timer_format]
        wild_props = Symbol[]
        return Component("timer", "Timer", "dash_more_components", available_props, wild_props; kwargs...)
end

