var path = require('path');
var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server')
var config = require('./webpack.config')

webpack_context = __dirname + "/..";
static_files = new Object();


static_files = {

    mainsite_index: ['./mainsite/static/mainsite/js/index_entry.js'],
	mainsite_error: ['./mainsite/static/mainsite/js/error_entry.js'],
    mainsite_inner: ['./mainsite/static/mainsite/js/inner_entry.js']

};

config.mode = 'development';
config.devtool = 'inline-source-map';
config.devServer = {
    contentBase: './static',
  };

config.context = webpack_context;
config.entry = static_files;
config.output.filename = '[name].js';
config.output.path = webpack_context + '/static/bundles';
config.output.publicPath = '/static/bundles/';

var compiler = webpack(config);

var server = new WebpackDevServer(compiler, {

    publicPath: '/static/bundles/',
    proxy: {
        "**": "http://localhost:8000"
    },
    hot: true,
});

server.listen(3000, 'localhost', function (err, result) {
  if (err) {
    console.log(err)
  }
  console.log('Listening at localhost:3000')
})