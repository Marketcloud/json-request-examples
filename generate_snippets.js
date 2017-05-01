const httpsnippet = require('httpsnippet');
const fs = require('fs')
const path = require('path')
const mkdirp = require('mkdirp');


var baseOutputDirectory = __dirname + '/code-examples'

function getDirectories(srcpath) {
  return fs.readdirSync(srcpath)
    .filter(file => fs.statSync(path.join(srcpath, file)).isDirectory())
}

function getFiles(srcpath) {
  return fs.readdirSync(srcpath)
}



var languages = [
  "cURL",
  "go",
  "java",
  "objective-c",
  "swift",
  "python",
  "c#"
]

var directoriesToIgnore =[".git","node_modules","code-examples"];


var files = {};

getDirectories(__dirname)
  .forEach((dir) => {

    if (directoriesToIgnore
      .indexOf(dir) > -1){
      console.log("Ignoring directory "+dir)
    return;
    }
      


    files[dir] = {};
    var resourcePath = __dirname + "/" + dir;
    var filesInDirectory = getFiles(resourcePath);

    languages.forEach(function(language) {
      var outputDirectory = baseOutputDirectory+'/' + language;
      mkdirp(outputDirectory + '/' + dir, function(err) {
        console.log("Ho la directory " + outputDirectory + '/' + dir)
          // path exists unless there was an error
        filesInDirectory.forEach((filename) => {
          var filepath = resourcePath + '/' + filename;
          var fileContent = fs.readFileSync(filepath);
          var snippet = new httpsnippet(JSON.parse(fileContent));
          var targetFilePath = outputDirectory + '/' + dir + '/' + filename;
          var fileExtension = '.go'
          targetFilePath = targetFilePath.replace('.json', fileExtension);
          console.log("Ora scrivo nel file " + targetFilePath)
          fs.writeFileSync(targetFilePath, snippet.convert('go'));
        })

      });

    })


  })