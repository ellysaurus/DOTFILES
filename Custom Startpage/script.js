window.onload = refreshGet;

function refreshGet() {
  console.log('---------------------------------');
  console.log('         data is updated');
  console.log('---------------------------------');

  var out = document.getElementById('output')
  var out2 = document.getElementById('output2')
  var out3 = document.getElementById('output3')
  var refreshSecs = 1000;
  //utskrift
  var dataPost = 'test test test test test'


 //settings for the scrape
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty",
    "method": "GET",
    "headers": {},
    "data": "{}"
  }

  // line 1
  $.ajax(settings).done(function(response) {
    //henter array med top story ids
    $.getJSON("https://hacker-news.firebaseio.com/v0/newstories.json",
      function(topstories) {
        var storyID = topstories[1]
        //output
        $.getJSON("https://hacker-news.firebaseio.com/v0/item/" + storyID + ".json?print=pretty",
          function(data) {
            console.log(data) //the whole json file logged out
            console.log('\n\n\n\n\n\n\n\n\n');
            if (data.type === "story"){
              out.innerHTML = '<a href="' + data.url + '" target="_blank" id="output" class="outputs">' + data.title + '.</a>';
            }else {
              out.innerHTML = '<p id="output" class="outputs">' + data.title + '.</p>';
            }

          });
      });
  });


  // line 2
  $.ajax(settings).done(function(response2) {
    //henter array med top story ids
    $.getJSON("https://hacker-news.firebaseio.com/v0/newstories.json",
      function(topstories2) {
        var storyID2 = topstories2[2]

        //output
        $.getJSON("https://hacker-news.firebaseio.com/v0/item/" + storyID2 + ".json?print=pretty",
          function(data2) {
            console.log(data2) //the whole json file logged out
            console.log('\n\n\n\n\n\n\n\n\n');
            if (data2.type === "story"){
              out2.innerHTML = '<a href="' + data2.url + '" target="_blank" id="output2" class="outputs">' + data2.title + '.</a>';
            }else {
              out2.innerHTML = '<p id="output2" class="outputs">' + data2.title + '.</p>';
            }

          });
      });
  });

    // line 3
    $.ajax(settings).done(function(response3) {
      //henter array med top story ids
      $.getJSON("https://hacker-news.firebaseio.com/v0/newstories.json",
        function(topstories3) {
          var storyID3 = topstories3[3]

          //output
          $.getJSON("https://hacker-news.firebaseio.com/v0/item/" + storyID3 + ".json?print=pretty",
            function(data3) {
              console.log(data3) //the whole json file logged out
              console.log('\n\n\n\n\n\n\n\n\n');
              if (data3.type === "story"){
                out3.innerHTML = '<a href="' + data3.url + '" target="_blank" id="output3" class="outputs">' + data3.title + '.</a>';
              }else {
                out3.innerHTML = '<p id="output3" class="outputs">' + data3.title + '.</p>';
              }

            });
        });
    });

  // hvor ofte den skal refreshes
  var t = setTimeout(refreshGet, refreshSecs * 60);
}
