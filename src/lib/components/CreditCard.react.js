import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Cards from 'react-credit-cards';
import 'react-credit-cards/es/styles-compiled.css';

/**
 * CreditCard component provides Beautiful credit cards for your payment forms
 * See react component here: https://github.com/amarofashion/react-credit-cards
 */
export default class CreditCard extends Component {

    render() {
        const {id, setProps, cvc, expiry, focus, name, number, locale, preview} = this.props;

        return (
            <div id={id}>                
                    <Cards
                          cvc={cvc}
                          expiry={expiry}
                          focused={focus}
                          name={name}
                          number={number}
                          locale={locale}
                          
                    />
                
            </div>
        );
    }
}


CreditCard.defaultProps = {};

CreditCard.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,    

    /**
     * CSV on credit card.
     */
    cvc: PropTypes.string,

    /**
     * expiry date on credit card.
     */
    expiry: PropTypes.string,

    /**
     * focus on credit card entry
     */
    focus: PropTypes.string,
    
    /**
     * Name as it appears on credit card
     */
    name: PropTypes.string,

    /**
     * account number credit card
     */
    number: PropTypes.string,

    /**
    * localization text - like the words 'valid thru' on card
    */
    locale: PropTypes.object
};
