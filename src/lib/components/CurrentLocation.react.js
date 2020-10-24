import React, {Component} from 'react';
import PropTypes from 'prop-types';

//import toIsoFormat from '../utils/toIsoFormat';

/**
 * The CurrentLocation component gets geolocation of device from the web browser.  See more info here:
 * https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
 *
 */

 /*
 *  TODO:
 *        - Change name of this component to GeoLocation - or GeoPosition so it's not confused with dcc.Location?
 *
 *        - success(pos)   How to update position vars properly?
 *
 *         - decide which date format to use.  Move toIsoFormat to utils
 *
 *        - anything else to do on  componentWillUnmount() ?
 *
 *         - make timeout a prop
 */



export default class CurrentLocation extends Component {
  constructor(props) {
    super(props);
    this.success = this.success.bind(this);
    this.error = this.error.bind(this);
    this.updatePosition = this.updatePosition.bind(this);
    this.toIsoFormatLocal = this.toIsoFormatLocal.bind(this);
    this.toIsoFormatUTC = this.toIsoFormatUTC.bind(this);
    this.pad = this.pad.bind(this);

  }

  pad (num) {
     var norm = Math.floor(Math.abs(num));
     return (norm < 10 ? '0' : '') + norm;
  }
  toIsoFormatLocal (date) {
        return date.getFullYear() +
            '-' + this.pad(date.getMonth() + 1) +
            '-' + this.pad(date.getDate()) +
            ' ' + this.pad(date.getHours()) +
            ':' + this.pad(date.getMinutes()) +
            ':' + this.pad(date.getSeconds())
  }
  toIsoFormatUTC (date) {
      return date.getUTCFullYear() +
          '-' + this.pad(date.getUTCMonth() + 1) +
          '-' + this.pad(date.getUTCDate()) +
          ' ' + this.pad(date.getUTCHours()) +
          ':' + this.pad(date.getUTCMinutes()) +
          ':' + this.pad(date.getUTCSeconds())
  }


  updatePosition() {
    if (!navigator.geolocation) {
        alert('Your browser does not support Geolocation');
    } else {
        this.props.setProps({
          update_now: false,
        });

        var positionOptions = {
            enableHighAccuracy: this.props.high_accuracy,
            maximumAge: 0,
            timeout: 100000,
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
     if ((prevProps.update_now !== this.props.update_now)
          || (prevProps.watch_position !== this.props.watch_position)
          || (prevProps.high_accuracy !== this.props.high_accuracy)) {
        this.updatePosition()
     }
  }



  success(pos) {
    // Date:  Reformat to local string and ISO formats:
    //
    const d= new Date(pos.timestamp)
    // Local date string
    const local_date_str = d.toLocaleString();
    /* ISO date format - UTC date and time  Format: YYYY-MM-DDThh:mm:ss
     *       THis has a T in the time. Better to use the toISOFormat function?
     * const iso = d.toISOString();
     * const isodate_UTC_str = iso.split('.')[0];
     */
     // ISO date format - local date and time  Format: YYYY-MM-DD hh:mm:ss
     const isodate_UTC_str = this.toIsoFormatUTC(d)
     // ISO date format - local date and time Format: YYYY-MM-DD hh:mm:ss
     const isodate_local_str = this.toIsoFormatLocal(d)

    // Position data
    //
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

    this.props.setProps({
      local_date: local_date_str,
      isodate_UTC: isodate_UTC_str,
      isodate_local: isodate_local_str,
      position : position_obj,
      position_error : null
    });
  }

  error(err) {
    alert(`ERROR(${err.code}): ${err.message}`);

    const error_obj = ({
       code: err.code,
       message: err.message,
    });
    this.props.setProps({
       position_error: error_obj,
       position : null
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
     * The UCT (zulu) time  when the device position was updated. ISO Format: YYYY-MM-DDThh:mm:ss
     */
    isodate_UTC: PropTypes.string,

    /**
    * The local time when the device position was updated. ISO Format: YYYY-MM-DDThh:mm:ss
    */
    isodate_local: PropTypes.string,

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








