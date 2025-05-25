// Portlet constructor
!function($) {
    "use strict";

    var Portlet = function() {
        this.$body = $("body"),
        this.$portletIdentifier = ".portlet",
        this.$portletCloser = '.portlet a[data-toggle="remove"]',
        this.$portletRefresher = '.portlet a[data-toggle="reload"]'
    };

    Portlet.prototype.init = function() {
        var $this = this;

        // Remove portlet
        $(document).on("click", this.$portletCloser, function (ev) {
            ev.preventDefault();
            var $portlet = $(this).closest($this.$portletIdentifier);
            var $portlet_parent = $portlet.parent();
            $portlet.remove();
            if ($portlet_parent.children().length == 0) {
                $portlet_parent.remove();
            }
        });

        // Reload portlet (simulate)
        $(document).on("click", this.$portletRefresher, function (ev) {
            ev.preventDefault();
            var $portlet = $(this).closest($this.$portletIdentifier);
            $portlet.append('<div class="panel-disabled"><div class="loader-1"></div></div>');
            var $pd = $portlet.find('.panel-disabled');
            setTimeout(function () {
                $pd.fadeOut('fast', function () {
                    $pd.remove();
                });
            }, 500 + 300 * (Math.random() * 5));
        });
    };

    $.Portlet = new Portlet;
    $.Portlet.Constructor = Portlet;

}(window.jQuery);

// Components initializer
!function($) {
    "use strict";

    var Components = function() {};

    Components.prototype.initTooltipPlugin = function() {
        $.fn.tooltip && $('[data-toggle="tooltip"]').tooltip();
    };

    Components.prototype.initPopoverPlugin = function() {
        $.fn.popover && $('[data-toggle="popover"]').popover();
    };

    Components.prototype.initCustomModalPlugin = function() {
        $('[data-plugin="custommodal"]').on('click', function(e) {
            Custombox.open({
                target: $(this).attr("href"),
                effect: $(this).attr("data-animation"),
                overlaySpeed: $(this).attr("data-overlaySpeed"),
                overlayColor: $(this).attr("data-overlayColor")
            });
            e.preventDefault();
        });
    };

    Components.prototype.initNiceScrollPlugin = function() {
        $.fn.niceScroll && $(".nicescroll").niceScroll({ cursorcolor: '#98a6ad', cursorwidth:'6px', cursorborderradius: '5px' });
    };

    Components.prototype.initRangeSlider = function() {
        $.fn.slider && $('[data-plugin="range-slider"]').slider({});
    };

    Components.prototype.initSwitchery = function() {
        $('[data-plugin="switchery"]').each(function () {
            new Switchery($(this)[0], $(this).data());
        });
    };

    Components.prototype.initMultiSelect = function() {
        $('[data-plugin="multiselect"]').multiSelect();
    };

    Components.prototype.initPeityCharts = function() {
        $('[data-plugin="peity-pie"]').each(function() {
            var colors = $(this).data('colors') ? $(this).data('colors').split(",") : [];
            var width = $(this).data('width') || 20;
            var height = $(this).data('height') || 20;
            $(this).peity("pie", { fill: colors, width: width, height: height });
        });

        $('[data-plugin="peity-donut"]').each(function() {
            var colors = $(this).data('colors') ? $(this).data('colors').split(",") : [];
            var width = $(this).data('width') || 20;
            var height = $(this).data('height') || 20;
            $(this).peity("donut", { fill: colors, width: width, height: height });
        });

        $('[data-plugin="peity-bar"]').each(function() {
            var colors = $(this).data('colors') ? $(this).data('colors').split(",") : [];
            var width = $(this).data('width') || 20;
            var height = $(this).data('height') || 20;
            $(this).peity("bar", { fill: colors, width: width, height: height });
        });
    };

    Components.prototype.initKnob = function() {
        $('[data-plugin="knob"]').knob();
    };

    Components.prototype.initCircliful = function() {
        $('[data-plugin="circliful"]').circliful();
    };

    Components.prototype.initCounterUp = function() {
        $('[data-plugin="counterup"]').each(function() {
            var delay = $(this).data('delay') || 100;
            var time = $(this).data('time') || 1200;
            $(this).counterUp({ delay: delay, time: time });
        });
    };

    Components.prototype.init = function() {
        this.initTooltipPlugin();
        this.initPopoverPlugin();
        this.initNiceScrollPlugin();
        this.initCustomModalPlugin();
        this.initRangeSlider();
        this.initSwitchery();
        this.initMultiSelect();
        this.initPeityCharts();
        this.initKnob();
        this.initCircliful();
        this.initCounterUp();

        $.Portlet.init();
    };

    $.Components = new Components();
    $.Components.Constructor = Components;

    // ⚠️ DOM tayyor bo‘lgandan keyin init qilamiz
    $(document).ready(function () {
        $.Components.init();
    });

}(window.jQuery);
