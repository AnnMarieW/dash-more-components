import PropTypes from 'prop-types';
import React, {Component} from 'react'; // eslint-disable-line no-unused-vars

/**
 * 
 *     This component is a countdown timer.  The starting duration and
 *     remaining duration are in seconds
 *    
 * 
 */
 

 
export default class CountdownTimer extends Component {
    constructor(props) {
        super(props);
        this.intervalId = null;
        this.interval = 1000;
        this.reportInterval = this.reportInterval.bind(this);
        this.handleTimer = this.handleTimer.bind(this);
    }

    handleTimer(props) {
        // Check if timer should stop or shouldn't even start
        if (           
            props.pause ||
            props.remaining_duration <= 0             
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
            return;
        }

        // it hasn't started yet (& it should start)
        this.intervalId = window.setInterval(
            this.reportInterval,
            this.interval,
            props.remaining_duration
        );
    }

    resetTimer(props) {
        const {setProps, starting_duration, remaining_duration} = this.props;
        this.clearTimer();
        setProps({remaining_duration: starting_duration});
        this.handleTimer(props);
    }

    clearTimer() {
        window.clearInterval(this.intervalId);
        this.intervalId = null;
    }

    reportInterval() {
        const {setProps, remaining_duration} = this.props;
        setProps({remaining_duration: remaining_duration - this.interval / 1000});
        console.log(`remaining duration in seconds : ${remaining_duration}`);
    }

    componentDidMount() {
        this.resetTimer(this.props);
    }

    componentDidUpdate(prevProps) {    
        if (prevProps.starting_duration !== this.props.starting_duration) {
            this.resetTimer(this.props);
        } else {
            this.handleTimer(this.props);
        }
    }

    componentWillUnmount() {
        this.clearTimer();
    }

    render() {
        return null;
    }
}


CountdownTimer.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,
    /**
     * The amount of time to count down in seconds
     * 
     */
    starting_duration: PropTypes.number,

    /**
     * If True, the counter will no longer update. If False, the timer will resume. 
     * 
     */
    pause: PropTypes.bool,

    /** 
    * remaining time left on countdown timer in seconds
    */
    remaining_duration: PropTypes.number,
    
    /**
     * Dash assigned callback
     */
    setProps: PropTypes.func,
};

CountdownTimer.defaultProps = {
  starting_duration : 0,
  remaining_duration : 0,
  pause : true,
};



