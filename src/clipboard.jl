# AUTO GENERATED FILE - DO NOT EDIT

export clipboard

"""
    clipboard(;kwargs...)

A Clipboard component.
The Clipboard component copies text to the clipboard
Keyword arguments:
- `id` (String; optional): The ID used to identify this component.
- `target_id` (String; required): id of target component containing text to copy to the clipboard.
 The inner text of the children will be copied to the clipboard.  If none, then the text from the
 value property will be copied.
"""
function clipboard(; kwargs...)
        available_props = Symbol[:id, :target_id]
        wild_props = Symbol[]
        return Component("clipboard", "Clipboard", "dash_more_components", available_props, wild_props; kwargs...)
end

