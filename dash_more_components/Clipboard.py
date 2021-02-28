# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Clipboard(Component):
    """A Clipboard component.
The Clipboard component copies text to the clipboard

Keyword arguments:
- id (string; optional): The ID used to identify this component.
- target_id (string; required): id of target component containing text to copy to the clipboard.
 The inner text of the `children` prop will be copied to the clipboard.  If none, then the text from the
 `value` prop will be copied.
- title (string; optional): The text shown as a tooltip when hovering over the copy icon.
- style (dict; optional): The icon's styles
- className (string; optional): The class  name of the icon element"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, target_id=Component.REQUIRED, title=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'target_id', 'title', 'style', 'className']
        self._type = 'Clipboard'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'target_id', 'title', 'style', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['target_id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Clipboard, self).__init__(**args)
