# AUTO GENERATED FILE - DO NOT EDIT

export countdowntimer

"""
    countdowntimer(;kwargs...)

A CountdownTimer component.
This component is a countdown timer.  The starting duration and
    remaining duration are in seconds
Keyword arguments:
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `starting_duration` (Real; optional): The amount of time to count down in seconds
- `pause` (Bool; optional): If True, the counter will no longer update. If False, the timer will resume.
- `remaining_duration` (Real; optional): remaining time left on countdown timer in seconds
"""
function countdowntimer(; kwargs...)
        available_props = Symbol[:id, :starting_duration, :pause, :remaining_duration]
        wild_props = Symbol[]
        return Component("countdowntimer", "CountdownTimer", "dash_more_components", available_props, wild_props; kwargs...)
end

