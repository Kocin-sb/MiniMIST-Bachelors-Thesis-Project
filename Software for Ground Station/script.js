var isPause;
        var chartVT, chartIT, chart_temp, chart_hum;
        var intervalID_solar, intervalID_sensor, intervalID_stream;
        var count = 0;
        var time_interval = 1000;
        var stream_button_state = 0;

        window.onload = function () {
            isPause = false;
            chartVT = new Highcharts.Chart({
                chart: {
                    renderTo: 'graphVT',
                    zoomType: 'xy',
                    panning: {
                        enabled: true,
                        type: 'xy'
                    },
                    panKey: 'ctrl',
                    type: 'spline'
                },
                title: { text: 'Solar Voltage Graph' },
                series: [{
                    name: "Voltage",
                    showInLegend: false,
                    data: [],
                    zones: [
                        {
                            value: 0.1,
                            color: '#434348'
                        },
                        {
                            value: 0.5,
                            color: '#F45B5B'
                        },
                        {
                            value: 2.5,
                            color: '#f7a35c'
                        },
                        { color: '#90ed7d' }
                    ]
                }],
                xAxis: {
                    type: 'datetime',
                    dateTimeLabelFormats: { second: '%H:%M:%S' }
                },
                yAxis: {
                    title: { text: 'Volatage (V)' }
                },
                plotOptions: {
                    line: {
                        animation: {
                            duration: 1000,
                            defer: 2
                        },
                        dataLabels: { enabled: true }
                    },
                    series: { color: '#308712' }
                },

                credits: { enabled: false }
            });

            chartIT = new Highcharts.Chart({
                chart: {
                    renderTo: 'graphIT',
                    zoomType: 'xy',
                    panning: {
                        enabled: true,
                        type: 'xy'
                    },
                    panKey: 'ctrl',
                    type: 'spline'
                },
                title: { text: 'Solar Current Graph' },
                series: [{
                    name: "Current Time",
                    showInLegend: false,
                    data: [],
                }],
                xAxis: {
                    type: 'datetime',
                    dateTimeLabelFormats: { second: '%H:%M:%S' }
                },
                yAxis: {
                    title: { text: 'Current (I/mA)' },
                },
                plotOptions: {
                    line: {
                        animation: {
                            duration: 1000,
                            defer: 2
                        },
                        dataLabels: { enabled: true }
                    },
                    series: { color: '#660000' }
                },
                credits: { enabled: false }
            });
            chartVI = new Highcharts.Chart({
                chart: {
                    renderTo: 'graphVI',
                    zoomType: 'xy',
                    panning: {
                        enabled: true,
                        type: 'xy'
                    },
                    panKey: 'ctrl',
                    type: 'scatter'
                },
                title: { text: 'VOltage Current' },
                series: [{
                    name: "Volt",
                    showInLegend: false,
                    data: [],
                }],
                xAxis: {
                    title: { text: "Voltage" }
                },
                yAxis: {
                    title: { text: 'Current (I/mA)' },
                },
                plotOptions: {
                    line: {
                        animation: {
                            duration: 1000,
                            defer: 2
                        },
                        dataLabels: { enabled: true }
                    },
                    series: { color: '#660000' }
                },
                credits: { enabled: false }
            });


            chart_temp = new Highcharts.Chart({
                chart: {
                    renderTo: 'temp',
                    zoomType: 'xy',
                    panning: {
                        enabled: true,
                        type: 'xy'
                    },
                    panKey: 'ctrl',
                    type: 'spline'
                },
                title: { text: 'Temperature' },
                series: [{
                    name: "TemperatureC",
                    showInLegend: false,
                    data: []
                }],
                xAxis: {
                    type: 'datetime',
                    dateTimeLabelFormats: { second: '%H:%M:%S' }
                },
                yAxis: {
                    title: { text: 'Temperature (C)' }
                },
                plotOptions: {
                    line: {
                        animation: {
                            duration: 1000,
                            defer: 2
                        },
                        dataLabels: { enabled: true }
                    }
                },
                credits: { enabled: false }
            });

            chart_hum = new Highcharts.Chart({
                chart: {
                    renderTo: 'hum',
                    zoomType: 'xy',
                    panning: {
                        enabled: true,
                        type: 'xy'
                    },
                    panKey: 'ctrl',
                    type: 'spline'
                },
                title: { text: 'Humidity' },
                series: [{
                    name: "Hum",
                    showInLegend: false,
                    data: []
                }],
                xAxis: {
                    type: 'datetime',
                    dateTimeLabelFormats: { second: '%H:%M:%S' }
                },
                yAxis: {
                    title: { text: 'humidity' }
                },
                plotOptions: {
                    line: {
                        animation: {
                            duration: 1000,
                            defer: 2
                        },
                        dataLabels: { enabled: true }
                    }
                },
                credits: { enabled: false }
            });

            // intervalID_solar = setInterval(updatesolar, time_interval);
            // intervalID_sensor = setInterval(updatesensor, 1020);
            setInterval(updatedatetime, 1000);
        }
        function updatedatetime() {
            if (!isPause) {
                var dt = new Date();
                document.getElementById("time").innerHTML = dt.toLocaleTimeString();
                document.getElementById("date").innerHTML = dt.toLocaleDateString();
            }
        }

        function check_interval(chart1, now) {
            return false;
        }

        function updatesolar(callback1) {
            var xhttp = new XMLHttpRequest();
            xhttp.onload = function () {
                if (this.status == 200) {
                    var x = (new Date()).getTime();
                    var temp = JSON.parse(this.responseText);
                    console.log(temp);
                    var y = parseFloat(parseFloat(temp["solar_voltage"]).toFixed(2));
                    var z = parseFloat(parseFloat(temp["solar_current"]).toFixed(3));
                    // var y = parseFloat((Math.random() * 10).toFixed(2));
                    // var z = y * 34 + 29;
                    // if (check_interval(chartVT,x)){chartVT.series.remove(true)};
                    if (chartVT.series[0].data.length > 15) { //TODO check timeinterval between new and first element of series: if large clear data else 
                        chartVI.series[0].addPoint([y, z], true, true, true);
                        chartVT.series[0].addPoint([x, y], true, true, true);
                        chartIT.series[0].addPoint([x, z], true, true, true);
                    } else {
                        chartVI.series[0].addPoint([y, z], true, false, true);
                        chartVT.series[0].addPoint([x, y], true, false, true);
                        chartIT.series[0].addPoint([x, z], true, false, true);
                    }
                    if (count % 5 == 0) {
                        document.getElementById("BatteryLevel").innerHTML = (parseFloat(temp["battery_voltage"]).toFixed(0)) + " %";
                    }
                    count++;
                    document.getElementById("Volt").innerHTML = (parseFloat(temp["solar_voltage"]).toFixed(1)) + " V";
                    document.getElementById("Cur").innerHTML = (parseFloat(temp["solar_current"]).toFixed(2)) + " mA";
                    document.getElementById("Power").innerHTML = (parseFloat(temp["solar_power"]).toFixed(2)) + " mW";
                }
            }
            xhttp.open("GET", "/getsolar", true);
            xhttp.send();
            console.log("solar done");
            setTimeout(() => {
                if (typeof (callback1) === 'function') { callback1(); }
            }, 500);
        }

        function updatesensor() {
            xhrtbl = new XMLHttpRequest();
            xhrtbl.open("GET", "/getsensor", true);
            xhrtbl.send();
            xhrtbl.onload = function () {
                if (this.status == 200) {
                    var response = JSON.parse(this.responseText);
                    var x = (new Date()).getTime();
                    var y = parseFloat(parseFloat(response["temperatureC"]).toFixed(2));
                    var z = parseFloat(parseFloat(response["humidity"]).toFixed(2));
                    console.log(response);
                    if (chart_hum.series[0].data.length > 15) {
                        chart_hum.series[0].addPoint([x, y], true, true, true);
                        chart_temp.series[0].addPoint([x, z], true, true, true);
                    } else {
                        chart_hum.series[0].addPoint([x, y], true, false, true);
                        chart_temp.series[0].addPoint([x, z], true, false, true);
                    }
                    document.getElementById("temperature").innerHTML = response["temperatureC"] + "°C";
                    document.getElementById("temperaturef").innerHTML = response["temperatureF"] + "°F";
                    document.getElementById("humidity").innerHTML = response["humidity"] + "%";
                }
            }
            xhrtbl.onerror = function () {
                console.log("Error Occured");
            }
            console.log("Sensor done");
        }

        function encode64(inputStr) {
            var b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
            var outputStr = "data:image.gif;base64,";
            var i = 0;

            while (i < inputStr.length) {
                var byte1 = inputStr.charCodeAt(i++) & 0xff;
                var byte2 = inputStr.charCodeAt(i++) & 0xff;
                var byte3 = inputStr.charCodeAt(i++) & 0xff;

                var enc1 = byte1 >> 2;
                var enc2 = ((byte1 & 3) << 4) | (byte2 >> 4);

                var enc3, enc4;
                if (isNaN(byte2)) {
                    enc3 = enc4 = 64;
                } else {
                    enc3 = ((byte2 & 15) << 2) | (byte3 >> 6);
                    if (isNaN(byte3)) {
                        enc4 = 64;
                    } else {
                        enc4 = byte3 & 63;
                    }
                }
                outputStr += b64.charAt(enc1) + b64.charAt(enc2) + b64.charAt(enc3) + b64.charAt(enc4);
            }
            return outputStr;
        }

        function loadImage(callback1, callback2) {

            var xhr1 = new XMLHttpRequest();
            xhr1.open("GET", "/getimage", true);
            xhr1.overrideMimeType('text/plain; charset=x-user-defined');
            xhr1.send();
            xhr1.onload = function () {
                if (this.status == 200) {
                    var image = document.getElementById("sat-image");
                    var response = xhr1.responseText;
                    source = encode64(response);
                    image.src = source;
                }
            }
            xhr1.onerror = function () {
                console.log("Error Occured");
            }
            console.log("Image done");

            // setTimeout(() => {
            //     if (typeof (callback1) === 'function' || typeof (callback2) === 'function') { callback1(callback2); }
            // }, 500);
        }

        function stream(stream_button) {
            stream_button_state = 1 - stream_button_state;
            var counterint = 0;
            var counterimg = 0;
            var countersen = 0;
            var countersol = 0;
            enable_stream_button(stream_button, stream_button_state);
            if (stream_button_state) {
                intervalID_stream = setInterval(() => {
                    console.log("Interval start", counterint++);
                    setTimeout(() => {
                        let start = (new Date()).getMilliseconds();
                        loadImage();
                        let end = (new Date()).getMilliseconds();
                        console.log("Load image end", counterimg++, "Time : ", end, "-", start, " = ", end - start);
                        setTimeout(() => {
                            updatesensor();
                            console.log("sensor end", countersen++);
                            setTimeout(() => {
                                updatesolar();
                                console.log("Solar end", countersol++);
                            }, 500);
                        }, 500);
                    }, 0);
                }, 5000);
            }
            else {
                clearInterval(intervalID_stream);
            }
        }
        function enable_stream_button(stream_button, state) {
            if (state) {
                stream_button.innerHTML = "Stream: ON";
                stream_button.style.background = "green";
                stream_button.style.color = "lightgreen";
                ["imagebutton", "solarbutton", "sensorbutton"].forEach((button) => {
                    document.getElementById(button).disabled = true;
                })
            }
            else {
                stream_button.innerHTML = "Stream: OFF";
                stream_button.style.background = "lightgrey";
                stream_button.style.color = "grey";
                ["imagebutton", "solarbutton", "sensorbutton"].forEach((button) => {
                    document.getElementById(button).disabled = false;
                })
            }
        }
