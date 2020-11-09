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
- `interval` (Real; optional): This component will increment the counter `n_intervals` every
`interval` milliseconds
- `disabled` (Bool; optional): If True, the n_interval counter  and the remaining_duration no longer updates.  This pauses the timer.
- `n_intervals` (Real; optional): Number of times the interval has passed (read-only)
- `max_intervals` (Real; optional): Number of times the interval will be fired.
If -1, then the interval has no limit (the default)
and if 0 then the interval stops running.
- `remaining_duration` (Real; optional): Number of milliseconds remaining on the timer.  (read-only)
- `countdown_duration` (Real; optional): Sets the number of milliseconds the timer will run.  If -1 the duration has no limit (the default)
and if 0 then the timer stops running.
- `reset` (Bool; optional): starts the timer at the beginning with the given prop settings.
"""
function timer(; kwargs...)
        available_props = Symbol[:id, :interval, :disabled, :n_intervals, :max_intervals, :remaining_duration, :countdown_duration, :reset]
        wild_props = Symbol[]
        return Component("timer", "Timer", "dash_more_components", available_props, wild_props; kwargs...)
end

