import {includes} from 'ramda';
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
 *            how to handle when callbacks take longer than the interval timer
 *             change name 5 places if rename back to Interval
 *             dependency:  https://github.com/sindresorhus/pretty-ms
 *             how to delete "ended" from auto generated timer.py
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
        this.countdown = 0;
    }

    handleTimer(props) {
        const {
            n_intervals,
            max_intervals,
            disabled,
            reset,
            rerun,
            interval,
        } = this.props;

        // Check if timer should stop or shouldn't even start
        if (
            max_intervals === 0 ||
            disabled ||
            (n_intervals >= max_intervals && max_intervals !== -1) ||
            (this.countdown === 0 && !rerun) ||
            (this.countdown > 0 && this.countdown < interval)
        ) {
            // stop existing timer
            if (this.intervalId) {
                this.clearTimer();
            }
            // and don't start a timer
            return;
        }

        // keep the existing timer running
        if (this.intervalId) {
            if (this.countdown === 0 && rerun) {
                this.initTimer(props)
            }
            return;
        }

        // it hasn't started yet (& it should start)
        this.intervalId = window.setInterval(this.reportInterval, interval);
    } // end handle timer

    handleMessages(props, new_timer) {
        const {messages, timer_format} = this.props;

        const messagesObj = Object.assign({}, messages);
        if (new_timer in messagesObj) {
            this.renderMessage = `${messagesObj[new_timer]}`;
        }

        const prettyMilliseconds = require('pretty-ms');
        const formatObj = Object.assign({}, timer_format);
        if (formatObj.display) {
            this.renderMessage = `${prettyMilliseconds(new_timer, formatObj)}`;
        }
    } // end handleMessages

    reportInterval() {
        const {setProps, n_intervals, interval, mode, duration, fire, timer} = this.props;

        const new_n_intervals = n_intervals + 1;
        setProps({n_intervals: new_n_intervals});


        this.countdown = duration - interval * new_n_intervals;
        let new_timer;
        if (mode === 'countdown' && duration !== -1 ) {
            new_timer = this.countdown;
        } else {
            // stopwatch.  Note - stopwatch mode only if duration === -1
            new_timer = interval * new_n_intervals;
        }

        this.handleMessages(this.props, new_timer);
        setProps({timer: new_timer});


        if (includes(new_timer, fire)) {
            setProps({at_interval: new_timer})
        } else {
            setProps({at_interval: null})
        }

    } // end report interval

    initTimer(props) {
        const {setProps, duration, mode, rerun} = this.props;

        setProps({
            n_intervals: 0,
            reset: false,
        });

        this.countdown = duration;
        let startTime;
        if (mode === 'countdown' && duration !== -1) {
            startTime = duration
        } else { // stopwatch
            startTime = 0
        }


        setProps({timer: startTime});
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
            prevProps.rerun !== this.props.rerun ||
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
     * This component will increment the counter `n_intervals` every
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
     * When in countdown mode, the timer will count down to zero from the starting `duration` and will show the number
     *  of milliseconds remaining.
     *  When in stopwatch mode, the timer will count up from zero and show the number of milliseconds elapsed.
     *  (read-only)
     */
    timer: PropTypes.number,

    /**
     * The timer will count down to zero in `countdown` mode and count up from zero in `stopwatch` mode
     */
    mode: PropTypes.oneOf(['stopwatch', 'countdown']),

    /**
     * Sets the number of milliseconds the timer will run.  If -1 the timer will not be limited by the duration. (the default)
     * and if 0 then the timer stops running.
     */
    duration: PropTypes.number,

    /**
     * This will start the timer at the beginning with the given prop settings.
     */
    reset: PropTypes.bool,

    /**
    * A list of the time(s) in milliseconds at which to fire a callback. This can be used to start a task at a given
     * time rather than using the timer. Since the timer is typically set at a small interval like one second, using
     * fire can reduce the number of times a callback is fired and can increase app performance. The time(s) must be a
     * multiple of the interval.
    */
    fire: PropTypes.arrayOf(PropTypes.number),


    /**
    * This number is updated when the timer reaches an interval in the fire property. (Read only)
    */
    at_interval: PropTypes.number,

    /**
     * When True, the timer repeats once the timer has run for the number of milliseconds set in the duration.
     */
    rerun: PropTypes.bool,

    /**
     * Timer messages to be displayed by the component rather than showing the timer. It is a dictionary in the form of:
     * {integer: string} where integer is the time in milliseconds of when the string message is to be displayed.
     * Note: timer_format will override messages. For example, {10000 : "updating in 10 seconds"} will display the message
     * "updating in 10 seconds" once the timer equals 10000.
     */
    messages: PropTypes.object,

    /**
     * If a timer is displayed, it will override timer `messages`.  This formats the timer (milliseconds) into human
     * readable formats.  For example: 1337000000 milliseconds will display the default format: '15d 11h 23m 20s'.
     */
    timer_format: PropTypes.exact({
        /**
         * If False, then no timer will be displayed. Timer messages will be displayed (if any). If True, for example,
         * 1337000000 milliseconds will display as: '15d 11h 23m 20s'
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
         * Display time in a colon notation. Useful when you want to display time without the time units, similar to
         * a digital watch. Will always shows time in at least minutes: 1s → 0:01.  Example - 5h 1m 45s → 5:01:45.
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
    rerun: false,
    messages: {},
    fire:[],
    at_interval:null,
};
