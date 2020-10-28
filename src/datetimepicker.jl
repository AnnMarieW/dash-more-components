# AUTO GENERATED FILE - DO NOT EDIT

export datetimepicker

"""
    datetimepicker(;kwargs...)

A Datetimepicker component.
TODO:
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `value` (Bool | Real | String | Dict | Array; optional): value is the selected time
- `format` (String; optional): Input format based on Unicode Technical Standard #35. 
Supported values are: y, M, MM, MMM, MMMM, d, dd, H, HH, h, hh, m, mm, s, ss, a
     
     example:  y-MM-dd h:mm:ss a
- `maxDetail` (a value equal to: 'hour', 'minute', 'second'; optional): (string, one of 'hour', 'minute', 'second, Default: 'minute')
  The level of detail to show on the datetime picker. View defined here also becomes the one on which
  clicking an item in the calendar will select a date.
- `minDetail` (a value equal to: "month", "year", "decade", "century"; optional): The least detailed calendar view that the user shall see.
- `maxTime` (String; optional): Maximum time the user can select
- `minTime` (String; optional): Minimum time the user can select
- `maxDate` (String; optional): Maximum date that the user can select. Periods partially overlapped by maxDate will also be selectable,
although React-DateTime-Picker will ensure that no later date is selected.
- `minDate` (String; optional): Minimum date that the user can select. Periods partially overlapped by minDate will also be selectable,
although React-DateTime-Picker will ensure that no earlier date is selected.
- `disabled` (Bool; optional): Whether the time picker should be disables
- `disableClock` (Bool; optional): When set to true will remove the clock and the button toggling its visibility
- `locale` (String; optional): Locale that should be used by the time picker and the clock.  Can be any
IEFE language tag. https://en.wikipedia.org/wiki/IETF_language_tag
Default from User's browser settings.
- `returnValue` (a value equal to: "start", "end", "range"; optional): Which dates shall be passed by the calendar to the onChange function and onClick{Period} functions.
Can be "start", "end" or "range". The latter will cause an array with start and end values to be passed.
"""
function datetimepicker(; kwargs...)
        available_props = Symbol[:id, :value, :format, :maxDetail, :minDetail, :maxTime, :minTime, :maxDate, :minDate, :disabled, :disableClock, :locale, :returnValue]
        wild_props = Symbol[]
        return Component("datetimepicker", "Datetimepicker", "dash_more_components", available_props, wild_props; kwargs...)
end

