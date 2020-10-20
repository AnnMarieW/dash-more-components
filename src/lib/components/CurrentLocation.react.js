import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * The CurrentLocation component gets geolocation of device from the web browser.  See more info here:
 * https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
 *
 */


 /*
 *  TODO:
 *        - Change name of this component to GeoLocation - or GeoPosition so it's not confused with dcc.Location?
 *        - How make an object a prop?  Currently position object is  {} in usage.py
 *               success(pos) seems really dopey.  How to update position vars properly?
 *        - format of datetime returned.  Currently formatted as local time. Add a field for datetime?
 *        - error handling and time-out.  Timeout currently set to 5 secs and all errors sent as alerts
  *               to be handled by browser.  Should it be a prop instead?
 *
 *        - anything else to do on  componentWillUnmount() ?
 *
 *
 *        - - figure out what WrappedComponent does in react-geolocated
 *             https://github.com/no23reason/react-geolocated/blob/master/src/index.js
 *
 *         - driving check:accuracy was variable.  Sometimes 30 meters, sometimes 100KM!  There have been some
 *              reports that it's flakey.
 *
 */



export default class CurrentLocation extends Component {
  constructor(props) {
    super(props);
    this.success = this.success.bind(this);
    this.updatePosition = this.updatePosition.bind(this);

  }

  updatePosition() {
    if (!navigator.geolocation) {
        alert('Your browser does not support Geolocation');
    } else {
        const date_str = new Date().toLocaleString();
        this.props.setProps({
          date: date_str,
          update_now: false,
        });

        var positionOptions = {
            enableHighAccuracy: this.props.high_accuracy,
            maximumAge: 0,
            timeout: 10000,
        };

        this.props.watch_position ? (
            navigator.geolocation.watchPosition(this.success, this.error, positionOptions)
        ) : (
            navigator.geolocation.getCurrentPosition(this.success, this.error, positionOptions)
        )
    }
  }


  componentDidMount() {
        this.updatePosition()
  }

  componentWillUnmount() {
            if (this.props.watch_position) {
                geolocationProvider.clearWatch(this.watchId);
            }
        }

  componentDidUpdate(prevProps) {
     if (prevProps.update_now !== this.props.update_now) {
        this.updatePosition()
     }
     if (prevProps.watch_position !== this.props.watch_position) {
        this.updatePosition()
     }
     if (prevProps.high_accuracy !== this.props.high_accuracy) {
        this.updatePosition()
     }
  }


  success(pos) {
    const crd = pos.coords
    const lat = crd.latitude;
    const lon = crd.longitude;
    const acc = crd.accuracy;

    this.props.setProps({
      latitude: lat,
      longitude: lon,
      accuracy: acc,
    });
  }


  error(err) {
  	alert(`ERROR(${err.code}): ${err.message}`);
    }

  render() {
    return  null;
  }
}


CurrentLocation.defaultProps = {
    watch_position : false,
    update_now : false,
    high_accuracy : false,
};

CurrentLocation.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The local date and time that the device position was updated
     */
    date: PropTypes.string,

    /**
     * The latitude of the device
    */
    latitude: PropTypes.number,

    /**
     * The longitude of the device
    */
    longitude: PropTypes.number,

    /**
     * The accuracy of the position in meters
    */
    accuracy: PropTypes.number,

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
    *  Position error  ** Add this prop? ***

    position_error: PropTypes.shape({
        code: PropTypes.oneOf([1, 2, 3]),
        message: PropTypes.string,
    }),
    */


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
    *  chip on a mobile device for example). If false (the default value), the device can take
    *  the liberty to save resources by responding more quickly and/or using less power.
    */
    high_accuracy: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};








