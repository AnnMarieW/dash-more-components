# AUTO GENERATED FILE - DO NOT EDIT

export timepicker

"""
    timepicker(;kwargs...)

A Timepicker component.
TODO:  Remove https://github.com/arqex/react-datetime - it takes a lot of space. 

           necessary to add className?  if sim test array of strings - classname
           how to use{...}  ?
           necessary to specify all vars in div in return?
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `value` (String; optional): value is the selected time
- `format` (String; optional): Input format based on Unicode Technical Standard #35. Supported values are: H, HH, h, hh, m, mm, s, ss, a.
     example: h:m:s a
- `maxDetail` (a value equal to: 'hour', 'minute', 'second'; optional): (string, one of 'hour', 'minute', 'second, Default: 'minute')
  The level of detail to show on the time picker.
- `maxTime` (String; optional): Maximum time the user can select
- `minTime` (String; optional): Minimum time the user can select
- `disabled` (Bool; optional): Whether the time picker should be disables
- `disableClock` (Bool; optional): When set to true will remove the clock and the button toggling its visibility
- `locale` (String; optional): Locale that should be used by the time picker and the clock.  Can be any
IEFE language tag. https://en.wikipedia.org/wiki/IETF_language_tag
Default from User's browser settings.
"""
function timepicker(; kwargs...)
        available_props = Symbol[:id, :value, :format, :maxDetail, :maxTime, :minTime, :disabled, :disableClock, :locale]
        wild_props = Symbol[]
        return Component("timepicker", "Timepicker", "dash_more_components", available_props, wild_props; kwargs...)
end

