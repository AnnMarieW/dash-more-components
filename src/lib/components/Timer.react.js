
import PropTypes from 'prop-types';
import React, {Component} from 'react'; // eslint-disable-line no-unused-vars


/**
 * A component that repeatedly increments a counter `n_intervals`
 * with a fixed time delay between each increment.
 * Interval is good for triggering a component on a recurring basis.
 * The time delay is set with the property "interval" in milliseconds.
 */


 /*
 *     TODO:  change to ComponentDidUpdate *
 *            how to handle time-outs
 *             change name 5 places if rename back to Interval
 *             dependancy:  https://github.com/sindresorhus/pretty-ms
 *              why is there a lag in the clientside timer?
 *

 */


export default class Timer extends Component {
    constructor(props) {
        super(props);
        this.intervalId = null;
        this.renderMessage = null;
        this.reportInterval = this.reportInterval.bind(this);
        this.handleTimer = this.handleTimer.bind(this);
        this.handleMessages = this.handleMessages.bind(this);

        // this.countdown is used to handle the timer within this component.  If it's in stopwatch mode
        //   then the count-up time is calculated just prior to setProps({timer:})
        this.countdown = 0
    }


    handleTimer(props) {
        // Check if timer should stop or shouldn't even start
        if (
            props.max_intervals === 0 ||
            props.disabled ||
            props.duration === -1 ||
            (props.n_intervals >= props.max_intervals &&
                props.max_intervals !== -1) ||
            (this.countdown === 0 &&
            !(props.repeat))

        ) {
            // stop existing timer
            if (this.intervalId) {
                this.clearTimer();
            }
            // and don't start a timer
            if (props.disabled && props.reset) {
                  this.initTimer(props)
            }
            return;
        }

        //  This doesn't work yet
        // handles the case where the last interval would make the countdown negative
        // for example, if interval is set to update every minute, but only 5 seconds remains,
        // then make last interval = 5 seconds.
        if (this.countdown !== 0 && this.countdown < interval && duration !== -1) {
            console.log(`in orphan`)
            this.clearTimer()
            const lastInterval = this.countdown
            this.countdown = 0
            this.intervalId = window.setInterval(
                this.reportInterval,
                lastInterval
            );
        }

        // keep the existing timer running
        if (this.intervalId) {
            return;
        }

        // it hasn't started yet (& it should start)
        this.intervalId = window.setInterval(
            this.reportInterval,
            props.interval
        );
    }  // end handle timer


    handleMessages(props) {
        const {messages, timer, timer_format} = this.props

        if (messages === null) {
            return
        };
        if (typeof messages === 'object') {
                const messagesObj = Object.assign({}, messages);
                if (timer in messagesObj) {
                    this.renderMessage = `${messagesObj[timer]}`
                };
        } else {
            const prettyMilliseconds = require('pretty-ms');
            const formatObj = Object.assign({}, timer_format);
            if (formatObj['display'] === false) {
                this.renderMessage = `${messages}`;
            } else {
              this.renderMessage = `${messages}  ${prettyMilliseconds(timer, formatObj)}`;
            };
        };
    }// end handleMessages


    reportInterval() {
        const {setProps, id, n_intervals, interval, timer, mode, duration, reset, repeat, messages} = this.props;

        if (
            reset ||
            (repeat && this.countdown === 0)
        ) {
            this.initTimer(this.props)
            return
        }

        const new_n_intervals = n_intervals + 1
        setProps({n_intervals: new_n_intervals });

        if (duration !== -1) {
            this.countdown = duration - interval * new_n_intervals
            if  (mode === 'countdown') {
                setProps({ timer: this.countdown })
            } else { // stopwatch
                setProps({timer: interval * new_n_intervals});
            }
            this.handleMessages(this.props);
        }
    }  // end report interval

   initTimer(props) {
        const {setProps, duration, timer, reset,  disabled, mode, messages} = this.props;

        setProps({
            n_intervals : 0,
            reset: false,
        });

        this.countdown = duration

        if  (mode === 'countdown') {
            setProps({ timer: duration})
        } else { // stopwatch
            setProps({timer: 0});
        }
   }

