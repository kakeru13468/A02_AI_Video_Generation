const express = require("express");
const { spawn } = require("child_process");
const path = require("path");

const app = express();
const port = 3000;

app.use(express.static(__dirname));
const absolutePath = path.join(__dirname, "../");

app.post("/generate", (req, res) => {
  let videoPath = "";
  const dry_run = req.query.dry_run ? true : false;

  var prompt = req.query.prompt;
  console.log("prompt: " + prompt);

  var voiceType = req.query.voiceType;
  // use example video
  if (prompt == "!example") {
    videoPath = "example.mp4";
    console.log("video: " + videoPath);
    res.send(videoPath);
  } else {
    let args = [
      path.join(absolutePath, "main.py"),
      prompt,
      dry_run ? "--dry-run" : "",
      voiceType ? `--voiceType=${voiceType}` : "",
    ];
    let result = {};

    let child_process = spawn("python", args, { cwd: absolutePath });
    console.log("##### start generating #####");
    if (dry_run) console.log("##### dry run #####");

    child_process.stdout.on("data", (data) => {
      console.log(`stdout: ${data}`);
      if (String(data).match(/[\d]*\.json/)) {
        textsPath = String(data).match(/[\d]*\.json/)[0];
        texts = require(path.join(absolutePath, "media", "texts", textsPath));
        result.texts = texts;
      }
    });
    child_process.stderr.on("data", (data) => {
      console.log(`stderr: ${data}`);
    });
    child_process.on("close", (code) => {
      console.log(`child process exited with code ${code}`);
      result.videoPath = "target.mp4";
      console.log("video: " + result.videoPath);
      res.send(result);
    });
  }
});

app.listen(port, () => console.log(`App listening on port ${port}.`));
