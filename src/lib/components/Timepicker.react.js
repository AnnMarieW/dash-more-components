
import React, {Component} from 'react';

import PropTypes from 'prop-types';
import TimePicker from 'react-time-picker'


/**
 * A time picker for Dash.
 * This is a wrapper for react component: https://github.com/wojtekmaj/react-time-picker
 */
 
 
 /**
 *   TODO:  Remove https://github.com/arqex/react-datetime - it takes a lot of space. 
*
 *            necessary to add className?  if sim test array of strings - classname
 *            how to use{...}  ?
 *            necessary to specify all vars in div in return?
 *
 */
 
 
 
export default class Timepicker extends Component {

    constructor(props) {
        super(props);        
    }	
	

    render() {
        const {id, value, format, maxDetail, maxTime, minTime, disabled, disableClock,setProps
        
        } = this.props;     
        
        return (
            
            <div id={id}>                
                    <TimePicker
        		value={value}    
        		format={format}
        		maxDetail={maxDetail} 
        		maxTime={maxTime}
        		minTime={minTime}
        		disabled={disabled}
        		disableClock={disableClock}
        		                   
                       
                       onChange={value => setProps({ value})}                      
                    
                    />
                
            </div>
            
        );
    }
}


Timepicker.defaultProps = {};

Timepicker.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    
    /**
    * value is the selected time
    */
   value: PropTypes.string,
   
   
    /**
    * Input format based on Unicode Technical Standard #35. Supported values are: H, HH, h, hh, m, mm, s, ss, a.
    *      example: h:m:s a
    */
   format: PropTypes.string,   
  
    
    /**
    * (string, one of 'hour', 'minute', 'second, Default: 'minute')
    *   The level of detail to show on the time picker.        
    */
    maxDetail: PropTypes.oneOf(['hour', 'minute', 'second']),
    
    /**
    * Maximum time the user can select
    */    
    maxTime: PropTypes.string,
    
    /**
    * Minimum time the user can select
    */
    minTime: PropTypes.string,
    
    /**
    * Whether the time picker should be disables
    */
    disabled: PropTypes.bool,
    
    /**
    * When set to true will remove the clock and the button toggling its visibility
    */
    disableClock: PropTypes.bool,
    
    /**
    * Locale that should be used by the time picker and the clock.  Can be any
    * IEFE language tag. https://en.wikipedia.org/wiki/IETF_language_tag
    * Default from User's browser settings.
    */
    locale: PropTypes.string,
    
  
    
    
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,    
};


