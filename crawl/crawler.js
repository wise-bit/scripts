var request = require('request');
var cheerio = require('cheerio');
var URL = require('url-parse');

// var URL = 'https://arstechnica.com/';
var URL = 'https://satrajit.tk/';

var allRelativeLinks = [];
var allAbsoluteLinks = [URL];

var mode = 1; // 1: Link grabber
var depth = 2; // How many times to run the list
var iterateForAbsoluteLinks = false;

function gatherer(callback) {

    var currentURL = allAbsoluteLinks.pop();

    request(currentURL, (error, response, html) => {
        
        if (error) {
            console.log(error);
        } 
        else if (!error && response.statusCode == 200) {

            var $ = cheerio.load(html);
            console.log("Page title: " + $('title').text() + "\n");

            var relativeLinks = $("a[href^='/']");
            relativeLinks.each(function() {
                allRelativeLinks.push($(this).attr('href'));

            });

            var absoluteLinks = $("a[href^='http']");
            absoluteLinks.each(function() {
                allAbsoluteLinks.push($(this).attr('href'));
            });

            // console.log("Found " + allRelativeLinks.length + " relative links");
            // console.log("Found " + allAbsoluteLinks.length + " absolute links");

        }
    });

    callback;

}

var p = function print() {

    console.log(allAbsoluteLinks.length);

    for (var i = 0; i < allRelativeLinks.length; i++) {
        console.log(URL + allRelativeLinks[i]);
    }

    for (var i = 0; i < allAbsoluteLinks.length; i++) {
        console.log(allAbsoluteLinks[i]);
    }

}

function delay(t){
    return new Promise(function(resolve){
        return setTimeout(resolve, t)
    });
}

for (var i = 0; i <= depth; i++) {
    delay(5000).then(gatherer(p));
    delay(5000).then(p);
}