    resetTimer(props) {
        this.clearTimer();
        this.initTimer(props);
        this.handleTimer(props);
    }

    clearTimer() {
        window.clearInterval(this.intervalId);
        this.intervalId = null;
    }

    componentDidMount() {
        this.initTimer(this.props);
        this.handleTimer(this.props);
    }


    componentDidUpdate(prevProps) {
        if (
            prevProps.interval !== this.props.interval ||
            prevProps.duration !== this.props.duration ||
            prevProps.max_intervals !== this.props.max_intervals ||
            prevProps.reset !== this.props.reset ||
            prevProps.disabled !== this.props.disabled ||
            prevProps.repeat !== this.props.repeat ||
            prevProps.messages !== this.props.messages ||
            prevProps.mode !== this.props.mode
        ) {
            this.resetTimer(this.props);
        } else {
            this.handleTimer(this.props);
        }
    }


    componentWillUnmount() {
        this.clearTimer();
    }


    render() {
        return <div>{this.renderMessage}</div>;
    }
}

Timer.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,
    /**
     * This component will increment the counter n_intervals every
     * `interval` milliseconds
     */
    interval: PropTypes.number,

    /**
     * If True, the n_interval counter  and the timer no longer updates.  This pauses the timer.
     */
    disabled: PropTypes.bool,

    /**
     * Number of times the interval has passed (read-only)
     */
    n_intervals: PropTypes.number,

    /**
     * Number of times the interval will be fired.
     * If -1, then the interval has no limit (the default)
     * and if 0 then the interval stops running.
     */
    max_intervals: PropTypes.number,

    /**
     * Number of milliseconds remaining on the timer. in countdown mode  or
     * Number of milliseconds on timer until the target duration (read-only)
     */
    timer: PropTypes.number,

    /**
     * Whether the timer is a countdown or stopwatch timer
     */
    mode: PropTypes.oneOf(['stopwatch', 'countdown']),

    /**
     * Sets the number of milliseconds the timer will run.  If -1 the duration has no limit (the default)
     * and if 0 then the timer stops running.
     */
    duration: PropTypes.number,

    /**
     * starts the timer at the beginning with the given prop settings.
     */
    reset: PropTypes.bool,

    /**
     * the timer timer repeats once it reaches zero.
     */
    repeat: PropTypes.bool,

    /**
     * timer messages to be displayed by the component. It may be a dictionary in the form of either:
     *  { integer: string} where integer is the time in milliseconds to display the string message.
     * for example, {10000 : "updating in 10 seconds} will display the message "updating in 10 seconds" when the
     * timer equals 10000
     *   or
     *  string, where string is the message that will be displayed prior to the  timer display.  For example,
     * "updating in:"  will display "updating in: 10s".  The timer will update with every interval. See timer_format
     *  property for display options.

     */
    messages: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.string,
    ]),

    /**
     * display_timer:  Formats the timer which is in milliseconds into human readable formats.
     * The default display example: milliseconds: 1337000000 will display as: '15d 11h 23m 20s'.  This may be changed
     * using the following options:
     */

  //   timer_format: PropTypes.any,

    timer_format: PropTypes.exact({
        /**
        * if False, then no timer will be displayed.  Default: True
        */
        display: PropTypes.bool,

        /**
        * Shows a compact timer display.  default: False
        * If True, it will only show the first unit: 1h 10m → 1h.
        */
        compact: PropTypes.bool,

        /**
        * Verbose will display full-length units. default: False
        *  Example - if true: 5h 1m 45s → 5 hours 1 minute 45 seconds
        */
        verbose: PropTypes.bool,

        /**
        * Display time in a colon notation. default: False
        * Example - if true:  5h 1m 45s → 5:01:45.
        * Will always shows time in at least minutes: 1s → 0:01
        * Useful when you want to display time without the time units, similar to a digital watch.
        */
        colonNotation: PropTypes.bool,
    }),

    /**
     * Dash assigned callback
     */
    setProps: PropTypes.func,
};

Timer.defaultProps = {
    interval: 1000,
    n_intervals: 0,
    max_intervals: -1,
    duration: -1,
    timer: 0,
    mode: 'countdown',
    reset: true,
    repeat: false,
    messages: '',
};


