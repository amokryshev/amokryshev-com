var path = require('path');
var webpack = require('webpack');
//var WebpackMd5Hash = require('webpack-md5-hash');
var config = require('./webpack.config');

webpack_context = __dirname + "/..";
static_files = new Object();

static_files = {

    mainsite_index: ['./mainsite/static/mainsite/js/index_entry.js'],
	mainsite_error: ['./mainsite/static/mainsite/js/error_entry.js'],
	mainsite_inner: ['./mainsite/static/mainsite/js/inner_entry.js']

};

config.mode = 'production';
config.context = webpack_context;
config.entry = static_files;
config.output.filename = '[name].js';//= '[chunkhash].[name].js';
config.output.path = webpack_context + '/static/bundles';
config.output.publicPath = '/static/bundles/';
//config.plugins.push(new WebpackMd5Hash());

var compiler = webpack(config);

compiler.run(function (err, stats) {
	if (err) {
    	console.log(err)
    }
	console.log(stats)
});