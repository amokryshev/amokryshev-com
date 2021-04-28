var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var path = require('path');
var CopyPlugin = require("copy-webpack-plugin");
var postcss = require("postcss");

module.exports = {

	output: {},

	plugins: [
	    new BundleTracker({
            path: __dirname + "/..",
            filename: './webpack-stats.json'}),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        }),
        new CopyPlugin({
            patterns: [
            { from: "./mainsite/static/mainsite/img", to: "./../img" }
            ]
        })
    ],
   /* optimization: {
        minimize: false
    },*/
    module: {
	    rules: [
	         {
	           test: /\.(css|s[ac]ss)$/i,
                use: [ 'style-loader', 'css-loader', 'sass-loader']
            },
	       {
	           test: /\.(ttf|eot|woff|woff2|png|ico|jpg|jpeg|gif|svg)$/i,
               loader: 'file-loader',
               options: {
	               name: '[hash].[ext]',
                   outputPath: '../img',
                   publicPath: '/static/img'}
            },
            {
              test: /\.js$/,
              use: {
                loader: 'babel-loader',
                options: {
                  presets: ['@babel/preset-env'],
                  ignore: ['node_modules']
                }
              }
            }
	    ]
    },

}