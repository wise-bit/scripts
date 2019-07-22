var request = require('request');
var cheerio = require('cheerio');
var URL = require('url-parse');

var allRelativeLinks = [];
var allAbsoluteLinks = [];

request('https://arstechnica.com/', (error, response, html) => {
    
    if (!error && response.statusCode == 200) {

        var $ = cheerio.load(html);
        // console.log($);
        console.log("Page title: " + $('title').text());

        var relativeLinks = $("a[href^='/']");
        relativeLinks.each(function() {
            allRelativeLinks.push($(this).attr('href'));

        });

        var absoluteLinks = $("a[href^='http']");
        absoluteLinks.each(function() {
            allAbsoluteLinks.push($(this).attr('href'));
        });

        console.log("Found " + allRelativeLinks.length + " relative links");
        console.log("Found " + allAbsoluteLinks.length + " absolute links");
    }
});