//import * as R from 'ramda';

import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * The CurrentLocation component gets geolocation of the device from the web browser.  See more info here:
 * https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
 */

 /*
 *  TODO/Questions:
 *        - Is this the best name for the component?
 *
 *         - The position data includes a timestamp, and I did timestamp/1000 to make it easier to convert
 *           to a datetime object in Python.
  *               ie:  datetime_obj = dt.datetime.utcfromtimestamp(timestamp)
  *          But will this cause a  problem in  julia or R?
 *
 *         - What is the best way to handle errors? For now, I have both alerts in the browser, and the errors available
 *           as props
 *
 *          - In current_location.py I have a checklist item to turn on or off watchPosition.  However it only works
 *            correctly the first time. When watchPosition is started for the second time I cannot make it stop
 *            without restarting the app.  Is there a way to force the component to re-mount?  (I heard that was an
 *            anti-pattern in React.)
 *
 *
 */



export default class CurrentLocation extends Component {
  constructor(props) {
    super(props);
    this.success = this.success.bind(this);
    this.error = this.error.bind(this);
    this.updatePosition = this.updatePosition.bind(this);
  }

  updatePosition() {
    if (!navigator.geolocation) {
        alert('Your browser does not support Geolocation');
    } else {
        this.props.setProps({
          update_now: false,
        });

        const positionOptions = {
            enableHighAccuracy: this.props.high_accuracy,
            maximumAge: this.props.maximum_age,
            timeout: this.props.timeout,
        };

        this.props.watch_position ? (
            this.watchID = navigator.geolocation.watchPosition(this.success, this.error, positionOptions),
            console.log(`watchID: ${this.watchID}`)
        ) : (
            console.log(`getpos`),
            navigator.geolocation.getCurrentPosition(this.success, this.error, positionOptions)
        )
    }
  }


  componentDidMount() {
        this.updatePosition()
  }

  componentWillUnmount() {
            if (this.props.watch_position) {
                navigator.geolocation.clearWatch(this.watchId);
            }
  }


  componentDidUpdate(prevProps) {
    if (prevProps.watch_position !== this.props.watch_position && prevProps.watch_position) {
         navigator.geolocation.clearWatch(this.watchId);
         console.log(`clear ${this.watchID} watch${this.props.watch_position}`);
    }
     if ( this.props.update_now
          || (prevProps.watch_position !== this.props.watch_position)
          || (prevProps.maximum_age !== this.props.maximum_age)
          || (prevProps.timeout !== this.props.timeout)
          || (prevProps.high_accuracy !== this.props.high_accuracy)) {
        this.updatePosition()
     }
  }


  success(pos) {
    console.log(`success1`)
    const crd = pos.coords
    const position_obj = ({
      latitude: crd.latitude,
      longitude: crd.longitude,
      accuracy: crd.accuracy,
      altitude: crd.altitude,
      altitudeAccuracy: crd.altitudeAccuracy,
      speed: crd.speed,
      heading: crd.heading,
    })
    /* why doesn't this work instead?
    const position_obj = Object.assign({}, pos.coords);
    or:
    const position_obj = R.mergeRight(this.position, pos.coords);
    or:
    this.props.setProps({ position : pos.coords })
    */


    this.props.setProps({
      local_date: new Date(pos.timestamp).toLocaleString(),
      timestamp: pos.timestamp / 1000,
      position : position_obj,
      position_error : null
    });
  }

  error(err) {
    alert(`ERROR(${err.code}): ${err.message}`);
    this.props.setProps({
       position : null,
       position_error: ({
          code: err.code,
          message: err.message,
       }),
    });
  }

  render() {
    return  null;
  }
}


CurrentLocation.defaultProps = {
    watch_position : false,
    update_now : false,
    high_accuracy : false,
    position_error : null,
    maximum_age : 0,
    timeout : Infinity,
};

CurrentLocation.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The local date and time when the device position was updated.
     * Format:  MM/DD/YYYY, hh:mm:ss p   where p is AM or PM
     */
    local_date: PropTypes.string,

    /**
     * timestamp
     */
    timestamp: PropTypes.number,


    /**
    * The position of the device
    */
    position: PropTypes.shape({
        latitude: PropTypes.number,
        longitude: PropTypes.number,
        altitude: PropTypes.number,
        accuracy: PropTypes.number,
        altitudeAccuracy: PropTypes.number,
        heading: PropTypes.number,
        speed: PropTypes.number,
    }),

    /**
    *  Position error
    */
    position_error: PropTypes.shape({
        code: PropTypes.number,
        message: PropTypes.string,
    }),

    /**
    *  (boolean; default False).  If false, position is obtained as an asynchronous request.  If true, then  position data
    * is updated when either the location changes or more accurate information becomes available
    */
    watch_position: PropTypes.bool,

    /**
    *  (boolean; default False).  Forces a one-time update to the position data.   If set to True in a callback, the browser
    *   will update the position data and reset update_now back to False.  This can, for example, to update the position
    *  with a button click or an interval timer.
    */
    update_now: PropTypes.bool,

    /**
    *  (boolean; default False).   If true and if the device is able to provide a more accurate position,
    *  it will do so. Note that this can result in slower response times or increased power consumption (with a GPS
    *  chip on a mobile device for example). If false (the default value), the device can save resources by
    *  responding more quickly and/or using less power.
    */
    high_accuracy: PropTypes.bool,

    /**
     * The maximum age in milliseconds of a possible cached position that is acceptable to return. If set to 0,
     * it means that the device cannot use a cached position and must attempt to retrieve the real current position.
     * If set to Infinity the device must return a cached position regardless of its age. Default: 0.
     */
    maximum_age: PropTypes.number,

    /**
     * The maximum length of time (in milliseconds) the device is allowed to take in order to return a position.
     * The default value is Infinity, meaning that data will not be return until the position is available.
     */
    timeout: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};








