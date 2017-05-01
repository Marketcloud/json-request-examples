const HTTPSnippet = require('httpsnippet')
const fs = require('fs')
const path = require('path')
const mkdirp = require('mkdirp')

var baseOutputDirectory = path.join(__dirname, 'code-examples')

function getDirectories (srcpath) {
  return fs.readdirSync(srcpath)
    .filter(file => fs.statSync(path.join(srcpath, file)).isDirectory())
}

function getFiles (srcpath) {
  return fs.readdirSync(srcpath)
}

var languages = [
  'shell',
  'go',
  'java',
  'objective-c',
  'swift',
  'python',
  'c#'
]

var extensions = {
  'shell': '.sh',
  'go': '.go',
  'java': '.java',
  'objective-c': '.m',
  'swift': '.swift',
  'python': '.py',
  'c#': '.cs'

}

var directoriesToIgnore = ['.git', 'node_modules', 'code-examples']

var files = {}

getDirectories(__dirname)
  .forEach((dir) => {
    if (directoriesToIgnore
      .indexOf(dir) > -1) {
      console.log('Ignoring directory ' + dir)
      return
    }

    files[dir] = {}

    var resourcePath = path.join(__dirname, dir)

    var filesInDirectory = getFiles(resourcePath)

    languages.forEach(function (language) {
      var outputDirectory = baseOutputDirectory + '/' + language
      mkdirp(outputDirectory + '/' + dir, function (err) {
        if (err) {
          throw new Error('An error has occurred while creating an output subdirectory')
        }
        console.log('Ho la directory ' + outputDirectory + '/' + dir)
          // path exists unless there was an error
        filesInDirectory.forEach((filename) => {
          var filepath = resourcePath + '/' + filename
          var fileContent = fs.readFileSync(filepath)
          var snippet = new HTTPSnippet(JSON.parse(fileContent))
          var targetFilePath = outputDirectory + '/' + dir + '/' + filename
          var fileExtension = extensions[language]
          targetFilePath = targetFilePath.replace('.json', fileExtension)
          console.log('Ora scrivo nel file ' + targetFilePath)
          fs.writeFileSync(targetFilePath, snippet.convert(language))
        })
      })
    })
  })
