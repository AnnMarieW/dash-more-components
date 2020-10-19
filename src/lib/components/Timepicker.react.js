
import React, {Component} from 'react';

import PropTypes from 'prop-types';
import TimePicker from 'react-time-picker'


/**
 * A time picker for Dash. Also allow selection of milliseconds. 
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


/**********************************************************************************************


    /**
    * (string or array of strings)  Class name(s) that will be added along with "react-time-picker"
    * to the main React-Time-Picker <div> element.
    */
   // className: PropTypes.string,
  
  
    
    /* (boolean or string,  default: True)  Defines the format for the date. It accepts any 
     * Moment.js date format (not in localized format). https://momentjs.com/docs/#/displaying/format/
     * If true the date will be displayed using the defaults for the current locale. 
     * If false the datepicker is disabled and the component can be used as timepicker
    */
  //  dateFormat: PropTypes.oneOfType([
  //    PropTypes.string,
  //    PropTypes.bool,    
  //  ]),

/*

amPmAriaLabel	aria-label for the AM/PM select input.	n/a	"Select AM/PM"
autoFocus	Automatically focuses the input on mount.	n/a	true
className	Class name(s) that will be added along with "react-time-picker" to the main React-Time-Picker <div> element.	n/a	
String: "class1 class2"
Array of strings: ["class1", "class2 class3"]
clearAriaLabel	aria-label for the clear button.	n/a	"Clear value"
clearIcon	Content of the clear button. Setting the value explicitly to null will hide the icon.	(default icon)	
String: "Clear"
React element: <ClearIcon />
clockAriaLabel	aria-label for the clock button.	n/a	"Toggle clock"
clockClassName	Class name(s) that will be added along with "react-clock" to the main React-Clock <time> element.	n/a	
String: "class1 class2"
Array of strings: ["class1", "class2 class3"]
clockIcon	Content of the clock button. Setting the value explicitly to null will hide the icon.	(default icon)	
String: "Clock"
React element: <ClockIcon />
closeClock	Whether to close the clock on value selection.	true	false
disabled	Whether the time picker should be disabled.	false	true
disableClock	When set to true, will remove the clock and the button toggling its visibility.	false	true

hourAriaLabel	aria-label for the hour input.	n/a	"Hour"
hourPlaceholder	placeholder for the hour input.	"--"	"hh"
isOpen	Whether the clock should be opened.	false	true
locale	Locale that should be used by the time picker and the clock. Can be any IETF language tag.	User's browser settings	"hu-HU"
maxDetail	How detailed time picking shall be. Can be "hour", "minute" or "second".	"minute"	"second"
maxTime	Maximum time that the user can select.	n/a	
Date: new Date()
String: "22:15:00"
minTime	Minimum date that the user can select.	n/a	
Date: new Date()
String: "22:15:00"
minuteAriaLabel	aria-label for the minute input.	n/a	"Minute"
minutePlaceholder	placeholder for the minute input.	"--"	"mm"
name	Input name.	"time"	"myCustomName"
nativeInputAriaLabel	aria-label for the native time input.	n/a	"Time"
onChange	Function called when the user picks a valid time.	n/a	(value) => alert('New time is: ', value)
onClockClose	Function called when the clock closes.	n/a	() => alert('Clock closed')
onClockOpen	Function called when the clock opens.	n/a	() => alert('Clock opened')
required	Whether date input should be required.	false	true
secondAriaLabel	aria-label for the second input.	n/a	"Second"
secondPlaceholder	placeholder for the second input.	"--"	"ss"
**********************************************************************************************/

