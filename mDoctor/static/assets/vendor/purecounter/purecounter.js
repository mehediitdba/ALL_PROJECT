/*!
 * purecounter.js - A simple yet configurable native javascript counter which you can count on.
 * Author: Stig Rex
 * Version: 1.1.4
 * Url: https://github.com/srexi/purecounterjs
 * License: MIT
 */!function(){"use strict";function e(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function t(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function r(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}new(function(){function n(e){!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,n),this.defaults={start:0,end:100,duration:2e3,delay:10,once:!0,decimals:0,legacy:!0,currency:!1,currencysymbol:!1,separator:!1,separatorsymbol:",",selector:".purecounter"},this.configOptions=Object.assign({},this.defaults,e||{}),this.registerEventListeners()}var a,i,o;return a=n,(i=[{key:"registerEventListeners",value:function(){var e=document.querySelectorAll(this.configOptions.selector);if(this.intersectionListenerSupported()){var t=new IntersectionObserver(this.animateElements.bind(this),{root:null,rootMargin:"20px",threshold:.5});e.forEach((function(e){t.observe(e)}))}else window.addEventListener&&(this.animateLegacy(e),window.addEventListener("scroll",(function(t){this.animateLegacy(e)}),{passive:!0}))}},{key:"animateLegacy",value:function(e){var t=this;e.forEach((function(e){!0===t.parseConfig(e).legacy&&t.elementIsInView(e)&&t.animateElements([e])}))}},{key:"animateElements",value:function(e,t){var r=this;e.forEach((function(e){var n=e.target||e,a=r.parseConfig(n);if(a.duration<=0)return n.innerHTML=r.formatNumber(a.end,a);if(!t&&!r.elementIsInView(e)||t&&e.intersectionRatio<.5){var i=a.start>a.end?a.end:a.start;return n.innerHTML=r.formatNumber(i,a)}setTimeout((function(){return r.startCounter(n,a)}),a.delay)}))}},{key:"startCounter",value:function(e,t){var r=this,n=(t.end-t.start)/(t.duration/t.delay),a="inc";t.start>t.end&&(a="dec",n*=-1);var i=this.parseValue(t.start);e.innerHTML=this.formatNumber(i,t),!0===t.once&&e.setAttribute("data-purecounter-duration",0);var o=setInterval((function(){var s=r.nextNumber(i,n,a);e.innerHTML=r.formatNumber(s,t),((i=s)>=t.end&&"inc"==a||i<=t.end&&"dec"==a)&&(e.innerHTML=r.formatNumber(t.end,t),clearInterval(o))}),t.delay)}},{key:"parseConfig",value:function(r){var n=this,a=function(r){for(var n=1;n<arguments.length;n++){var a=null!=arguments[n]?arguments[n]:{};n%2?e(Object(a),!0).forEach((function(e){t(r,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(r,Object.getOwnPropertyDescriptors(a)):e(Object(a)).forEach((function(e){Object.defineProperty(r,e,Object.getOwnPropertyDescriptor(a,e))}))}return r}({},this.configOptions),i=[].filter.call(r.attributes,(function(e){return/^data-purecounter-/.test(e.name)})),o={};return i.forEach((function(e){var t=e.name.replace("data-purecounter-","").toLowerCase(),r="duration"==t?parseInt(1e3*n.parseValue(e.value)):n.parseValue(e.value);o[t]=r})),Object.assign(a,o)}},{key:"nextNumber",value:function(e,t){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"inc";return e=this.parseValue(e),t=this.parseValue(t),parseFloat("inc"===r?e+t:e-t)}},{key:"convertToCurrencySystem",value:function(e,t){var r=t.currencysymbol||"",n=t.decimals||1;return r+((e=Math.abs(Number(e)))>=1e12?"".concat((e/1e12).toFixed(n)," T"):e>=1e9?"".concat((e/1e9).toFixed(n)," B"):e>=1e6?"".concat((e/1e6).toFixed(n)," M"):e>=1e3?"".concat((e/1e12).toFixed(n)," K"):e.toFixed(n))}},{key:"applySeparator",value:function(e,t){return t.separator?e.replace(/(\d)(?=(\d{3})+(?!\d))/g,"$1,").replace(new RegExp(/,/gi,"gi"),t.separatorsymbol):e.replace(new RegExp(/,/gi,"gi"),"")}},{key:"formatNumber",value:function(e,t){var r={minimumFractionDigits:t.decimals,maximumFractionDigits:t.decimals};return e=t.currency?this.convertToCurrencySystem(e,t):parseFloat(e),this.applySeparator(e.toLocaleString(void 0,r),t)}},{key:"parseValue",value:function(e){return/^[0-9]+\.[0-9]+$/.test(e)?parseFloat(e):/^[0-9]+$/.test(e)?parseInt(e):/^true|false/i.test(e)?/^true/i.test(e):e}},{key:"elementIsInView",value:function(e){for(var t=e.offsetTop,r=e.offsetLeft,n=e.offsetWidth,a=e.offsetHeight;e.offsetParent;)t+=(e=e.offsetParent).offsetTop,r+=e.offsetLeft;return t>=window.pageYOffset&&r>=window.pageXOffset&&t+a<=window.pageYOffset+window.innerHeight&&r+n<=window.pageXOffset+window.innerWidth}},{key:"intersectionListenerSupported",value:function(){return"IntersectionObserver"in window&&"IntersectionObserverEntry"in window&&"intersectionRatio"in window.IntersectionObserverEntry.prototype}}])&&r(a.prototype,i),o&&r(a,o),n}())}();
//# sourceMappingURL=purecounter.js.map


export default class PureCounter {
    constructor(options = {}) {
        /** Default configurations */
        this.defaults = {
            start: 0, // Starting number [uint]
            end: 100, // End number [uint]
            duration: 2000, // Count duration [milisecond]
            delay: 10, // Count delay [milisecond]
            once: true, // Counting at once or recount when scroll [boolean]
            pulse: false, // Pulse count for certain time [boolean|milisecond]
            decimals: 0, // Decimal places [uint]
            legacy: true, // If this is true it will use the scroll event listener on browsers
            filesizing: false, // Is it for filesize?
            currency: false, // Is it for currency? Use it for set the symbol too [boolean|char|string]
            separator: false, // Do you want to use thausands separator? use it for set the symbol too [boolean|char|string]
            formater: "us-US", // Number toLocaleString locale/formater, by default is "en-US" [string|boolean:false]
            selector: ".purecounter", // HTML query selector for spesific element
        };
        /** Set default configuration based on user input */
        this.configOptions = this.setOptions(options, this.defaults);
        /** Get all elemenets based on default selector */
        this.elements = document.querySelectorAll(this.configOptions.selector);
        /** Get browser Intersection Listener Support */
        this.intersectionSupport = this.intersectionListenerSupported();
        /** Initiate event listened */
        this.registerEventListeners();
    }

    /** This method is for create and merge configuration */
    setOptions(config, baseConfig = {}) {
        // Create new Config object;
        var newConfig = {};
        // Loop config items to set it value into newConfig
        for (var key in config) {
            // if baseConfig is set, only accept the baseconfig property
            if (Object.keys(baseConfig).length !== 0 && !baseConfig.hasOwnProperty(key))
                continue;
            // var parse the config value
            var val = this.parseValue(config[key]);
            // set the newConfig property value
            newConfig[key] = val;
            // Exclusive for 'duration' or 'pulse' property, recheck the value
            // If it's not a boolean, just set it to milisecond uint
            if (key.match(/duration|pulse/)) {
                newConfig[key] = typeof val != "boolean" ? val * 1000 : val;
            }
        }

        // Finally, we can just merge the baseConfig (if any), with newConfig.
        return Object.assign({}, baseConfig, newConfig);
    }

    /** Initial setup method */
    registerEventListeners() {
        /** Get all elements with class 'purecounter' */
        var elements = this.elements;
        /** Return if no elements */
        if (elements.length === 0) return;

        /** Run animateElements base on Intersection Support */
        if (this.intersectionSupport) {
            var intersectObserver = new IntersectionObserver(
                this.animateElements.bind(this),
                {
                    root: null,
                    rootMargin: "20px",
                    threshold: 0.5,
                }
            );

            elements.forEach((element) => {
                intersectObserver.observe(element);
            });
        } else {
            if (window.addEventListener) {
                this.animateLegacy(elements);
                window.addEventListener(
                    "scroll",
                    function (e) {
                        this.animateLegacy(elements);
                    },
                    { passive: true }
                );
            }
        }
    }

    /** This legacy to make Purecounter use very lightweight & fast */
    animateLegacy(elements) {
        elements.forEach((element) => {
            var config = this.parseConfig(element);
            if (config.legacy === true && this.elementIsInView(element)) {
                this.animateElements([element]);
            }
        });
    }

    /** Main Element Count Animation */
    animateElements(elements, observer) {
        elements.forEach((element) => {
            var elm = element.target || element; // Just make sure which element will be used
            var elementConfig = this.parseConfig(elm); // Get config value on that element

            // console.log(elementConfig);
            // If duration is less than or equal zero, just format the 'end' value
            if (elementConfig.duration <= 0) {
                return (elm.innerHTML = this.formatNumber(
                    elementConfig.end,
                    elementConfig
                ));
            }

            if (
                (!observer && !this.elementIsInView(element)) ||
                (observer && element.intersectionRatio < 0.5)
            ) {
                var value =
                    elementConfig.start > elementConfig.end
                        ? elementConfig.end
                        : elementConfig.start;
                return (elm.innerHTML = this.formatNumber(value, elementConfig));
            }

            // If duration is more than 0, then start the counter
            setTimeout(() => {
                return this.startCounter(elm, elementConfig);
            }, elementConfig.delay);
        });
    }

    /** This is the the counter method */
    startCounter(element, config) {
        // First, get the increments step
        var incrementsPerStep =
            (config.end - config.start) / (config.duration / config.delay);
        // Next, set the counter mode (Increment or Decrement)
        var countMode = "inc";

        // Set mode to 'decrement' and 'increment step' to minus if start is larger than end
        if (config.start > config.end) {
            countMode = "dec";
            incrementsPerStep *= -1;
        }

        // Next, determine the starting value
        var currentCount = this.parseValue(config.start);
        // And then print it's value to the page
        element.innerHTML = this.formatNumber(currentCount, config);

        // If the config 'once' is true, then set the 'duration' to 0
        if (config.once === true) {
            element.setAttribute("data-purecounter-duration", 0);
        }

        // Now, start counting with counterWorker using Interval method based on delay
        var counterWorker = setInterval(() => {
            // First, determine the next value base on current value, increment value, and count mode
            var nextNum = this.nextNumber(currentCount, incrementsPerStep, countMode);
            // Next, print that value to the page
            element.innerHTML = this.formatNumber(nextNum, config);
            // Now set that value to the current value, because it's already printed
            currentCount = nextNum;

            // If the value is larger or less than the 'end' (base on mode), then  print the end value and stop the Interval
            if (
                (currentCount >= config.end && countMode === "inc") ||
                (currentCount <= config.end && countMode === "dec")
            ) {
                element.innerHTML = this.formatNumber(config.end, config);
                // If 'pulse' is set ignore the 'once' config
                if (config.pulse) {
                    // First set the 'duration' to zero
                    element.setAttribute("data-purecounter-duration", 0);
                    // Next, use timeout to reset it duration back based on 'pulse' config
                    setTimeout(() => {
                        element.setAttribute(
                            "data-purecounter-duration",
                            config.duration / 1000
                        );
                    }, config.pulse);
                }
                // Now, we can close the conterWorker peacefully
                clearInterval(counterWorker);
            }
        }, config.delay);
    }

    /** This method is to generate the element Config */
    parseConfig(element) {
        // Next, get all 'data-precounter-*' attributes value. Store to array
        var configValues = [].filter.call(element.attributes, function (attr) {
            return /^data-purecounter-/.test(attr.name);
        });

        // Now, we create element config as an object
        var elementConfig =
            configValues.length != 0
                ? Object.assign(
                      {},
                      ...configValues.map(({ name, value }) => {
                          var key = name.replace("data-purecounter-", "").toLowerCase(),
                              val = this.parseValue(value);

                          return { [key]: val };
                      })
                  )
                : {};

        // Last setOptions and return
        return this.setOptions(elementConfig, this.configOptions);
    }

    /** This method is to get the next number */
    nextNumber(number, steps, mode = "inc") {
        // First, get the exact value from the number and step (int or float)
        number = this.parseValue(number);
        steps = this.parseValue(steps);

        // Last, get the next number based on current number, increment step, and count mode
        // Always return it as float
        return parseFloat(mode === "inc" ? number + steps : number - steps);
    }

    /** This method is to get the converted number */
    convertNumber(number, config) {
        /** Use converter if filesizing or currency is on */
        if (config.filesizing || config.currency) {
            number = Math.abs(Number(number)); // Get the absolute value of number

            var baseNumber = 1000, // Base multiplying treshold
                symbol =
                    config.currency && typeof config.currency === "string"
                        ? config.currency
                        : "", // Set the Currency Symbol (if any)
                limit = config.decimals || 1, // Set the decimal limit (default is 1)
                uint = ["", "K", "M", "B", "T"], // Number uint based exponent threshold
                value = ""; // Define value variable

            /** Changes base number and its uint for filesizing */
            if (config.filesizing) {
                baseNumber = 1024; // Use 1024 instead of 1000
                uint = ["bytes", "KB", "MB", "GB", "TB"]; // Change to 'bytes' uint
            }

            /** Set value based on the threshold */
            for (var i = 4; i >= 0; i--) {
                // If the exponent is 0
                if (i === 0) value = `${number.toFixed(limit)} ${uint[i]}`;
                // If the exponent is above zero
                if (number >= this.getFilesizeThreshold(baseNumber, i)) {
                    value = `${(
                        number / this.getFilesizeThreshold(baseNumber, i)
                    ).toFixed(limit)} ${uint[i]}`;
                    break;
                }
            }

            // Apply symbol before the value and return it as string
            return symbol + value;
        } else {
            /** Return its value as float if not using filesizing or currency*/
            return parseFloat(number);
        }
    }

    /** This method will get the given base.  */
    getFilesizeThreshold(baseNumber, index) {
        return Math.pow(baseNumber, index);
    }

    /** This method is to get the last formated number */
    applySeparator(value, config) {
        // Get replaced value based on it's separator/symbol.
        function replacedValue(val, separator) {
            // Well this is my regExp for detecting the Thausands Separator
            // I use 3 groups to determine it's separator
            // THen the group 4 is to get the decimals value
            var separatorRegExp =
                /^(?:(\d{1,3},(?:\d{1,3},?)*)|(\d{1,3}\.(?:\d{1,3}\.?)*)|(\d{1,3}(?:\s\d{1,3})*))([\.,]?\d{0,2}?)$/gi;

            return val.replace(separatorRegExp, function (match, g1, g2, g3, g4) {
                // set initial result value
                var result = "",
                    sep = "";
                if (g1 !== undefined) {
                    // Group 1 is using comma as thausands separator, and period as decimal separator
                    result = g1.replace(new RegExp(/,/gi, "gi"), separator);
                    sep = ",";
                } else if (g2 !== undefined) {
                    // Group 2 is using period as thausands separator, and comma as decimal separator
                    result = g2.replace(new RegExp(/\./gi, "gi"), separator);
                } else if (g3 !== undefined) {
                    // Group 3 is using space as thausands separator, and comma as decimal separator
                    result = g3.replace(new RegExp(/ /gi, "gi"), separator);
                }
                if (g4 !== undefined) {
                    var decimal = sep !== "," ? (separator !== "," ? "," : ".") : ".";
                    result += g4.replace(new RegExp(/\.|,/gi, "gi"), decimal);
                }
                // Returning result value;
                return result;
            });
        }
        // If config formater is not false, then apply separator
        if (config.formater) {
            // Now get the separator symbol
            var symbol = config.separator // if config separator is setted
                ? typeof config.separator === "string" // Check the type of value
                    ? config.separator // If it's type is string, then apply it's value
                    : "," // If it's not string (boolean), then apply comma as default separator
                : "";
            // Special exception when locale is not 'en-US' but separator value is 'true'
            // Use it's default locale thausands separator.
            if (config.formater !== "en-US" && config.separator === true) {
                return value;
            }
            // Return the replaced Value based on it's symbol
            return replacedValue(value, symbol);
        }
        // If config formater is false, then return it's default value
        return value;
    }

    /** This method is to get formated number to be printed in the page */
    formatNumber(number, config) {
        // This is the configuration for 'toLocaleString' method
        var strConfig = {
            minimumFractionDigits: config.decimals,
            maximumFractionDigits: config.decimals,
        };
        // Get locale from config formater
        var locale = typeof config.formater === "string" ? config.formater : undefined;

        // Set and convert the number base on its config.
        number = this.convertNumber(number, config);

        // Now format the number to string base on it's locale
        number = config.formater
            ? number.toLocaleString(locale, strConfig)
            : parseInt(number).toString();
        // Last, apply the number separator using number as string
        return this.applySeparator(number, config);
    }

    getLocaleSeparator() {
        var regExp =
            /^(?:(\d{1,3}(?:,\d{1,3})*(?:\.\d{0,3})?)|(\d{1,3}(?:\.\d{1,3})*(?:,\d{0,3})?)|(\d{1,3}(?:\s\d{1,3})*(?:,\d{0,3})?))$/i;
        return;
    }

    /** This method is to get the parsed value */
    parseValue(data) {
        // If number with dot (.), will be parsed as float
        if (/^[0-9]+\.[0-9]+$/.test(data)) {
            return parseFloat(data);
        }
        // If just number, will be parsed as integer
        if (/^[0-9]+$/.test(data)) {
            return parseInt(data);
        }
        // If it's boolean string, will be parsed as boolean
        if (/^true|false/i.test(data)) {
            return /^true/i.test(data);
        }
        // Return it's value as default
        return data;
    }

    /** This method is to detect the element is in view or not. */
    elementIsInView(element) {
        var top = element.offsetTop;
        var left = element.offsetLeft;
        var width = element.offsetWidth;
        var height = element.offsetHeight;

        while (element.offsetParent) {
            element = element.offsetParent;
            top += element.offsetTop;
            left += element.offsetLeft;
        }

        return (
            top >= window.pageYOffset &&
            left >= window.pageXOffset &&
            top + height <= window.pageYOffset + window.innerHeight &&
            left + width <= window.pageXOffset + window.innerWidth
        );
    }

    /** Just some condition to check browser Intersection Support */
    intersectionListenerSupported() {
        return (
            "IntersectionObserver" in window &&
            "IntersectionObserverEntry" in window &&
            "intersectionRatio" in window.IntersectionObserverEntry.prototype
        );
    }
}