var jQueryBridget = require('jquery-bridget');
var Isotope = require("isotope-layout");
jQueryBridget( 'isotope', Isotope, $ );
import "jquery.easing/jquery.easing.min.js";
import "waypoints/lib/jquery.waypoints.min.js";
import "bootstrap/dist/js/bootstrap.min.js";
import "jquery.counterup/jquery.counterup.min.js";
import "venobox/venobox/venobox.min.js";
import "owl.carousel/dist/owl.carousel.min.js";
import Typed from "typed.js";
window.Typed = Typed;
import AOS from "aos";
window.AOS = AOS;
require("../css/index.sass");
require("./base.js");
require("./index.js");
require("./tagcloud.js");