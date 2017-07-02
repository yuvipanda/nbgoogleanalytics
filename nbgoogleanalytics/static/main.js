define([
    'base/js/utils',
    'services/config'
], function (utils, configmod) {

    function setupGA(tracking_id) {
        // Code from GA
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

        ga('create', tracking_id, 'auto');
        ga('send', 'pageview');
    }

    var load_ipython_extension = function () {
        // Only load GA if DNT is not set
        if (navigator.doNotTrack != "1" && // Most Firefox & Chrome
            window.doNotTrack != "1" && // IE & Safari
            navigator.msDoNotTrack != "1" // Old IE
           ) {
            var base_url = utils.get_body_data("baseUrl");
            var configSection = new configmod.ConfigSection('common', {base_url: base_url});

            // FIXME: This seems to fetch the config again
            // However, just attaching a then to configSection.loaded
            // Does not seem to work. MAKE IT WORK.
            configSection.load().then(function() {
                setupGA(configSection.data['GoogleAnalytics']['tracking_id']);
            });
        }
    };

    return {
        load_ipython_extension: load_ipython_extension,
    };
});
