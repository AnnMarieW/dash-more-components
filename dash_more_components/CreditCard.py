# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CreditCard(Component):
    """A CreditCard component.
CreditCard component provides Beautiful credit cards for your payment forms
See react component here: https://github.com/amarofashion/react-credit-cards

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- cvc (string; optional): CSV on credit card.
- expiry (string; optional): expiry date on credit card.
- focus (string; optional): focus on credit card entry
- name (string; optional): Name as it appears on credit card
- number (string; optional): account number credit card
- locale (dict; optional): localization text - like the words 'valid thru' on card"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, cvc=Component.UNDEFINED, expiry=Component.UNDEFINED, focus=Component.UNDEFINED, name=Component.UNDEFINED, number=Component.UNDEFINED, locale=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'cvc', 'expiry', 'focus', 'name', 'number', 'locale']
        self._type = 'CreditCard'
        self._namespace = 'dash_more_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cvc', 'expiry', 'focus', 'name', 'number', 'locale']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CreditCard, self).__init__(**args)
