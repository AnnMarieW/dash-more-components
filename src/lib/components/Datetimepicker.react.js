
import React, {Component} from 'react';

import PropTypes from 'prop-types';
import DateTimePicker from 'react-datetime-picker';


/**
 * A datetime picker for Dash. Also includes a way to scroll by years.
 * This is a wrapper for react component: https://github.com/wojtekmaj/react-datetime-picker
 */
 
 
 /**
 *   TODO:  more checking for valid dates.
 *          do I need to specify defaults for them to show up automatically in the docstring?
*
 *          
 *          
 *          
 *
 */
 
 
 
export default class Datetimepicker extends Component {

    constructor(props) {
        super(props);
        this.convertDate = this.convertDate.bind(this);
    }

    convertDate(value)  {
        if (value == undefined) {
           return value
        } else {
           return new Date(value)
        }

    }




    render() {
        const {id, value, format, maxDetail,minDetail, maxTime, minTime, disabled, disableClock,
        minDate, maxDate, disableCalendar, returnValue, setValue, required, yearPlaceholder,
        monthPlaceholder, dayPlaceholder, hourPlaceholder, minutePlaceholder, secondPlaceholder,
        setProps
        } = this.props;

        const newvalue = this.convertDate(value)
        console.log(`value ${newvalue}`)
        console.log(typeof newvalue)
        console.log(new Date(newvalue))

        return (
            
            <div
                id={id}
            >
                <DateTimePicker
                    value={this.convertDate(value)}
                    format={format}
                    maxDetail={maxDetail}
                    minDetail={minDetail}
                    maxTime={maxTime}
                    minTime={minTime}
                    maxDate={this.convertDate(maxDate)}
                    minDate={this.convertDate(minDate)}
                    disabled={disabled}
                    disableClock={disableClock}
                    disableCalendar={disableCalendar}
                    returnValue={returnValue}
                    required={required}
                    yearPlaceholder={yearPlaceholder}
                    monthPlaceholder={monthPlaceholder}
                    dayPlaceholder={dayPlaceholder}
                    hourPlaceholder={hourPlaceholder}
                    minutePlaceholder= {minutePlaceholder}
                    secondPlaceholder={secondPlaceholder}
                    onChange={value => setProps({ value})}
                    
                />
            </div>
 
      
        );
    }
    
}

   
Datetimepicker.defaultProps = {};

Datetimepicker.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    
    /**
    * value is the selected datetime.   type:  datetime objec
    */
   value: PropTypes.any,

   /**
   * string value of date.  from app. need to convert to datetime object
   *
   */
   setValue: PropTypes.any,
   
   
    /**
    * Input format based on Unicode Technical Standard #35.  This changes how the date and time is displayed.
    * Supported values are: y, M, MM, MMM, MMMM, d, dd, H, HH, h, hh, m, mm, s, ss, a
    *      
    *      example:  y-MM-dd h:mm:ss a   isodate:y-MM-dd HH:mm:ss
    */
   format: PropTypes.string,   
   
 
    
    /**
    * (string, one of 'hour', 'minute', 'second, Default: 'minute')
    *   The level of detail to show on the datetime picker. View defined here also becomes the one on which
    *   clicking an item in the calendar will select a date.        
    */
    maxDetail: PropTypes.oneOf(['hour', 'minute', 'second']),
    
    /**
    * The least detailed calendar view that the user shall see. 
    * 
    */
    minDetail: PropTypes.oneOf(["month", "year", "decade", "century"]),
    
    /**
    * Maximum time the user can select
    */    
    maxTime: PropTypes.string,
    
    /**
    * Minimum time the user can select
    */
    minTime: PropTypes.string,
    
    /**
    * Maximum date that the user can select. Periods partially overlapped by maxDate will also be selectable,
    * although React-DateTime-Picker will ensure that no later date is selected.
    */
    maxDate: PropTypes.string,
    
    /**
    * Minimum date that the user can select. Periods partially overlapped by minDate will also be selectable,
    * although React-DateTime-Picker will ensure that no earlier date is selected.
    */
    minDate: PropTypes.string,
    
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
    * Which dates shall be passed by the calendar to the onChange function and onClick{Period} functions.
    * Can be "start", "end" or "range". The latter will cause an array with start and end values to be passed.
    */
    returnValue: PropTypes.oneOf(["start", "end", "range"]),

    /**
    * Whether datetime input should be required
    */
    required: PropTypes.bool,

    /**
    * aria-label for the year input.
    */
    yearPlaceholder: PropTypes.string,

    /**
    * aria-label for the month input.
    */
    monthPlaceholder: PropTypes.string,

    /**
    * aria-label for the day input.
    */
    dayPlaceholder: PropTypes.string,

    /**
    * aria-label for the hour input.
    */
    hourPlaceholder: PropTypes.string,

    /**
    * aria-label for the minute input.
    */
    minutePlaceholder: PropTypes.string,

    /**
    * aria-label for the second input.
    *
    */
    secondPlaceholder: PropTypes.string,

    /**
    *  Whether to close the widgets on value selection.  Default: True
    */
    closeWidgets: PropTypes.bool,

    
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,    
};

