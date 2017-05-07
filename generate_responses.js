const HTTPSnippet = require('httpsnippet')
const fs = require('fs')
const path = require('path')
const mkdirp = require('mkdirp')

var baseOutputDirectory = path.join(__dirname, 'code-examples')

var baseRequestsDirectory = path.join(__dirname,'requests');

function getDirectories (srcpath) {
  return fs.readdirSync(srcpath)
    .filter(file => fs.statSync(path.join(srcpath, file)).isDirectory())
}

function getFiles (srcpath) {
  return fs.readdirSync(srcpath)
}



var directoriesToIgnore = ['.git', 'node_modules', 'code-examples']

var files = {}

getDirectories(baseRequestsDirectory)
  .forEach((dir) => {
    if (directoriesToIgnore
      .indexOf(dir) > -1) {
      console.log('Ignoring directory ' + dir)
      return
    }

    files[dir] = {}

    var resourcePath = path.join(baseRequestsDirectory, dir);

    var filesInDirectory = getFiles(resourcePath);


    filesInDirectory.forEach((file) => {
      var filepath = path.join(resourcePath,file);
      var text = fs.readFileSync(filepath);
      var requestHAR = JSON.parse(text);
      console.log(requestHAR.postData);
      //var exampleBody = requestHAR.postData.text;
      //console.log("EAMPLE BODY",exampleBody)
    });

    


  })
