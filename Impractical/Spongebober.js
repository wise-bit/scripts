### Make any string into the spongebob meme format 

function spongeMeme(sentence) {
  var s = sentence.split("");
  for (var i = 0; i < sentence.length; i++){
    s[i] = i%2==1?s[i].toLowerCase():s[i].toUpperCase();
  }
  return s.join("");
}
