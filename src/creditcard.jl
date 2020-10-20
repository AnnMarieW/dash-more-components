# AUTO GENERATED FILE - DO NOT EDIT

export creditcard

"""
    creditcard(;kwargs...)

A CreditCard component.
CreditCard component provides Beautiful credit cards for your payment forms
See react component here: https://github.com/amarofashion/react-credit-cards
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `cvc` (String; optional): CSV on credit card.
- `expiry` (String; optional): expiry date on credit card.
- `focus` (String; optional): focus on credit card entry
- `name` (String; optional): Name as it appears on credit card
- `number` (String; optional): account number credit card
- `locale` (Dict; optional): localization text - like the words 'valid thru' on card
"""
function creditcard(; kwargs...)
        available_props = Symbol[:id, :cvc, :expiry, :focus, :name, :number, :locale]
        wild_props = Symbol[]
        return Component("creditcard", "CreditCard", "dash_more_components", available_props, wild_props; kwargs...)
end

