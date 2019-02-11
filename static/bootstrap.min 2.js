/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under the MIT license
 */
if("undefined"==typeof jQuery)throw new Error("Bootstrap's JavaScript requires jQuery");+function(a){"use strict";var b=a.fn.jquery.split(" ")[0].split(".");if(b[0]<2&&b[1]<9||1==b[0]&&9==b[1]&&b[2]<1||b[0]>3)throw new Error("Bootstrap's JavaScript requires jQuery version 1.9.1 or higher, but lower than version 4")}(jQuery),+function(a){"use strict";function b(){var a=document.createElement("bootstrap"),b={WebkitTransition:"webkitTransitionEnd",MozTransition:"transitionend",OTransition:"oTransitionEnd otransitionend",transition:"transitionend"};for(var c in b)if(void 0!==a.style[c])return{end:b[c]};return!1}a.fn.emulateTransitionEnd=function(b){var c=!1,d=this;a(this).one("bsTransitionEnd",function(){c=!0});var e=function(){c||a(d).trigger(a.support.transition.end)};return setTimeout(e,b),this},a(function(){a.support.transition=b(),a.support.transition&&(a.event.special.bsTransitionEnd={bindType:a.support.transition.end,delegateType:a.support.transition.end,handle:function(b){if(a(b.target).is(this))return b.handleObj.handler.apply(this,arguments)}})})}(jQuery),+function(a){"use strict";function b(b){return this.each(function(){var c=a(this),e=c.data("bs.alert");e||c.data("bs.alert",e=new d(this)),"string"==typeof b&&e[b].call(c)})}var c='[data-dismiss="alert"]',d=function(b){a(b).on("click",c,this.close)};d.VERSION="3.3.7",d.TRANSITION_DURATION=150,d.prototype.close=function(b){function c(){g.detach().trigger("closed.bs.alert").remove()}var e=a(this),f=e.attr("data-target");f||(f=e.attr("href"),f=f&&f.replace(/.*(?=#[^\s]*$)/,""));var g=a("#"===f?[]:f);b&&b.preventDefault(),g.length||(g=e.closest(".alert")),g.trigger(b=a.Event("close.bs.alert")),b.isDefaultPrevented()||(g.removeClass("in"),a.support.transition&&g.hasClass("fade")?g.one("bsTransitionEnd",c).emulateTransitionEnd(d.TRANSITION_DURATION):c())};var e=a.fn.alert;a.fn.alert=b,a.fn.alert.Constructor=d,a.fn.alert.noConflict=function(){return a.fn.alert=e,this},a(document).on("click.bs.alert.data-api",c,d.prototype.close)}(jQuery),+function(a){"use strict";function b(b){return this.each(function(){var d=a(this),e=d.data("bs.button"),f="object"==typeof b&&b;e||d.data("bs.button",e=new c(this,f)),"toggle"==b?e.toggle():b&&e.setState(b)})}var c=function(b,d){this.$element=a(b),this.options=a.extend({},c.DEFAULTS,d),this.isLoading=!1};c.VERSION="3.3.7",c.DEFAULTS={loadingText:"loading..."},c.prototype.setState=function(b){var c="disabled",d=this.$element,e=d.is("input")?"val":"html",f=d.data();b+="Text",null==f.resetText&&d.data("resetText",d[e]()),setTimeout(a.proxy(function(){d[e](null==f[b]?this.options[b]:f[b]),"loadingText"==b?(this.isLoading=!0,d.addClass(c).attr(c,c).prop(c,!0)):this.isLoading&&(this.isLoading=!1,d.removeClass(c).removeAttr(c).prop(c,!1))},this),0)},c.prototype.toggle=function(){var a=!0,b=this.$element.closest('[data-toggle="buttons"]');if(b.length){var c=this.$element.find("input");"radio"==c.prop("type")?(c.prop("checked")&&(a=!1),b.find(".active").removeClass("active"),this.$element.addClass("active")):"checkbox"==c.prop("type")&&(c.prop("checked")!==this.$element.hasClass("active")&&(a=!1),this.$element.toggleClass("active")),c.prop("checked",this.$element.hasClass("active")),a&&c.trigger("change")}else this.$element.attr("aria-pressed",!this.$element.hasClass("active")),this.$element.toggleClass("active")};var d=a.fn.button;a.fn.button=b,a.fn.button.Constructor=c,a.fn.button.noConflict=function(){return a.fn.button=d,this},a(document).on("click.bs.button.data-api",'[data-toggle^="button"]',function(c){var d=a(c.target).closest(".btn");b.call(d,"toggle"),a(c.target).is('input[type="radio"], input[type="checkbox"]')||(c.preventDefault(),d.is("input,button")?d.trigger("focus"):d.find("input:visible,button:visible").first().trigger("focus"))}).on("focus.bs.button.data-api blur.bs.button.data-api",'[data-toggle^="button"]',function(b){a(b.target).closest(".btn").toggleClass("focus",/^focus(in)?$/.test(b.type))})}(jQuery),+function(a){"use strict";function b(b){return this.each(function(){var d=a(this),e=d.data("bs.carousel"),f=a.extend({},c.DEFAULTS,d.data(),"object"==typeof b&&b),g="string"==typeof b?b:f.slide;e||d.data("bs.carousel",e=new c(this,f)),"number"==typeof b?e.to(b):g?e[g]():f.interval&&e.pause().cycle()})}var c=function(b,c){this.$element=a(b),this.$indicators=this.$element.find(".carousel-indicators"),this.options=c,this.paused=null,this.sliding=null,this.interval=null,this.$active=null,this.$items=null,this.options.keyboard&&this.$element.on("keydown.bs.carousel",a.proxy(this.keydown,this)),"hover"==this.options.pause&&!("ontouchstart"in document.documentElement)&&this.$element.on("mouseenter.bs.carousel",a.proxy(this.pause,this)).on("mouseleave.bs.carousel",a.proxy(this.cycle,this))};c.VERSION="3.3.7",c.TRANSITION_DURATION=600,c.DEFAULTS={interval:5e3,pause:"hover",wrap:!0,keyboard:!0},c.prototype.keydown=function(a){if(!/input|textarea/i.test(a.target.tagName)){switch(a.which){case 37:this.prev();break;case 39:this.next();break;default:return}a.preventDefault()}},c.prototype.cycle=function(b){return b||(this.paused=!1),this.interval&&clearInterval(this.interval),this.options.interval&&!this.paused&&(this.interval=setInterval(a.proxy(this.next,this),this.options.interval)),this},c.prototype.getItemIndex=function(a){return this.$items=a.parent().children(".item"),this.$items.index(a||this.$active)},c.prototype.getItemForDirection=function(a,b){var c=this.getItemIndex(b),d="prev"==a&&0===c||"next"==a&&c==this.$items.length-1;if(d&&!this.options.wrap)return b;var e="prev"==a?-1:1,f=(c+e)%this.$items.length;return this.$items.eq(f)},c.prototype.to=function(a){var b=this,c=this.getItemIndex(this.$active=this.$element.find(".item.active"));if(!(a>this.$items.length-1||a<0))return this.sliding?this.$element.one("slid.bs.carousel",function(){b.to(a)}):c==a?this.pause().cycle():this.slide(a>c?"next":"prev",this.$items.eq(a))},c.prototype.pause=function(b){return b||(this.paused=!0),this.$element.find(".next, .prev").length&&a.support.transition&&(this.$element.trigger(a.support.transition.end),this.cycle(!0)),this.interval=clearInterval(this.interval),this},c.prototype.next=function(){if(!this.sliding)return this.slide("next")},c.prototype.prev=function(){if(!this.sliding)return this.slide("prev")},c.prototype.slide=function(b,d){var e=this.$element.find(".item.active"),f=d||this.getItemForDirection(b,e),g=this.interval,h="next"==b?"left":"right",i=this;if(f.hasClass("active"))return this.sliding=!1;var j=f[0],k=a.Event("slide.bs.carousel",{relatedTarget:j,direction:h});if(this.$element.trigger(k),!k.isDefaultPrevented()){if(this.sliding=!0,g&&this.pause(),this.$indicators.length){this.$indicators.find(".active").removeClass("active");var l=a(this.$indicators.children()[this.getItemIndex(f)]);l&&l.addClass("active")}var m=a.Event("slid.bs.carousel",{relatedTarget:j,direction:h});return a.support.transition&&this.$element.hasClass("slide")?(f.addClass(b),f[0].offsetWidth,e.addClass(h),f.addClass(h),e.one("bsTransitionEnd",function(){f.removeClass([b,h].join(" ")).addClass("active"),e.removeClass(["active",h].join(" ")),i.sliding=!1,setTimeout(function(){i.$element.trigger(m)},0)}).emulateTransitionEnd(c.TRANSITION_DURATION)):(e.removeClass("active"),f.addClass("active"),this.sliding=!1,this.$element.trigger(m)),g&&this.cycle(),this}};var d=a.fn.carousel;a.fn.carousel=b,a.fn.carousel.Constructor=c,a.fn.carousel.noConflict=function(){return a.fn.carousel=d,this};var e=function(c){var d,e=a(this),f=a(e.attr("data-target")||(d=e.attr("href"))&&d.replace(/.*(?=#[^\s]+$)/,""));if(f.hasClass("carousel")){var g=a.extend({},f.data(),e.data()),h=e.attr("data-slide-to");h&&(g.interval=!1),b.call(f,g),h&&f.data("bs.carousel").to(h),c.preventDefault()}};a(document).on("click.bs.carousel.data-api","[data-slide]",e).on("click.bs.carousel.data-api","[data-slide-to]",e),a(window).on("load",function(){a('[data-ride="carousel"]').each(function(){var c=a(this);b.call(c,c.data())})})}(jQuery),+function(a){"use strict";function b(b){var c,d=b.attr("data-target")||(c=b.attr("href"))&&c.replace(/.*(?=#[^\s]+$)/,"");return a(d)}function c(b){return this.each(function(){var c=a(this),e=c.data("bs.collapse"),f=a.extend({},d.DEFAULTS,c.data(),"object"==typeof b&&b);!e&&f.toggle&&/show|hide/.test(b)&&(f.toggle=!1),e||c.data("bs.collapse",e=new d(this,f)),"string"==typeof b&&e[b]()})}var d=function(b,c){this.$element=a(b),this.options=a.extend({},d.DEFAULTS,c),this.$trigger=a('[data-toggle="collapse"][href="#'+b.id+'"],[data-toggle="collapse"][data-target="#'+b.id+'"]'),this.transitioning=null,this.options.parent?this.$parent=this.getParent():this.addAriaAndCollapsedClass(this.$element,this.$trigger),this.options.toggle&&this.toggle()};d.VERSION="3.3.7",d.TRANSITION_DURATION=350,d.DEFAULTS={toggle:!0},d.prototype.dimension=function(){var a=this.$element.hasClass("width");return a?"width":"height"},d.prototype.show=function(){if(!this.transitioning&&!this.$element.hasClass("in")){var b,e=this.$parent&&this.$parent.children(".panel").children(".in, .collapsing");if(!(e&&e.length&&(b=e.data("bs.collapse"),b&&b.transitioning))){var f=a.Event("show.bs.collapse");if(this.$element.trigger(f),!f.isDefaultPrevented()){e&&e.length&&(c.call(e,"hide"),b||e.data("bs.collapse",null));var g=this.dimension();this.$element.removeClass("collapse").addClass("collapsing")[g](0).attr("aria-expanded",!0),this.$trigger.removeClass("collapsed").attr("aria-expanded",!0),this.transitioning=1;var h=function(){this.$element.removeClass("collapsing").addClass("collapse in")[g](""),this.transitioning=0,this.$element.trigger("shown.bs.collapse")};if(!a.support.transition)return h.call(this);var i=a.camelCase(["scroll",g].join("-"));this.$element.one("bsTransitionEnd",a.proxy(h,this)).emulateTransitionEnd(d.TRANSITION_DURATION)[g](this.$element[0][i])}}}},d.prototype.hide=function(){if(!this.transitioning&&this.$element.hasClass("in")){var b=a.Event("hide.bs.collapse");if(this.$element.trigger(b),!b.isDefaultPrevented()){var c=this.dimension();this.$element[c](this.$element[c]())[0].offsetHeight,this.$element.addClass("collapsing").removeClass("collapse in").attr("aria-expanded",!1),this.$trigger.addClass("collapsed").attr("aria-expanded",!1),this.transitioning=1;var e=function(){this.transitioning=0,this.$element.removeClass("collapsing").addClass("collapse").trigger("hidden.bs.collapse")};return a.support.transition?void this.$element[c](0).one("bsTransitionEnd",a.proxy(e,this)).emulateTransitionEnd(d.TRANSITION_DURATION):e.call(this)}}},d.prototype.toggle=function(){this[this.$element.hasClass("in")?"hide":"show"]()},d.prototype.getParent=function(){return a(this.options.parent).find('[data-toggle="collapse"][data-parent="'+this.options.parent+'"]').each(a.proxy(function(c,d){var e=a(d);this.addAriaAndCollapsedClass(b(e),e)},this)).end()},d.prototype.addAriaAndCollapsedClass=function(a,b){var c=a.hasClass("in");a.attr("aria-expanded",c),b.toggleClass("collapsed",!c).attr("aria-expanded",c)};var e=a.fn.collapse;a.fn.collapse=c,a.fn.collapse.Constructor=d,a.fn.collapse.noConflict=function(){return a.fn.collapse=e,this},a(document).on("click.bs.collapse.data-api",'[data-toggle="collapse"]',function(d){var e=a(this);e.attr("data-target")||d.preventDefault();var f=b(e),g=f.data("bs.collapse"),h=g?"toggle":e.data();c.call(f,h)})}(jQuery),+function(a){"use strict";function b(b){var c=b.attr("data-target");c||(c=b.attr("href"),c=c&&/#[A-Za-z]/.test(c)&&c.replace(/.*(?=#[^\s]*$)/,""));var d=c&&a(c);return d&&d.length?d:b.parent()}function c(c){c&&3===c.which||(a(e).remove(),a(f).each(function(){var d=a(this),e=b(d),f={relatedTarget:this};e.hasClass("open")&&(c&&"click"==c.type&&/input|textarea/i.test(c.target.tagName)&&a.contains(e[0],c.target)||(e.trigger(c=a.Event("hide.bs.dropdown",f)),c.isDefaultPrevented()||(d.attr("aria-expanded","false"),e.removeClass("open").trigger(a.Event("hidden.bs.dropdown",f)))))}))}function d(b){return this.each(function(){var c=a(this),d=c.data("bs.dropdown");d||c.data("bs.dropdown",d=new g(this)),"string"==typeof b&&d[b].call(c)})}var e=".dropdown-backdrop",f='[data-toggle="dropdown"]',g=function(b){a(b).on("click.bs.dropdown",this.toggle)};g.VERSION="3.3.7",g.prototype.toggle=function(d){var e=a(this);if(!e.is(".disabled, :disabled")){var f=b(e),g=f.hasClass("open");if(c(),!g){"ontouchstart"in document.documentElement&&!f.closest(".navbar-nav").length&&a(document.createElement("div")).addClass("dropdown-backdrop").insertAfter(a(this)).on("click",c);var h={relatedTarget:this};if(f.trigger(d=a.Event("show.bs.dropdown",h)),d.isDefaultPrevented())return;e.trigger("focus").attr("aria-expanded","true"),f.toggleClass("open").trigger(a.Event("shown.bs.dropdown",h))}return!1}},g.prototype.keydown=function(c){if(/(38|40|27|32)/.test(c.which)&&!/input|textarea/i.test(c.target.tagName)){var d=a(this);if(c.preventDefault(),c.stopPropagation(),!d.is(".disabled, :disabled")){var e=b(d),g=e.hasClass("open");if(!g&&27!=c.which||g&&27==c.which)return 27==c.which&&e.find(f).trigger("focus"),d.trigger("click");var h=" li:not(.disabled):visible a",i=e.find(".dropdown-menu"+h);if(i.length){var j=i.index(c.target);38==c.which&&j>0&&j--,40==c.which&&j<i.length-1&&j++,~j||(j=0),i.eq(j).trigger("focus")}}}};var h=a.fn.dropdown;a.fn.dropdown=d,a.fn.dropdown.Constructor=g,a.fn.dropdown.noConflict=function(){return a.fn.dropdown=h,this},a(document).on("click.bs.dropdown.data-api",c).on("click.bs.dropdown.data-api",".dropdown form",function(a){a.stopPropagation()}).on("click.bs.dropdown.data-api",f,g.prototype.toggle).on("keydown.bs.dropdown.data-api",f,g.prototype.keydown).on("keydown.bs.dropdown.data-api",".dropdown-menu",g.prototype.keydown)}(jQuery),+function(a){"use strict";function b(b,d){return this.each(function(){var e=a(this),f=e.data("bs.modal"),g=a.extend({},c.DEFAULTS,e.data(),"object"==typeof b&&b);f||e.data("bs.modal",f=new c(this,g)),"string"==typeof b?f[b](d):g.show&&f.show(d)})}var c=function(b,c){this.options=c,this.$body=a(document.body),this.$element=a(b),this.$dialog=this.$element.find(".modal-dialog"),this.$backdrop=null,this.isShown=null,this.originalBodyPad=null,this.scrollbarWidth=0,this.ignoreBackdropClick=!1,this.options.remote&&this.$element.find(".modal-content").load(this.options.remote,a.proxy(function(){this.$element.trigger("loaded.bs.modal")},this))};c.VERSION="3.3.7",c.TRANSITION_DURATION=300,c.BACKDROP_TRANSITION_DURATION=150,c.DEFAULTS={backdrop:!0,keyboard:!0,show:!0},c.prototype.toggle=function(a){return this.isShown?this.hide():this.show(a)},c.prototype.show=function(b){var d=this,e=a.Event("show.bs.modal",{relatedTarget:b});this.$element.trigger(e),this.isShown||e.isDefaultPrevented()||(this.isShown=!0,this.checkScrollbar(),this.setScrollbar(),this.$body.addClass("modal-open"),this.escape(),this.resize(),this.$element.on("click.dismiss.bs.modal",'[data-dismiss="modal"]',a.proxy(this.hide,this)),this.$dialog.on("mousedown.dismiss.bs.modal",function(){d.$element.one("mouseup.dismiss.bs.modal",function(b){a(b.target).is(d.$element)&&(d.ignoreBackdropClick=!0)})}),this.backdrop(function(){var e=a.support.transition&&d.$element.hasClass("fade");d.$element.parent().length||d.$element.appendTo(d.$body),d.$element.show().scrollTop(0),d.adjustDialog(),e&&d.$element[0].offsetWidth,d.$element.addClass("in"),d.enforceFocus();var f=a.Event("shown.bs.modal",{relatedTarget:b});e?d.$dialog.one("bsTransitionEnd",function(){d.$element.trigger("focus").trigger(f)}).emulateTransitionEnd(c.TRANSITION_DURATION):d.$element.trigger("focus").trigger(f)}))},c.prototype.hide=function(b){b&&b.preventDefault(),b=a.Event("hide.bs.modal"),this.$element.trigger(b),this.isShown&&!b.isDefaultPrevented()&&(this.isShown=!1,this.escape(),this.resize(),a(document).off("focusin.bs.modal"),this.$element.removeClass("in").off("click.dismiss.bs.modal").off("mouseup.dismiss.bs.modal"),this.$dialog.off("mousedown.dismiss.bs.modal"),a.support.transition&&this.$element.hasClass("fade")?this.$element.one("bsTransitionEnd",a.proxy(this.hideModal,this)).emulateTransitionEnd(c.TRANSITION_DURATION):this.hideModal())},c.prototype.enforceFocus=function(){a(document).off("focusin.bs.modal").on("focusin.bs.modal",a.proxy(function(a){document===a.target||this.$element[0]===a.target||this.$element.has(a.target).length||this.$element.trigger("focus")},this))},c.prototype.escape=function(){this.isShown&&this.options.keyboard?this.$element.on("keydown.dismiss.bs.modal",a.proxy(function(a){27==a.which&&this.hide()},this)):this.isShown||this.$element.off("keydown.dismiss.bs.modal")},c.prototype.resize=function(){this.isShown?a(window).on("resize.bs.modal",a.proxy(this.handleUpdate,this)):a(window).off("resize.bs.modal")},c.prototype.hideModal=function(){var a=this;this.$element.hide(),this.backdrop(function(){a.$body.removeClass("modal-open"),a.resetAdjustments(),a.resetScrollbar(),a.$element.trigger("hidden.bs.modal")})},c.prototype.removeBackdrop=function(){this.$backdrop&&this.$backdrop.remove(),this.$backdrop=null},c.prototype.backdrop=function(b){var d=this,e=this.$element.hasClass("fade")?"fade":"";if(this.isShown&&this.options.backdrop){var f=a.support.transition&&e;if(this.$backdrop=a(document.createElement("div")).addClass("modal-backdrop "+e).appendTo(this.$body),this.$element.on("click.dismiss.bs.modal",a.proxy(function(a){return this.ignoreBackdropClick?void(this.ignoreBackdropClick=!1):void(a.target===a.currentTarget&&("static"==this.options.backdrop?this.$element[0].focus():this.hide()))},this)),f&&this.$backdrop[0].offsetWidth,this.$backdrop.addClass("in"),!b)return;f?this.$backdrop.one("bsTransitionEnd",b).emulateTransitionEnd(c.BACKDROP_TRANSITION_DURATION):b()}else if(!this.isShown&&this.$backdrop){this.$backdrop.removeClass("in");var g=function(){d.removeBackdrop(),b&&b()};a.support.transition&&this.$element.hasClass("fade")?this.$backdrop.one("bsTransitionEnd",g).emulateTransitionEnd(c.BACKDROP_TRANSITION_DURATION):g()}else b&&b()},c.prototype.handleUpdate=function(){this.adjustDialog()},c.prototype.adjustDialog=function(){var a=this.$element[0].scrollHeight>document.documentElement.clientHeight;this.$element.css({paddingLeft:!this.bodyIsOverflowing&&a?this.scrollbarWidth:"",paddingRight:this.bodyIsOverflowing&&!a?this.scrollbarWidth:""})},c.prototype.resetAdjustments=function(){this.$element.css({paddingLeft:"",paddingRight:""})},c.prototype.checkScrollbar=function(){var a=window.innerWidth;if(!a){var b=document.documentElement.getBoundingClientRect();a=b.right-Math.abs(b.left)}this.bodyIsOverflowing=document.body.clientWidth<a,this.scrollbarWidth=this.measureScrollbar()},c.prototype.setScrollbar=function(){var a=parseInt(this.$body.css("padding-right")||0,10);this.originalBodyPad=document.body.style.paddingRight||"",this.bodyIsOverflowing&&this.$body.css("padding-right",a+this.scrollbarWidth)},c.prototype.resetScrollbar=function(){this.$body.css("padding-right",this.originalBodyPad)},c.prototype.measureScrollbar=function(){var a=document.createElement("div");a.className="modal-scrollbar-measure",this.$body.append(a);var b=a.offsetWidth-a.clientWidth;return this.$body[0].removeChild(a),b};var d=a.fn.modal;a.fn.modal=b,a.fn.modal.Constructor=c,a.fn.modal.noConflict=function(){return a.fn.modal=d,this},a(document).on("click.bs.modal.data-api",'[data-toggle="modal"]',function(c){var d=a(this),e=d.attr("href"),f=a(d.attr("data-target")||e&&e.replace(/.*(?=#[^\s]+$)/,"")),g=f.data("bs.modal")?"toggle":a.extend({remote:!/#/.test(e)&&e},f.data(),d.data());d.is("a")&&c.preventDefault(),f.one("show.bs.modal",function(a){a.isDefaultPrevented()||f.one("hidden.bs.modal",function(){d.is(":visible")&&d.trigger("focus")})}),b.call(f,g,this)})}(jQuery),+function(a){"use strict";function b(b){return this.each(function(){var d=a(this),e=d.data("bs.tooltip"),f="object"==typeof b&&b;!e&&/destroy|hide/.test(b)||(e||d.data("bs.tooltip",e=new c(this,f)),"string"==typeof b&&e[b]())})}var c=function(a,b){this.type=null,this.options=null,this.enabled=null,this.timeout=null,this.hoverState=null,this.$element=null,this.inState=null,this.init("tooltip",a,b)};c.VERSION="3.3.7",c.TRANSITION_DURATION=150,c.DEFAULTS={animation:!0,placement:"top",selector:!1,template:'<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',trigger:"hover focus",title:"",delay:0,html:!1,container:!1,viewport:{selector:"body",padding:0}},c.prototype.init=function(b,c,d){if(this.enabled=!0,this.type=b,this.$element=a(c),this.options=this.getOptions(d),this.$viewport=this.options.viewport&&a(a.isFunction(this.options.viewport)?this.options.viewport.call(this,this.$element):this.options.viewport.selector||this.options.viewport),this.inState={click:!1,hover:!1,focus:!1},this.$element[0]instanceof document.constructor&&!this.options.selector)throw new Error("`selector` option must be specified when initializing "+this.type+" on the window.document object!");for(var e=this.options.trigger.split(" "),f=e.length;f--;){var g=e[f];if("click"==g)this.$element.on("click."+this.type,this.options.selector,a.proxy(this.toggle,this));else if("manual"!=g){var h="hover"==g?"mouseenter":"focusin",i="hover"==g?"mouseleave":"focusout";this.$element.on(h+"."+this.type,this.options.selector,a.proxy(this.enter,this)),this.$element.on(i+"."+this.type,this.options.selector,a.proxy(this.leave,this))}}this.options.selector?this._options=a.extend({},this.options,{trigger:"manual",selector:""}):this.fixTitle()},c.prototype.getDefaults=function(){return c.DEFAULTS},c.prototype.getOptions=function(b){return b=a.extend({},this.getDefaults(),this.$element.data(),b),b.delay&&"number"==typeof b.delay&&(b.delay={show:b.delay,hide:b.delay}),b},c.prototype.getDelegateOptions=function(){var b={},c=this.getDefaults();return this._options&&a.each(this._options,function(a,d){c[a]!=d&&(b[a]=d)}),b},c.prototype.enter=function(b){var c=b instanceof this.constructor?b:a(b.currentTarget).data("bs."+this.type);return c||(c=new this.constructor(b.currentTarget,this.getDelegateOptions()),a(b.currentTarget).data("bs."+this.type,c)),b instanceof a.Event&&(c.inState["focusin"==b.type?"focus":"hover"]=!0),c.tip().hasClass("in")||"in"==c.hoverState?void(c.hoverState="in"):(clearTimeout(c.timeout),c.hoverState="in",c.options.delay&&c.options.delay.show?void(c.timeout=setTimeout(function(){"in"==c.hoverState&&c.show()},c.options.delay.show)):c.show())},c.prototype.isInStateTrue=function(){for(var a in this.inState)if(this.inState[a])return!0;return!1},c.prototype.leave=function(b){var c=b instanceof this.constructor?b:a(b.currentTarget).data("bs."+this.type);if(c||(c=new this.constructor(b.currentTarget,this.getDelegateOptions()),a(b.currentTarget).data("bs."+this.type,c)),b instanceof a.Event&&(c.inState["focusout"==b.type?"focus":"hover"]=!1),!c.isInStateTrue())return clearTimeout(c.timeout),c.hoverState="out",c.options.delay&&c.options.delay.hide?void(c.timeout=setTimeout(function(){"out"==c.hoverState&&c.hide()},c.options.delay.hide)):c.hide()},c.prototype.show=function(){var b=a.Event("show.bs."+this.type);if(this.hasContent()&&this.enabled){this.$element.trigger(b);var d=a.contains(this.$element[0].ownerDocument.documentElement,this.$element[0]);if(b.isDefaultPrevented()||!d)return;var e=this,f=this.tip(),g=this.getUID(this.type);this.setContent(),f.attr("id",g),this.$element.attr("aria-describedby",g),this.options.animation&&f.addClass("fade");var h="function"==typeof this.options.placement?this.options.placement.call(this,f[0],this.$element[0]):this.options.placement,i=/\s?auto?\s?/i,j=i.test(h);j&&(h=h.replace(i,"")||"top"),f.detach().css({top:0,left:0,display:"block"}).addClass(h).data("bs."+this.type,this),this.options.container?f.appendTo(this.options.container):f.insertAfter(this.$element),this.$element.trigger("inserted.bs."+this.type);var k=this.getPosition(),l=f[0].offsetWidth,m=f[0].offsetHeight;if(j){var n=h,o=this.getPosition(this.$viewport);h="bottom"==h&&k.bottom+m>o.bottom?"top":"top"==h&&k.top-m<o.top?"bottom":"right"==h&&k.right+l>o.width?"left":"left"==h&&k.left-l<o.left?"right":h,f.removeClass(n).addClass(h)}var p=this.getCalculatedOffset(h,k,l,m);this.applyPlacement(p,h);var q=function(){var a=e.hoverState;e.$element.trigger("shown.bs."+e.type),e.hoverState=null,"out"==a&&e.leave(e)};a.support.transition&&this.$tip.hasClass("fade")?f.one("bsTransitionEnd",q).emulateTransitionEnd(c.TRANSITION_DURATION):q()}},c.prototype.applyPlacement=function(b,c){var d=this.tip(),e=d[0].offsetWidth,f=d[0].offsetHeight,g=parseInt(d.css("margin-top"),10),h=parseInt(d.css("margin-left"),10);isNaN(g)&&(g=0),isNaN(h)&&(h=0),b.top+=g,b.left+=h,a.offset.setOffset(d[0],a.extend({using:function(a){d.css({top:Math.round(a.top),left:Math.round(a.left)})}},b),0),d.addClass("in");var i=d[0].offsetWidth,j=d[0].offsetHeight;"top"==c&&j!=f&&(b.top=b.top+f-j);var k=this.getViewportAdjustedDelta(c,b,i,j);k.left?b.left+=k.left:b.top+=k.top;var l=/top|bottom/.test(c),m=l?2*k.left-e+i:2*k.top-f+j,n=l?"offsetWidth":"offsetHeight";d.offset(b),this.replaceArrow(m,d[0][n],l)},c.prototype.replaceArrow=function(a,b,c){this.arrow().css(c?"left":"top",50*(1-a/b)+"%").css(c?"top":"left","")},c.prototype.setContent=function(){var a=this.tip(),b=this.getTitle();a.find(".tooltip-inner")[this.options.html?"html":"text"](b),a.removeClass("fade in top bottom left right")},c.prototype.hide=function(b){function d(){"in"!=e.hoverState&&f.detach(),e.$element&&e.$element.removeAttr("aria-describedby").trigger("hidden.bs."+e.type),b&&b()}var e=this,f=a(this.$tip),g=a.Event("hide.bs."+this.type);if(this.$element.trigger(g),!g.isDefaultPrevented())return f.removeClass("in"),a.support.transition&&f.hasClass("fade")?f.one("bsTransitionEnd",d).emulateTransitionEnd(c.TRANSITION_DURATION):d(),this.hoverState=null,this},c.prototype.fixTitle=function(){var a=this.$element;(a.attr("title")||"string"!=typeof a.attr("data-original-title"))&&a.attr("data-original-title",a.attr("title")||"").attr("title","")},c.prototype.hasContent=function(){return this.getTitle()},c.prototype.getPosition=function(b){b=b||this.$element;var c=b[0],d="BODY"==c.tagName,e=c.getBoundingClientRect();null==e.width&&(e=a.extend({},e,{width:e.right-e.left,height:e.bottom-e.top}));var f=window.SVGElement&&c instanceof window.SVGElement,g=d?{top:0,left:0}:f?null:b.offset(),h={scroll:d?document.documentElement.scrollTop||document.body.scrollTop:b.scrollTop()},i=d?{width:a(window).width(),height:a(window).height()}:null;return a.extend({},e,h,i,g)},c.prototype.getCalculatedOffset=function(a,b,c,d){return"bottom"==a?{top:b.top+b.height,left:b.left+b.width/2-c/2}:"top"==a?{top:b.top-d,left:b.left+b.width/2-c/2}:"left"==a?{top:b.top+b.height/2-d/2,left:b.left-c}:{top:b.top+b.height/2-d/2,left:b.left+b.width}},c.prototype.getViewportAdjustedDelta=function(a,b,c,d){var e={top:0,left:0};if(!this.$viewport)return e;var f=this.options.viewport&&this.options.viewport.padding||0,g=this.getPosition(this.$viewport);if(/right|left/.test(a)){var h=b.top-f-g.scroll,i=b.top+f-g.scroll+d;h<g.top?e.top=g.top-h:i>g.top+g.height&&(e.top=g.top+g.height-i)}else{var j=b.left-f,k=b.left+f+c;j<g.left?e.left=g.left-j:k>g.right&&(e.left=g.left+g.width-k)}return e},c.prototype.getTitle=function(){var a,b=this.$element,c=this.options;return a=b.attr("data-original-title")||("function"==typeof c.title?c.title.call(b[0]):c.title)},c.prototype.getUID=function(a){do a+=~~(1e6*Math.random());while(document.getElementById(a));return a},c.prototype.tip=function(){if(!this.$tip&&(this.$tip=a(this.options.template),1!=this.$tip.length))throw new Error(this.type+" `template` option must consist of exactly 1 top-level element!");return this.$tip},c.prototype.arrow=function(){return this.$arrow=this.$arrow||this.tip().find(".tooltip-arrow")},c.prototype.enable=function(){this.enabled=!0},c.prototype.disable=function(){this.enabled=!1},c.prototype.toggleEnabled=function(){this.enabled=!this.enabled},c.prototype.toggle=function(b){var c=this;b&&(c=a(b.currentTarget).data("bs."+this.type),c||(c=new this.constructor(b.currentTarget,this.getDelegateOptions()),a(b.currentTarget).data("bs."+this.type,c))),b?(c.inState.click=!c.inState.click,c.isInStateTrue()?c.enter(c):c.leave(c)):c.tip().hasClass("in")?c.leave(c):c.enter(c)},c.prototype.destroy=function(){var a=this;clearTimeout(this.timeout),this.hide(function(){a.$element.off("."+a.type).removeData("bs."+a.type),a.$tip&&a.$tip.detach(),a.$tip=null,a.$arrow=null,a.$viewport=null,a.$element=null})};var d=a.fn.tooltip;a.fn.tooltip=b,a.fn.tooltip.Constructor=c,a.fn.tooltip.noConflict=function(){return a.fn.tooltip=d,this}}(jQuery),+function(a){"use strict";function b(b){return this.each(function(){var d=a(this),e=d.data("bs.popover"),f="object"==typeof b&&b;!e&&/destroy|hide/.test(b)||(e||d.data("bs.popover",e=new c(this,f)),"string"==typeof b&&e[b]())})}var c=function(a,b){this.init("popover",a,b)};if(!a.fn.tooltip)throw new Error("Popover requires tooltip.js");c.VERSION="3.3.7",c.DEFAULTS=a.extend({},a.fn.tooltip.Constructor.DEFAULTS,{placement:"right",trigger:"click",content:"",template:'<div class="popover" role="tooltip"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>'}),c.prototype=a.extend({},a.fn.tooltip.Constructor.prototype),c.prototype.constructor=c,c.prototype.getDefaults=function(){return c.DEFAULTS},c.prototype.setContent=function(){var a=this.tip(),b=this.getTitle(),c=this.getContent();a.find(".popover-title")[this.options.html?"html":"text"](b),a.find(".popover-content").children().detach().end()[this.options.html?"string"==typeof c?"html":"append":"text"](c),a.removeClass("fade top bottom left right in"),a.find(".popover-title").html()||a.find(".popover-title").hide()},c.prototype.hasContent=function(){return this.getTitle()||this.getContent()},c.prototype.getContent=function(){var a=this.$element,b=this.options;return a.attr("data-content")||("function"==typeof b.content?b.content.call(a[0]):b.content)},c.prototype.arrow=function(){return this.$arrow=this.$arrow||this.tip().find(".arrow")};var d=a.fn.popover;a.fn.popover=b,a.fn.popover.Constructor=c,a.fn.popover.noConflict=function(){return a.fn.popover=d,this}}(jQuery),+function(a){"use strict";function b(c,d){this.$body=a(document.body),this.$scrollElement=a(a(c).is(document.body)?window:c),this.options=a.extend({},b.DEFAULTS,d),this.selector=(this.options.target||"")+" .nav li > a",this.offsets=[],this.targets=[],this.activeTarget=null,this.scrollHeight=0,this.$scrollElement.on("scroll.bs.scrollspy",a.proxy(this.process,this)),this.refresh(),this.process()}function c(c){return this.each(function(){var d=a(this),e=d.data("bs.scrollspy"),f="object"==typeof c&&c;e||d.data("bs.scrollspy",e=new b(this,f)),"string"==typeof c&&e[c]()})}b.VERSION="3.3.7",b.DEFAULTS={offset:10},b.prototype.getScrollHeight=function(){return this.$scrollElement[0].scrollHeight||Math.max(this.$body[0].scrollHeight,document.documentElement.scrollHeight)},b.prototype.refresh=function(){var b=this,c="offset",d=0;this.offsets=[],this.targets=[],this.scrollHeight=this.getScrollHeight(),a.isWindow(this.$scrollElement[0])||(c="position",d=this.$scrollElement.scrollTop()),this.$body.find(this.selector).map(function(){var b=a(this),e=b.data("target")||b.attr("href"),f=/^#./.test(e)&&a(e);return f&&f.length&&f.is(":visible")&&[[f[c]().top+d,e]]||null}).sort(function(a,b){return a[0]-b[0]}).each(function(){b.offsets.push(this[0]),b.targets.push(this[1])})},b.prototype.process=function(){var a,b=this.$scrollElement.scrollTop()+this.options.offset,c=this.getScrollHeight(),d=this.options.offset+c-this.$scrollElement.height(),e=this.offsets,f=this.targets,g=this.activeTarget;if(this.scrollHeight!=c&&this.refresh(),b>=d)return g!=(a=f[f.length-1])&&this.activate(a);if(g&&b<e[0])return this.activeTarget=null,this.clear();for(a=e.length;a--;)g!=f[a]&&b>=e[a]&&(void 0===e[a+1]||b<e[a+1])&&this.activate(f[a])},b.prototype.activate=function(b){
this.activeTarget=b,this.clear();var c=this.selector+'[data-target="'+b+'"],'+this.selector+'[href="'+b+'"]',d=a(c).parents("li").addClass("active");d.parent(".dropdown-menu").length&&(d=d.closest("li.dropdown").addClass("active")),d.trigger("activate.bs.scrollspy")},b.prototype.clear=function(){a(this.selector).parentsUntil(this.options.target,".active").removeClass("active")};var d=a.fn.scrollspy;a.fn.scrollspy=c,a.fn.scrollspy.Constructor=b,a.fn.scrollspy.noConflict=function(){return a.fn.scrollspy=d,this},a(window).on("load.bs.scrollspy.data-api",function(){a('[data-spy="scroll"]').each(function(){var b=a(this);c.call(b,b.data())})})}(jQuery),+function(a){"use strict";function b(b){return this.each(function(){var d=a(this),e=d.data("bs.tab");e||d.data("bs.tab",e=new c(this)),"string"==typeof b&&e[b]()})}var c=function(b){this.element=a(b)};c.VERSION="3.3.7",c.TRANSITION_DURATION=150,c.prototype.show=function(){var b=this.element,c=b.closest("ul:not(.dropdown-menu)"),d=b.data("target");if(d||(d=b.attr("href"),d=d&&d.replace(/.*(?=#[^\s]*$)/,"")),!b.parent("li").hasClass("active")){var e=c.find(".active:last a"),f=a.Event("hide.bs.tab",{relatedTarget:b[0]}),g=a.Event("show.bs.tab",{relatedTarget:e[0]});if(e.trigger(f),b.trigger(g),!g.isDefaultPrevented()&&!f.isDefaultPrevented()){var h=a(d);this.activate(b.closest("li"),c),this.activate(h,h.parent(),function(){e.trigger({type:"hidden.bs.tab",relatedTarget:b[0]}),b.trigger({type:"shown.bs.tab",relatedTarget:e[0]})})}}},c.prototype.activate=function(b,d,e){function f(){g.removeClass("active").find("> .dropdown-menu > .active").removeClass("active").end().find('[data-toggle="tab"]').attr("aria-expanded",!1),b.addClass("active").find('[data-toggle="tab"]').attr("aria-expanded",!0),h?(b[0].offsetWidth,b.addClass("in")):b.removeClass("fade"),b.parent(".dropdown-menu").length&&b.closest("li.dropdown").addClass("active").end().find('[data-toggle="tab"]').attr("aria-expanded",!0),e&&e()}var g=d.find("> .active"),h=e&&a.support.transition&&(g.length&&g.hasClass("fade")||!!d.find("> .fade").length);g.length&&h?g.one("bsTransitionEnd",f).emulateTransitionEnd(c.TRANSITION_DURATION):f(),g.removeClass("in")};var d=a.fn.tab;a.fn.tab=b,a.fn.tab.Constructor=c,a.fn.tab.noConflict=function(){return a.fn.tab=d,this};var e=function(c){c.preventDefault(),b.call(a(this),"show")};a(document).on("click.bs.tab.data-api",'[data-toggle="tab"]',e).on("click.bs.tab.data-api",'[data-toggle="pill"]',e)}(jQuery),+function(a){"use strict";function b(b){return this.each(function(){var d=a(this),e=d.data("bs.affix"),f="object"==typeof b&&b;e||d.data("bs.affix",e=new c(this,f)),"string"==typeof b&&e[b]()})}var c=function(b,d){this.options=a.extend({},c.DEFAULTS,d),this.$target=a(this.options.target).on("scroll.bs.affix.data-api",a.proxy(this.checkPosition,this)).on("click.bs.affix.data-api",a.proxy(this.checkPositionWithEventLoop,this)),this.$element=a(b),this.affixed=null,this.unpin=null,this.pinnedOffset=null,this.checkPosition()};c.VERSION="3.3.7",c.RESET="affix affix-top affix-bottom",c.DEFAULTS={offset:0,target:window},c.prototype.getState=function(a,b,c,d){var e=this.$target.scrollTop(),f=this.$element.offset(),g=this.$target.height();if(null!=c&&"top"==this.affixed)return e<c&&"top";if("bottom"==this.affixed)return null!=c?!(e+this.unpin<=f.top)&&"bottom":!(e+g<=a-d)&&"bottom";var h=null==this.affixed,i=h?e:f.top,j=h?g:b;return null!=c&&e<=c?"top":null!=d&&i+j>=a-d&&"bottom"},c.prototype.getPinnedOffset=function(){if(this.pinnedOffset)return this.pinnedOffset;this.$element.removeClass(c.RESET).addClass("affix");var a=this.$target.scrollTop(),b=this.$element.offset();return this.pinnedOffset=b.top-a},c.prototype.checkPositionWithEventLoop=function(){setTimeout(a.proxy(this.checkPosition,this),1)},c.prototype.checkPosition=function(){if(this.$element.is(":visible")){var b=this.$element.height(),d=this.options.offset,e=d.top,f=d.bottom,g=Math.max(a(document).height(),a(document.body).height());"object"!=typeof d&&(f=e=d),"function"==typeof e&&(e=d.top(this.$element)),"function"==typeof f&&(f=d.bottom(this.$element));var h=this.getState(g,b,e,f);if(this.affixed!=h){null!=this.unpin&&this.$element.css("top","");var i="affix"+(h?"-"+h:""),j=a.Event(i+".bs.affix");if(this.$element.trigger(j),j.isDefaultPrevented())return;this.affixed=h,this.unpin="bottom"==h?this.getPinnedOffset():null,this.$element.removeClass(c.RESET).addClass(i).trigger(i.replace("affix","affixed")+".bs.affix")}"bottom"==h&&this.$element.offset({top:g-b-f})}};var d=a.fn.affix;a.fn.affix=b,a.fn.affix.Constructor=c,a.fn.affix.noConflict=function(){return a.fn.affix=d,this},a(window).on("load",function(){a('[data-spy="affix"]').each(function(){var c=a(this),d=c.data();d.offset=d.offset||{},null!=d.offsetBottom&&(d.offset.bottom=d.offsetBottom),null!=d.offsetTop&&(d.offset.top=d.offsetTop),b.call(c,d)})})}(jQuery);




var url_lingerie;
var cart, wishlist,lingerie_sidebar,login,links;


var button_click;
var gutscheincode;

 // This is called with the results from from FB.getLoginStatus().
  function statusChangeCallback(response) {
	  
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
	 // alert(response.status)
	  facebook_einloggen()


    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into Facebook.';
    }
  }

  // This function is called when someone finishes with the Login
  // Button.  See the onlogin handler attached to it in the sample
  // code below.
  function checkLoginState() {

    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
	  //alert(response)
    });
  }
  


  window.fbAsyncInit = function() {

	  button_click=0
  FB.init({
    appId      : '1796917517246883',
    cookie     : true,  // enable cookies to allow the server to access 
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.8' // use graph api version 2.5
  });
  

  // Now that we've initialized the JavaScript SDK, we call 
  // FB.getLoginStatus().  This function gets the state of the
  // person visiting this page and can return one of three states to
  // the callback you provide.  They can be:
  //
  // 1. Logged into your app ('connected')
  // 2. Logged into Facebook, but not your app ('not_authorized')
  // 3. Not logged into Facebook and can't tell if they are logged into
  //    your app or not.
  //
  // These three cases are handled in the callback function.

  FB.getLoginStatus(function(response) {
	
	
    statusChangeCallback(response);
  });
  
     FB.Event.subscribe('auth.login', function () {
		  facebook_einloggen()
        //  window.location = "http://example.com";
      });

  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  // Here we run a very simple test of the Graph API after login is
  // successful.  See statusChangeCallback() for when this call is made.

	
	
	function gutscheincode_laden_fb(code)
	{
		gutscheincode=code;
		
	}
	
	function fb_login() {
		
    button_logo("0","facebook_login_button_text","facebook_login_button_logo","facebook_login_button")	

    FB.login( function() {}, { scope: 'email,public_profile' } );
	    console.log('Welcome!  Fetching your information.... ');
	FB.api('/me?fields=first_name,last_name,email,age_range,gender,locale,link', function(response) {
		
  button_click=1;
  facebook_einloggen()
    });
    button_logo("1","facebook_login_button_text","facebook_login_button_logo","facebook_login_button")	
}



function facebook_einloggen()
{

	if (button_click==1)
	{
	    button_logo("0","facebook_login_button_text","facebook_login_button_logo","facebook_login_button")	
		FB.api('/me?fields=first_name,last_name,email,age_range,gender,locale,link', function(response) {


		$.ajax({
				type: "POST",
				url: "/login_via_facebook/",
				dataType: "json",
				data: { "id":response.id,"vorname":response.first_name,"nachname":  response.last_name,"email":  response.email,"min_alter":response.age_range.min,"max_alter":response.age_range.max,"geschlecht":response.gender,"gutscheincode":gutscheincode},
				success: function(data) {

					if(data=="ok")
					{
					
							fbq('track', 'CompleteRegistration', {
							      content_name: "Registration/Login via Facebook", 
							      value: "",
							      status: "Successful registration",
							      currency: 'EUR' 
							    });
                        button_logo("1","facebook_login_button_text","facebook_login_button_logo","facebook_login_button")	
						alert_userdata_registration_successful("ERFOLGREICH ANGEMELDET","Du hast dich erfolgreicht registriert.")
                    }
				}
				});
			 });
	}
			

}
  
  
  


function preloader() {

}
function addLoadEvent(func) {
	var oldonload = window.onload;
	if (typeof window.onload != 'function') {
		window.onload = func;
	} else {
		window.onload = function() {
			if (oldonload) {
				oldonload();
			}
			func();
		}
	}
}
addLoadEvent(preloader);




function warenkorb_abrufen(anzahl)
{
	cart_gesamt=0;
	i=0;
	while(i<=cart.length-1)
	{
		cart_gesamt=cart_gesamt+parseInt(cart[i].anzahl)
		i=i+1;	
	}
	insert_quantity_into_cart(cart_gesamt)
}


function insert_quantity_into_cart(cart_gesamt)
{
	if (cart_gesamt!=0)
	{			
		document.getElementsByClassName("cart_text")[0].innerHTML=cart_gesamt;
		document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-open.png')";

	}
	else
	{

		document.getElementsByClassName("cart_text")[0].innerHTML=" ";
		document.getElementsByClassName("cart")[0].style.backgroundImage="url('/static/Cart-closed.png')";

	}	
}

function insert_quantity_into_wishlist(wishlist_gesamt)
{
	if (wishlist_gesamt!=0)
		document.getElementsByClassName("text_wishlist")[0].innerHTML=wishlist_gesamt;
	else
		document.getElementsByClassName("text_wishlist")[0].innerHTML=" ";
}




function wishlist_abrufen_anzahl(anzahl)
{
	wishlist_gesamt=0;
	i=0;
	while(i<=wishlist.length-1)
	{
		wishlist_gesamt=wishlist_gesamt+1
		i=i+1;	
	}
	insert_quantity_into_wishlist(wishlist_gesamt)
}


function show_cart()
{

	cart=JSON.parse(document.getElementsByClassName("warenkorb_daten")[0].innerHTML)

}

function load_wishlist()
{
	wishlist=JSON.parse(document.getElementsByClassName("wishlist")[0].innerHTML)

}

function login_click_schliessen()
{
	enableScroll();
	el.style.visibility = "hidden"
	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	document.getElementById("x-mask").style.opacity="1.0";

}

 function alert_userdata_registration_successful(content1,content2)
 {	 


	document.getElementById("alert_box_reload_headline").innerHTML=content1;

	document.getElementById("alert_box_reload_body").innerHTML=content2;
	$('#alert_box_reload').modal('show');
	$('#login').modal('hide');




 }
 
  $('#password_check').on('hide.bs.modal', function () {

  window.location= "/";

});
 
 $('#alert_box_reload').on('hide.bs.modal', function () {

  location.reload();

});
 
  function alert_userdata(content1,content2)
 {	 
	
	document.getElementById("alert_box_headline").innerHTML=content1;
	document.getElementById("alert_box_body").innerHTML=content2;
	$('#alert_box').modal('show');
 }

function load_registration_login()
{

	$.ajax({
	type: "GET",
	url: "/check_whether_logged_in/",
	dataType: "json",
	data: { "data":""},
	success: function(data) {	


		if(data!="yes")
		{

				closeNav();
				document.getElementById("eingabe_fehler").innerHTML=""
				document.getElementById("username").value=""
				document.getElementById("passwort").value=""
				$('#login').modal('show');
		}
		else
			location.reload();
	}
	})
}

function reset_header()
{

	hide_dropdown(0);

	hide_dropdown(1);

}

function reset_sidebar()
{

	if(document.getElementsByClassName ("modal_mobile_sidebar")[0].style.visibility == "visible")
		closeNav();

}

function open_links_belehrungen(link)
{
	window.open(link)
	
}



function load_header(login_)
{

	login=login_;

	var box="<div class='header_block_links'><div class='header_top_style_left' >Was ist Darling Lace?</div></div>\r";
	box=box+"<div class='mobile_menu' onclick='openNav()'>&nbsp;</div>"


	box=box+"<div class='header_block_rechts'>"
	box=box+"<div class='header_top_style_right'  onmouseenter='show_dropdown(0)' onmouseleave='hide_dropdown(0)' id='header_top_style_right_warenkorb'><div class='loader_header' style='display:none'></div><div class='cart' onclick='warenkorb_aufrufen()'><div class='cart_text' ></div><div class='warenkorb_betitelung'>Warenkorb</div><div class='cart_overview_text_leer'>&nbsp;</div></div>"
	box=box+"<div class='dropdown_content' id='dropdown_content_warenkorb' >"

	
	

	box=box+"</div>";
	
	box=box+"</div>";
	
	box=box+"<div class='header_top_style_right' onmouseenter='show_dropdown(1)' onmouseleave='hide_dropdown(1)' id='header_top_style_right_wishlist'><div class='loader_header' style='display:none'></div><div class='wishlist_overview' ><div class='text_wishlist' ></div><div class='wishlist_overview_text' onclick='wishlist_aufrufen()'>Wunschliste</div><div class='wishlist_overview_text_leer' onclick='wishlist_aufrufen()'>&nbsp;</div>"
	box=box+"<div class='dropdown_content'  id='dropdown_content_wishlist'>"

	
	

	box=box+"</div>";
	
	box=box+"</div>";
	box=box+"</div>";
	if (login_=="true")
	{
		box=box+"<div class='header_top_style_right' onmouseenter='show_dropdown(2)' onmouseleave='hide_dropdown(2)' id='header_top_style_right_profil'><div class='account_overview'> <div class='account_overview_text' onclick='account_aufrufen()'>Profil</div><div class='account_overview_text_leer' onclick='account_aufrufen()'>&nbsp;</div>"
		box=box+"<div class='dropdown_content' id='dropdown_content_profil'>"
		box=box+"<div class='dropdown_content_account' onclick='account_aufrufen()'><div class='dropdown_content_account_overview' ><div class='dropdown_content_account_text' >Übersicht Profil</div></div></div>"

		if(document.getElementsByClassName("bestellungen")[0].innerHTML!="[]")
		{
			
			box=box+"<div class='dropdown_content_account' onclick='bestellungen_bearbeiten()'><div class='dropdown_content_orders_overview' ><div class='dropdown_content_account_text' >Meine Bestellungen</div></div></div>"
			box=box+"<div class='dropdown_content_account' onclick='bestellung_zuruecksenden()'><div class='dropdown_content_exchanges_overview' ><div class='dropdown_content_account_text' >Rücksendungen</div></div></div>"
		}
		else
		{
			
			box=box+"<div class='dropdown_content_account' style='opacity:0.4;pointerEvents:none;cursor:initial;'><div class='dropdown_content_orders_overview' ><div class='dropdown_content_account_text' >Meine Bestellungen</div></div></div>"
			box=box+"<div class='dropdown_content_account' style='opacity:0.4;pointerEvents:none;cursor:initial;'><div class='dropdown_content_exchanges_overview' ><div class='dropdown_content_account_text' >Rücksendungen</div></div></div>"			
		}


		box=box+"<div class='dropdown_content_account' onclick='freunde_einladen()'><div class='dropdown_content_invite_friends_overview' ><div class='dropdown_content_account_text' >Freunde einladen</div></div></div>"			
		box=box+"<div class='dropdown_content_account' style='border-top:1px solid #e6e6e6' onclick='log_out()'><div class='dropdown_content_logout_overview' ><div class='dropdown_content_account_text' >Log-Out</div></div></div>"

		box=box+"</div></div></div>"
	}
	else
		box=box+"<div class='header_top_style_right' onclick='load_registration_login()' id='header_top_style_right_profil'> <div class='dropdown_content_registrierung_overview' ><div class='registrierung_overview_text' >Anmelden</div><div class='registrierung_overview_text_leer' >&nbsp;</div></div></div>"	
//<div class='header_top_style_right' onclick='log_out_aufrufen()'>Log-out</div>	
	box=box+"<div class='logo_huelle'><div class='header_logo'  onclick='logo_click()'/></div></div>\r"

	document.getElementsByClassName("header_top")[0].innerHTML=box;
	
	box=box+"<img class='header_logo' src='/static/darling_lace.png' /></img>\r"
	
	var box_bottom_1="<div class='box_links'><div><b>Darling Lace</b></div><div id='ueber_uns' class='links_header' onclick='link_abrufen(this.id)'>Über uns</div><div id='wie_funktioniert_VIP' class='links_header' onclick='link_abrufen(this.id)'>Wie funktioniert VIP?</div><div id='agb' class='links_header' onclick='link_abrufen(this.id)'>AGB</div></div>";
	var box_bottom_2="<div class='box_links'><div><b>&nbsp;</b></div><div id='datenschutz' class='links_header' onclick='link_abrufen(this.id)'>Datenschutz</div><div id='widerrufsbelehrung' class='links_header' onclick='link_abrufen(this.id)'>Widerrufsbelehrung</div><div id='impressum' class='links_header' ><a href='/impressum'>Impressum</a></div></div>";
	var box_bottom_3="<div class='box_links'><div><b>Hilfe & Support</b></div><div id='help_center' onclick='open_help_center()' class='links_header' >Help Center</div><div id='support' onclick='link_abrufen(this.id)' class='links_header' >Kontaktiere uns</div><div id='versand_rueckversand' onclick='link_abrufen(this.id)' class='links_header' >Versand & Rückversand</div></div>";
	var box_bottom_4="<div class='box_links'><div><b>Social Media</b><br><img class='logos' src='/static/facebook.png' /></img><img class='logos' src='/static/instagram.png' /></img><img class='logos' src='/static/twitter.png' /></img></div>";

	document.getElementsByClassName("header-bottom")[0].innerHTML="<div class='header_bottom_style'>"+box_bottom_1+box_bottom_2+box_bottom_3+box_bottom_4+"</div>";
	insert_quantity_into_cart(document.getElementsByClassName("cart_quantity")[0].innerHTML)
	insert_quantity_into_wishlist(document.getElementsByClassName("wishlist_quantity")[0].innerHTML)
	wishlist="";
	cart="";

//	insert_cart_content_in_header()

//	insert_wishlist_content_in_header()


}

function open_help_center()
{
	window.open('https://darlinglace.zendesk.com/hc/de')
}





function show_dropdown(id)
{


	if(id==0 && cart=="")
	{
			document.getElementsByClassName("loader_header")[0].style.display="block";
			document.getElementsByClassName("cart")[0].style.opacity="0.4";
			document.getElementsByClassName("cart")[0].style.pointerEvents = 'none';
			

			$.ajax({
				type: "GET",
				url: "/warenkorb_abrufen/",
				dataType: "json",
				data: { "":""  },
				success: function(data) {	

					cart=JSON.parse(data)
	
					insert_cart_content_in_header()
					document.getElementsByClassName("loader_header")[0].style.display="none";
					document.getElementsByClassName("cart")[0].style.opacity="1.0";
					document.getElementsByClassName("cart")[0].style.pointerEvents = 'auto';
				
				}
				
			})		
		
		
	}

	
	if(id==1 && wishlist=="")
	{
			document.getElementsByClassName("loader_header")[1].style.display="block";
			document.getElementsByClassName("wishlist_overview")[0].style.opacity="0.4";
			document.getElementsByClassName("wishlist_overview")[0].style.pointerEvents = 'none';
			

			$.ajax({
				type: "GET",
				url: "/wishlist_abrufen/",
				dataType: "json",
				data: { "":""  },
				success: function(data) {	
	
					wishlist=JSON.parse(data)
	
					insert_wishlist_content_in_header()
					document.getElementsByClassName("loader_header")[1].style.display="none";
					document.getElementsByClassName("wishlist_overview")[0].style.opacity="1.0";
					document.getElementsByClassName("wishlist_overview")[0].style.pointerEvents = 'auto';
				
				}
				
			})		
		
		
	}

	if(window.innerWidth>=767)
		document.getElementsByClassName("dropdown_content")[id].style.display="block";

	
}

function hide_dropdown(id)
{
	if(window.innerWidth>=767)
		document.getElementsByClassName("dropdown_content")[id].style.display="none";
	
}


function link_abrufen(link_name)
{
	window.location.href="/"+link_name
}

function wishlist_aufrufen()
{
	button_logo(0,"get_to_wishlist_id_text","get_to_wishlist_id_logo","get_to_wishlist_id")	
	if(wishlist!="")
		window.location.href="/overview/Wunschliste/"		
	else
		button_logo(1,"get_to_wishlist_id_text","get_to_wishlist_id_logo","get_to_wishlist_id")	
	
}


function insert_cart_content_in_header()
{

		i=0;
		box=""

	while(i<=cart.length-1)
	{


		box=box+"<div class='cart_dropdown'>"
	
		box=box+"<img src='"+cart[i].picture+"' class='cart_dropdown_picture' onclick='content_abrufen_cart("+i+")'/>"

		box=box+"<div style='margin-left:10px;float:left;	width:60px;font-size:12px;'><b>"+cart[i].style+"</b></div>"

		box=box+"<img class='schliessen_alert_cart' src='/static/x.png' width='7' onclick='cart_entfernen("+i+");' height='7'/></img>"

		
		box=box+"<br><div style='float:left;margin-left:10px;'>"+cart[i].bhgroesse+"</div> <br>"
		box=box+"<div style='float:left;margin-left:10px;'>"+cart[i].slipgroesse+"</div><br>"
		box=box+"<div style='float:left;margin-left:10px;'>Anz: "+cart[i].anzahl+"x</div><br><br>"
		


		box=box+"</div>";

		box=box+"<div class='linie_2'></div>"

		i=i+1;
	}
	
	if(cart.length-1>=0)
	{
		
		box=box+"<button  id='get_to_cart_id' name='submit' class='get_to_cart'  onclick='warenkorb_aufrufen()'>"

		box=box+"<i class='fa fa-circle-o-notch fa-spin' id='get_to_cart_id_logo' style='display:none'></i>"
		box=box+"<div id='get_to_cart_id_text'>Zum Warenkorb</div>"
		box=box+"</button>"
	}
	
	document.getElementsByClassName('dropdown_content')[0].innerHTML=box;
	warenkorb_abrufen()

}


function insert_wishlist_content_in_header()
{
		i=0;
		box=""

	while(i<=wishlist.length-1)
	{

		
		box=box+"<div class='wishlist_dropdown'>"
	
		box=box+"<img src='"+wishlist[i].picture+"' class='wishlist_dropdown_picture' onclick='content_abrufen_wishlist("+i+")'/>"

		box=box+"<div style='margin-left:10px;float:left;	width:60px;font-size:12px;'><b>"+wishlist[i].name+"</b></div>"

		box=box+"<img class='schliessen_alert_cart' src='/static/x.png' width='7' onclick='wishlist_entfernen("+i+");' height='7'/></img>"

		box=box+"<br><br><br><br><br></div>";

		box=box+"<div class='linie_2'></div>"

		i=i+1;
	}
	
	if(wishlist.length-1>=0)
	{
		box=box+"<button  id='get_to_wishlist_id' name='submit' class='get_to_cart'  onclick='wishlist_aufrufen()'>"

		box=box+"<i class='fa fa-circle-o-notch fa-spin' id='get_to_wishlist_id_logo' style='display:none'></i>"
		box=box+"<div id='get_to_wishlist_id_text'>Zur Wunschliste</div>"
		box=box+"</button>"
	}
	document.getElementsByClassName("dropdown_content")[1].innerHTML=box;
	wishlist_abrufen_anzahl()

}

function wishlist_entfernen(id)
{
	j=0;
	id2=-1
	while(j<=lingerie_selection.length-1)
	{

		if(wishlist[id].name==lingerie_selection[j].name)
			id2=j
		j=j+1;
	}


	if(id2==-1)
		wishlist_abrufen(id2,id)
	
	if(id2>=0)
		wishlist_abrufen(id2,"")
		
}

function cart_entfernen(id)
{
	

	
		$.ajax({
			type: "GET",
			url: "/add/",
			dataType: "json",
			data: { "add_or_erase":"change","anzahl":0,"gerichtname": cart[id].style,"stylecode": cart[id].stylecode,"colorcode": cart[id].colorcode,"bh_groesse": cart[id].bhgroesse,"slip_groesse": cart[id].slipgroesse,"slip_groesse_2":""  },
			success: function(data) {	

				cart=JSON.parse(data)

				insert_cart_content_in_header()
			
			}
			
		})
		
		
		
}




 function links_laden(url)
 {



	if(document.getElementsByClassName("links")[0].innerHTML!="Dein Profil")
 		links=JSON.parse(document.getElementsByClassName("links")[0].innerHTML);
 	else
 		links=JSON.parse(document.getElementsByClassName("links")[1].innerHTML);

 	i=0;
 	box="<div class='_block_'>\r"
 	url_lingerie="Wunschliste"
	while (i<=links.length-1)
	{
		if (i==url)
		{
	 		if(links[i].name=="Mein Showroom" && links[i].group1=="no")
	  			box=box+"<div class='link_gruppen' onmouseenter='link_markieren("+i+")'><a href='javascript:void(0)' onclick='quiz_laden();'>"+links[i].name+"</a></div>\r"		
	 		else
	 			box=box+"<div class='link_gruppen' onmouseenter='link_markieren("+i+")'><a href='"+links[i].name+"'>"+links[i].name+"</a></div>\r"
	 			url_lingerie=links[i].name
 		}
 		else
 		{
		 		if(links[i].name=="Mein Showroom" && links[i].group1=="no")
		  			box=box+"<div class='link_gruppen' onmouseenter='link_markieren("+i+")' onmouseleave='link_entmarkieren("+i+")'><a href='javascript:void(0)' onclick='quiz_laden();'>"+links[i].name+"</a></div>\r"		
		 		else
		 			box=box+"<div class='link_gruppen' onmouseenter='link_markieren("+i+")' onmouseleave='link_entmarkieren("+i+")'><a href='"+links[i].name+"'>"+links[i].name+"</a></div>\r"
		 			url_lingerie=links[i].name
 		}
 		

 		i=i+1;
 	}
 	box=box+"<span class='stretch'></span></div>\r"
 	box=box+"</div>\r"
 	

	if(url!=-1)
	{
	 	document.getElementsByClassName("sidebar_content")[0].innerHTML=box
	
		if(url!="None")
	 		link_markieren(url)
	 }

 }
 
 
 function bestellungen_bearbeiten()
{
	
	window.location.href="/account_page/bestellungen_ansehen";
}

function bestellung_zuruecksenden()
{
	
	window.location.href="/account_page/bestellung_zuruecksenden";
}

function freunde_einladen()
{
	
	window.location.href="/account_page/freunde_einladen";
}


 
 function link_markieren(url)
 {


 		document.getElementsByClassName("link_gruppen")[url].style.color="#CC3366";
 		document.getElementsByClassName("link_gruppen")[url].style.borderBottom="2px solid #CC3366";
 		

 		
 	
 }
 
  function link_entmarkieren(url)
 {


	document.getElementsByClassName("link_gruppen")[url].style.color="#4E4E4E";
	document.getElementsByClassName("link_gruppen")[url].style.borderBottom="";

 		
 	
 }
//E47272

  function content_abrufen_cart(i)
 {

			 		$.ajax({
					type: "GET",
					url: "/get_link_based_on_lingerie_name/",
					dataType: "json",
					data: { "lingerie_name":cart[i].style		},
					success: function(data) {	
 								window.location= "/"+data;
 								
 								
 							}					
 					})
	
 }
 
  
 
  function content_abrufen_wishlist(i)
 {
 	
 				 		$.ajax({
					type: "GET",
					url: "/get_link_based_on_lingerie_name/",
					dataType: "json",
					data: { "lingerie_name":wishlist[i].name			},
					success: function(data) {	

 								window.location= "/"+data;
 								
 								
 							}					
 					})

 }
 
 
 function content_abrufen(i)
 {

 	if(links[i].name=="Mein Showroom" && links[i].group1=="no")
 		quiz_laden();

	else
		window.location.href="/overview/"+links[i].name		
 }




function kollektion_abrufen()
{
	alert("kollektion")
	i=0;
	while(i<=document.getElementsByClassName("link_gruppen").length-1)
	{
		if(document.getElementsByClassName("link_gruppen")[i].style.borderBottom!="")
			link=i
		
		i=i+1;
	}

		$.ajax({
		type: "GET",
		url: "/kollektion_abrufen/",
		dataType: "json",
		data: {  "group":lingerie_selection[0].productgroup,"link":links[link].name },
		success: function(data) {			
			window.location= "/overview/"+data+"/";


		}
	});

}


function account_aufrufen()
{
	window.location= "/account_page/";
}

function logo_click()
{
	window.location= "/";
}

function login_aufrufen()
{
	window.location= "/";
}


function log_out()
{

	window.location= "/log_out/";
}

function warenkorb_aufrufen()
{
	button_logo(0,"get_to_cart_id_text","get_to_cart_id_logo","get_to_cart_id")	
	if(document.getElementsByClassName("cart_text")[0].innerHTML>0)
		window.location= "/cart/";
	else
		button_logo(1,"get_to_cart_id_text","get_to_cart_id_logo","get_to_cart_id")	
}


 
 function check_vollstaendigkeit()
 {
	 if(document.getElementById("username").value=="" || document.getElementById("passwort").value=="")
		  document.getElementById("eingabe_fehler").innerHTML="Bitte E-Mail Adresse und Passwort angeben";
	  else
		  return true		 
	 
 }
 
 
 function passwort_lang_genug()
 {

	 if(document.getElementById("passwort").value.length<6)
		  document.getElementById("eingabe_fehler").innerHTML="Das Passwort muss mindestens 6 Stellen haben";
	  else
		  return true
	 
	 
 }
 
 function eingabe_fehler_herausnehmen()
 {
	 document.getElementById("eingabe_fehler").innerHTML="";
 }
 

 
 
 function register()
 {
	 
	 if (check_vollstaendigkeit())
	 {
		if(passwort_lang_genug())
		{
			
			button_logo("0","registrierung_button_text","registrierung_button_logo","registrierung_button")	

			document.getElementsByClassName("login")[0].style.pointerEvents = 'none';
			document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'none';


			 $.ajax({
				type: "POST",
				url: "/updater_user_registration/",
				dataType: "json",
				data: { "item": document.getElementById("username").value+","+document.getElementById("passwort").value},
				success: function(data) {

					if(data=="exists already")
					{
						button_logo("1","registrierung_button_text","registrierung_button_logo","registrierung_button")	
						document.getElementById("eingabe_fehler").innerHTML="Ein User mit dieser E-Mail Adresse existiert bereits"
						document.getElementsByClassName("login")[0].style.pointerEvents = 'auto';
						document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';

					}
					else	
					{
						if(data=="email falsch")
						{
							button_logo("1","registrierung_button_text","registrierung_button_logo","registrierung_button")	
							document.getElementById("eingabe_fehler").innerHTML="Bitte eine gültige E-Mail Adresse angeben";
							document.getElementsByClassName("login")[0].style.pointerEvents = 'auto';
							document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';

						}
						else
							if(data!="")
							{
								fbq('track', 'CompleteRegistration', {
							      content_name: "Registration via E-Mail", 
							      value: "0.1",
							      status: "Successful registration",
							      currency: 'EUR' 
							    });
								button_logo("1","registrierung_button_text","registrierung_button_logo","registrierung_button")	
								alert_userdata_registration_successful("ERFOLGREICH ANGEMELDET","Du hast dich erfolgreich registriert.")

							}

				
						

							
					}
				}
			}); 
		}
	 }
 }
 
 
 function login_logo(index,text_area,logo_area,button_)
 {
	 
	 if (index==0)
	 {
		document.getElementsByClassName(""+text_area+"")[0].style.display="none";
		document.getElementsByClassName(""+logo_area+"")[0].style.display="block";

		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'none';
		

		
	 }
	 else
	 {
		document.getElementsByClassName(""+text_area+"")[0].style.display="block";
		document.getElementsByClassName(""+logo_area+"")[0].style.display="none";	
		document.getElementsByClassName(""+button_+"")[0].style.pointerEvents = 'auto';
		
		 
	 }
	 
 }
 
 
 
   function button_logo(index,text_area,logo_area,button_)
 {
	 if (index==0)
	 {
		document.getElementById(""+text_area+"").style.display="none";
		document.getElementById(""+logo_area+"").style.display="block";
		document.getElementById(""+button_+"").style.pointerEvents = 'none';
	 }
	 else
	 {
		document.getElementById(""+text_area+"").style.display="block";
		document.getElementById(""+logo_area+"").style.display="none";	
		document.getElementById(""+button_+"").style.pointerEvents = 'auto';		 
	 }	 
 }
 
 
 
 
  function login_user()
 {	
 
	

	
	 if (check_vollstaendigkeit())
	 {
		button_logo("0","login_button_text","login_button_logo","login_button")	
	//	 login_logo(0,"login_text","login_logo","login")
		document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'none';
		document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'none';
		
		
		$.ajax({
			type: "GET",
			url: "/check_whether_logged_in/",
			dataType: "json",
			data: { "data":""},
			success: function(data) {	
			
				if(data!="yes")
				{

						 $.ajax({
							type: "POST",
							url: "/login_user/",
							dataType: "json",
							data: { "item": document.getElementById("username").value+","+document.getElementById("passwort").value },
							success: function(data) {
				
								
								button_logo("1","login_button_text","login_button_logo","login_button")							
				
					
								if(data=="wrong data")
								{
				
									document.getElementById("eingabe_fehler").innerHTML="Bitte überprüfe noch einmal Deine E-Mail Adresse und Dein Passwort.";
									//login_logo(1,"login_text","login_logo","login")
									document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'auto';
									document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
				
								}
								else			
								{
									location.reload();
								}
								
				
				
				
							},
							failure: function(data){
								button_logo("1","login_button_text","login_button_logo","login_button")	
								document.getElementsByClassName("registrierung")[0].style.pointerEvents = 'auto';
								document.getElementsByClassName("facebook_login")[0].style.pointerEvents = 'auto';
				
								
							}
						});
			}
			else
				location.reload();
			}
		});
	 }
}
function openNav() {

		disableScroll();




	
	open_sidebar_main();
	


}

function closeNav() {

		enableScroll();
    document.getElementById("mySidenav").style.width = "0";
	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	
	document.getElementById("x-mask").style.opacity="1.0";

	document.getElementsByClassName ("modal_mobile_sidebar")[0].style.visibility = "hidden";

}


function open_sidebar_main(){

	block=""
	block=block+"<input class='search_field' name='search' placeholder='Suchen..' onfocus='search_field_sidebar()'>"
	block=block+"<div class='main_group_shopping' onlick='logo_click'>Shopping</div>"
	
	i=0;

	while (i<=links.length-1)
	{

		if (url_lingerie==links[i].name)
			block=block+"<div class='sub_group' onclick='content_abrufen("+i+")' ><b>"+links[i].name+"</b></div>"
 		else
 			block=block+"<div class='sub_group' onclick='content_abrufen("+i+")' >"+links[i].name+"</div>"
 		i=i+1;
 	}

	block=block+"<div class='main_group_wishlist' onclick='wishlist_aufrufen()'>Meine Wunschliste</div>"
	block=block+"<div class='linie_1'></div>"

	if(login=="true")
	{

		block=block+"<div class='main_group_account' onclick='account_aufrufen()'>Account</div>"
		block=block+"<div class='sub_group' onclick='account_aufrufen()'>Account Übersicht</div>"
		

		if(document.getElementsByClassName("bestellungen")[0].innerHTML!="[]")
		{
			block=block+"<div class='sub_group' onclick='bestellungen_bearbeiten()'>Meine Bestellungen</div>"
			block=block+"<div class='sub_group' onclick='bestellung_zuruecksenden()'>Rücksendungen</div>"
		}
		else
		{
			box=box+"<div class='dropdown_content_account' style='opacity:0.4;pointerEvents:none;cursor:initial;'><div class='dropdown_content_orders_overview' ><div class='dropdown_content_account_text' >Meine Bestellungen</div></div></div>"
			box=box+"<div class='dropdown_content_account' style='opacity:0.4;pointerEvents:none;cursor:initial;'><div class='dropdown_content_exchanges_overview' ><div class='dropdown_content_account_text' >Rücksendungen</div></div></div>"			
		}

		block=block+"<div class='linie_1'></div>"
		block=block+"<div class='main_group_log_out' onclick='log_out()'>Log-Out</div>"
	}
	else
	{
		block=block+"<div class='main_group_account' onclick='load_registration_login()'>Login/ Registrierung</div>"
	}
	block=block+"<div class='main_group_help'>Hilfe</div>"
	
	document.getElementById("mySidenav").innerHTML =block;
    document.getElementById("mySidenav").style.width = "250px";

	document.getElementsByClassName ("overlay")[0].style.visibility = "visible";


	
	document.getElementById("x-mask").style.opacity="0.4";


	document.getElementsByClassName ("modal_mobile_sidebar")[0].style.visibility = "visible";
}
	

	
	
	
function full_text_search()
{

			 $.ajax({
			type: "GET",
			url: "/full_text_search/",
			dataType: "json",
			data: { "search_item": document.getElementById("searchbox").value  },
			success: function(data) {


					load_lingerie_sidebar(data)

				
			},
			error:function() {

					load_lingerie_sidebar("")

				
			}
			
			})
	
}


function load_lingerie_sidebar(data)
{
	lingerie_sidebar=data
	 var pics =[]
	 zaehler=0;
	 box=""

	i=0;
	 while(i<=lingerie_sidebar.length-1)
	 {
		var arr1 = lingerie_sidebar[i].pic.split(",");	
		for (j = 0; j < arr1.length; j++) {
			pics[j]=arr1[j].split(",");
		}  
		if(zaehler==0)
			box=box+"<div class='block'>\r";
		box=box+"<div class='box_1_small_image'><div><img class='image_box' src='"+pics[0]+"' onclick='detail_page_sidebar("+i+")'></img></div><div class='box_erste_ebene'><div class='gericht_auswahl_text' >"+lingerie_sidebar[i].name+"</div></div></div>\r";
		zaehler=zaehler+1;
			
		if(zaehler>=4)
		{
			box=box+"<span class='stretch'></span></div>\r"
			zaehler=0;
		}
		i=i+1;
	}

	document.getElementById("lingerie_sidebar").innerHTML =box;
}
	
	
	 function detail_page_sidebar(i)
 {

 	window.location.href=lingerie_sidebar[i].name;
 }
	
function search_field_sidebar(){
	enableScroll();
	    document.getElementById("mySidenav").style.width = "100%";
	block=""
	block=block+"<input type='text' id='searchbox' name='search' placeholder='Suchen..' autofocus='autofocus' style='width:80%;margin-left:10px;' oninput='full_text_search()'><img class='schliessen_searchbox' src='/static/x.png' width='15' onclick='close_searchbox_mobile()' height='15'/></img><br><br><div id='lingerie_sidebar'></div>"
	
	document.getElementById("mySidenav").innerHTML =block;	

}


function close_searchbox_mobile()
{
	
	
	openNav();	

}
	
	
	
	function password_check(passwort)
{

	if (passwort=="not ok")
	{

		$('#password_check').modal({backdrop: 'static', keyboard: false})  
	}
	

}




function passwort_bearbeiten()
{
	
		window.location.href="/account_page/passwort_bearbeiten/";
}

function quiz_laden()
{

					$('#showroom').modal('show');
				
					 quiz_page_initialize();
					//quiz_page_laden(0)


	
}

 function alert_click_schliessen() {
	document.getElementsByClassName ("modal")[0].style.visibility = "hidden"
	document.getElementsByClassName ("overlay")[0].style.visibility = "hidden"
	document.getElementById("x-mask").style.opacity="1.0";
	enableScroll();
}


function onleave_webpage(){
			 $.ajax({
			type: "GET",
			url: "/onleave_message_abrufen/",
			dataType: "json",
			data: { "":""  },
			success: function(data) {

					if(data=="not ok")
						$('#alert_box_onleave_webpage').modal('show');
					

				
			}
			
			})	
	
}



var keys = {37: 1, 38: 1, 39: 1, 40: 1};

function preventDefault(e) {
  e = e || window.event;
  if (e.preventDefault)
      e.preventDefault();
  e.returnValue = false;  
}

function preventDefaultForScrollKeys(e) {
    if (keys[e.keyCode]) {
        preventDefault(e);
        return false;
    }
}




function disableScroll() {
  if (window.addEventListener) // older FF
      window.addEventListener('DOMMouseScroll', preventDefault, false);
  window.onwheel = preventDefault; // modern standard
  window.onmousewheel = document.onmousewheel = preventDefault; // older browsers, IE
  window.ontouchmove  = preventDefault; // mobile
  document.body.onkeydown  = preventDefaultForScrollKeys;
  
  document.body.style.overflow = "hidden";
  


  

}

function enableScroll() {
   if (window.removeEventListener)
        window.removeEventListener('DOMMouseScroll', preventDefault, false);
    window.onmousewheel = document.onmousewheel = null; 
    window.onwheel = null; 
    window.ontouchmove = null;  
    document.onkeydown = null;  

    document.body.style.overflowX = "hidden";
    document.body.style.overflowY = "visible";
}

