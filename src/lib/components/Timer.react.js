
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
 */


export default class Timer extends Component {
    constructor(props) {
        super(props);
        this.intervalId = null;
        this.reportInterval = this.reportInterval.bind(this);
        this.handleTimer = this.handleTimer.bind(this);



    }

    handleTimer(props) {
        // Check if timer should stop or shouldn't even start
        if (
            props.max_intervals === 0 ||
            props.disabled ||
            (props.n_intervals >= props.max_intervals &&
                props.max_intervals !== -1) ||
            (props.remaining_duration  === 0 &&
                props.countdown_duration !== -1)

        ) {
            console.log('im here')
            // stop existing timer
            if (this.intervalId) {
                console.log(`intervalId: ${this.intervalId}`)
                this.clearTimer();
            }
            // and don't start a timer
            if (props.disabled && props.reset) {
                  this.initTimer(props)
            }
            return;
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
    }

   initTimer(props) {
        const {setProps, countdown_duration, remaining_duration, reset, disabled} = this.props;
        console.log('inside initTimer')
            setProps({
                remaining_duration: countdown_duration,
                n_intervals : 0,
                reset: false,
            });
   }


    resetTimer(props) {
        this.clearTimer();
        this.handleTimer(props);
    }

    clearTimer() {
        window.clearInterval(this.intervalId);
        this.intervalId = null;
    }

    reportInterval() {
        const {setProps, n_intervals, interval, remaining_duration, countdown_duration, reset} = this.props;
        if (reset) {
            this.initTimer(this.props)
            return
        }

        // handles the case where the last interval would make the remaining_duration negative
        // for example, if interval is set to update every minute, but only 5 seconds remains,
        // then make last interval = 5 seconds.
        if (remaining_duration < interval && countdown_duration !== -1) {
            this.clearTimer()
            this.intervalId = window.setInterval(
                this.reportInterval,
                remaining_duration
            );
            setProps({remaining_duration: 0});
            return
        }

        setProps({
            n_intervals: n_intervals + 1,
        });

        if (countdown_duration !== -1) {
            setProps({
                remaining_duration: countdown_duration - interval * n_intervals
            });
        }
    }


    componentDidMount() {
        this.initTimer(this.props);
        this.handleTimer(this.props);
    }

    UNSAFE_componentWillReceiveProps(nextProps) {
        if (
            nextProps.interval !== this.props.interval ||
            nextProps.countdown_duration !== this.props.countdown_durationduration ||
            nextProps.max_intervals !== this.props.max_intervals ||
            nextProps.reset !== this.props.reset ||
            nextProps.disabled !== this.props.disabled

            ) {
            this.resetTimer(nextProps);
        } else {
            this.handleTimer(nextProps);
        }
    }


    componentWillUnmount() {
        this.clearTimer();
    }

    render() {
        return null;
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
     * If True, the n_interval counter  and the remaining_duration no longer updates.  This pauses the timer.
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
     * Number of milliseconds remaining on the timer.  (read-only)
     */
    remaining_duration: PropTypes.number,

    /**
     * Sets the number of milliseconds the timer will run.  If -1 the duration has no limit (the default)
     * and if 0 then the timer stops running.
     */
    countdown_duration: PropTypes.number,

    /**
     * starts the timer at the beginning with the given prop settings.
     */
    reset: PropTypes.bool,


    /**
     * Dash assigned callback
     */
    setProps: PropTypes.func,
};

Timer.defaultProps = {
    interval: 1000,
    n_intervals: 0,
    max_intervals: -1,
    countdown_duration: -1,
    remaining_duration: -1,
    reset: true,

};































//
///*==========================================================================================
//
//import PropTypes from 'prop-types';
//import React, {Component} from 'react'; // eslint-disable-line no-unused-vars
//
///**
// *
// *     This component is a countdown timer.  The starting duration and
// *     remaining duration are in seconds
// *
// *
// */
//
//
//
//export default class CountdownTimer extends Component {
//    constructor(props) {
//        super(props);
//        this.intervalId = null;
//        this.interval = 1000;
//        this.reportInterval = this.reportInterval.bind(this);
//        this.handleTimer = this.handleTimer.bind(this);
//    }
//
//    handleTimer(props) {
//        // Check if timer should stop or shouldn't even start
//        if (
//            props.pause ||
//            props.remaining_duration <= 0
//        ) {
//            // stop existing timer
//            if (this.intervalId) {
//                this.clearTimer();
//            }
//            // and don't start a timer
//            return;
//        }
//
//        // keep the existing timer running
//        if (this.intervalId) {
//            return;
//        }
//
//        // it hasn't started yet (& it should start)
//        this.intervalId = window.setInterval(
//            this.reportInterval,
//            this.interval,
//            props.remaining_duration
//        );
//    }
//
//    resetTimer(props) {
//        const {setProps, starting_duration, remaining_duration} = this.props;
//        this.clearTimer();
//        setProps({remaining_duration: starting_duration});
//        this.handleTimer(props);
//    }
//
//    clearTimer() {
//        window.clearInterval(this.intervalId);
//        this.intervalId = null;
//    }
//
//    reportInterval() {
//        const {setProps, remaining_duration} = this.props;
//        setProps({remaining_duration: remaining_duration - this.interval / 1000});
//        console.log(`remaining duration in seconds : ${remaining_duration}`);
//    }
//
//    componentDidMount() {
//        this.resetTimer(this.props);
//    }
//
//    componentDidUpdate(prevProps) {
//        if (prevProps.starting_duration !== this.props.starting_duration) {
//            this.resetTimer(this.props);
//        } else {
//            this.handleTimer(this.props);
//        }
//    }
//
//    componentWillUnmount() {
//        this.clearTimer();
//    }
//
//    render() {
//        return null;
//    }
//}
//
//
//CountdownTimer.propTypes = {
//    /**
//     * The ID of this component, used to identify dash components
//     * in callbacks. The ID needs to be unique across all of the
//     * components in an app.
//     */
//    id: PropTypes.string,
//    /**
//     * The amount of time to count down in seconds
//     *
//     */
//    starting_duration: PropTypes.number,
//
//    /**
//     * If True, the counter will no longer update. If False, the timer will resume.
//     *
//     */
//    pause: PropTypes.bool,
//
//    /**
//    * remaining time left on countdown timer in seconds
//    */
//    remaining_duration: PropTypes.number,
//
//    /**
//     * Dash assigned callback
//     */
//    setProps: PropTypes.func,
//};
//
//CountdownTimer.defaultProps = {
//  starting_duration : 0,
//  remaining_duration : 0,
//  pause : true,
//};
//
//
//*/
//
//
//
